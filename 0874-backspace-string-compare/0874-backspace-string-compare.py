class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace_run(s):
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        final_s = backspace_run(s)
        final_t = backspace_run(t)
        return final_s == final_t