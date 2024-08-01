// Longest common prefix (Leetcode - Q.14)
// Level : easy
//
// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"

// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

//     1 <= strs.length <= 200
//     0 <= strs[i].length <= 200
//     strs[i] consists of only lowercase English letters.

pub fn longest_common_prefix(strs: Vec<String>) -> String {
    if strs.len() == 0 {
        return String::new();
    } else if strs.len() == 1 {
         return strs[0].clone();
    }
    let mut string: String = String::new();
    let mut count: usize = 0;
    let test: String = strs[0].clone();
    loop {
        let mut flag: bool = false;
        for i in 0..strs.len() {
            if strs[i].len() == 0 {
                flag = true;
                break;
            }
            if test.get(count..=count) != strs[i].get(count..=count) {
                flag = true;
                break;
            } else {
                if test.get(count..=count) == None {
                    flag = true;
                    break;
                }
            }
        }
        if !flag {
            string.push_str(test.get(count..=count).unwrap());
            count = count + 1;
        } else {
            break;
        }
    }
    string
}

fn main() {
    let str: String = longest_common_prefix(vec!["flower".to_string(),"flow".to_string(),"flight".to_string()]);
    // let str: String = longest_common_prefix(vec!["".to_string(), "".to_string()]);
    // let str: String = longest_common_prefix(vec!["ab".to_string(), "a".to_string()]);
    // let str: String = longest_common_prefix(vec!["flower".to_string(), "flower".to_string()]);
    println!("longest common prefix is : {}", str);
}