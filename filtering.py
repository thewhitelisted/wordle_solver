from feedback import compute_feedback
from collections import defaultdict
import math

def filter_candidates(candidates: list[str], guess: str, feedback: str) -> list[str]:
    return [w for w in candidates if compute_feedback(guess, w) == feedback]

def expected_entropy(guess: str, candidates: list[str]) -> float:
    pattern_counts = defaultdict(int)
    for answer in candidates:
        pattern = compute_feedback(guess, answer)
        pattern_counts[pattern] += 1

    total = len(candidates)
    entropy = 0
    for count in pattern_counts.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    print(f"Entropy for guess '{guess}': {entropy:.4f}")
    return entropy

def best_guess(possible: list[str], candidates: list[str]) -> str:
    return max(possible, key=lambda guess: expected_entropy(guess, candidates))