# Dataset Documentation: Wine Critic Score Prediction (Task B2)

## 1. Dataset Overview
- **Dataset Name:** Wine Reviews (Winemag 130k v2)
- **Primary Source:** Kaggle (`zynicide/wine-reviews`)
- **Direct Mirror:** [GitHub Raw Kaggle Mirror](https://raw.githubusercontent.com/morisasy/kaggle/master/data/winemag-data-130k-v2.csv)
- **Target Variable:** `points` (Continuous/Ordinal integer score between 80 and 100, awarded by professional sommeliers and wine critics).
- **Domain:** Enology, sensory analysis, natural language processing, multimodal tabular regression.

## 2. Dataset Description & Schema
The dataset consists of approximately 129,971 reviews scraped from *WineEnthusiast* magazine in November 2017. Each sample comprises:
- **`country`** (categorical): Country of origin.
- **`description`** (text): Sommelier tasting notes (~40 words describing aroma, palate, tannins, acidity, finish).
- **`designation`** (categorical): Specific vineyard or blend designation.
- **`points`** (integer target, 80–100): Professional rating score.
- **`price`** (numeric continuous): Bottle retail price in USD (contains ~6.9% missing values).
- **`province`** (categorical): Province or state where the wine was produced.
- **`region_1` / `region_2`** (categorical): Specific growing sub-regions.
- **`taster_name`** (categorical): Name of the professional reviewer.
- **`taster_twitter_handle`** (categorical): Social media handle of reviewer.
- **`title`** (text): Full title of the wine vintage.
- **`variety`** (categorical): Grape variety (e.g., Pinot Noir, Chardonnay, Cabernet Sauvignon).
- **`winery`** (categorical): Producing estate or winery.

## 3. Data Integrity & Preprocessing Protocol
1. **De-duplication Pre-Split:** The raw dataset contains 9,983 exact duplicate reviews where identical tasting notes and titles appear multiple times due to syndication. To prevent severe train-to-test data leakage, all duplicates on `['title', 'description']` are pruned before any partitioning.
2. **Train/Val/Test Split:** Partitioned into an **80/10/10** ratio with fixed seed `random_state=42`.
3. **Price Normalization:** Log-transformed as $\log(1 + \text{price})$ to address right-skewness, with median imputation and a binary missing-value indicator fitted exclusively on the training set.
4. **Categorical Metadata:** Frequency-based top-N encoding for high-cardinality features (`country`, `province`, `variety`, `winery`, `taster_name`), grouping low-frequency categories into an `"Other"` token.
5. **Text Representation:** Sublinear TF-IDF vectorizer (unigrams + bigrams, top 10,000 features, min_df=5) fit strictly on training descriptions.

## 4. Download Instructions
To download the dataset into this folder:
```bash
# Option 1: Via curl / PowerShell
curl -L -o data/winemag-data-130k-v2.csv "https://raw.githubusercontent.com/morisasy/kaggle/master/data/winemag-data-130k-v2.csv"

# Option 2: Via Kaggle CLI
kaggle datasets download -d zynicide/wine-reviews --unzip -p data/
```

## 5. Citation
```bibtex
@misc{thoutt2017wine,
  author = {Zack Thoutt},
  title = {Wine Reviews: 130k wine reviews with variety, location, winery, price, and points},
  year = {2017},
  publisher = {Kaggle},
  url = {https://www.kaggle.com/datasets/zynicide/wine-reviews}
}
```
