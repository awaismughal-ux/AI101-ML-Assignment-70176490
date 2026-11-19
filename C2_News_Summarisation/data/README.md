# Dataset Provenance: XSum (Extreme Summarisation)

## Overview & Provenance
The **XSum (Extreme Summarisation)** dataset consists of 226,711 BBC news articles spanning 2010 to 2017, accompanied by professionally written, one-sentence abstractive summaries. Unlike traditional news corpora (e.g., CNN/DailyMail) where the lead sentences often capture the core event verbatim, XSum summaries are written by BBC journalists as standalone, abstractive executive takeaways that require non-extractive synthesis.

- **Primary Source:** EdinburghNLP / University of Edinburgh (Narayan et al., 2018, *Don't Give Me the Details, Just the Summary! Topic-Conditioned Abstractive Summarization*, EMNLP).
- **Hugging Face Repository:** `https://huggingface.co/datasets/EdinburghNLP/xsum`
- **Split Breakdown:**
  - Official Train: 204,045 articles
  - Official Validation: 11,332 articles
  - Official Test: 11,334 articles
- **Sampled Subset for this Investigation (Seed 42):**
  - Train: 20,000 articles
  - Validation: 1,000 articles
  - Test: 1,000 articles

## Data Fields & Schema
Each record contains the following fields:
1. `document` (*string*): The full text of the BBC news article (truncated to ~400 tokens for recurrent modeling).
2. `summary` (*string*): The gold-standard one-sentence abstractive summary written by BBC journalists.
3. `id` (*string*): Unique BBC article identifier.

## Download & Acquisition Instructions
The official splits are distributed as Apache Parquet files on Hugging Face:
```bash
# Using Hugging Face datasets library:
from datasets import load_dataset
dataset = load_dataset("EdinburghNLP/xsum")

# Direct download of official parquet files:
curl -L -O https://huggingface.co/datasets/EdinburghNLP/xsum/resolve/main/data/train-00000-of-00001.parquet
curl -L -O https://huggingface.co/datasets/EdinburghNLP/xsum/resolve/main/data/validation-00000-of-00001.parquet
curl -L -O https://huggingface.co/datasets/EdinburghNLP/xsum/resolve/main/data/test-00000-of-00001.parquet
```

## Citation
```bibtex
@inproceedings{narayan2018dont,
  title={Don't Give Me the Details, Just the Summary! Topic-Conditioned Abstractive Summarization},
  author={Narayan, Shashi and Cohen, Shay B and Lapata, Mirella},
  booktitle={Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  pages={1797--1807},
  year={2018}
}
```
