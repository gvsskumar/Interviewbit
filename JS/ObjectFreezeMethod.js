const obj = {
    a: 1,
    b: 2,
    c: 3
}
Object.freeze(obj);
obj.c = 4;
console.log(obj);   // { a: 1, b: 2, c: 3 }

//-------------------------//

const name = "Surya";
age = 20;
console.log(delete name);    // false
console.log(delete age);    // true