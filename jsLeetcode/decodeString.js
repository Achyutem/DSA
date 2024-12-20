function decodeString(s) {
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    if (char !== ']') {
      stack.push(char);
    } else {
      let substr = '';
      while (stack.length > 0 && stack[stack.length - 1] !== '[') {
        substr = stack.pop() + substr;
      }

      stack.pop();

      let k = '';
      while (stack.length > 0 && !isNaN(stack[stack.length - 1])) {
        k = stack.pop() + k;
      }

      k = parseInt(k);
      let repeated = substr.repeat(k);
      stack.push(repeated);
    }
  }

  return stack.join('');
}

