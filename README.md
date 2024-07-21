<h1 align="center"> LEARN </h1>

<details>
  <summary> Vector </summary>  
  
  ### 1. Creating a Vector
  
  - **`new`**: Creates a new, empty vector.
  - **`with_capacity`**: Creates a new, empty vector with a specified capacity.
  - **`vec!`**: Macro for creating a vector with initial values.
  
  ```rust
  fn main() {
      let v: Vec<i32> = Vec::new();
      let v_with_capacity: Vec<i32> = Vec::with_capacity(10);
      let v_macro = vec![1, 2, 3, 4, 5];
  }
  ```
  
  ### 2. Adding Elements
  
  - **`push`**: Adds an element to the end of the vector.
  
  ```rust
  fn main() {
      let mut v = Vec::new();
      v.push(1);
      v.push(2);
      println!("{:?}", v); // Output: [1, 2]
  }
  ```
  
  ### 3. Removing Elements
  
  - **`pop`**: Removes the last element from the vector and returns it.
  
  ```rust
  fn main() {
      let mut v = vec![1, 2, 3];
      let last = v.pop();
      println!("{:?}, {:?}", v, last); // Output: [1, 2], Some(3)
  }
  ```
  
  - **`remove`**: Removes the element at a specified index.
  
  ```rust
  fn main() {
      let mut v = vec![1, 2, 3];
      let second = v.remove(1);
      println!("{:?}, {:?}", v, second); // Output: [1, 3], 2
  }
  ```
  
  ### 4. Accessing Elements
  
  - **`get`**: Returns an option reference to the element at the specified index.
  
  ```rust
  fn main() {
      let v = vec![1, 2, 3];
      match v.get(1) {
          Some(value) => println!("Value at index 1: {}", value),
          None => println!("No value at index 1"),
      }
  }
  ```
  
  - **Indexing**: Using square brackets to access elements (panics if out of bounds).
  
  ```rust
  fn main() {
      let v = vec![1, 2, 3];
      let first = v[0];
      println!("First element: {}", first); // Output: 1
  }
  ```
  
  ### 5. Iterating
  
  - **`iter`**: Returns an iterator over the vector.
  - **`iter_mut`**: Returns a mutable iterator over the vector.
  - **`into_iter`**: Consumes the vector and returns an iterator that takes ownership.
  
  ```rust
  fn main() {
      let v = vec![1, 2, 3];
      
      // Immutable iteration
      for val in v.iter() {
          println!("{}", val);
      }
      
      // Mutable iteration
      let mut v = vec![1, 2, 3];
      for val in v.iter_mut() {
          *val *= 2;
      }
      println!("{:?}", v); // Output: [2, 4, 6]
      
      // Consuming iteration
      for val in v.into_iter() {
          println!("{}", val);
      }
  }
  ```
  
  ### 6. Transforming and Extending
  
  - **`extend`**: Extends the vector by appending elements from an iterator.
  
  ```rust
  fn main() {
      let mut v = vec![1, 2, 3];
      v.extend(vec![4, 5, 6]);
      println!("{:?}", v); // Output: [1, 2, 3, 4, 5, 6]
  }
  ```
  
  - **`map`**: Transforms elements (used with iterators).
  
  ```rust
  fn main() {
      let v = vec![1, 2, 3];
      let v2: Vec<_> = v.iter().map(|x| x * 2).collect();
      println!("{:?}", v2); // Output: [2, 4, 6]
  }
  ```
  
  ### 7. Slicing
  
  - **`as_slice`**: Returns a slice of the whole vector.
  - **`split_at`**: Splits the vector at a given index.
  
  ```rust
  fn main() {
      let v = vec![1, 2, 3, 4, 5];
      let slice = v.as_slice();
      println!("{:?}", slice); // Output: [1, 2, 3, 4, 5]
      
      let (left, right) = v.split_at(2);
      println!("{:?}, {:?}", left, right); // Output: [1, 2], [3, 4, 5]
  }
  ```
  
  ### 8. Checking Properties
  
  - **`is_empty`**: Checks if the vector is empty.
  - **`len`**: Returns the number of elements in the vector.
  
  ```rust
  fn main() {
      let v: Vec<i32> = Vec::new();
      println!("Is empty: {}", v.is_empty()); // Output: true
      
      let v = vec![1, 2, 3];
      println!("Length: {}", v.len()); // Output: 3
  }
  ```
  
  ### 9. Sorting
  
  - **`sort`**: Sorts the vector in place.
  
  ```rust
  fn main() {
      let mut v = vec![3, 1, 2];
      v.sort();
      println!("{:?}", v); // Output: [1, 2, 3]
  }
  ```
  
  ### 10. Removing Elements by Condition
  
  - **`retain`**: Retains only the elements specified by the predicate.
  
  ```rust
  fn main() {
      let mut v = vec![1, 2, 3, 4, 5];
      v.retain(|&x| x % 2 == 0);
      println!("{:?}", v); // Output: [2, 4]
  }
  ```
