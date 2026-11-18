# AI-101 Machine Learning Assignment: Training ML Models on Three Data Modalities

**Course:** AI-101: Introduction to Artificial Intelligence (Fall 2026)  
**Institution:** Department of Intelligent Systems, The University of Lahore  
**Instructor:** Dr. Muhammad Awais (AI Architect, Department of Intelligent Systems)  

---

## Student Information

| Field | Detail |
| :--- | :--- |
| **Student Name** | Muhammad Awais |
| **Roll Number** | 70176490 |
| **Section** | Section A |
| **Degree Program** | Bachelor of Science in Embedded Systems & Artificial Intelligence |
| **Repository URL** | [https://github.com/MuhammadAwais-70176490/AI101-ML-Assignment-70176490](https://github.com/MuhammadAwais-70176490/AI101-ML-Assignment-70176490) |

---

## Tasks Overview & Completion Matrix

This repository contains the complete implementation, executed notebooks, extracted figures, dataset documentation, and 2-page double-column IEEE reports for **all 9 tasks across all 3 pools** (3 Graded Tasks + 6 Bonus Tasks for +5 Bonus Marks).

### Primary Graded Tasks (One per Pool)
- **Pool A (Numerical):** Task **A1** — Breast Cancer Diagnosis from Cell-Nucleus Measurements
- **Pool B (Mixed: Numerical + Text):** Task **B1** — Detecting Fraudulent Job Postings (EMSCAD)
- **Pool C (Sequence-to-Sequence):** Task **C1** — English-to-Urdu Neural Machine Translation (OPUS-100)

### Bonus Tasks (All Remaining 6 Tasks Attempted)
- **Pool A (Numerical):** Task **A2** — Predicting Concrete Compressive Strength
- **Pool A (Numerical):** Task **A3** — Dry Bean Variety Recognition from Shape Features
- **Pool B (Mixed: Numerical + Text):** Task **B2** — Predicting Wine Critic Scores from Tasting Notes & Metadata
- **Pool B (Mixed: Numerical + Text):** Task **B3** — Predicting Star Ratings of E-Commerce Clothing Reviews
- **Pool C (Sequence-to-Sequence):** Task **C2** — Abstractive News Summarisation of BBC News Articles (XSum)
- **Pool C (Sequence-to-Sequence):** Task **C3** — Image Captioning with CNN Encoder and LSTM Decoder (Flickr8k)

---

## Directory Navigation & Deliverables

| Pool | Task ID | Task Description | Notebook (.ipynb) | Report (PDF) | LaTeX Source |
| :---: | :---: | :--- | :---: | :---: | :---: |
| **A** | **A1** (Graded) | Breast Cancer Diagnosis | [A1 Notebook](./A1_Breast_Cancer/A1_notebook.ipynb) | [A1 Report PDF](./A1_Breast_Cancer/report/70176490_A1_Report.pdf) | [A1 .tex](./A1_Breast_Cancer/report/source/70176490_A1_Report.tex) |
| **A** | **A2** (Bonus) | Concrete Compressive Strength | [A2 Notebook](./A2_Concrete_Strength/A2_notebook.ipynb) | [A2 Report PDF](./A2_Concrete_Strength/report/70176490_A2_Report.pdf) | [A2 .tex](./A2_Concrete_Strength/report/source/70176490_A2_Report.tex) |
| **A** | **A3** (Bonus) | Dry Bean Variety Recognition | [A3 Notebook](./A3_Dry_Bean/A3_notebook.ipynb) | [A3 Report PDF](./A3_Dry_Bean/report/70176490_A3_Report.pdf) | [A3 .tex](./A3_Dry_Bean/report/source/70176490_A3_Report.tex) |
| **B** | **B1** (Graded) | Fraudulent Job Posting Detection | [B1 Notebook](./B1_Fake_Job_Postings/B1_notebook.ipynb) | [B1 Report PDF](./B1_Fake_Job_Postings/report/70176490_B1_Report.pdf) | [B1 .tex](./B1_Fake_Job_Postings/report/source/70176490_B1_Report.tex) |
| **B** | **B2** (Bonus) | Wine Critic Score Prediction | [B2 Notebook](./B2_Wine_Reviews/B2_notebook.ipynb) | [B2 Report PDF](./B2_Wine_Reviews/report/70176490_B2_Report.pdf) | [B2 .tex](./B2_Wine_Reviews/report/source/70176490_B2_Report.tex) |
| **B** | **B3** (Bonus) | Clothing Review Star Ratings | [B3 Notebook](./B3_Clothing_Reviews/B3_notebook.ipynb) | [B3 Report PDF](./B3_Clothing_Reviews/report/70176490_B3_Report.pdf) | [B3 .tex](./B3_Clothing_Reviews/report/source/70176490_B3_Report.tex) |
| **C** | **C1** (Graded) | English-to-Urdu NMT | [C1 Notebook](./C1_English_to_Urdu_NMT/C1_notebook.ipynb) | [C1 Report PDF](./C1_English_to_Urdu_NMT/report/70176490_C1_Report.pdf) | [C1 .tex](./C1_English_to_Urdu_NMT/report/source/70176490_C1_Report.tex) |
| **C** | **C2** (Bonus) | BBC News Summarisation | [C2 Notebook](./C2_News_Summarisation/C2_notebook.ipynb) | [C2 Report PDF](./C2_News_Summarisation/report/70176490_C2_Report.pdf) | [C2 .tex](./C2_News_Summarisation/report/source/70176490_C2_Report.tex) |
| **C** | **C3** (Bonus) | Image Captioning (Flickr8k) | [C3 Notebook](./C3_Image_Captioning/C3_notebook.ipynb) | [C3 Report PDF](./C3_Image_Captioning/report/70176490_C3_Report.pdf) | [C3 .tex](./C3_Image_Captioning/report/source/70176490_C3_Report.tex) |

---

## How to Set Up the Environment and Run

### 1. Clone the Repository
```bash
git clone https://github.com/MuhammadAwais-70176490/AI101-ML-Assignment-70176490.git
cd AI101-ML-Assignment-70176490
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Running the Notebooks
Launch Jupyter Notebook or JupyterLab:
```bash
jupyter lab
```
Navigate to any task directory (e.g., `A1_Breast_Cancer/A1_notebook.ipynb`) and execute all cells sequentially from top to bottom.
