//https://leetcode.com/problems/simplify-path

function simplifyPath(path) {
    let stack = []
    let components = path.split('/')

    for (const part of components) {
        if (part === '..') {
            if (stack.length > 0) {
                stack.pop()
            }
        } else if (part !== '.' && part !== '') {
            stack.push(part)
        }
    }
    let res = '/' + stack.join('/')
    return res
}
