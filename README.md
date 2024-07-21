<h1 align="center"> Problems </h1>

<div align="center">
  
  `rust`
</div>

<h3> 1) Electricity bill calculator </h3>

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

<h3> 2) Median of Two Sorted Arrays </h3>

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

