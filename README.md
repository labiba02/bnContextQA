# bnContextQA

**bnContextQA** is a benchmark dataset for evaluating **long-context comprehension in Bangla**. It is specifically designed to study **positional bias** in large language models (LLMs), addressing the gap in multilingual long-context QA research. The dataset contains **350 multi-passage QA instances**, each with **30 context paragraphs**, including one gold passage containing the answer and carefully designed distractors.

---

## Motivation
While large language models have advanced in processing long input sequences, they often show a **positional bias**, prioritizing information at the beginning or end of the input while neglecting middle sections. Most studies on this bias are limited to English. **bnContextQA** aims to:  

- Provide a benchmark for long-context QA in Bangla, a widely spoken but computationally underrepresented language.  
- Support research on **cross-linguistic positional effects**.  
- Encourage evaluation of **multilingual LLMs** on realistic long-context comprehension tasks.

---
## Dataset Overview
- **Total instances:** 350  
- **Passages per instance:** 30  
- **Average passage length:** 175 tokens  
- **Answer type:** Short, unambiguous Bangla phrases or sentences  
- **Source:** Bangla Wikipedia, Banglapedia  
- **Language:** Bangla (`bn`)  

Each instance simulates **multi-document question answering**, with **one gold passage** and multiple **topically relevant distractors**.

---

## Dataset Structure
Each data sample is a JSON object:

```json
{
  "question": "<Bangla question>",
  "language": "bn",
  "documents": [
    {
      "title": "<passage title>",
      "content": "<passage content>",
      "source": "<source URL or reference>"
    },
    ...
    {
      "title": "<passage title 30>",
      "content": "<passage content>",
      "source": "<source URL or reference>"
    }
  ],
  "answer": "<Bangla answer>",
  "relevant_document_index": 5,
  "context_length": 30,
  "metadata": {
    "topic_category": "<category>",
    "article_id": "<ID>",
    "notes": "<additional notes>"
  }
}
```

- **relevant_document_index** points to the passage containing the correct answer.  
- **documents** include both the gold passage and distractors designed to be topically and lexically similar.

---

## Data Acquisition

- Passages curated from **Bangla Wikipedia** for broad domain coverage.  
- Manual curation ensured **correctness, quality, and domain diversity**.  
- Existing Bangla QA datasets (e.g., Bengali-SQuAD, SQuAD_Bn, BanglaQA) are mostly short-passage, so this dataset fills the gap for **long-context evaluation**.

---

## Question Generation

- Topics selected from **Banglapedia** and **Wikibangla** to ensure multiple related articles.  
- Candidate questions generated with **ChatGPT**, followed by **manual filtering** to:  
  - Ensure short, unambiguous answers  
  - Avoid questions that can be answered without consulting the gold passage  
  - Align with the goal of evaluating **long-context reasoning**

---

## Distractor Design

Distractors are carefully constructed to increase task difficulty:  

- **Topical relevance:** Same broad domain as the gold passage.  
- **Lexical similarity:** Shares key vocabulary and stylistic features.  
- **Factual distinction:** Does not contain the answer.  
- **Structural parity:** Matches gold passage in length and complexity.  

This human-guided approach ensures distractors are **plausible, challenging, and semantically aligned**.

---

## Preprocessing and Cleaning

- Removed redundant citations, bracketed references, and extraneous symbols.  
- Normalized Bangla script to a **consistent Unicode form**.  
- Translated essential English terms to Bangla; removed repetitive English words.  
- Standardized passage lengths and added metadata (topic category, article ID, gold passage index).  

The result is a **linguistically coherent, semantically consistent dataset** suitable for evaluating **long-context reasoning in Bangla**.

---

## Context Shortening Utility

We provide `shorten_contexts.py` to **reduce the number of passages per instance**, enabling experiments with **shorter context lengths**.

---

## Evaluation

- Designed to measure **LLM performance across context positions**.  
- Common metrics: **Exact Match (EM)**, **F1 score**.  
- Facilitates analysis of **positional bias** and reasoning over **long Bangla contexts**.

---

## Repository Structure
```
bnContextQA/
├── data/ # JSON files of all QA instances
├── scripts/ # Utilities like shorten_contexts.py
└── README.md # This file
```
