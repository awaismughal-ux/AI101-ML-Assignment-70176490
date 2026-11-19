# Dataset Documentation: English-to-Urdu Neural Machine Translation (Task C1)

## 1. Dataset Overview
- **Dataset Name:** OPUS-100 Parallel Corpus (English–Urdu subset)
- **Primary Source:** [Helsinki-NLP / OPUS-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100)
- **Original Repository:** [StatMT OPUS-100 Repository](https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/)
- **Task:** Sequence-to-Sequence Supervised Machine Translation ($\text{English} \rightarrow \text{Urdu}$).
- **Domain:** Web subtitles, software localisation, religious texts, news snippets, and open-source documentation.

## 2. Dataset Description & Linguistic Context
The corpus provides sentence-aligned parallel translation pairs between English (source, SVO word order, left-to-right script) and Urdu (target, SOV word order, right-to-left Perso-Arabic script, complex morphological inflection).
- **Official Partitions:**
  - Training: ~750,000 raw translation pairs.
  - Development/Validation: 2,000 parallel pairs.
  - Test Set: 2,000 parallel pairs.
- **Experimental Scope:** Under assignment instructions, a cleaned 50k–100k training subset is extracted and filtered.

## 3. Data Cleaning & Normalization Protocol
Because OPUS-100 is mined from diverse heterogeneous web sources, raw data contains noisy, unaligned, or non-Urdu text. We apply a four-stage sequential filtering pipeline:
1. **Deduplication & Empty Pair Removal:** Eliminating empty lines and duplicate $(x, y)$ parallel sentences.
2. **Length-Ratio Filtering:** Pruning sentence pairs where $\frac{\max(\text{len}_{\text{en}}, \text{len}_{\text{ur}})}{\min(\text{len}_{\text{en}}, \text{len}_{\text{ur}})} > 3.0$ to discard severely misaligned segments.
3. **Sentence Length Truncation:** Retaining only sentences where both English and Urdu lengths are $\le 30$ tokens.
4. **Urdu Script Verification:** Enforcing that every target sentence contains valid Urdu Unicode script characters (`\u0600–\u06FF`, `\uFB50–\uFDFF`, `\uFE70–\uFEFF`), purging untranslated English or corrupted symbols.

## 4. Download Instructions
```bash
# Option 1: Direct download via StatMT repository
curl -O https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/opus.en-ur-train.en
curl -O https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/opus.en-ur-train.ur
curl -O https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/opus.en-ur-dev.en
curl -O https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/opus.en-ur-dev.ur
curl -O https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/opus.en-ur-test.en
curl -O https://data.statmt.org/opus-100-corpus/v1.0/supervised/en-ur/opus.en-ur-test.ur

# Option 2: Via Hugging Face datasets
python -c "from datasets import load_dataset; ds = load_dataset('Helsinki-NLP/opus-100', 'en-ur')"
```

## 5. Pretrained Baseline Reference
- **Model:** `Helsinki-NLP/opus-mt-en-ur` (MarianMT architecture trained on OPUS).
- **Hugging Face Model Card:** [https://huggingface.co/Helsinki-NLP/opus-mt-en-ur](https://huggingface.co/Helsinki-NLP/opus-mt-en-ur)

## 6. Citation
```bibtex
@inproceedings{tiedemann-2020-opus,
  title = "The {OPUS}-100 Corpus: Multilingual Pre-training for Machine Translation",
  author = "Tiedemann, J{\"o}rg",
  booktitle = "Proceedings of the 22nd Annual Conference of the European Association for Machine Translation",
  year = "2020",
  pages = "425--434"
}
```
