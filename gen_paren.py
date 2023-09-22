def generate_parenthesis(N):
    stack = []
    ans  = []
    def backtrack(open, close):
        if open == close == N:
            ans.append("".join(stack))
            return
        if open < N:
            stack.append("(")
            backtrack(open+1, close)
            stack.pop()
        if close < open:
            stack.append(")")
            backtrack(open, close+1)
            stack.pop()
    backtrack(0,0)
    return ans
N = int(input())
print(generate_parenthesis(N))
            