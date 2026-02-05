// Currying Function
function add(a) {
    return function (b) {
        return a + b;
    }
}   

const add5 = add(5);
console.log(add5(10));  // 15

//--------------//
function Currying(a) {
  return function (b) {
    return function (c) {
      return function (d) {
        return a + b + c + d;
      };
    };
  };
}

console.log(Currying(1)(2)(3)(4)); // 10

//---------------//

function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    }
    return (...nextArgs) => curried(...args, ...nextArgs);
  };
}

function add(a, b, c, d) {
  return a + b + c + d;
}

const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)(4)); // 10
