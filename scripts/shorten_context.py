"""
Shrink each sample's documents from N to target_length:
- Always keep the first document (index 0).
- Add (target_length - 1) more randomly from the remaining documents.
- Update `context_length` accordingly.
- Preserve other fields unchanged.

Usage:
  python shrink_context.py input.json output.json --target_length 10 --seed 42
"""
import argparse
import json
import random
from typing import List, Dict, Any

def shrink_sample(sample: Dict[str, Any], rng: random.Random, target_length: int) -> Dict[str, Any]:
    docs: List[Dict[str, Any]] = sample.get("documents", [])
    if not docs:
        sample["context_length"] = 0
        return sample

    # Always keep the first document
    kept_indices = [0]

    # Figure out how many more to add
    remaining = max(0, len(docs) - 1)
    k_more = min(target_length - 1, remaining)

    if k_more > 0:
        # Randomly choose additional unique indices from 1..len(docs)-1
        extra_indices = rng.sample(range(1, len(docs)), k_more)
        extra_indices.sort()  # preserve original order
        kept_indices.extend(extra_indices)

    # Build the new documents list
    new_docs = [docs[i] for i in kept_indices]

    # Update fields
    sample["documents"] = new_docs
    sample["context_length"] = len(new_docs)

    # Ensure relevant_document_index is still 0 (since we keep doc[0])
    if "relevant_document_index" in sample:
        sample["relevant_document_index"] = 0

    return sample

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json", help="Path to input JSON file (list of samples)")
    ap.add_argument("output_json", help="Path to write the shrunk JSON")
    ap.add_argument("--target_length", type=int, default=10,
                    help="Number of documents to keep (default: 10)")
    ap.add_argument("--seed", type=int, default=42,
                    help="Random seed for reproducibility")
    args = ap.parse_args()

    rng = random.Random(args.seed)

    with open(args.input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    out: List[Dict[str, Any]] = [
        shrink_sample(sample, rng, args.target_length) for sample in data
    ]

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
