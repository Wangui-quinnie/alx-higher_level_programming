#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const [arg] = process.argv.slice(2);
const num = parseInt(arg);
console.log(factorial(num));
