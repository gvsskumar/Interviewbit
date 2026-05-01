let str = "abdcsbdfgbbadgfb";
let ch = "b";
// 1. Using split() Method
let count = str.split(ch).length - 1;

console.log(count); // 5
// 2. Using for Loop
let count = 0;

for (let i = 0; i < str.length; i++) {
    if (str[i] === ch) {
        count++;
    }
}

console.log(count); // 5
// 3. Using filter() Method
let count = str.split('').filter(char => char === ch).length;

console.log(count); // 5
// 4. Using reduce() Method
let count = str.split('').reduce((acc, curr) => {
    return curr === ch ? acc + 1 : acc;
}, 0);

console.log(count); // 5
// 5. Using match() Method
let count = (str.match(/b/g) || []).length;

console.log(count); // 5
// 6. Using for...of Loop
let count = 0;

for (let char of str) {
    if (char === ch) {
        count++;
    }
}

console.log(count); // 5
// Interview Best Answer
// Use for loop or reduce() because they show logic understanding instead of shortcut methods.