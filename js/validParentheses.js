// Valid Parentheses (Leetcode - Q.20)
// Level : easy 
//
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//     Every close bracket has a corresponding open bracket of the same type.
 

// Example 1:

// Input: s = "()"
// Output: true

// Example 2:

// Input: s = "()[]{}"
// Output: true

// Example 3:

// Input: s = "(]"
// Output: false
 

// Constraints:

//     1 <= s.length <= 104
//     s consists of parentheses only '()[]{}'.


var isValid = function(s) {
    let list = [];
    for (char of s.split("")) {
        if ("({[".includes(char)) {
            list.push(char);
        } else {
            let cha;
            switch (char) {
                case ")": cha = "(";
                break;
                case "}": cha = "{";
                break;
                case "]": cha = "[";
                break;
            }
            if (list.pop() != cha) {
                return false;
            }
        }
    }
    return list.length === 0;
};

console.log(isValid("(){}[]")); // true
console.log(isValid("(){}(}")); // false
console.log(isValid("({})")); // true
console.log(isValid("({[]})")); // true
console.log(isValid("({]})")); // false
console.log(isValid("(")); // false