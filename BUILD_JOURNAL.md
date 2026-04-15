Build Journal
Entry 1 — [10:12] Understanding Project Requirement
Tool: ChatGPT
Prompt: "Build a single-page web application that ingests CSV and provides a construction project health dashboard. Explain what this means, don’t give the code."
What AI produced: Explained requirement meaning, clarified expectations (local app, CSV ingestion, dashboard, no cloud).
What I accepted: Understanding of scope and constraints.
What I changed: None.
Bugs found: None.
________________________________________
Entry 2 — [10:37] Choosing Tech Stack
Tool: ChatGPT
Prompt: "Which is a better option to build project with sortable/filterable data and visualization?"
What AI produced: Suggested React vs Streamlit vs plain JS with pros/cons.
What I accepted: Chose Streamlit for speed (4-hour constraint).
What I changed: Ignored React due to time and chose streamlit for time constraint and easier implementation with my knowledge.
Bugs found: None.
________________________________________
Entry 3 — [10:45] Time Constraint Optimization
Tool: ChatGPT
Prompt: "To be built in 4 hours"
What AI produced: Recommended fastest approach (Streamlit + built-in features).
What I accepted: Outline and suggested approach.
What I changed: Used the template to consider sections further implemented changes in accordance to next prompts.
Bugs found: None.
________________________________________
Entry 4 — [11:20] Improving Dashboard Idea
Tool: ChatGPT
Prompt: "Give better than just a simple dashboard"
What AI produced: Suggested rule engine, alerts, KPIs, health score.
What I accepted: Rule engine + KPIs structure.
What I changed: Simplified health score initially, maintained structure started to change rules by inventing 3 on own and considering 3 from the problem statement document.
Bugs found: None.
________________________________________
Entry 5 — [11:40] Data Requirements Clarification
Tool: ChatGPT
Prompt: "Does this display sortable/filterable data?"
What AI produced: Confirmed Streamlit table supports sorting.
What I accepted: Default table behavior.
What I changed: Added custom filters.
Bugs found: None.
________________________________________
Entry 6 — [12:05] Adding Filtering Requirements
Tool: ChatGPT
Prompt: "I want sorting, basic filtering and advanced filtering"
What AI produced: Template with sidebar filters + advanced filter logic.
What I accepted: Sidebar filtering structure.
What I changed: Removed overly complex advanced filter initially ensuring customization.
Bugs found: None.
________________________________________
Entry 7 — [12:15] Dataset Structure Input
Tool: ChatGPT
Prompt: "Sample column names..."
What AI produced: Domain understanding + RFI-based dashboard logic.
What I accepted: Entire domain mapping since that plays key role for the dashboard without these the project might not serve purpose.
What I changed: Adjusted thresholds and started cross evaluating my idea with it.
Bugs found: None.
________________________________________
Entry 8 — [12:30] Developing the Rule Engine
Tool: ChatGPT
Prompt: "Give placeholders for rule engine"
What AI produced: SLA breach, quantity mismatch, result issue, long pending.
What I accepted: All base rules.
What I changed: Added custom rules later.
Bugs found: None.
________________________________________
Entry 9 — [12:35] Custom Rule Design
Tool: ChatGPT
Prompt: User-defined rules (rejection rate, contractor performance, etc.)
What AI produced: Structured critical/warning/info rules with code.
What I accepted: Most rules.
What I changed: Adjusted thresholds (e.g., 35%).
Bugs found: None.
________________________________________
Entry 10 — [12:54] Visualization Planning
Tool: ChatGPT
Prompt: "What visualizations are better for..."
What AI produced: Mapping of chart types to use cases.
What I accepted: All chart recommendations.
What I changed: Limited complexity for time.
Bugs found: None.
________________________________________
Entry 11 — [1:01] Productivity Rule Update
Tool: ChatGPT
Prompt: "Within 3 months not 7 days"
What AI produced: Updated logic using DateOffset.
What I accepted: Full logic.
What I changed: Added average comparison.
Bugs found: None.
________________________________________
Entry 12 — [1:07] Rule 6 Completion
Tool: ChatGPT
Prompt: "Give complete rule 6"
What AI produced: Final structured productivity rule.
What I accepted: Entire implementation.
What I changed: Minor formatting.
Bugs found: None.
________________________________________
Entry 13 — [1:15] Table + Filters Implementation
Tool: ChatGPT
Prompt: "Parse CSV and display sortable/filterable table "
What AI produced: Full Streamlit filtering code.
What I accepted: Cross checking core structure.
What I changed: Integrated into dashboard.
Bugs found: None.
________________________________________
Entry 14 — [1:23] Code Review (First Pass)
Tool: ChatGPT
Prompt: "Check my code for syntax errors"
What AI produced: Identified missing columns, loop issues, redundancy.
What I accepted: All fixes.
What I changed: Refactored rule engine.
Bugs found: Multiple (groupby inside loop, undefined variables).
________________________________________
Entry 15 — [1:30] Code Refactoring
Tool: ChatGPT
Prompt: "Corrected and complete code"
What AI produced: Clean structured version by removing minor syntactical tab spacing errors.
What I accepted: Most improvements.
What I changed: Adjusted UI and formatting.
Bugs found: Minor.
________________________________________
Entry 16 — [1:35] Final Debugging
Tool: ChatGPT
Prompt: "See the UI/UX design and tell about it strictly"
What AI produced: Suggested consistent approach.
What I accepted: Suggestions, comparisions, crosschecking with requirements.
What I changed: Used my version of hybrid visualization to access more information from plots as per the requirement by choosing between streamlit and matplotlib visualization.
Bugs found: Syntax + edge case bugs.
________________________________________
Entry 17 — [1:47] Build Journal Creation
Tool: ChatGPT
Prompt: "Create build journal editable format including all prompts"
What AI produced: Structured BUILD_JOURNAL.md covering entire workflow.
What I accepted: Full editable document.
What I changed: Timestamps, Changed, accepted and bugs found columns at each entry.
Bugs found: None.
________________________________________
Summary
Total AI tool calls: 18 major + 5 minor repetitive prompts to get better results.
Most useful tool/moment:  Choosing Tech Stack, Rule engine redesign, Visualization tool selection and debugging phase.
Biggest AI failure: Initial inefficient loop-based logic.
What I would do differently: Consider the base structure and redesign or develop components and append them according to time, feasibility and requirements.

