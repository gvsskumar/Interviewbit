// Spread Operator (...): Expands elements of an array or properties of an object.
const arr1 = [1, 2, 3];
const arr2 = [4, 5];

const result = [...arr1, ...arr2];
console.log(result); // [1, 2, 3, 4, 5]

// Rest Operator (...): Collects multiple values into an array
const [a, b, ...rest] = [1, 2, 3, 4, 5];
console.log(a); // 1    
console.log(b); // 2
console.log(rest); // [3, 4, 5]