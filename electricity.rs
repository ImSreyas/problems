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
    if used_units <= 0 { 
        return 0.0; 
    } else if used_units <= 100 { 
        return (used_units*2) as f32; 
    } else if used_units <= 200 { 
        return 100.0*2.0+((used_units-100) as f32)*2.5; 
    } else if used_units <= 300 { 
        return 100.0*4.5+((used_units-200) as f32)*3.0; 
    } else { 
        return 100.0*7.5+((used_units-300) as f32)*4.0; 
    }
}