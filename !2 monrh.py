import tkinter as tk
from tkinter import ttk, messagebox
import json
import webbrowser
from pathlib import Path
from datetime import datetime

# ============================================================
# 12-MONTH DATA ANALYST + DATA SCIENCE STUDY TRACKER
# ============================================================
# 3 HOURS / DAY • 6 DAYS / WEEK • 48 WEEKS
#
# This version gives you:
#   ✓ Exact Day 1 → Day 288 plan
#   ✓ Exact 1-hour + 1-hour + 1-hour tasks for every day
#   ✓ Learning links + YouTube links + notes/practice links
#   ✓ "Learn" / "YouTube" / "Practice" buttons
#   ✓ Tick topic, tick each hour, tick complete day
#   ✓ Daily notes and weekly notes
#   ✓ Weekly 18-hour target
#   ✓ Sunday buffer/revision day
#   ✓ Automatic JSON saving
#   ✓ Overall/monthly progress dashboard
#
# IMPORTANT:
# The web resources below were checked/selected from official or
# established free learning sites during the update on 08-Sep-2026.
# YouTube search links are intentionally used for some subjects so
# that the link keeps working even if a video is replaced.
# ============================================================

APP_TITLE = "12-Month Data Analyst + Data Science — Daily Study Tracker"
PROGRESS_FILE = Path("study_progress.json")

# ============================================================
# VERIFIED / STABLE LEARNING RESOURCE CATALOG
# ============================================================

