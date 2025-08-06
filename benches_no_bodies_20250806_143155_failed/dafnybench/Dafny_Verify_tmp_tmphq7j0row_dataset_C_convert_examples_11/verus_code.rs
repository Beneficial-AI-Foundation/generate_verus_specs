use vstd::prelude::*;

verus! {
    fn main_method(x: i32) -> (result: (i32, i32))
        requires 
            x > 0,
            x <= 1073741823, // prevent overflow (2^30 - 1)
        ensures result.0 == 2 * x,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}