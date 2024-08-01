// String pattern transform 
// Level : easy
//
// The input will be a string, the output should be a string transformed as given below : 
//
// '*' should be removed.
// 0 should be removed.
// Every numbers should present in the string should be at the beginning of output string in the reverse order.
// Replace any number in the input string with 0 at it's original position. 
// If a Upper case then lower case letters found close, swap those characters

let string = "Sre*125*00hij*ab" // output : 521rS*e000hijab

let result = "";
let flag = false;

for (char of string.split("")) {
    if (char == 0 || char == "*") continue;
    if (parseInt(char)) {
        result = char + result;
        result = result + "0";
    } else {
        if (char.toUpperCase() == char) {
            result += char;
            flag = true;
        } else {
            if (flag) {
                result = result.slice(0, result.length - 1) + char + result.charAt(result.length - 1) + "*";
                flag = false;
            } else {
                    result += char;
            }
        }
    }
}                                                                                                          
console.log(result);