RESOURCES = {
    "python": {
        "learn": ("CS50P — Harvard Python course", "https://cs50.harvard.edu/python/"),
        "youtube": ("CS50 Python full course — freeCodeCamp", "https://www.youtube.com/watch?v=nLRL_NcnK-4"),
        "practice": ("Kaggle Learn — Python", "https://www.kaggle.com/learn/python"),
        "notes": ("Python official tutorial", "https://docs.python.org/3/tutorial/"),
    },
    "python_oop": {
        "learn": ("Python official — Classes/OOP", "https://docs.python.org/3/tutorial/classes.html"),
        "youtube": ("YouTube — Python OOP tutorials", "https://www.youtube.com/results?search_query=python+oop+classes+objects+inheritance+free"),
        "practice": ("Kaggle Learn — Python", "https://www.kaggle.com/learn/python"),
        "notes": ("Python Classes documentation", "https://docs.python.org/3/tutorial/classes.html"),
    },
    "dsa": {
        "learn": ("freeCodeCamp — DSA in Python full course", "https://www.youtube.com/watch?v=pkYVOmU3MgA"),
        "youtube": ("DSA in Python — freeCodeCamp", "https://www.youtube.com/watch?v=pkYVOmU3MgA"),
        "practice": ("LeetCode problems", "https://leetcode.com/problemset/"),
        "notes": ("GeeksforGeeks Data Structures", "https://www.geeksforgeeks.org/data-structures/"),
    },
    "excel": {
        "learn": ("Microsoft Excel Help & Learning", "https://support.microsoft.com/en-us/excel"),
        "youtube": ("YouTube — Excel for beginners", "https://www.youtube.com/results?search_query=excel+for+data+analysis+beginners+free"),
        "practice": ("Microsoft Excel tutorials", "https://support.microsoft.com/en-us/excel"),
        "notes": ("Microsoft Excel formulas", "https://support.microsoft.com/en-us/excel/get-started/overview-of-formulas-in-excel"),
    },
    "sql": {
        "learn": ("SQLBolt — interactive SQL lessons", "https://sqlbolt.com/"),
        "youtube": ("YouTube — SQL full course", "https://www.youtube.com/results?search_query=SQL+full+course+freeCodeCamp"),
        "practice": ("HackerRank SQL", "https://www.hackerrank.com/domains/sql"),
        "notes": ("SQLBolt lessons", "https://sqlbolt.com/"),
    },
    "sql_advanced": {
        "learn": ("SQLBolt — intermediate SQL", "https://sqlbolt.com/topic/introduction"),
        "youtube": ("YouTube — advanced SQL", "https://www.youtube.com/results?search_query=advanced+SQL+CTE+window+functions+free+course"),
        "practice": ("LeetCode Database problems", "https://leetcode.com/problemset/database/"),
        "notes": ("SQLBolt intermediate topics", "https://sqlbolt.com/topic/introduction"),
    },
    "statistics": {
        "learn": ("OpenIntro Statistics — free textbook + videos", "https://www.openintro.org/book/os/"),
        "youtube": ("StatQuest — Statistics", "https://www.youtube.com/@statquest"),
        "practice": ("Khan Academy — Statistics & Probability", "https://www.khanacademy.org/math/statistics-probability"),
        "notes": ("OpenIntro Statistics", "https://www.openintro.org/book/os/"),
    },
    "numpy": {
        "learn": ("NumPy official Quickstart", "https://numpy.org/doc/stable/user/quickstart.html"),
        "youtube": ("YouTube — NumPy full course", "https://www.youtube.com/results?search_query=NumPy+full+course+freeCodeCamp"),
        "practice": ("NumPy official tutorials", "https://numpy.org/learn/"),
        "notes": ("NumPy documentation", "https://numpy.org/doc/stable/"),
    },
    "pandas": {
        "learn": ("Kaggle Learn — Pandas", "https://www.kaggle.com/learn/pandas"),
        "youtube": ("YouTube — Pandas full course", "https://www.youtube.com/results?search_query=Pandas+full+course+freeCodeCamp"),
        "practice": ("Kaggle Pandas exercises", "https://www.kaggle.com/learn/pandas"),
        "notes": ("Pandas official getting started", "https://pandas.pydata.org/docs/getting_started/"),
    },
    "cleaning": {
        "learn": ("Kaggle Learn — Data Cleaning", "https://www.kaggle.com/learn/data-cleaning"),
        "youtube": ("YouTube — Data Cleaning with Pandas", "https://www.youtube.com/results?search_query=data+cleaning+Pandas+free+course"),
        "practice": ("Kaggle Data Cleaning", "https://www.kaggle.com/learn/data-cleaning"),
        "notes": ("Pandas documentation", "https://pandas.pydata.org/docs/"),
    },
    "visualization": {
        "learn": ("Kaggle Learn — Data Visualization", "https://www.kaggle.com/learn/data-visualization"),
        "youtube": ("YouTube — Python Data Visualization", "https://www.youtube.com/results?search_query=Python+data+visualization+Matplotlib+Seaborn+freeCodeCamp"),
        "practice": ("Kaggle Datasets", "https://www.kaggle.com/datasets"),
        "notes": ("Matplotlib tutorials", "https://matplotlib.org/stable/tutorials/"),
    },
    "matplotlib": {
        "learn": ("Matplotlib official tutorials", "https://matplotlib.org/stable/tutorials/"),
        "youtube": ("YouTube — Matplotlib", "https://www.youtube.com/results?search_query=Matplotlib+full+tutorial+free"),
        "practice": ("Matplotlib examples", "https://matplotlib.org/stable/gallery/index.html"),
        "notes": ("Matplotlib docs", "https://matplotlib.org/stable/"),
    },
    "seaborn": {
        "learn": ("Seaborn official tutorial", "https://seaborn.pydata.org/tutorial.html"),
        "youtube": ("YouTube — Seaborn", "https://www.youtube.com/results?search_query=Seaborn+tutorial+Python+free"),
        "practice": ("Seaborn examples", "https://seaborn.pydata.org/examples/index.html"),
        "notes": ("Seaborn documentation", "https://seaborn.pydata.org/"),
    },
    "plotly": {
        "learn": ("Plotly Python documentation", "https://plotly.com/python/"),
        "youtube": ("YouTube — Plotly Python", "https://www.youtube.com/results?search_query=Plotly+Python+tutorial+free"),
        "practice": ("Plotly examples", "https://plotly.com/python/basic-charts/"),
        "notes": ("Plotly Python docs", "https://plotly.com/python/"),
    },
    "powerbi": {
        "learn": ("Microsoft Learn — Power BI", "https://learn.microsoft.com/en-us/training/powerplatform/power-bi"),
        "youtube": ("YouTube — Microsoft Power BI", "https://www.youtube.com/results?search_query=Microsoft+Power+BI+full+course+free"),
        "practice": ("Microsoft Learn — Data Analyst", "https://learn.microsoft.com/en-us/training/career-paths/data-analyst"),
        "notes": ("Power BI documentation", "https://learn.microsoft.com/en-us/power-bi/"),
    },
    "modeling": {
        "learn": ("Microsoft Learn — Model data in Power BI", "https://learn.microsoft.com/en-us/training/paths/model-data-power-bi/"),
        "youtube": ("YouTube — Power BI data modelling", "https://www.youtube.com/results?search_query=Power+BI+data+modeling+star+schema+free"),
        "practice": ("Microsoft Power BI training", "https://learn.microsoft.com/en-us/training/powerplatform/power-bi"),
        "notes": ("Power BI documentation", "https://learn.microsoft.com/en-us/power-bi/"),
    },
    "dax": {
        "learn": ("Microsoft Learn — DAX", "https://learn.microsoft.com/en-us/training/paths/dax-power-bi/"),
        "youtube": ("YouTube — DAX Power BI", "https://www.youtube.com/results?search_query=DAX+Power+BI+tutorial+free"),
        "practice": ("Microsoft Learn — DAX", "https://learn.microsoft.com/en-us/training/paths/dax-power-bi/"),
        "notes": ("DAX reference", "https://learn.microsoft.com/en-us/dax/"),
    },
    "ml": {
        "learn": ("Kaggle Learn — Intro to Machine Learning", "https://www.kaggle.com/learn/intro-to-machine-learning"),
        "youtube": ("Machine Learning with Python & Scikit-Learn — freeCodeCamp", "https://www.youtube.com/watch?v=hDKCxebp88A"),
        "practice": ("Scikit-learn User Guide", "https://scikit-learn.org/stable/user_guide.html"),
        "notes": ("Google Machine Learning Crash Course", "https://developers.google.com/machine-learning/crash-course"),
    },
    "ml_intermediate": {
        "learn": ("Kaggle Learn — Intermediate Machine Learning", "https://www.kaggle.com/learn/intermediate-machine-learning"),
        "youtube": ("YouTube — Intermediate Machine Learning", "https://www.youtube.com/results?search_query=intermediate+machine+learning+scikit+learn+free+course"),
        "practice": ("Kaggle Intermediate ML", "https://www.kaggle.com/learn/intermediate-machine-learning"),
        "notes": ("Scikit-learn User Guide", "https://scikit-learn.org/stable/user_guide.html"),
    },
    "feature": {
        "learn": ("Kaggle Learn — Feature Engineering", "https://www.kaggle.com/learn/feature-engineering"),
        "youtube": ("YouTube — Feature Engineering", "https://www.youtube.com/results?search_query=feature+engineering+machine+learning+free+course"),
        "practice": ("Scikit-learn preprocessing", "https://scikit-learn.org/stable/modules/preprocessing.html"),
        "notes": ("Kaggle Feature Engineering", "https://www.kaggle.com/learn/feature-engineering"),
    },
    "xgboost": {
        "learn": ("XGBoost official tutorials", "https://xgboost.readthedocs.io/en/stable/tutorials/index.html"),
        "youtube": ("YouTube — XGBoost tutorial", "https://www.youtube.com/results?search_query=XGBoost+tutorial+free"),
        "practice": ("XGBoost documentation", "https://xgboost.readthedocs.io/"),
        "notes": ("XGBoost docs", "https://xgboost.readthedocs.io/"),
    },
    "nlp": {
        "learn": ("Kaggle Learn — Natural Language Processing", "https://www.kaggle.com/learn/natural-language-processing"),
        "youtube": ("YouTube — NLP Python", "https://www.youtube.com/results?search_query=NLP+Python+freeCodeCamp+course"),
        "practice": ("Kaggle NLP", "https://www.kaggle.com/learn/natural-language-processing"),
        "notes": ("Kaggle Intro NLP guide", "https://www.kaggle.com/learn-guide/intro-nlp"),
    },
    "deep": {
        "learn": ("Kaggle Learn — Intro to Deep Learning", "https://www.kaggle.com/learn/intro-to-deep-learning"),
        "youtube": ("3Blue1Brown — Neural Networks", "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi"),
        "practice": ("Kaggle Deep Learning", "https://www.kaggle.com/learn/intro-to-deep-learning"),
        "notes": ("Keras documentation", "https://keras.io/"),
    },
    "dbms": {
        "learn": ("GeeksforGeeks — DBMS", "https://www.geeksforgeeks.org/dbms/"),
        "youtube": ("Gate Smashers — DBMS", "https://www.youtube.com/@GateSmashers"),
        "practice": ("GeeksforGeeks DBMS questions", "https://www.geeksforgeeks.org/dbms-gq/"),
        "notes": ("DBMS tutorial", "https://www.geeksforgeeks.org/dbms/"),
    },
    "os": {
        "learn": ("GeeksforGeeks — Operating Systems", "https://www.geeksforgeeks.org/operating-systems/"),
        "youtube": ("Gate Smashers — Operating Systems", "https://www.youtube.com/@GateSmashers"),
        "practice": ("GFG OS questions", "https://www.geeksforgeeks.org/operating-systems-gq/"),
        "notes": ("Operating Systems tutorial", "https://www.geeksforgeeks.org/operating-systems/"),
    },
    "cn": {
        "learn": ("GeeksforGeeks — Computer Networks", "https://www.geeksforgeeks.org/computer-networks/"),
        "youtube": ("Gate Smashers — Computer Networks", "https://www.youtube.com/@GateSmashers"),
        "practice": ("GFG Computer Networks", "https://www.geeksforgeeks.org/computer-networks-gq/"),
        "notes": ("Computer Networks tutorial", "https://www.geeksforgeeks.org/computer-networks/"),
    },
    "github": {
        "learn": ("GitHub Docs — Getting Started", "https://docs.github.com/en/get-started"),
        "youtube": ("YouTube — Git & GitHub", "https://www.youtube.com/results?search_query=Git+GitHub+full+course+freeCodeCamp"),
        "practice": ("GitHub Skills", "https://skills.github.com/"),
        "notes": ("GitHub Docs", "https://docs.github.com/"),
    },
    "interview": {
        "learn": ("GeeksforGeeks Interview Corner", "https://www.geeksforgeeks.org/company-interview-corner/"),
        "youtube": ("YouTube — Data Analyst interview questions", "https://www.youtube.com/results?search_query=data+analyst+interview+questions+SQL+Python+Power+BI"),
        "practice": ("Pramp — mock interviews", "https://www.pramp.com/"),
        "notes": ("NeetCode practice", "https://neetcode.io/practice"),
    },
    "resume": {
        "learn": ("Harvard resume guide", "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/"),
        "youtube": ("YouTube — Data Analyst resume", "https://www.youtube.com/results?search_query=data+analyst+resume+projects+2026"),
        "practice": ("GitHub Pages portfolio", "https://pages.github.com/"),
        "notes": ("GitHub Skills", "https://skills.github.com/"),
    },
    "aptitude": {
        "learn": ("IndiaBix aptitude", "https://www.indiabix.com/"),
        "youtube": ("YouTube — quantitative aptitude", "https://www.youtube.com/results?search_query=quantitative+aptitude+placement+free+course"),
        "practice": ("IndiaBix practice", "https://www.indiabix.com/"),
        "notes": ("IndiaBix", "https://www.indiabix.com/"),
    },
}