</details>

<details>
  <summary> String </summary>
  
  ### 1. Creating and Initializing
  
  - **`new`**: Creates a new, empty `String`.
  - **`from`**: Creates a `String` from a `&str`.
  
  ```rust
  fn main() {
      let s1 = String::new();
      let s2 = String::from("hello");
  }
  ```
  
  ### 2. Appending
  
  - **`push`**: Appends a character to the end of a `String`.
  - **`push_str`**: Appends a string slice to the end of a `String`.
  
  ```rust
  fn main() {
      let mut s = String::from("hello");
      s.push(' ');
      s.push_str("world");
      println!("{}", s); // Output: "hello world"
  }
  ```
  
  ### 3. Accessing Characters and Slices
  
  - **`chars`**: Returns an iterator over the characters of the string.
  - **`get`**: Returns an option reference to a substring.
  
  ```rust
  fn main() {
      let s = String::from("hello");
      
      // Iterating over characters
      for c in s.chars() {
          println!("{}", c);
      }
  
      // Getting a substring
      if let Some(sub) = s.get(1..4) {
          println!("{}", sub); // Output: "ell"
      }
  }
  ```
  
  ### 4. Length and Capacity
  
  - **`len`**: Returns the number of bytes in the string.
  - **`is_empty`**: Checks if the string is empty.
  - **`capacity`**: Returns the total capacity of the string in bytes.
  
  ```rust
  fn main() {
      let s = String::from("hello");
      println!("Length: {}", s.len()); // Output: 5
      println!("Is empty: {}", s.is_empty()); // Output: false
      println!("Capacity: {}", s.capacity()); // Output: varies
  }
  ```
  
  ### 5. Modifying
  
  - **`clear`**: Clears the string, removing all contents.
  - **`replace`**: Replaces all matches of a pattern with another string.
  
  ```rust
  fn main() {
      let mut s = String::from("hello");
      s.clear();
      println!("Cleared string: '{}'", s); // Output: ""
  
      let s = String::from("hello world");
      let replaced = s.replace("world", "Rust");
      println!("Replaced string: {}", replaced); // Output: "hello Rust"
  }
  ```
  
  ### 6. Trimming and Splitting
  
  - **`trim`**: Removes whitespace from both ends of a string.
  - **`split`**: Splits the string on a pattern, returning an iterator.
  
  ```rust
  fn main() {
      let s = String::from("  hello  ");
      let trimmed = s.trim();
      println!("Trimmed: '{}'", trimmed); // Output: "hello"
  
      let s = String::from("hello world");
      for part in s.split(' ') {
          println!("{}", part); // Output: "hello" and "world"
      }
  }
  ```
  
  ### 7. Case Conversion
  
  - **`to_lowercase`**: Converts the string to lowercase.
  - **`to_uppercase`**: Converts the string to uppercase.
  
  ```rust
  fn main() {
      let s = String::from("HeLLo WoRLd");
      println!("Lowercase: {}", s.to_lowercase()); // Output: "hello world"
      println!("Uppercase: {}", s.to_uppercase()); // Output: "HELLO WORLD"
  }
  ```
  
  ### 8. Searching
  
  - **`contains`**: Checks if the string contains a substring.
  - **`find`**: Finds the byte index of the first occurrence of a pattern.
  
  ```rust
  fn main() {
      let s = String::from("hello world");
      println!("Contains 'world': {}", s.contains("world")); // Output: true
  
      if let Some(index) = s.find('o') {
          println!("First 'o' at index: {}", index); // Output: 4
      }
  }
  ```
  
  ### 9. Conversion
  
  - **`parse`**: Parses a string into another type that implements the `FromStr` trait.
  - **`as_str`**: Converts the `String` to a `&str`.
  
  ```rust
  fn main() {
      let s = String::from("42");
      let num: i32 = s.parse().expect("Not a number!");
      println!("Parsed number: {}", num); // Output: 42
  
      let s = String::from("hello");
      let slice: &str = s.as_str();
      println!("String slice: {}", slice); // Output: "hello"
  }
  ```
  
  ### 10. Concatenation
  
  - **`+` Operator**: Concatenates two strings.
  - **`format!` Macro**: Formats a string using the given arguments.
  
  ```rust
  fn main() {
      let s1 = String::from("hello");
      let s2 = String::from("world");
      let s3 = s1 + " " + &s2;
      println!("{}", s3); // Output: "hello world"
  
      let s1 = String::from("hello");
      let s2 = String::from("world");
      let s3 = format!("{} {}", s1, s2);
      println!("{}", s3); // Output: "hello world"
  }
  ```
