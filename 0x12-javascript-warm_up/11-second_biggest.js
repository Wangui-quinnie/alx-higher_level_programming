#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(Number).filter(num => !isNaN(num));
if (numbers.length < 2) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
