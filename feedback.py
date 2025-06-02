from collections import Counter

def compute_feedback(guess: str, answer: str) -> str:
    # Use a list for feedback (more efficient for modifications)
    feedback = ['_'] * len(guess)
    
    # Create a Counter to track remaining letters in answer after first pass
    remaining_letters = Counter()
    
    # First pass: mark correct positions and count remaining letters
    for i in range(min(len(guess), len(answer))):
        if guess[i] == answer[i]:
            feedback[i] = 'G'
        else:
            remaining_letters[answer[i]] += 1
    
    # Second pass: check for correct letters in wrong positions
    for i in range(min(len(guess), len(answer))):
        if feedback[i] == '_':
            if remaining_letters[guess[i]] > 0:
                feedback[i] = 'Y'
                remaining_letters[guess[i]] -= 1
            else:
                feedback[i] = 'B'
    
    # Handle any additional characters in guess that exceed answer length
    for i in range(len(answer), len(guess)):
        feedback[i] = 'B'
    
    return ''.join(feedback)

if __name__ == "__main__":
    # Test case 1: Exact match
    test1_guess = "hello"
    test1_answer = "hello"
    test1_result = compute_feedback(test1_guess, test1_answer)
    print(f"Test 1: {test1_result == 'GGGGG'}, Expected: GGGGG, Got: {test1_result}")
    
    # Test case 2: No match
    test2_guess = "abcde"
    test2_answer = "fghij"
    test2_result = compute_feedback(test2_guess, test2_answer)
    print(f"Test 2: {test2_result == 'BBBBB'}, Expected: BBBBB, Got: {test2_result}")
    
    # Test case 3: Mixed feedback
    test3_guess = "house"
    test3_answer = "mouse"
    test3_result = compute_feedback(test3_guess, test3_answer)
    print(f"Test 3: {test3_result == 'BGGGG'}, Expected: BGGGG, Got: {test3_result}")
    
    # Test case 4: Repeated letters in guess
    test4_guess = "hello"
    test4_answer = "below"
    test4_result = compute_feedback(test4_guess, test4_answer)
    print(f"Test 4: {test4_result == 'BGGBY'}, Expected: BGGBY, Got: {test4_result}")
    
    # Test case 5: Repeated letters in answer
    test5_guess = "boost"
    test5_answer = "robot"
    test5_result = compute_feedback(test5_guess, test5_answer)
    print(f"Test 5: {test5_result == 'YGYBG'}, Expected: YGYBG, Got: {test5_result}")
