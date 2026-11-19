# Dataset Documentation: Clothing Review Star Rating Prediction (Task B3)

## 1. Dataset Overview
- **Dataset Name:** Women’s E-Commerce Clothing Reviews
- **Primary Source:** Kaggle (`nicapotato/womens-ecommerce-clothing-reviews`)
- **Direct GitHub Mirror:** [ecommerce-reviews-analysis Mirror](https://raw.githubusercontent.com/AFAgarap/ecommerce-reviews-analysis/master/Womens%20Clothing%20E-Commerce%20Reviews.csv)
- **Target Variable:** `Rating` (Ordinal multi-class integer rating from 1 to 5 stars).
- **Domain:** E-commerce, customer sentiment analysis, text mining, tabular-text multimodal learning.

## 2. Dataset Description & Schema
The dataset comprises 23,486 real-world customer reviews collected from an anonymous women's apparel e-commerce store:
- **`Clothing ID`** (integer): Categorical item identifier.
- **`Age`** (numeric): Age of the reviewer (ranging from 18 to 99).
- **`Title`** (text): Short headline of the review.
- **`Review Text`** (text): Main review body describing fit, quality, material, and sentiment.
- **`Rating`** (integer target, 1–5): Customer satisfaction rating (heavily imbalanced toward 5 stars).
- **`Recommended IND`** (binary): Recommendation flag (1 if recommended, 0 otherwise). **STRICTLY EXCLUDED TO PREVENT DATA LEAKAGE.**
- **`Positive Feedback Count`** (numeric): Number of other customers who found this review helpful.
- **`Division Name`** (categorical): High-level category (e.g., General, Petite, Initmates).
- **`Department Name`** (categorical): Department (e.g., Tops, Dresses, Bottoms).
- **`Class Name`** (categorical): Specific clothing type (e.g., Blouses, Knits, Pants).

## 3. Strict Data Hygiene & Leakage Prevention Rules
1. **Target Leakage Prohibition:** Under assignment specifications, the column `Recommended IND` is permanently dropped prior to model development. In real deployment, the rating is what must be predicted from customer text and demographics; allowing `Recommended IND` provides a trivial shortcut that yields artificially high metrics while failing in operational environments.
2. **Missing Text Filtering:** Rows with missing `Review Text` (845 samples, 3.6%) are dropped, as the primary objective requires evaluating unstructured customer sentiment.
3. **Text Merging:** `Title` and `Review Text` are concatenated into a unified text field.
4. **Data Splitting:** Stratified **70/15/15** train/validation/test split with fixed seed `random_state=42`.
5. **Feature Preprocessing:**
   - Text: `TfidfVectorizer` (unigrams + bigrams, top 8,000 features, min_df=3, sublinear_tf=True).
   - Numeric: `Age`, $\log(1 + \text{Positive Feedback Count})$, review length (standardized).
   - Categorical: `Division Name`, `Department Name`, `Class Name` one-hot encoded.
   - All scalers, imputers, and encoders are fit strictly on the training partition.

## 4. Download Instructions
```bash
# Option 1: Via curl / PowerShell
curl -L -o data/Womens_Clothing_E-Commerce_Reviews.csv "https://raw.githubusercontent.com/AFAgarap/ecommerce-reviews-analysis/master/Womens%20Clothing%20E-Commerce%20Reviews.csv"

# Option 2: Via Kaggle CLI
kaggle datasets download -d nicapotato/womens-ecommerce-clothing-reviews --unzip -p data/
```

## 5. Citation
```bibtex
@misc{agarap2018clothing,
  author = {A. F. Agarap and Kaggle Contributors},
  title = {Women's E-Commerce Clothing Reviews},
  year = {2018},
  publisher = {Kaggle},
  url = {https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews}
}
```
