#  BUILD JOURNAL

---

## Entry 1 — [10:12] Understanding Project Requirement
**Tool:** ChatGPT  
**Prompt:** "Build a single-page web application that ingests CSV and provides a construction project health dashboard. Explain what this means, don’t give the code."  

**What AI produced:**  
Explained requirement meaning, clarified expectations (local app, CSV ingestion, dashboard, no cloud).

**What I accepted:**  
Understanding of scope and constraints.

**What I changed:**  
None.

**Bugs found:**  
None.

---

## Entry 2 — [10:37] Choosing Tech Stack
**Tool:** ChatGPT  
**Prompt:** "Which is a better option to build project with sortable/filterable data and visualization?"

**What AI produced:**  
Suggested React vs Streamlit vs plain JS with pros/cons.

**What I accepted:**  
Chose Streamlit for speed (4-hour constraint).

**What I changed:**  
Ignored React due to time and chose Streamlit for easier implementation.

**Bugs found:**  
None.

---

## Entry 3 — [10:45] Time Constraint Optimization
**Tool:** ChatGPT  
**Prompt:** "To be built in 4 hours"

**What AI produced:**  
Recommended fastest approach (Streamlit + built-in features).

**What I accepted:**  
Outline and suggested approach.

**What I changed:**  
Used template and adapted based on further prompts.

**Bugs found:**  
None.

---

## Entry 4 — [11:20] Improving Dashboard Idea
**Tool:** ChatGPT  
**Prompt:** "Give better than just a simple dashboard"

**What AI produced:**  
Suggested rule engine, alerts, KPIs, health score.

**What I accepted:**  
Rule engine + KPIs structure.

**What I changed:**  
Simplified health score, added 3 custom rules.

**Bugs found:**  
None.

---

## Entry 5 — [11:40] Data Requirements Clarification
**Tool:** ChatGPT  
**Prompt:** "Does this display sortable/filterable data?"

**What AI produced:**  
Confirmed Streamlit table supports sorting.

**What I accepted:**  
Default table behavior.

**What I changed:**  
Added custom filters.

**Bugs found:**  
None.

---

## Entry 6 — [12:05] Adding Filtering Requirements
**Tool:** ChatGPT  
**Prompt:** "I want sorting, basic filtering and advanced filtering"

**What AI produced:**  
Sidebar filtering + advanced filter logic.

**What I accepted:**  
Sidebar filtering structure.

**What I changed:**  
Simplified advanced filtering.

**Bugs found:**  
None.

---

## Entry 7 — [12:15] Dataset Structure Input
**Tool:** ChatGPT  
**Prompt:** "Sample column names..."

**What AI produced:**  
Domain understanding + RFI-based logic.

**What I accepted:**  
Entire domain mapping.

**What I changed:**  
Adjusted thresholds.

**Bugs found:**  
None.

---

## Entry 8 — [12:30] Developing the Rule Engine
**Tool:** ChatGPT  
**Prompt:** "Give placeholders for rule engine"

**What AI produced:**  
SLA breach, quantity mismatch, result issue, long pending.

**What I accepted:**  
Base rules.

**What I changed:**  
Added custom rules later.

**Bugs found:**  
None.

---

## Entry 9 — [12:35] Custom Rule Design
**Tool:** ChatGPT  
**Prompt:** Custom rules (rejection rate, contractor performance)

**What AI produced:**  
Structured rules with severity levels.

**What I accepted:**  
Most rules.

**What I changed:**  
Adjusted thresholds (e.g., 35%).

**Bugs found:**  
None.

---

## Entry 10 — [12:54] Visualization Planning
**Tool:** ChatGPT  
**Prompt:** "What visualizations are better for..."

**What AI produced:**  
Chart mapping to use cases.

**What I accepted:**  
All chart recommendations.

**What I changed:**  
Reduced complexity.

**Bugs found:**  
None.

---

## Entry 11 — [1:01] Productivity Rule Update
**Tool:** ChatGPT  
**Prompt:** "Within 3 months not 7 days"

**What AI produced:**  
Updated logic using DateOffset.

**What I accepted:**  
Full logic.

**What I changed:**  
Added average comparison.

**Bugs found:**  
None.

---

## Entry 12 — [1:07] Rule 6 Completion
**Tool:** ChatGPT  
**Prompt:** "Give complete rule 6"

**What AI produced:**  
Final structured productivity rule.

**What I accepted:**  
Entire implementation.

**What I changed:**  
Minor formatting.

**Bugs found:**  
None.

---

## Entry 13 — [1:15] Table + Filters Implementation
**Tool:** ChatGPT  
**Prompt:** "Parse CSV and display sortable/filterable table"

**What AI produced:**  
Full filtering implementation.

**What I accepted:**  
Core structure.

**What I changed:**  
Integrated into dashboard.

**Bugs found:**  
None.

---

## Entry 14 — [1:23] Code Review (First Pass)
**Tool:** ChatGPT  
**Prompt:** "Check my code for syntax errors"

**What AI produced:**  
Identified issues (loops, undefined variables).

**What I accepted:**  
All fixes.

**What I changed:**  
Refactored rule engine.

**Bugs found:**  
Multiple (groupby inside loop, undefined variables).

---

## Entry 15 — [1:30] Code Refactoring
**Tool:** ChatGPT  
**Prompt:** "Corrected and complete code"

**What AI produced:**  
Clean structured version.

**What I accepted:**  
Most improvements.

**What I changed:**  
UI adjustments.

**Bugs found:**  
Minor.

---

## Entry 16 — [1:35] Final Debugging & UI Review
**Tool:** ChatGPT  
**Prompt:** "See the UI/UX design and review strictly"

**What AI produced:**  
UI consistency suggestions.

**What I accepted:**  
Hybrid visualization approach.

**What I changed:**  
Balanced Streamlit + matplotlib usage.

**Bugs found:**  
Minor edge case bugs.

---

## Entry 17 — [1:47] Build Journal Creation
**Tool:** ChatGPT  
**Prompt:** "Create build journal editable format"

**What AI produced:**  
Structured BUILD_JOURNAL.md.

**What I accepted:**  
Full document.

**What I changed:**  
Added timestamps and refinements.

**Bugs found:**  
None.

---

# 📊 Summary

**Total AI tool calls:**  
18 major + 5 minor prompts  

**Most useful moments:**  
- Tech stack selection  
- Rule engine design  
- Visualization planning  
- Debugging  

**Biggest AI failure:**  
Initial inefficient loop-based logic  

**What I would do differently:**  
Start with a stronger base structure and modular design, then extend based on time and requirements.
