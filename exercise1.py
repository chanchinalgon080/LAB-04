def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)

    reversed_str = ''
    while stack:
        reversed_str += stack.pop()

    return reversed_str

test_cases = [
    "hello",
    "racecar",
    "bye"
]

for i, test in enumerate(test_cases, 1):
    result = reverse_string(test)
    print(f"Test Case {i}: Input: '{test}' → Reversed: '{result}'")
