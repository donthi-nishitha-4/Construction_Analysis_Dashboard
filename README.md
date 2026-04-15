# 📊 Construction Analysis Dashboard 
A Streamlit-based dashboard to analyze construction project RFIs, detect quality issues, and monitor project health.

## 🚀 Features

- Upload CSV and explore data interactively
- Advanced filtering (package, station, subsystem, result, date)
- Rule-based alert engine (Critical / Warning / Info)
- Visualizations:
  - RFI count by station
  - Accepted vs Rejected trends
  - Closure rate by package
  - Contractor performance
  - Station vs Activity heatmap
- Cross-entity anomaly detection (Inspector vs Contractor)

## 🧠 Key Insights

- Identifies SLA breaches
- Detects frequent rejection patterns
- Flags underperforming contractors
- Highlights low productivity packages
- Detects unusual inspector–contractor interactions

## ⚙️ Setup Instructions

pip install -r requirements.txt
streamlit run app.py

📂 Input Format
Upload a CSV file with columns like:
•	rfi_id, package, station, subsystem_type 
•	activity_name, contractor_id, inspector_id 
•	raised_date, sla_deadline, closed_date 
•	result, remarks


Build Journal Link : 
## 🏗 Approach

### 1. Data Handling
- Parsed CSV using pandas
- Converted date fields for time-based analysis

### 2. Filtering System
- Implemented sidebar filters for:
  - Package
  - Station
  - Subsystem
  - Result
  - Date range

---

## 🚨 Rule Engine

Implemented 6 rules with severity levels:

- **CRITICAL**
  - RFIs open beyond SLA
  - Contractor with high rejection rate (>40%)

- **WARNING**
  - Frequent rejection patterns (activity + station)
  - Station-level high rejection rate (>30%)
  - Inspector–Contractor anomalies

- **INFO**
  - Low RFI volume (possible low productivity)

---

## 📊 Visualizations

- Station-wise RFI distribution
- Accepted vs Rejected trends over time
- Closure rate by package
- Contractor performance comparison
- Heatmap (station vs activity)

---
---
## 🔍 Key Enhancements

- Built reusable alert-card system
- Added cross-entity anomaly detection
- Improved UI with layout structuring and spacing
- Ensured data is filterable and sortable

---

## ⚠️ Challenges

- Managing clutter in heatmaps
- Handling inconsistent theme between Streamlit and matplotlib
- Designing readable alerts without overwhelming UI

---

## 🚀 Future Improvements

- Predictive SLA breach detection
- NLP-based remarks analysis
- Exportable reports (PDF/CSV)
- Interactive Plotly charts

---

## ✅ Outcome

Developed a functional and scalable dashboard that provides actionable insights into construction project health.

