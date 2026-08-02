# Student Score Prediction System

🚀 **AI & Machine Learning Internship Capstone Project**  
**Company:** [Codomax Digital Solutions](https://in.linkedin.com/company/codomaxdigital)  
**Participant:** Atharv Gangwar  
**Project Goal:** Build a machine learning predictive model to determine student examination scores based on their daily study hours.

---

## 📌 Project Overview
This repository contains the complete daily tasks and code developed during the **Codomax AI & ML Internship**. The final product is a **Student Score Prediction System** built on **Simple Linear Regression** ($\text{Scores} = \beta_1 \times \text{Hours\_Studied} + \beta_0$). It guides the user from raw data loading, preprocessing, visual exploration, and statistical analysis, through model training, metric evaluation, and finally, deployment as an interactive prediction script.

### 📊 Model Performance Highlights
*   **Pearson Correlation ($R$):** $0.98$ (indicating an exceptionally strong linear relationship)
*   **Mean Absolute Error (MAE):** $3.92$ marks
*   **Root Mean Squared Error (RMSE):** $4.35$ marks
*   **R-squared ($R^2$) Score:** **$96.78\%$** (meaning study hours explain $96.78\%$ of the variance in student grades)

---

## 📂 Repository Directory Structure

```text
Codomax-Internship/
├── LICENSE
├── README.md                          # Main repository documentation
├── Day_1/                             # Environment Verification
│   ├── Day_1_Codomax.ipynb
│   ├── main.py                        # Verification script
│   └── Terminal_result.png
├── Day_2/                             # Core Python Principles
│   ├── Variable_and_datatype.py
│   ├── Operators.py
│   ├── Conditional_Loops.py
│   ├── While_Loops.py
│   ├── Reusable_Functions.py
│   └── *.png                          # Script execution captures
├── Day_3/                             # Matrix Operations (NumPy)
│   └── Day_3_Codomax.ipynb
├── Day_4/                             # Data Exploration (Pandas)
│   ├── student_scores.csv
│   └── Day_4_Codomax.ipynb
├── Day_5/                             # Data Preprocessing
│   ├── student_scores_dirty.csv
│   ├── student_scores_cleaned.csv
│   └── Day_5_Codomax.ipynb
├── Day_6/                             # Basic Visualizations (Matplotlib)
│   ├── Day_6_Codomax.ipynb
│   ├── bar_chart.png
│   ├── scatter_plot.png
│   └── line_chart.png
├── Day_7/                             # Statistical & Advanced Visualization
│   ├── student_scores.csv
│   └── Day_7_Codomax.ipynb
├── Day_8/                             # Model Building & Training
│   ├── student_scores.csv
│   └── Day_8_Codomax.ipynb
├── Day_9/                             # Predicting Test Cases
│   ├── student_scores.csv
│   └── Day_9_Codomax.ipynb
├── Day_10/                            # Model Performance Evaluation
│   ├── student_scores.csv
│   └── Day_10_Codomax.ipynb
├── Day_11/                            # Prediction Application
│   ├── student_scores.csv
│   ├── Day_11_Codomax.ipynb           # Interactive Colab app
│   └── prediction_app.py              # Standalone console app
├── Day_12/                            # Formatting & Code Consolidation
│   ├── student_scores.csv
│   └── Day_12_Codomax.ipynb           # Master project notebook
├── Day_13/                            # Documentation
│   ├── github_guide.txt               # Instruction guide for GitHub uploads
│   └── (This README.md)
└── Day_14/                            # Final Submission Validation
    └── Day_14_Submission.md           # Submission checklist log
```

---

## 🗓️ 14-Day Internship Roadmap

### **Phase 1: Foundations & Environments**
*   **Day 1: Development Setup**
    *   Checked OS compatibility, installed Python, Git, VS Code CLI.
    *   Created our first Jupyter notebook and plotted a line chart using `matplotlib`.
*   **Day 2: Python Fundamentals**
    *   Explored standard variables, datatypes, operators, conditionals, functions, and loop controls.
    *   Captured execution terminal screen captures.
*   **Day 3: Matrix Operations**
    *   Practiced array generation, slicing, and index mapping using the `NumPy` library.

### **Phase 2: Data Preprocessing & Visualization**
*   **Day 4: Pandas Integration**
    *   Imported Pandas, loaded the initial student scores dataset, and analyzed columns, shapes, and types.
*   **Day 5: Data Cleaning**
    *   Addressed missing (null) items and duplicated rows in `student_scores_dirty.csv`, producing a clean CSV.
*   **Day 6: Basic Data Visualization**
    *   Plotted bar charts, line graphs, and scatter plots using `matplotlib.pyplot` to visually inspect study hours vs scores.
*   **Day 7: Advanced Visualization & Analysis**
    *   Created Seaborn regression plots and generated correlation matrix coefficients ($r = 0.98$).

### **Phase 3: Model Building & Evaluation**
*   **Day 8: Model Training**
    *   Configured OLS Linear Regression, split data into 80% train / 20% test, and trained the regression parameters using Scikit-Learn.
*   **Day 9: Score Prediction**
    *   Generated predicted test scores and evaluated sample study inputs (e.g. 7 study hours predicts 70.60%).
*   **Day 10: Model Evaluation**
    *   Evaluated quality using standard metrics: MAE (3.92), MSE (18.94), RMSE (4.35), and $R^2$ (0.9678).

### **Phase 4: Optimization, Deployment & Documentation**
*   **Day 11: Deployment (Prediction App)**
    *   Wrote an interactive notebook script using `input()` and a standalone CLI python executable `prediction_app.py` for user testing.
*   **Day 12: Formatting & Consolidation**
    *   Assembled all daily milestones into a single consolidated master notebook (`Day_12_Codomax.ipynb`) with standard markdown math formulations.
*   **Day 13: GitHub Documentation**
    *   Constructed a detailed repository readme detailing our daily log and system metrics, and wrote a GitHub upload instruction guide (`Day_13/github_guide.txt`).
*   **Day 14: Final Submission**
    *   Validated directory compliance and prepared files for the submission review.

---

## 🛠️ How to Run the Prediction App

You can execute the prediction system in two ways:

### Method A: Standalone Console Script (Local Terminal)
No special environment is required. You can run the app with standard Python 3.
```bash
# Navigate to the Day 11 directory
cd Day_11

# Run the executable script
python3 prediction_app.py
```
*Features:* Prompts for study hours, prints the capped score (0-100), offers qualitative feedback, and loops until you type `q`.

### Method B: Google Colab (Cloud Notebook)
1.  Upload `Day_11_Codomax.ipynb` and `student_scores.csv` to Google Drive or open directly.
2.  Click **Run All** in Google Colab.
3.  The interactive code cell will prompt you for study hours inside the browser interface.

---

## 📜 License
This project is open-source and licensed under the MIT License. See [LICENSE](file:///Users/atharvgangwar/Desktop/Codomax-Internship/LICENSE) for details.
