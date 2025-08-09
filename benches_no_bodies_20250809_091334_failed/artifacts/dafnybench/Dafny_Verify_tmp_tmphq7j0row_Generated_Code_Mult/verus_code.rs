use vstd::prelude::*;

verus! {
    fn mult(a: u32, b: u32) -> (x: u32)
        requires 
            a >= 0 && b >= 0,
            a <= 100,
            b <= 100,
        ensures x == a * b,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}