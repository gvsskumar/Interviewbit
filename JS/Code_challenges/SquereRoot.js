// You can calculate square root without using Math.sqrt() by using methods like Binary Search or Newton’s Method.
// For positive integers and Infinity, here’s a clean JavaScript approach.
// Binary Search → good for integer square root
const squareRoot = (num) => {
    if (num===Infinity) return Infinity;
    if(num<0) return "Allowed positive number only";
    if(num==0 || num==1)return num;
    let low = 1
    let high = num
    while(low<=high){
        mid = Math.floor((low+high)/2);
        if (mid*mid==num) return mid;
        else if (mid*mid<num){
            low = mid+1
        }
        else if(mid*mid>num){
            high = mid-1
        } 
    }
    return high;
}
console.log(squareRoot(25))