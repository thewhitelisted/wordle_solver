from feedback import compute_feedback

def filter_candidates(candidates: list[str], guess: str, feedback: str) -> list[str]:
    return [w for w in candidates if compute_feedback(guess, w) == feedback]