</details>

<h1 align="center"> PROBLEMS </h1>

<div align="center">
  
  `rust`
</div>

<details>
  <summary>
    <h3> 1) Electricity bill calculator (easy) </h3>
  </summary>

  ```rust
  // Electricity bill calculator
  // Level : easy
  // 
  // Calculate the electricity bill, 
  // The inputs will be previous and current reading of electricity/power used in units,
  // Output should be the total amount of price (unit price is given below)
  // unit price - 
  // for the first 0 to 100 units in the total units used - price per unit is 2
  // for the second 100 units, that is from 101 to 200 units - price per unit is 2.5
  // for the third 100 units, that is from 201 to 300 units - price per unit is 3
  // for the fourth 100 units, that is above 300 - price per unit is 4
  // eg. for a consumer who used 267 units of power - the bill will be 651 
  // for the first 100 units 100 times 2 is 200, second 100 unit 100 times 2.5 is 250, third remaining 67 units 67 times 3 is 201
  // the total of 200, 250 and 201 is 651
  
  
  use std::io::{Write, stdin, stdout};
  
  fn main(){
      let mut p_reading: String = String::new(); 
      print!("Enter the previous reading : ");
      stdout().flush().unwrap();
      stdin().read_line(&mut p_reading).expect("Something went wrong");
      let p_reading: i32 = p_reading.trim().parse().expect("Not a number");
  
      let mut c_reading: String = String::new(); 
      print!("Enter the current reading : ");
      stdout().flush().unwrap();
      stdin().read_line(&mut c_reading).expect("Something went wrong");
      let c_reading: i32 = c_reading.trim().parse().expect("Not a number");
  
      let used_units: i32 = c_reading - p_reading;
      let amount: f32 = calculate_unit_price(used_units);
      println!("amount is : {}", amount);
  }
  
  fn calculate_unit_price(used_units: i32) -> f32 {
      let used: f32 = (used_units as f32/100.0).ceil();
      match used {
          x if x < 1.0 => 0.0,
          1.0 => (used_units*2) as f32,
          2.0 => 100.0*2.0+((used_units-100) as f32)*2.5,
          3.0 => 100.0*4.5+((used_units-200) as f32)*3.0,
          _ => 100.0*7.5+((used_units-300) as f32)*4.0 
      }
  }
  ```
</details>

