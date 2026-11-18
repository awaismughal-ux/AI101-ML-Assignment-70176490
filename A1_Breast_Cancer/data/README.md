# Dataset Documentation: Breast Cancer Wisconsin (Diagnostic)

## Overview
The Breast Cancer Wisconsin (Diagnostic) dataset is a classical benchmark in biomedical machine learning, originally contributed by Dr. William H. Wolberg, W. Nick Street, and Olvi L. Mangasarian from the University of Wisconsin-Madison in 1995.

- **Primary Source:** UCI Machine Learning Repository (Dataset ID: 17)
- **Direct Link:** [https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)
- **Scikit-Learn Interface:** `sklearn.datasets.load_breast_cancer()`
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Dataset Specifications
- **Instances:** 569 patient samples
- **Features:** 30 continuous real-valued geometric features computed from digitized images of Fine Needle Aspirates (FNA) of breast masses.
- **Feature Categories:** 10 core morphological characteristics computed across three statistics (mean, standard error, and worst/maximum):
  1. `radius` (mean of distances from center to points on the perimeter)
  2. `texture` (standard deviation of gray-scale values)
  3. `perimeter`
  4. `area`
  5. `smoothness` (local variation in radius lengths)
  6. `compactness` ($perimeter^2 / area - 1.0$)
  7. `concavity` (severity of concave portions of the contour)
  8. `concave points` (number of concave portions of the contour)
  9. `symmetry`
  10. `fractal dimension` ("coastline approximation" - 1)
- **Target Variable:** Binary diagnostic outcome:
  - `Malignant` (Positive Class, 1): 212 samples (37.26%)
  - `Benign` (Negative Class, 0): 357 samples (62.74%)
- **Missing Values:** None (0.0%).

## Data Access & Reproduction
The dataset is bundled directly inside `scikit-learn`:
```python
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer(as_frame=True)
X = data.data
# Note: scikit-learn assigns 0 to malignant and 1 to benign by default.
# For clinical screening standards, malignant is re-mapped to 1 (positive) and benign to 0 (negative).
y = (data.target == 0).astype(int)
```
Alternatively, via `ucimlrepo`:
```python
from ucimlrepo import fetch_ucirepo
bc = fetch_ucirepo(id=17)
X = bc.data.features
y = (bc.data.targets['Diagnosis'] == 'M').astype(int)
```
