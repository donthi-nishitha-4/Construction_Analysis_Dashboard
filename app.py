import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
theme = st.get_option("theme.base")
if theme == "dark":
    plt.style.use("dark_background")
elif theme:
    plt.style.use("default")
st.title("Construction Analysis Dashboard")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # ----------------------------
    # 🔧 DATA PREPROCESSING
    # ----------------------------
    df["raised_date"] = pd.to_datetime(df["raised_date"], errors='coerce')
    df["sla_deadline"] = pd.to_datetime(df["sla_deadline"], errors='coerce')
    df["closed_date"] = pd.to_datetime(df["closed_date"], errors='coerce')

    # ----------------------------
    # 🔍 FILTERS
    # ----------------------------
    st.sidebar.header("🔍 Filters")

    selected_package = st.sidebar.multiselect("Package", df["package"].dropna().unique())
    selected_station = st.sidebar.multiselect("Station", df["station"].dropna().unique())
    selected_subsystem = st.sidebar.multiselect("Subsystem", df["subsystem_type"].dropna().unique())
    selected_result = st.sidebar.multiselect("Result", df["result"].dropna().unique())

    min_date = df["raised_date"].min()
    max_date = df["raised_date"].max()

    date_range = st.sidebar.date_input("Raised Date Range", [min_date, max_date])

    # ----------------------------
    # 🔄 APPLY FILTERS
    # ----------------------------
    filtered_df = df.copy()

    if selected_package:
        filtered_df = filtered_df[filtered_df["package"].isin(selected_package)]

    if selected_station:
        filtered_df = filtered_df[filtered_df["station"].isin(selected_station)]

    if selected_subsystem:
        filtered_df = filtered_df[filtered_df["subsystem_type"].isin(selected_subsystem)]

    if selected_result:
        filtered_df = filtered_df[filtered_df["result"].isin(selected_result)]

    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df["raised_date"] >= pd.to_datetime(start_date)) &
            (filtered_df["raised_date"] <= pd.to_datetime(end_date))
        ]

    # ----------------------------
    # 📋 TABLE
    # ----------------------------
    st.subheader("📋 Filtered RFI Data")
    st.dataframe(filtered_df, width='stretch')
    st.write(f"Showing {len(filtered_df)} of {len(df)} records")

    # ----------------------------
    # 📊 KPI METRICS
    # ----------------------------
    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    total_rfis = len(filtered_df)
    open_rfis = filtered_df[filtered_df["closed_date"].isna()]

    sla_breach = filtered_df[
        (filtered_df["closed_date"] > filtered_df["sla_deadline"]) |
        (filtered_df["closed_date"].isna() & (pd.Timestamp.today() > filtered_df["sla_deadline"]))
    ]

    col1.metric("Total RFIs", total_rfis)
    col2.metric("Open RFIs", len(open_rfis))
    col3.metric("SLA Breaches", len(sla_breach))

    # ----------------------------
    # 🚨 RULE ENGINE
    # ----------------------------
    def show_card(severity, title, message):
        if severity == "CRITICAL":
            st.error(f"🔴 {title}\n\n{message}")
        elif severity == "WARNING":
            st.warning(f"🟡 {title}\n\n{message}")
        else:
            st.info(f"🔵 {title}\n\n{message}")

    st.subheader("🚨 RFI Alerts")

    # 🔴 Rule 1: Open beyond SLA
    critical_rfis = filtered_df[
        (filtered_df["closed_date"].isna()) & (filtered_df["sla_deadline"].notna()) & 
        (pd.Timestamp.today() > filtered_df["sla_deadline"])
    ]
    if not critical_rfis.empty:
        show_card(
            "CRITICAL",
            "RFIs Open Beyond SLA",
            f"{len(critical_rfis)} RFIs are overdue"
        )

    # 🔴 Rule 2: Activity + Station rejection pattern
    grp = filtered_df.groupby(["station", "activity_name"])
    for (station, activity), g in grp:
        rejected = g[g["result"].fillna("").str.lower() != "approved"]

        if len(rejected) >= 3:
            show_card(
                "WARNING",
                "Frequent Rejections",
                f"{station} - {activity} rejected {len(rejected)} times"
            )

    # 🔴 Rule 3: Station rejection rate
    station_grp = filtered_df.groupby("station")
    for station, g in station_grp:
        rejection_rate = (g["result"].fillna("").str.lower() != "approved").mean()
        if rejection_rate > 0.35:
            show_card(
                "WARNING",
                "High Station Rejection Rate",
                f"{station} has {rejection_rate*100:.1f}% rejection rate"
            )

    # 🔴 Rule 4: Contractor performance
    grp = filtered_df.groupby(["contractor_id", "station"])
    for (contractor, station), g in grp:
        rejection_rate = (g["result"].fillna("").str.lower() != "approved").mean()
        if rejection_rate > 0.4:
            show_card(
                "CRITICAL",
                "Poor Contractor Performance",
                f"Contractor {contractor} at {station}: {rejection_rate*100:.1f}% rejection"
            )
            
    # 🔴 Rule 5: Low RFI volume
    if filtered_df["package"].nunique() > 0:
        avg_rfis = len(filtered_df) / filtered_df["package"].nunique()

        package_grp = filtered_df.groupby("package")
        for package, g in package_grp:
            if len(g) < avg_rfis * 0.5:
                show_card(
                    "INFO",
                    "Low RFI Volume",
                    f"{package} has only {len(g)} RFIs (below avg {avg_rfis:.1f})"
                )    

    # 🔴 Rule 6: 3-month productivity
    st.subheader("📉 Productivity Insights (Last 3 Months)")

    recent_df = filtered_df[
        filtered_df["raised_date"] > (pd.Timestamp.today() - pd.DateOffset(months=3))
    ]

    package_recent = recent_df.groupby("package").size()

    avg_recent = package_recent.mean() if len(package_recent) > 0 else 0

    for package in filtered_df["package"].unique():
        count = package_recent.get(package, 0)

        if count == 0:
            show_card("CRITICAL", "No Activity", f"{package} → 0 RFIs in last 3 months")
        elif avg_recent > 0 and count < avg_recent * 0.5:
            show_card("WARNING", "Low Activity", f"{package} → {count} RFIs (low)") 
        else:
            show_card("WARNING", "Low Activity", f"{package} → {count} RFIs (low)")

    # ----------------------------
    # 📈 VISUALIZATIONS
    # ----------------------------
    st.subheader("📈 Visualizations")
    # 1. Station count
    station_counts = filtered_df["station"].value_counts()
    st.write("X-axis: Station | Y-axis: Number of RFIs")
    st.bar_chart(filtered_df["station"].value_counts())

    # fig, ax = plt.subplots()
    # ax.bar(station_counts.index, station_counts.values)
    # ax.set_xlabel("Station")
    # ax.set_ylabel("Number of RFIs")
    # ax.set_title("RFI Count by Station")
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # st.pyplot(fig)

    # 2. Accepted vs Rejected over time
    st.subheader("Accepted vs Rejected RFIs Over Time")
    status_series = filtered_df["result"].apply(
        lambda x: "Accepted" if str(x).lower() in ["approved", "accepted"] else "Rejected"
    )
    time_grp = filtered_df.groupby(
        [filtered_df["raised_date"].dt.date, status_series]
    ).size().unstack().fillna(0)

    st.line_chart(time_grp)
    # for col in time_grp.columns:
    #     ax.plot(time_grp.index, time_grp[col], label=col)

    # ax.set_xlabel("Date")
    # ax.set_ylabel("Number of RFIs")
    # ax.set_title("Accepted vs Rejected RFIs Over Time")
    # ax.legend()
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # st.pyplot(fig)

    # 3. Closure rate by package
    closure_rate = filtered_df.groupby("package")["closed_date"].apply(lambda x : x.notna().mean())
    fig, ax = plt.subplots()
    ax.bar(closure_rate.index, closure_rate.values)
    ax.set_xlabel("Package")
    ax.set_ylabel("Closure Rate")
    ax.set_title("RFI Closure Rate by Package")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.write("")  
    st.write("")
    
    # 4. Contractor performance
    acceptance_rate = filtered_df.groupby("contractor_id")["result"].apply(
    lambda x: x.str.lower().isin(["approved", "accepted"]).mean()).sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.bar(acceptance_rate.index, acceptance_rate.values)
    ax.set_xlabel("Contractor")
    ax.set_ylabel("Acceptance Rate")
    ax.set_title("Contractor Performance (Acceptance Rate)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig)
    st.write("")  
    st.write("")
    
    # 5. Heatmap (station vs activity)
    pivot = filtered_df.pivot_table(
        index="station",
        columns="activity_name",
        values="rfi_id",
        aggfunc="count",
        fill_value=0
    )
    top_activities = filtered_df["activity_name"].value_counts().head(10).index
    pivot = pivot[[col for col in top_activities if col in pivot.columns]]
    
    fig, ax = plt.subplots(figsize=(12,6))
    cax = ax.imshow(pivot, aspect='auto')
    fig.colorbar(cax)
    short_labels = [col[:12] + "..." if len(col) > 12 else col for col in pivot.columns]
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(short_labels, rotation=45,ha='right')
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_xlabel("Activity")
    ax.set_ylabel("Station")
    ax.set_title("Station vs Activity RFI Count")
    plt.tight_layout()
    st.pyplot(fig)


    def alert_card(severity, title, description, rfi_ids):
        if severity == "CRITICAL":
            color = "#ff4b4b"
        elif severity == "WARNING":
            color = "#ffa500"
        else:
            color = "#00c853"

        st.markdown(f"""<div style="border-left: 6px solid {color};
            background-color: rgba(255,255,255,0.05);padding: 12px;
            margin-bottom: 10px;border-radius: 8px;">
            <b style="color:{color};">{severity}</b> — {title}<br>
            <span style="font-size: 13px;">{description}</span><br>
            <span style="font-size: 12px; color: gray;">
                RFIs: {', '.join(map(str, rfi_ids[:5]))}
                {"..." if len(rfi_ids) > 5 else ""}
            </span></div>""", unsafe_allow_html=True)
    st.write("")  
    st.write("")
    st.subheader("🧠 Inspector vs Contractor Patterns")
    pair_grp = filtered_df.groupby(["inspector_id", "contractor_id"])

    for (inspector, contractor), g in pair_grp:
        if len(g) < 5:
            continue
        rejection_rate = (g["result"].str.lower() != "approved").mean() 

        contractor_base = filtered_df[
            filtered_df["contractor_id"] == contractor
        ]
        base_rate = (contractor_base["result"].str.lower() != "approved").mean()

        if rejection_rate > base_rate + 0.3:
            alert_card(
                "WARNING",
                f"Inspector {inspector} vs Contractor {contractor}",
                f"Unusually high rejection rate ({rejection_rate:.2%} vs avg {base_rate:.2%})",
                g["rfi_id"].tolist()
            )

