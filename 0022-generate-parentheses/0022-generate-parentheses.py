class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(open_count,closed_count):
            if open_count==closed_count==n:       #if open_count and closed count and n equals 3 it checks after executing the inner if loops using backtracking
                res.append("".join(stack))      
                return  #terminate the recursive call without returning anything
            if open_count<n:
                stack.append("(")
                backtrack(open_count+1,closed_count)
                stack.pop()
            if closed_count<open_count:
                stack.append(")")
                backtrack(open_count,closed_count+1)
                stack.pop()
        backtrack(0,0)    #initialize the backtracking process, representing the initial state where no parentheses have been added,
        return res