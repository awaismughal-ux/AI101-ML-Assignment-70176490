# Dataset Documentation: Real or Fake Job Postings (EMSCAD)

## Overview
The Employment Scam Aegean Dataset (EMSCAD) is an openly published benchmark dataset created in 2017 by researchers at the University of the Aegean, Greece (S. Vidros, C. Kolias, G. Kambourakis, and L. Akoglu). It was assembled to enable machine learning research into automated fraudulent online job recruitment scams.

- **Primary Source:** Kaggle: `shivamb/real-or-fake-fake-jobposting-prediction`
- **University Archive:** University of the Aegean Laboratory of Information and Communication Systems Security (Info-Sec-Lab)
- **Direct Kaggle Link:** [https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
- **License:** CC BY-NC-SA 4.0 (Non-Commercial, ShareAlike)
- **Primary Publication:** S. Vidros, C. Kolias, G. Kambourakis, and L. Akoglu, "Automatic Detection of Online Recruitment Frauds: Characteristics, Methods, and a Public Dataset," *Future Internet*, vol. 9, no. 1, p. 6, 2017.

## Dataset Specifications
- **Instances:** 17,880 published job postings
- **Target Variable (`fraudulent`):**
  - `0 (Real / Legitimate)`: 17,014 postings (95.16%)
  - `1 (Fraudulent / Scam)`: 866 postings (4.84%)
  - Class Imbalance: Severe (~19.6 : 1 ratio)
- **Features (17 predictor variables):**
  - **Free-Text Fields (5 columns):** `title`, `company_profile`, `description`, `requirements`, `benefits`
  - **Categorical Fields (6 columns):** `location`, `department`, `employment_type`, `required_experience`, `required_education`, `industry`, `function`
  - **Binary Attribute Flags (3 columns):** `telecommuting` (0/1), `has_company_logo` (0/1), `has_questions` (0/1)
  - **Numeric / Mixed:** `salary_range` (often null or formatted as min-max)
  - **Identifier:** `job_id` (excluded from training)

## Missing Data & Structural Signals
In job postings, missingness itself provides strong discriminative signal:
- `company_profile` is missing in ~18.5% of postings, but missing in over 67% of fraudulent postings.
- `has_company_logo` is 0 in 71.5% of fraudulent postings versus only 17.5% of legitimate postings.

## Data Access & Reproduction
Download via Kaggle CLI:
```bash
kaggle datasets download -d shivamb/real-or-fake-fake-jobposting-prediction --unzip -p data/
```
Or directly load in Python:
```python
import pandas as pd
url = "https://raw.githubusercontent.com/abbylmm/fake_job_posting/main/data/fake_job_postings.csv"
df = pd.read_csv(url)
```
