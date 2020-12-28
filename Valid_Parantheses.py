# Program to find if the given sequence of parantheses is valid.
# Some examples of Valid Parantheses - () or ()[] or {[]}
# Some examples of Invalid Parantheses - ([)] or {{}
# Time Complexity - O(n)
# Space Complexity - O(n)


class Solution:
    def isValid(self, s: str):
        stack = []  # Initialize a stack S
        mapping = {')': '(', "}": "{", "]": "["}
        for c in s:  # Process each bracket of the expression one at a time.
            # If we encounter a closing bracket, then we check the element on top of the stack.
            if c in mapping:
                topmost = stack.pop() if stack else '*'
                # If the element at the top of the stack is an opening bracket of the different type - implies an invalid expression
                if mapping[c] != topmost:
                    return False
            else:  # If we encounter an opening bracket, we simply push it onto the stack
                stack.append(c)
        return not stack


randomSequence = '([])'
print("Given RandomSequence is Valid?", Solution().isValid(randomSequence))
