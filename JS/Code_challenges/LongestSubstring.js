// Return Longest Substring
function longestSubstringSET(s) {
    let set = new Set();
    let left = 0;

    let maxLength = 0;
    let start = 0; // track start of result

    for (let right = 0; right < s.length; right++) {
        while (set.has(s[right])) {
            set.delete(s[left]);
            left++;
        }

        set.add(s[right]);

        if (right - left + 1 > maxLength) {
            maxLength = right - left + 1;
            start = left;
        }
    }

    return s.substring(start, start + maxLength);
}
console.log(longestSubstringSET("abcabcbb")) // abc
//---------------------------------------------//

// Optimized Version (Using Map — Better in Interviews)
function longestSubstringMAP(s) {
    let map = new Map();
    let left = 0;

    let maxLength = 0;
    let start = 0;

    for (let right = 0; right < s.length; right++) {
        if (map.has(s[right])) {
            left = Math.max(map.get(s[right]) + 1, left);
        }

        map.set(s[right], right);

        if (right - left + 1 > maxLength) {
            maxLength = right - left + 1;
            start = left;
        }
    }

    return s.substring(start, start + maxLength);
}
console.log(longestSubstringMAP("abcabcbb")) // abc