# This example simulates a development workflow where different AI coding tools
# contribute to a single code artifact, as discussed in the article.

# --- Simulated AI 1: Code Generation ---
# An AI tool generates the core logic for a function based on a prompt.
# For instance, 'Write a Python function to calculate the nth Fibonacci number.'
def calculate_fibonacci(n):
    """
    --- Simulated AI 3: Documentation Generation ---
    An AI tool generates a comprehensive docstring for the function.

    Calculates the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The index of the Fibonacci number to calculate. Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer or not an integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# --- Simulated AI 2: Test Generation ---
# Another AI tool generates unit tests to verify the correctness of the generated code.
def run_tests():
    """
    Runs a series of tests for the calculate_fibonacci function.
    This simulates an AI generating test cases to ensure correctness and robustness.
    """
    print("\n[AI 2 - Test Generation]: Generating and running unit tests...")
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
        (20, 6765)
    ]

    all_passed = True
    for input_n, expected_output in test_cases:
        try:
            actual_output = calculate_fibonacci(input_n)
            assert actual_output == expected_output, \
                f"  Test failed for input {input_n}: Expected {expected_output}, Got {actual_output}"
            print(f"  Test passed for input {input_n} (Output: {actual_output})")
        except AssertionError as e:
            print(f"  {e}")
            all_passed = False
        except ValueError as e:
            print(f"  Test failed for input {input_n} with ValueError: {e}")
            all_passed = False

    # Test edge case: negative input (should raise ValueError)
    try:
        calculate_fibonacci(-1)
        print("  Test failed for negative input: Expected ValueError, but no error was raised.")
        all_passed = False
    except ValueError as e:
        print(f"  Test passed for negative input: Caught expected error '{e}'")
    except Exception as e:
        print(f"  Test failed for negative input: Caught unexpected error '{e}'")
        all_passed = False

    if all_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed. Review the output above.")


if __name__ == "__main__":
    print("--- AI-Assisted Development Workflow Simulation ---")
    print("This example demonstrates how different AI tools can contribute to a complete, tested, and documented code artifact.")

    # Step 1: Simulate AI 1 (Code Generation) provides the core function.
    print("\n[AI 1 - Code Generation]: The core utility function 'calculate_fibonacci' is generated.")
    print("  (Function definition is above this main block.)")

    # Step 2: Simulate AI 3 (Documentation Generation) provides the docstring.
    print("\n[AI 3 - Documentation Generation]: A comprehensive docstring for 'calculate_fibonacci' is generated.")
    print("  --- Function Documentation ---")
    print(calculate_fibonacci.__doc__)
    print("  ----------------------------")

    # Step 3: Simulate AI 2 (Test Generation) provides and runs tests.
    run_tests()

    print("\n--- End of AI Workflow Simulation ---")
    print("Final check: Calculating Fibonacci for 7 (should be 13): ", calculate_fibonacci(7))
