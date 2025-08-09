use vstd::prelude::*;

verus! {
    fn compute_double(x: i32) -> (result: (i32, i32))
        requires 
            x > 0,
            x <= i32::MAX / 2,  // Prevent overflow
        ensures result.0 == 2 * x,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}