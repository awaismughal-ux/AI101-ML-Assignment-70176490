# Dataset Documentation: Dry Bean Dataset

## Overview
The Dry Bean dataset was created and contributed by Murat Koklu and Ilker Ali Ozkan from Selcuk University, Turkey, in 2020. It comprises high-resolution computer vision shape measurements extracted from 13,611 individual grains across seven registered commercial dry bean cultivars.

- **Primary Source:** UCI Machine Learning Repository (Dataset ID: 602)
- **Direct Link:** [https://archive.ics.uci.edu/dataset/602/dry+bean+dataset](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Primary Publication:** M. Koklu and I. A. Ozkan, "Multiclass classification of dry beans using computer vision and machine learning techniques," *Computers and Electronics in Agriculture*, vol. 174, p. 105507, 2020.

## Dataset Specifications
- **Instances:** 13,611 grain samples
- **Features (16 continuous numeric shape attributes):**
  1. `Area` ($A$): Area of the bean zone and the number of pixels within its boundary.
  2. `Perimeter` ($P$): Circumference of bean circumference.
  3. `MajorAxisLength` ($L$): Distance between ends of the longest line.
  4. `MinorAxisLength` ($l$): Longest line perpendicular to major axis.
  5. `AspectRation` ($K$): Ratio $L/l$.
  6. `Eccentricity` ($Ec$): Eccentricity of the ellipse having identical second moments.
  7. `ConvexArea` ($C$): Smallest convex polygon containing the bean region.
  8. `EquivDiameter` ($Ed$): Diameter of a circle with equivalent area $\sqrt{4A/\pi}$.
  9. `Extent` ($Ex$): Ratio of pixels in bean area to pixels in bounding box.
  10. `Solidity` ($S$): Ratio of Area to ConvexArea ($A/C$).
  11. `roundness` ($R$): Compactness formula $4\pi A / P^2$.
  12. `Compactness` ($CO$): Measure of roundness $Ed/L$.
  13. `ShapeFactor1` ($SF1$)
  14. `ShapeFactor2` ($SF2$)
  15. `ShapeFactor3` ($SF3$)
  16. `ShapeFactor4` ($SF4$)
- **Target Variable (7 imbalanced bean cultivars):**
  1. `DERMASON`: 3,546 samples (26.05%)
  2. `SIRA`: 2,636 samples (19.37%)
  3. `SEKER`: 2,027 samples (14.89%)
  4. `HOROZ`: 1,928 samples (14.16%)
  5. `CALI`: 1,630 samples (11.98%)
  6. `BARBUNYA`: 1,322 samples (9.71%)
  7. `BOMBAY`: 522 samples (3.84%)
- **Missing Values:** None (0.0%).

## Data Access & Reproduction
Via `ucimlrepo`:
```python
from ucimlrepo import fetch_ucirepo
bean = fetch_ucirepo(id=602)
X = bean.data.features
y = bean.data.targets['Class']
```