<details>
  <summary>
    <h3> 2) Median of Two Sorted Arrays (hard) </h3>
  </summary>
  
  ```rust
  // Median of two sorted arrays (Leetcode - Q.04)
  // Level: hard
  //
  // Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
  
  // The overall run time complexity should be O(log (m+n)).
  
  // Example 1:
  
  // Input: nums1 = [1,3], nums2 = [2]
  // Output: 2.00000
  // Explanation: merged array = [1,2,3] and median is 2.
  
  // Example 2:
  
  // Input: nums1 = [1,2], nums2 = [3,4]
  // Output: 2.50000
  // Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
  
  
  pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
      let l1: i32 = nums1.len() as i32;
      let l2: i32 = nums2.len() as i32;
      let t_len: i32 = l1 + l2;
      let middle: i32 = ((t_len - 1) as f32 / 2.0).ceil() as i32;
      let mut i: i32 = 0;
      let mut j: i32 = 0;
      let is_even: bool = t_len % 2 == 0;
      let mut amount: i32 = 0;
      let mut mean: f64 = 0.0;
      if l1 == 0 || l2 == 0 {
          if l1 == 0 {
              if is_even {
                  mean = (nums2[(middle-1) as usize] + nums2[middle as usize]) as f64 / 2.0;
              } else {
                  mean = nums2[middle as usize] as f64;
              }
          } else {
              if is_even {
                  mean = (nums1[(middle-1) as usize] + nums1[middle as usize]) as f64 / 2.0;
              } else {
                  mean = nums1[middle as usize] as f64;
              }
          }
      } else {
          for count in 0..=middle {
              if nums1[i as usize] < nums2[j as usize] {
                  if is_even && count == middle - 1 {
                      amount = amount + nums1[i as usize];
                  }
                  if count == middle {
                      amount = amount + nums1[i as usize];
                  }
                  i = i + 1;
              } else {
                  if is_even && count == middle - 1 {
                      amount = amount + nums2[j as usize];
                  }
                  if count == middle {
                      amount = amount + nums2[j as usize];
                  }
                  j = j + 1;
              }
              if i >= l1 || j >= l2 {
                  break;
              }
          }
          if (i+j-1) == middle {
              mean = if is_even { amount as f64/2.0 } else { amount as f64 };
          } else if j >= l2 {
              if (i+j-1) == middle-1 {
                  if is_even {
                      mean = (amount + nums1[(middle - j) as usize]) as f64 / 2.0;
                  } else {
                      mean = nums1[(middle - j) as usize] as f64;
                  }
              } else {
                  if is_even {
                      mean = (nums1[(middle-j-1) as usize] + nums1[(middle-j) as usize]) as f64 / 2.0;
                  } else {
                      mean = nums1[(middle - j) as usize] as f64;
                  }
              }
          } else if i >= l1 {
              if (i+j-1) == middle-1 {
                  if is_even {
                      mean = (amount + nums2[(middle - i) as usize]) as f64 / 2.0;
                  } else {
                      mean = nums2[(middle - i) as usize] as f64;
                  }
              } else {
                  if is_even {
                      mean = (nums2[(middle-i-1) as usize] + nums2[(middle-i) as usize]) as f64 / 2.0;
                  } else {
                      mean = nums2[(middle - i) as usize] as f64;
                  }
              }
          }
      }
      return mean;
  }
  fn main() {
      assert_eq!(2.5 , find_median_sorted_arrays(vec![1, 2], vec![3, 4]), "median should be 2.5");
      assert_eq!(1.0 , find_median_sorted_arrays(vec![], vec![1]), "median should be 1.2");
      assert_eq!(2.0 , find_median_sorted_arrays(vec![1, 2], vec![3]), "median should be 2.0");
      assert_eq!(4.0 , find_median_sorted_arrays(vec![1, 4, 6], vec![2, 3, 5, 7]), "median should be 4.0");
      println!("Test passed...");
  }
  ```
</details>

<details>
  <summary>
    <h3> 3) Longest common prefix (easy) </h3>
  </summary>

  ```rust
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
  ```
</details>
