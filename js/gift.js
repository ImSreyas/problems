// inputs 
let seq = 4;
let size = 3;

while (true) {

}

        if names.len() < 2 { return names }
        let mut names = names.clone();
        let mut heights = heights.clone();
        for i in 0..heights.len()-1 {
            for j in 0..heights.len()-i-1 {
                if heights[j] < heights[j+1] {
                    let temp: String = names[j].clone();
                    names[j] = names[j+1].clone();
                    names[j+1] = temp;

                    let temp: i32 = heights[j];
                    heights[j] = heights[j+1];
                    heights[j+1] = temp;
                }
            }
        }
        return names;


        let size: i32 = nums.len() as i32;
        let sum: i32 = (size*(size-1))/2;
        let mut total: i32 = 0;
        for i in 0..size {
            total = total + nums[i as usize];
        }
        return total - sum;