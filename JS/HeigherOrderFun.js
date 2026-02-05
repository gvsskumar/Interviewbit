function add(a, b) {
    return a + b;
}
function multiply(a, b) {
    return a * b;
}

function higherOrderFun(a, b, callback) {
    return callback(a, b);
}

const result = higherOrderFun(4, 3, add);
console.log(result); // 7

const result1 = higherOrderFun(4, 3, multiply);
console.log(result); // 12 