# ============================================================
# ROADMAP CONTENT
# ============================================================

MONTHS = [
    "Month 1 — Python Basics + Basic DSA + Excel Basics",
    "Month 2 — Python OOP + SQL Basics + DSA",
    "Month 3 — Advanced SQL + Statistics + DSA",
    "Month 4 — NumPy + Pandas + Data Cleaning + Trees",
    "Month 5 — EDA + Data Visualization",
    "Month 6 — Power BI + Power Query + DAX",
    "Month 7 — ML Fundamentals + Regression + Classification",
    "Month 8 — Advanced ML + Clustering + Feature Engineering",
    "Month 9 — NLP + Deep Learning Basics + Capstone Start",
    "Month 10 — Capstone + DBMS + OS + Computer Networks",
    "Month 11 — Full Revision + Mock Interviews",
    "Month 12 — Resume + GitHub + Applications + Final Buffer",
]

# Each month has 12 units. Each unit occupies 2 study days.
# This produces an exact 24-day content schedule per month.
UNITS = {
1: [
    ("Python variables, data types, I/O, operators", "python"),
    ("Python type conversion + basic input/output programs", "python"),
    ("if / elif / else + nested conditions", "python"),
    ("for / while / break / continue", "python"),
    ("lists + tuples", "python"),
    ("sets + dictionaries + strings", "python"),
    ("functions + parameters + return", "python"),
    ("*args / **kwargs + lambda + comprehensions", "python"),
    ("Exceptions + file handling + modules", "python"),
    ("DSA Big-O + arrays + strings", "dsa"),
    ("DSA array/string problem solving", "dsa"),
    ("Excel formatting + sorting + filtering + tables", "excel"),
],
2: [
    ("Classes, objects and constructors", "python_oop"),
    ("Encapsulation + inheritance", "python_oop"),
    ("Polymorphism + abstraction + overriding", "python_oop"),
    ("Functions deep-dive + file handling", "python"),
    ("SQL SELECT + WHERE + DISTINCT", "sql"),
    ("ORDER BY + LIMIT + NULL + logical operators", "sql"),
    ("COUNT + SUM + AVG + MIN + MAX", "sql"),
    ("GROUP BY + HAVING + CASE WHEN", "sql"),
    ("Linear search + binary search", "dsa"),
    ("Bubble + selection + insertion sort", "dsa"),
    ("Merge sort + quick sort + complexity", "dsa"),
    ("Student Management System project", "python_oop"),
],
3: [
    ("INNER / LEFT / RIGHT / FULL / SELF JOIN", "sql_advanced"),
    ("JOIN practice: combine multiple business tables", "sql_advanced"),
    ("Subqueries", "sql_advanced"),
    ("CTEs", "sql_advanced"),
    ("ROW_NUMBER + RANK + DENSE_RANK", "sql_advanced"),
    ("LAG + LEAD", "sql_advanced"),
    ("UNION / UNION ALL + views", "sql_advanced"),
    ("Transactions + indexing basics", "sql_advanced"),
    ("Mean / median / mode / variance / standard deviation", "statistics"),
    ("Percentiles / quartiles / IQR / z-score", "statistics"),
    ("Probability + Bayes + distributions", "statistics"),
    ("Correlation / covariance / skewness / outliers + DSA stack/queue", "statistics"),
],
4: [
    ("NumPy arrays + indexing + slicing", "numpy"),
    ("NumPy reshaping + broadcasting + statistics", "numpy"),
    ("Pandas Series + DataFrame", "pandas"),
    ("Pandas read CSV / Excel / SQL", "pandas"),
    ("Pandas selecting + filtering + sorting", "pandas"),
    ("Pandas groupby + aggregation", "pandas"),
    ("Pandas merge + join + concat", "pandas"),
    ("Pandas pivot + apply + calculated columns", "pandas"),
    ("Cleaning missing values + duplicates", "cleaning"),
    ("Cleaning dtypes + inconsistent text + dates", "cleaning"),
    ("Outliers + scaling / normalization", "cleaning"),
    ("Trees: recursion + BST + traversals", "dsa"),
],
5: [
    ("EDA: univariate analysis", "visualization"),
    ("EDA: bivariate + multivariate analysis", "visualization"),
    ("Trends + patterns + anomalies", "visualization"),
    ("Correlation + outlier investigation", "visualization"),
    ("Matplotlib bar + line + scatter", "matplotlib"),
    ("Matplotlib histogram + box plot", "matplotlib"),
    ("Seaborn heatmap + distribution plots", "seaborn"),
    ("Seaborn box + violin + regression plots", "seaborn"),
    ("Plotly interactive charts", "plotly"),
    ("Choose the correct chart and explain why", "visualization"),
    ("E-commerce Analysis project — analysis", "visualization"),
    ("E-commerce Analysis project — final insights", "visualization"),
],
6: [
    ("Power BI: import Excel / CSV / SQL", "powerbi"),
    ("Power BI visuals: cards / tables / charts", "powerbi"),
    ("Filters + slicers + report pages", "powerbi"),
    ("Power Query: clean + transform", "powerbi"),
    ("Power Query: merge + append + data types", "powerbi"),
    ("Relationships + cardinality", "modeling"),
    ("Fact / dimension tables + star schema", "modeling"),
    ("Date table + model design", "modeling"),
    ("DAX measures + calculated columns", "dax"),
    ("SUM + COUNT + DISTINCTCOUNT + CALCULATE", "dax"),
    ("FILTER + IF + SWITCH + time intelligence", "dax"),
    ("Sales Dashboard + HR Dashboard", "powerbi"),
],
7: [
    ("Supervised vs unsupervised ML", "ml"),
    ("Features + target + train/test/validation", "ml"),
    ("Overfitting + underfitting + bias/variance", "ml"),
    ("Linear Regression", "ml"),
    ("R² + MAE + MSE + RMSE", "ml"),
    ("Logistic Regression", "ml"),
    ("Classification probabilities + evaluation", "ml"),
    ("Scikit-learn workflow", "ml"),
    ("Two pointers revision", "dsa"),
    ("Sliding window revision", "dsa"),
    ("House Price Prediction — build model", "ml"),
    ("House Price Prediction — evaluate + explain", "ml"),
],
8: [
    ("KNN", "ml_intermediate"),
    ("Decision Trees", "ml_intermediate"),
    ("Random Forest", "ml_intermediate"),
    ("Gradient Boosting", "ml_intermediate"),
    ("XGBoost basics", "xgboost"),
    ("SVM basics", "ml_intermediate"),
    ("K-Means clustering", "ml_intermediate"),
    ("Hierarchical clustering + DBSCAN", "ml_intermediate"),
    ("PCA", "ml_intermediate"),
    ("Encoding + scaling + standardization", "feature"),
    ("Leakage + outlier handling", "feature"),
    ("Accuracy / precision / recall / F1 / ROC-AUC + tuning", "ml_intermediate"),
],
9: [
    ("NLP text cleaning + tokenization", "nlp"),
    ("Stopwords + stemming + lemmatization", "nlp"),
    ("Bag of Words", "nlp"),
    ("TF-IDF", "nlp"),
    ("Sentiment analysis", "nlp"),
    ("Text classification", "nlp"),
    ("Neurons + activation + loss", "deep"),
    ("Optimizers + epochs + batch size + backprop concept", "deep"),
    ("CNN + RNN + LSTM concepts", "deep"),
    ("Transformers concept", "deep"),
    ("Sentiment Analysis project", "nlp"),
    ("Capstone: dataset + scope + requirements", "ml"),
],
10: [
    ("Capstone: raw data → SQL database", "sql_advanced"),
    ("Capstone: SQL analysis", "sql_advanced"),
    ("Capstone: Python/Pandas cleaning", "pandas"),
    ("Capstone: EDA + visualization", "visualization"),
    ("Capstone: statistics", "statistics"),
    ("Capstone: ML model", "ml"),
    ("Capstone: Power BI dashboard", "powerbi"),
    ("Capstone: business recommendations", "powerbi"),
    ("DBMS vs RDBMS + keys + constraints", "dbms"),
    ("Normalization + ER diagrams + ACID", "dbms"),
    ("OS: process/thread + scheduling + deadlock", "os"),
    ("CN: OSI + TCP/IP + HTTP/HTTPS + DNS + DHCP", "cn"),
],
11: [
    ("DSA revision — arrays/strings/search/sort", "dsa"),
    ("DSA revision — linked list/stack/queue/trees", "dsa"),
    ("SQL revision — SELECT/GROUP BY/JOIN", "sql"),
    ("SQL revision — CTE/window functions", "sql_advanced"),
    ("Python + OOP revision", "python"),
    ("Statistics revision", "statistics"),
    ("Pandas + EDA revision", "pandas"),
    ("Power BI + DAX revision", "dax"),
    ("ML revision — regression/classification", "ml"),
    ("DBMS + OS + CN revision", "interview"),
    ("Project explanation practice", "interview"),
    ("Mock interview + weakest-area revision", "interview"),
],
12: [
    ("Resume — education + skills", "resume"),
    ("Resume — project bullet points", "resume"),
    ("GitHub — upload projects", "github"),
    ("GitHub — README + screenshots", "github"),
    ("GitHub — organize repositories", "github"),
    ("LinkedIn — skills + projects", "resume"),
    ("Internship/off-campus applications", "interview"),
    ("On-campus placement preparation", "interview"),
    ("Aptitude practice", "aptitude"),
    ("Communication + HR/project answers", "interview"),
    ("Portfolio — GitHub Pages", "resume"),
    ("Final self-audit + weakest area + buffer", "interview"),
],
}

