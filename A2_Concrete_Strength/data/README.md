# Dataset Documentation: Concrete Compressive Strength

## Overview
The Concrete Compressive Strength dataset was created and donated by Prof. I-Cheng Yeh from Chung-Hua University, Taiwan, in 1998. It has served as a principal empirical benchmark for high-performance concrete modeling and non-linear regression analysis.

- **Primary Source:** UCI Machine Learning Repository (Dataset ID: 165)
- **Direct Link:** [https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Primary Publication:** I-Cheng Yeh, "Modeling of strength of high-performance concrete using artificial neural networks," *Cement and Concrete Research*, vol. 28, no. 12, pp. 1797-1808, 1998.

## Dataset Specifications
- **Instances:** 1,030 experimental concrete batches
- **Input Features (8 numeric variables):**
  1. `cement`: Cement content (kg/m³)
  2. `slag`: Blast-furnace slag (kg/m³)
  3. `ash`: Fly ash (kg/m³)
  4. `water`: Water content (kg/m³)
  5. `superplastic`: Superplasticizer (kg/m³)
  6. `coarseagg`: Coarse aggregate (kg/m³)
  7. `fineagg`: Fine aggregate (kg/m³)
  8. `age`: Curing age in days (range: 1 to 365 days)
- **Target Variable:**
  - `strength`: Concrete compressive strength tested after laboratory curing (continuous in MPa, range: 2.33 to 82.60 MPa)
- **Missing Values:** None (0.0%).

## Data Access & Reproduction
The dataset can be fetched via `ucimlrepo` or loaded from standard public repositories:
```python
from ucimlrepo import fetch_ucirepo
concrete = fetch_ucirepo(id=165)
X = concrete.data.features
y = concrete.data.targets
```
Alternatively, via public mirrored CSV:
```python
import pandas as pd
url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/concrete.csv"
df = pd.read_csv(url)
X = df.drop(columns=['strength'])
y = df['strength']
```
