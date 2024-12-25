//https://leetcode.com/problems/generate-parentheses/

function generateParenthesis(n){
    let stack = []
    let res = []

    function dfs(open, close){
        if(open === close && close === n){
            res.push(stack.join(''))
            return
        }

        if (open < n){
            stack.push('(')
            dfs(open + 1, close)
            stack.pop()
        }

        if (close < open){
            stack.push(')')
            dfs(open, close + 1)
            stack.pop()
        }
    }

    dfs(0,0)

    return res
};
