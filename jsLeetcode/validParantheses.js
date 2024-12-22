//https://leetcode.com/problems/valid-parentheses/


function isValid(s){
    let stack = []
    let openToClose = {")":"(", "]":"[", "}":"{"}

    for(const c of s){
        if (c in openToClose){
            if (stack.length > 0 && stack[stack.length - 1] === openToClose[c]){
                stack.pop()
            }
            else{
                return false
            }
        }
        else{
            stack.push(c)
        }
    }

    return stack.length === 0
}