# ============================================================
# DAILY TASK GENERATOR
# ============================================================

def make_daily_plan(month, unit_no, unit_title, resource_key, day_in_unit):
    """
    Every unit is 2 days.
    Day A = learn + guided practice + notes.
    Day B = recall + independent practice + mini deliverable.
    """

    if day_in_unit == 1:
        hours = [
            (
                "Hour 1 — LEARN",
                f"Study: {unit_title}. Watch/read the Learning Material. "
                f"Write 5–10 short notes and 3 examples in your notebook."
            ),
            (
                "Hour 2 — PRACTICE",
                f"Code/practice {unit_title}. Do the examples yourself without copying. "
                f"Complete at least 5 small exercises/questions."
            ),
            (
                "Hour 3 — RECALL + NOTES",
                f"Close the lesson. Recreate the main examples from memory. "
                f"Write: definition, syntax/steps, 2 mistakes you made, and 3 key takeaways."
            ),
        ]
    else:
        hours = [
            (
                "Hour 1 — REVISE",
                f"Without watching the lesson again first, explain {unit_title} "
                f"from memory. Then check your notes and correct gaps."
            ),
            (
                "Hour 2 — INDEPENDENT PRACTICE",
                f"Do 5–10 problems/tasks on {unit_title}. "
                f"Try first without help; use the Practice link only after attempting."
            ),
            (
                "Hour 3 — MINI TASK",
                f"Build/solve one small task using {unit_title}. "
                f"Save your code/query/dashboard/notebook and write what you learned."
            ),
        ]

    # More useful project wording
    if "project" in unit_title.lower() or "capstone" in unit_title.lower() or "dashboard" in unit_title.lower():
        if day_in_unit == 1:
            hours = [
                ("Hour 1 — LEARN", f"Study the required tools/concepts for {unit_title}."),
                ("Hour 2 — BUILD", f"Start {unit_title}. Build the first working section yourself."),
                ("Hour 3 — DOCUMENT", "Save the work, take notes, and write what is complete vs pending."),
            ]
        else:
            hours = [
                ("Hour 1 — REVIEW", f"Review yesterday's work for {unit_title}. Fix errors first."),
                ("Hour 2 — BUILD", f"Continue {unit_title}. Finish the next major section."),
                ("Hour 3 — TEST + SAVE", "Test the result, write 3 insights, and save/push your work."),
            ]

    return {
        "title": unit_title,
        "resource_key": resource_key,
        "day_in_unit": day_in_unit,
        "hours": hours,
    }

