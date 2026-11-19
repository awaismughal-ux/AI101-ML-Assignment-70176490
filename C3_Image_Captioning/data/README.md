# Flickr8k Image Captioning Dataset

## 1. Dataset Overview & Provenance
The **Flickr8k** dataset is a benchmark multimodal corpus designed for image description, retrieval, and caption generation. It was introduced by Hodosh, Young, and Hockenmaier (2013) in the *Journal of Artificial Intelligence Research (JAIR)*:
- **Reference**: Hodosh, M., Young, P., & Hockenmaier, J. (2013). Framing Image Description as a Ranking Task: Data, Models and Evaluation Metrics. *Journal of Artificial Intelligence Research*, 47, 853–899.
- **Source**: Collected via the Flickr photo-sharing platform under Creative Commons licensing and annotated via Amazon Mechanical Turk.
- **Hosted Mirrors**:
  - Direct Archive: [Jason Brownlee's Datasets Repository](https://github.com/jbrownlee/Datasets/releases/tag/Flickr8k)
  - Kaggle Benchmark: [adityajn105/flickr8k](https://www.kaggle.com/datasets/adityajn105/flickr8k)

---

## 2. Dataset Structure and Files
The dataset comprises 8,091 JPEG images depicting everyday situations, people, animals, and landscapes, paired with 5 human-written captions per image:

```
data/
├── Flickr8k.token.txt           # 40,455 caption entries (format: <image_id>#<caption_idx>\t<text>)
├── Flickr8k.lemma.token.txt     # Lemmatized version of token annotations
├── Flickr_8k.trainImages.txt    # Official training set image filenames (6,000 images)
├── Flickr_8k.devImages.txt      # Official validation set image filenames (1,000 images)
├── Flickr_8k.testImages.txt     # Official test set image filenames (1,000 images)
├── CrowdFlowerAnnotations.txt   # Quality and alignment crowd-sourced evaluations
├── ExpertAnnotations.txt        # Expert human consensus scores
└── Flickr8k_Dataset/            # Directory containing 8,091 JPEG photographs
```

---

## 3. Data Splits & Split Integrity
To prevent data leakage, dataset splitting is strictly enforced at the **image level**. All 5 reference captions corresponding to any photograph reside entirely within that photograph's designated split:
- **Training Set**: 6,000 images (30,000 caption pairs; 74.15%)
- **Validation Set (`dev`)**: 1,000 images (5,000 caption pairs; 12.36%)
- **Test Set**: 1,000 images (5,000 caption pairs; 12.36%)
- **Total**: 8,091 images (40,455 captions; 91 images reserved in ancillary evaluation sets)

---

## 4. Preprocessing & Feature Extraction Pipeline
1. **Caption Preprocessing**:
   - Conversion to lower-case characters.
   - Removal of non-alphanumeric punctuation while preserving contraction apostrophes.
   - Prepended `<start>` / `<sos>` and appended `<end>` / `<eos>` sequence delimiters.
   - Word frequency filtering with threshold $\text{min\_freq} = 5$. Infrequent tokens are mapped to `<unk>`.
   - Zero-padding to uniform sequence length with `<pad>`.

2. **Visual Feature Extraction (CNN Encoder)**:
   - Deep Convolutional Neural Network: Pretrained **ResNet-50** on ImageNet-1K.
   - Input normalization: Images scaled to $224 \times 224$ pixels, standardized using ImageNet channel-wise statistics ($\mu = [0.485, 0.456, 0.406]$, $\sigma = [0.229, 0.224, 0.225]$).
   - Global Representation (Model 1 - Merge Architecture): Feature vector extracted post global average pooling layer, yielding a dense 2048-dimensional embedding $\mathbf{v} \in \mathbb{R}^{2048}$.
   - Spatial Representation (Model 2 - Show, Attend and Tell): Feature maps extracted from the final residual block (`conv5_block3_out`), producing a $7 \times 7 \times 2048$ spatial tensor ($L = 49$ feature vectors $\mathbf{a}_i \in \mathbb{R}^{2048}$).

---

## 5. Download Instructions
To download and extract the dataset:
```bash
# 1. Download caption annotations and split definitions (2.3 MB)
curl -L -o data/Flickr8k_text.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip
unzip data/Flickr8k_text.zip -d data/

# 2. Download Flickr8k image photographs (1.1 GB)
curl -L -o data/Flickr8k_Dataset.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip
unzip data/Flickr8k_Dataset.zip -d data/
```
Large binary assets (`*.zip`, `*.jpg`, `*.pt`, `*.pkl`) are strictly ignored via `.gitignore` to comply with Git repository storage standards.
