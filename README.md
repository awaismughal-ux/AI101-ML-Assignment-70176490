# AI-101 Machine Learning Assignment: Training ML Models on Three Data Modalities

**Course:** AI-101: Introduction to Artificial Intelligence (Fall 2026)  
**Institution:** Department of Intelligent Systems, Faculty of Information Technology, The University of Lahore  
**Instructor:** Dr. Muhammad Awais (AI Architect, Department of Intelligent Systems)  
**Student Name:** Muhammad Awais  
**Roll Number:** `70176490`  
**Section:** Section A  
**Degree Program:** Bachelor of Science in Embedded Systems & Artificial Intelligence (BS ESAI)  
**Student Email:** `awaismughal12255@gmail.com`  
**Repository URL:** [https://github.com/awaismughal-ux/AI101-ML-Assignment-70176490](https://github.com/awaismughal-ux/AI101-ML-Assignment-70176490)  
**Submission Tag:** `submission`  

---

## Executive Summary & Completion Matrix

This repository presents the exhaustive, end-to-end implementation and empirical investigation for **all nine tasks across all three modalities** specified in the AI-101 assignment rubric. To achieve the maximum grade (30 base marks + 5 bonus marks = 35/30), three primary graded tasks (one per pool) and all six bonus tasks have been completed, executed, analyzed, and documented with publication-grade IEEE conference reports.

### Primary Graded Tasks (30 Marks Base)
1. **Pool A (Pure Numerical Data):** Task **A1** — Breast Cancer Diagnosis from Fine-Needle Aspirate Cell Nuclei Measurements
2. **Pool B (Mixed Numerical + Text Data):** Task **B1** — Detecting Fraudulent Job Postings in the EMSCAD Corpus
3. **Pool C (Sequence-to-Sequence Modeling):** Task **C1** — English-to-Urdu Neural Machine Translation with Bahdanau Attention

### Bonus Tasks (+5 Marks Extra Credit)
4. **Pool A (Bonus):** Task **A2** — Predicting High-Performance Concrete Compressive Strength
5. **Pool A (Bonus):** Task **A3** — Seven-Class Dry Bean Variety Recognition from Geometric Features
6. **Pool B (Bonus):** Task **B2** — Predicting Sommelier Wine Critic Scores from Tasting Notes & Metadata (130k v2)
7. **Pool B (Bonus):** Task **B3** — Multi-Class Rating Prediction for Women's E-Commerce Clothing Reviews
8. **Pool C (Bonus):** Task **C2** — Abstractive News Summarisation of BBC News Articles (XSum)
9. **Pool C (Bonus):** Task **C3** — Multi-Modal Image Captioning with Pretrained ResNet-50 and LSTM Decoders (Flickr8k)

---

## Directory Navigation & Deliverable Manifest

Every individual task folder contains:
- `data/README.md`: Provenance, licensing, download instructions, and exact feature schemas.
- `<TaskID>_notebook.ipynb`: A completely executed Jupyter notebook with all outputs, markdown analyses, error handling, and ablation benchmarks.
- `figures/`: High-resolution (300 DPI) publication-quality figures (`.png`).
- `report/<RollNo>_<TaskID>_Report.pdf`: Strictly 2-content-page IEEE double-column conference report.
- `report/source/<RollNo>_<TaskID>_Report.tex`: Standalone LaTeX source document matching the PDF.

| Pool | Task ID | Problem Description | Executed Notebook | IEEE Report (PDF) | LaTeX Source | Key Metric | Best Model |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **A** | **A1** *(Graded)* | Breast Cancer Diagnosis | [A1 Notebook](./A1_Breast_Cancer/A1_notebook.ipynb) | [A1 Report PDF](./A1_Breast_Cancer/report/70176490_A1_Report.pdf) | [A1 .tex](./A1_Breast_Cancer/report/source/70176490_A1_Report.tex) | Test Acc: **98.25%**, Macro F1: **98.09%**, PR-AUC: **0.9982** | Deep MLP (AdamW) |
| **A** | **A2** *(Bonus)* | Concrete Compressive Strength | [A2 Notebook](./A2_Concrete_Strength/A2_notebook.ipynb) | [A2 Report PDF](./A2_Concrete_Strength/report/70176490_A2_Report.pdf) | [A2 .tex](./A2_Concrete_Strength/report/source/70176490_A2_Report.tex) | Test RMSE: **5.34 MPa**, $R^2$: **0.891** | Deep MLP (AdamW) |
| **A** | **A3** *(Bonus)* | Dry Bean Variety Recognition | [A3 Notebook](./A3_Dry_Bean/A3_notebook.ipynb) | [A3 Report PDF](./A3_Dry_Bean/report/70176490_A3_Report.pdf) | [A3 .tex](./A3_Dry_Bean/report/source/70176490_A3_Report.tex) | Test Acc: **93.39%**, Macro F1: **93.58%** | Deep MLP (BN+Dropout) |
| **B** | **B1** *(Graded)* | Fraudulent Job Posting Detection | [B1 Notebook](./B1_Fake_Job_Postings/B1_notebook.ipynb) | [B1 Report PDF](./B1_Fake_Job_Postings/report/70176490_B1_Report.pdf) | [B1 .tex](./B1_Fake_Job_Postings/report/source/70176490_B1_Report.tex) | Test PR-AUC: **0.8653**, Minority F1: **0.7619** | LightGBM + TF-IDF |
| **B** | **B2** *(Bonus)* | Wine Critic Score Prediction | [B2 Notebook](./B2_Wine_Reviews/B2_notebook.ipynb) | [B2 Report PDF](./B2_Wine_Reviews/report/70176490_B2_Report.pdf) | [B2 .tex](./B2_Wine_Reviews/report/source/70176490_B2_Report.tex) | Test RMSE: **1.74 pts**, $R^2$: **0.687** | LightGBM + TF-IDF |
| **B** | **B3** *(Bonus)* | Clothing Review Star Ratings | [B3 Notebook](./B3_Clothing_Reviews/B3_notebook.ipynb) | [B3 Report PDF](./B3_Clothing_Reviews/report/70176490_B3_Report.pdf) | [B3 .tex](./B3_Clothing_Reviews/report/source/70176490_B3_Report.tex) | Test Acc: **66.42%**, Macro F1: **58.74%** | LightGBM + TF-IDF |
| **C** | **C1** *(Graded)* | English-to-Urdu NMT | [C1 Notebook](./C1_Translation_En_Ur/C1_notebook.ipynb) | [C1 Report PDF](./C1_Translation_En_Ur/report/70176490_C1_Report.pdf) | [C1 .tex](./C1_Translation_En_Ur/report/source/70176490_C1_Report.tex) | Test BLEU: **9.92** (Beam width 4) | BiGRU + Bahdanau Attn |
| **C** | **C2** *(Bonus)* | BBC News Summarisation | [C2 Notebook](./C2_News_Summarisation/C2_notebook.ipynb) | [C2 Report PDF](./C2_News_Summarisation/report/70176490_C2_Report.pdf) | [C2 .tex](./C2_News_Summarisation/report/source/70176490_C2_Report.tex) | Test ROUGE-1: **17.93%**, ROUGE-L: **12.54%** | T5-Small Pretrained |
| **C** | **C3** *(Bonus)* | Image Captioning (Flickr8k) | [C3 Notebook](./C3_Image_Captioning/C3_notebook.ipynb) | [C3 Report PDF](./C3_Image_Captioning/report/70176490_C3_Report.pdf) | [C3 .tex](./C3_Image_Captioning/report/source/70176490_C3_Report.tex) | Test BLEU-1: **12.62%**, BLEU-4: **0.30%** | Show & Tell / Merge |

---

## Detailed Empirical Findings Across Modality Pools

### Pool A: Pure Numerical Data
- **Data Preprocessing & Leakage Prevention:** All scalers (StandardScaler, RobustScaler) were strictly fitted on training partitions and applied downstream to validation and testing sets.
- **Model Comparison:** Evaluated baseline linear models (Logistic Regression, Ridge Regression) against deep Multi-Layer Perceptrons (MLPs) incorporating Layer Normalization/Batch Normalization, Dropout ($p \in [0.1, 0.3]$), and residual projections.
- **Validation:** 5-fold stratified cross-validation confirmed consistent generalization across all splits without statistical variance anomalies.

### Pool B: Mixed Numerical and Textual Data
- **Dual-Modality Feature Fusion:** Concatenated sparse sublinear TF-IDF n-gram matrices (unigrams + bigrams, top 3,000–5,000 features) with scaled dense numeric metadata and categorical target-encoded features.
- **Class Imbalance Handling:** In Task B1 (fraudulent job postings, 4.8% minority class), threshold calibration and focal/cost-sensitive weights (`scale_pos_weight=5.0`) boosted Precision-Recall AUC from 0.7712 to 0.8653.
- **Model Comparison:** Gradient-boosted decision trees (LightGBM) consistently outperformed linear baselines by capturing high-order non-linear feature interactions between tabular metadata and lexical cues.

### Pool C: Sequence-to-Sequence Modeling
- **Task C1 (NMT):** Implemented an end-to-end encoder-decoder with bidirectional GRU and Bahdanau additive attention. Beam search decoding ($k=4$, length penalty $\alpha=0.6$) yielded a +1.14 BLEU improvement over greedy decoding on unseen test sentences.
- **Task C2 (Summarisation):** Addressed extreme abstractiveness in the BBC XSum benchmark. Evaluated Lead-1 extractive baseline (17.57% ROUGE-1), custom sequence-to-sequence BiGRU with attention (13.08% ROUGE-1), and pretrained T5-Small (17.93% ROUGE-1, 12.54% ROUGE-L). Measured hallucination rates via token attribution.
- **Task C3 (Image Captioning):** Extracted deep semantic representations from raw Flickr8k images using pretrained ResNet-50 (`avgpool` 2048-dimensional feature vectors). Benchmarked the Merge architecture (Tanti et al., 2018; multimodal fusion at decoder feedforward layer) against Show and Tell (Vinyals et al., 2015; visual conditioning of initial recurrent hidden states). Evaluated standard corpus BLEU-1 through BLEU-4 with brevity penalties.

---

## Repository Structure

```
AI101-ML-Assignment-70176490/
├── README.md                               # Master documentation & completion matrix
├── requirements.txt                        # Unified dependency specification
├── .gitignore                              # Strict exclusion of large datasets & temp files
│
├── A1_Breast_Cancer/                       # Pool A - Graded Task
│   ├── data/README.md                      # Dataset documentation & provenance
│   ├── figures/                            # High-resolution figures (EDA, ROC/PR curves)
│   ├── report/                             # 2-page IEEE report PDF
│   │   └── 70176490_A1_Report.pdf
│   ├── report/source/                      # LaTeX source files
│   │   └── 70176490_A1_Report.tex
│   └── A1_notebook.ipynb                   # Fully executed Jupyter notebook
│
├── A2_Concrete_Strength/                   # Pool A - Bonus Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_A2_Report.pdf
│   ├── report/source/70176490_A2_Report.tex
│   └── A2_notebook.ipynb
│
├── A3_Dry_Bean/                            # Pool A - Bonus Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_A3_Report.pdf
│   ├── report/source/70176490_A3_Report.tex
│   └── A3_notebook.ipynb
│
├── B1_Fake_Job_Postings/                   # Pool B - Graded Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_B1_Report.pdf
│   ├── report/source/70176490_B1_Report.tex
│   └── B1_notebook.ipynb
│
├── B2_Wine_Reviews/                        # Pool B - Bonus Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_B2_Report.pdf
│   ├── report/source/70176490_B2_Report.tex
│   └── B2_notebook.ipynb
│
├── B3_Clothing_Reviews/                    # Pool B - Bonus Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_B3_Report.pdf
│   ├── report/source/70176490_B3_Report.tex
│   └── B3_notebook.ipynb
│
├── C1_Translation_En_Ur/                   # Pool C - Graded Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_C1_Report.pdf
│   ├── report/source/70176490_C1_Report.tex
│   └── C1_notebook.ipynb
│
├── C2_News_Summarisation/                  # Pool C - Bonus Task
│   ├── data/README.md
│   ├── figures/
│   ├── report/70176490_C2_Report.pdf
│   ├── report/source/70176490_C2_Report.tex
│   └── C2_notebook.ipynb
│
└── C3_Image_Captioning/                    # Pool C - Bonus Task
    ├── data/README.md
    ├── figures/
    ├── report/70176490_C3_Report.pdf
    ├── report/source/70176490_C3_Report.tex
    └── C3_notebook.ipynb
```

---

## Environment Setup & Reproducibility

### 1. Clone the Repository
```bash
git clone https://github.com/awaismughal-ux/AI101-ML-Assignment-70176490.git
cd AI101-ML-Assignment-70176490
```

### 2. Create and Activate a Dedicated Virtual Environment
```bash
# Using Python 3.11+
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Linux / macOS:
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Running the Notebooks
Launch the Jupyter interface:
```bash
jupyter lab
```
Navigate to any task directory and run all cells sequentially. Every notebook has self-contained dataset fetching routines (using `urllib`, `requests`, `ucimlrepo`, or `datasets`) so no manual data downloading is required.

---

## Git Commit History & Tag Verification

Per assignment requirements, all 9 tasks have at least 5 fine-grained, descriptive commits tracking data setup, exploratory data analysis, modeling, notebook execution, and report generation. The final submission is tagged with the annotated tag `submission`:

```bash
# Verify tag and commit history
git tag -n
git log --oneline --graph
```

---

## Academic Integrity & Authorship Declaration

I hereby declare that this assignment is entirely my own original academic work. All external sources, libraries, datasets, and literature references have been meticulously cited according to IEEE referencing standards in both the notebooks and the corresponding conference reports.

**Muhammad Awais**  
Department of Intelligent Systems  
The University of Lahore  
Student Email: `awaismughal12255@gmail.com`  
Instructor: Dr. Muhammad Awais (`muhammad.awais@is.uol.edu.pk`)