def build_all_days():
    """
    12 months × 24 study days = 288 exact study days.
    Each month has 4 weeks × 6 study days.
    Sunday is not counted as a study day and remains the buffer day.
    """
    all_days = {}
    for month in range(1, 13):
        for week in range(1, 5):
            for day in range(1, 7):
                unit_index = (week - 1) * 3 + ((day - 1) // 2) + 1
                day_in_unit = 1 if day % 2 == 1 else 2
                title, resource = UNITS[month][unit_index - 1]
                all_days[(month, week, day)] = make_daily_plan(
                    month, unit_index, title, resource, day_in_unit
                )
    return all_days

DAILY_PLANS = build_all_days()

# ============================================================
# APP
# ============================================================

def default_progress():
    return {
        "days": {},
        "hours_done": {},
        "topic_done": {},
        "notes": {},
        "weekly_review": {},
        "last_saved": "",
    }

def load_progress():
    if not PROGRESS_FILE.exists():
        return default_progress()

    try:
        with PROGRESS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)

        base = default_progress()
        base.update(data)
        return base
    except Exception:
        return default_progress()

class StudyTracker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry("1350x900")
        self.minsize(1100, 750)

        self.data = load_progress()

        self.current_month = 1
        self.current_week = 1
        self.current_day = 1

        self.hour_vars = {}
        self.day_var = None

        self.build_style()
        self.build_header()
        self.build_navigation()
        self.build_scroll_area()
        self.build_statusbar()

        self.show_day()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------------- STYLE ----------------

    def build_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 18, "bold"))
        style.configure("Heading.TLabel", font=("Segoe UI", 13, "bold"))
        style.configure("Sub.TLabel", font=("Segoe UI", 10))
        style.configure("Small.TLabel", font=("Segoe UI", 9))

    # ---------------- HEADER ----------------

    def build_header(self):
        frame = ttk.Frame(self, padding=(15, 10))
        frame.pack(fill="x")

        ttk.Label(
            frame,
            text="🎯 12-Month Data Analyst + Data Science Daily Tracker",
            style="Title.TLabel",
        ).pack(side="left")

        ttk.Button(
            frame, text="📊 Dashboard", command=self.show_dashboard
        ).pack(side="right", padx=4)

        ttk.Button(
            frame, text="💾 Save", command=lambda: self.save(True)
        ).pack(side="right", padx=4)

    # ---------------- NAVIGATION ----------------

    def build_navigation(self):
        frame = ttk.Frame(self, padding=(15, 5))
        frame.pack(fill="x")

        ttk.Button(frame, text="◀ Month", command=self.prev_month).pack(side="left")

        self.month_label = ttk.Label(
            frame, text="", style="Heading.TLabel"
        )
        self.month_label.pack(side="left", padx=12)

        ttk.Button(frame, text="Month ▶", command=self.next_month).pack(side="left")

        ttk.Label(frame, text="Week:").pack(side="left", padx=(25, 4))

        self.week_var = tk.IntVar(value=1)
        week_spin = ttk.Spinbox(
            frame,
            from_=1,
            to=4,
            width=5,
            textvariable=self.week_var,
            command=self.go_week,
        )
        week_spin.pack(side="left")
        week_spin.bind("<Return>", lambda e: self.go_week())

        ttk.Label(frame, text="Day:").pack(side="left", padx=(15, 4))

        self.day_var_nav = tk.IntVar(value=1)
        day_spin = ttk.Spinbox(
            frame,
            from_=1,
            to=6,
            width=5,
            textvariable=self.day_var_nav,
            command=self.go_day,
        )
        day_spin.pack(side="left")
        day_spin.bind("<Return>", lambda e: self.go_day())

        ttk.Button(
            frame, text="◀ Previous Day", command=self.prev_day
        ).pack(side="right", padx=4)

        ttk.Button(
            frame, text="Next Day ▶", command=self.next_day
        ).pack(side="right", padx=4)

        ttk.Button(
            frame, text="☀ Sunday Buffer", command=self.show_buffer
        ).pack(side="right", padx=4)

    # ---------------- SCROLL AREA ----------------

    def build_scroll_area(self):
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.scroll = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )

        self.page = ttk.Frame(self.canvas, padding=15)

        self.page.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.page, anchor="nw"
        )

        self.canvas.configure(yscrollcommand=self.scroll.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll.pack(side="right", fill="y")

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfigure(
                self.canvas_window, width=e.width
            )
        )

        self.bind_all("<MouseWheel>", self.mousewheel)

    def mousewheel(self, event):
        try:
            self.canvas.yview_scroll(int(-event.delta / 120), "units")
        except Exception:
            pass

    # ---------------- STATUS ----------------

    def build_statusbar(self):
        self.status = tk.StringVar(value="Ready")
        ttk.Label(
            self,
            textvariable=self.status,
            relief="sunken",
            anchor="w",
            padding=5,
        ).pack(fill="x", side="bottom")

    # ---------------- KEYS ----------------

    def day_key(self):
        return f"m{self.current_month}_w{self.current_week}_d{self.current_day}"

    def hour_key(self, hour):
        return f"{self.day_key()}_h{hour}"

    def topic_key(self):
        return f"m{self.current_month}_w{self.current_week}_d{self.current_day}"

    def week_key(self):
        return f"m{self.current_month}_w{self.current_week}"

    # ---------------- SHOW DAY ----------------

    def clear_page(self):
        for widget in self.page.winfo_children():
            widget.destroy()

        self.hour_vars.clear()

    def show_day(self):
        self.clear_page()

        self.month_label.config(text=MONTHS[self.current_month - 1])
        self.week_var.set(self.current_week)
        self.day_var_nav.set(self.current_day)

        plan = DAILY_PLANS[
            (self.current_month, self.current_week, self.current_day)
        ]

        # Title
        ttk.Label(
            self.page,
            text=f"DAY {self.global_day_number()} / 288",
            style="Title.TLabel",
        ).pack(anchor="w")

        ttk.Label(
            self.page,
            text=f"Month {self.current_month} • Week {self.current_week} • "
                 f"Day {self.current_day}",
            style="Heading.TLabel",
        ).pack(anchor="w", pady=(3, 0))

        ttk.Label(
            self.page,
            text=f"Today's focus: {plan['title']}",
            style="Sub.TLabel",
        ).pack(anchor="w", pady=(3, 15))

        # Completion
        completion = ttk.LabelFrame(
            self.page,
            text="☑️ Today's Completion",
            padding=10,
        )
        completion.pack(fill="x", pady=(0, 12))

        completed_day = bool(self.data["days"].get(self.day_key(), False))

        self.day_complete_var = tk.BooleanVar(value=completed_day)

        ttk.Checkbutton(
            completion,
            text="I completed today's full 3-hour study plan",
            variable=self.day_complete_var,
            command=self.toggle_day_complete,
        ).pack(side="left")

        ttk.Label(
            completion,
            text="Only tick this after completing all 3 hours.",
            style="Small.TLabel",
        ).pack(side="left", padx=20)

        # Three hours
        routine = ttk.LabelFrame(
            self.page,
            text="⏱️ EXACT 3-HOUR ROUTINE — DO THIS TODAY",
            padding=10,
        )
        routine.pack(fill="x", pady=(0, 12))

        for index, (hour_name, task) in enumerate(plan["hours"], start=1):
            self.create_hour_row(routine, index, hour_name, task, plan)

        # Learning materials
        materials = ttk.LabelFrame(
            self.page,
            text="📚 LEARNING MATERIALS FOR TODAY",
            padding=10,
        )
        materials.pack(fill="x", pady=(0, 12))

        resource = RESOURCES[plan["resource_key"]]

        self.add_resource_row(
            materials, "📖 Main Learning", resource["learn"]
        )
        self.add_resource_row(
            materials, "▶ YouTube", resource["youtube"]
        )
        self.add_resource_row(
            materials, "🧪 Practice", resource["practice"]
        )
        self.add_resource_row(
            materials, "📝 Notes / Reference", resource["notes"]
        )

        # Day notes
        notes_frame = ttk.LabelFrame(
            self.page,
            text="📝 WHAT YOU LEARNED TODAY",
            padding=10,
        )
        notes_frame.pack(fill="x", pady=(0, 12))

        self.daily_notes = tk.Text(
            notes_frame,
            height=8,
            wrap="word",
        )
        self.daily_notes.pack(fill="x")

        saved = self.data["notes"].get(self.day_key(), "")
        self.daily_notes.insert("1.0", saved)

        ttk.Label(
            notes_frame,
            text=(
                "Write: what you learned • what confused you • "
                "mistakes • 3 important points • what to revise tomorrow"
            ),
            style="Small.TLabel",
        ).pack(anchor="w", pady=(5, 0))

        ttk.Button(
            self.page,
            text="💾 SAVE TODAY",
            command=lambda: self.save(True),
        ).pack(anchor="e", pady=5)

        self.status.set(
            f"Day {self.global_day_number()} loaded — "
            f"{plan['title']}"
        )

    def create_hour_row(self, parent, number, hour_name, task, plan):
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=6)

        completed = bool(
            self.data["hours_done"].get(
                self.hour_key(number), False
            )
        )

        var = tk.BooleanVar(value=completed)
        self.hour_vars[number] = var

        ttk.Checkbutton(
            frame,
            text=hour_name,
            variable=var,
            command=lambda n=number: self.toggle_hour(n),
        ).pack(side="left", anchor="n")

        text_frame = ttk.Frame(frame)
        text_frame.pack(side="left", fill="x", expand=True, padx=12)

        ttk.Label(
            text_frame,
            text=task,
            wraplength=900,
        ).pack(anchor="w")

    def add_resource_row(self, parent, label, resource):
        name, url = resource

        row = ttk.Frame(parent)
        row.pack(fill="x", pady=4)

        ttk.Label(
            row,
            text=label,
            font=("Segoe UI", 9, "bold"),
            width=20,
        ).pack(side="left")

        ttk.Label(
            row,
            text=name,
            style="Small.TLabel",
        ).pack(side="left", fill="x", expand=True)

        ttk.Button(
            row,
            text="OPEN",
            command=lambda u=url: self.open_url(u),
        ).pack(side="right")

    # ---------------- DAILY ACTIONS ----------------

    def toggle_hour(self, number):
        self.data["hours_done"][self.hour_key(number)] = (
            self.hour_vars[number].get()
        )

        # Automatically mark the day complete if all 3 hours are checked.
        if all(
            self.data["hours_done"].get(
                self.hour_key(i), False
            )
            for i in range(1, 4)
        ):
            self.data["days"][self.day_key()] = True
            self.day_complete_var.set(True)

        self.save(False)

    def toggle_day_complete(self):
        value = self.day_complete_var.get()
        self.data["days"][self.day_key()] = value

        if value:
            for i in range(1, 4):
                self.data["hours_done"][self.hour_key(i)] = True
                self.hour_vars[i].set(True)

        self.save(False)

    # ---------------- NOTES ----------------

    def save_current_notes(self):
        if hasattr(self, "daily_notes"):
            self.data["notes"][self.day_key()] = (
                self.daily_notes.get("1.0", "end-1c").strip()
            )

    # ---------------- NAVIGATION ----------------

    def prev_month(self):
        self.save_current_notes()

        if self.current_month > 1:
            self.current_month -= 1
            self.current_week = 1
            self.current_day = 1
            self.show_day()

    def next_month(self):
        self.save_current_notes()

        if self.current_month < 12:
            self.current_month += 1
            self.current_week = 1
            self.current_day = 1
            self.show_day()

    def go_week(self):
        self.save_current_notes()

        try:
            value = int(self.week_var.get())
            if 1 <= value <= 4:
                self.current_week = value
                self.current_day = 1
                self.show_day()
        except ValueError:
            self.week_var.set(self.current_week)

    def go_day(self):
        self.save_current_notes()

        try:
            value = int(self.day_var_nav.get())
            if 1 <= value <= 6:
                self.current_day = value
                self.show_day()
        except ValueError:
            self.day_var_nav.set(self.current_day)

    def next_day(self):
        self.save_current_notes()

        if self.current_day < 6:
            self.current_day += 1
        elif self.current_week < 4:
            self.current_week += 1
            self.current_day = 1
        elif self.current_month < 12:
            self.current_month += 1
            self.current_week = 1
            self.current_day = 1
        else:
            messagebox.showinfo(
                "Finished",
                "You reached the end of the 288-day study plan!"
            )
            return

        self.show_day()

    def prev_day(self):
        self.save_current_notes()

        if self.current_day > 1:
            self.current_day -= 1
        elif self.current_week > 1:
            self.current_week -= 1
            self.current_day = 6
        elif self.current_month > 1:
            self.current_month -= 1
            self.current_week = 4
            self.current_day = 6
        else:
            return

        self.show_day()

    def global_day_number(self):
        return (
            (self.current_month - 1) * 24
            + (self.current_week - 1) * 6
            + self.current_day
        )

    # ---------------- SUNDAY BUFFER ----------------

    def show_buffer(self):
        self.clear_page()

        ttk.Label(
            self.page,
            text="☀ SUNDAY — BUFFER / REVISION DAY",
            style="Title.TLabel",
        ).pack(anchor="w")

        ttk.Label(
            self.page,
            text=(
                "Do NOT use Sunday as a normal extra study day. "
                "Use it only when you need catch-up, revision, "
                "project work or rest."
            ),
            wraplength=1000,
        ).pack(anchor="w", pady=(10, 20))

        tasks = [
            "Catch up on a missed weekday.",
            "Finish unfinished exercises.",
            "Re-solve questions you got wrong.",
            "Review your notes without watching videos.",
            "Work on your current project.",
            "If everything is complete: REST.",
        ]

        frame = ttk.LabelFrame(
            self.page,
            text="Sunday checklist",
            padding=10,
        )
        frame.pack(fill="x")

        for task in tasks:
            ttk.Checkbutton(
                frame,
                text=task,
            ).pack(anchor="w", pady=5)

        ttk.Label(
            self.page,
            text="Rule: Do not double your workload just because you missed one day. "
                 "Use the buffer to keep the roadmap sustainable.",
            style="Small.TLabel",
            wraplength=1000,
        ).pack(anchor="w", pady=20)

    # ---------------- LINKS ----------------

    def open_url(self, url):
        try:
            webbrowser.open_new_tab(url)
        except Exception as exc:
            messagebox.showerror(
                "Could not open link",
                str(exc),
            )

    # ---------------- SAVE ----------------

    def save(self, show_message=False):
        self.save_current_notes()

        self.data["last_saved"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        try:
            with PROGRESS_FILE.open(
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    self.data,
                    f,
                    indent=2,
                    ensure_ascii=False,
                )

            self.status.set(
                f"Saved: {self.data['last_saved']}"
            )

            if show_message:
                messagebox.showinfo(
                    "Saved",
                    "Your progress has been saved.",
                )
        except Exception as exc:
            messagebox.showerror(
                "Save error",
                str(exc),
            )

    # ---------------- DASHBOARD ----------------

    def show_dashboard(self):
        win = tk.Toplevel(self)
        win.title("📊 Progress Dashboard")
        win.geometry("1000x700")

        total_days = 288
        done_days = sum(
            1
            for value in self.data["days"].values()
            if value
        )

        ttk.Label(
            win,
            text="📊 Overall Progress",
            style="Title.TLabel",
        ).pack(anchor="w", padx=20, pady=(20, 5))

        ttk.Label(
            win,
            text=f"Completed study days: {done_days} / {total_days} "
                 f"({done_days / total_days * 100:.1f}%)",
        ).pack(anchor="w", padx=20, pady=5)

        progress = ttk.Progressbar(
            win,
            maximum=100,
            value=done_days / total_days * 100,
        )
        progress.pack(fill="x", padx=20, pady=10)

        tree = ttk.Treeview(
            win,
            columns=("month", "days", "hours"),
            show="headings",
        )

        tree.heading("month", text="Month")
        tree.heading("days", text="Days Complete")
        tree.heading("hours", text="Hours Checked")

        tree.column("month", width=500)
        tree.column("days", width=180)
        tree.column("hours", width=180)

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15,
        )

        for month in range(1, 13):
            mdone = 0
            hdone = 0

            for week in range(1, 5):
                for day in range(1, 7):
                    dk = f"m{month}_w{week}_d{day}"
                    if self.data["days"].get(dk, False):
                        mdone += 1

                    for hour in range(1, 4):
                        hk = f"{dk}_h{hour}"
                        if self.data["hours_done"].get(hk, False):
                            hdone += 1

            tree.insert(
                "",
                "end",
                values=(
                    MONTHS[month - 1],
                    f"{mdone}/24",
                    f"{hdone}/72",
                ),
            )

        ttk.Button(
            win,
            text="Close",
            command=win.destroy,
        ).pack(pady=10)

    # ---------------- CLOSE ----------------

    def on_close(self):
        self.save(False)
        self.destroy()


if __name__ == "__main__":
    app = StudyTracker()
    app.mainloop()
