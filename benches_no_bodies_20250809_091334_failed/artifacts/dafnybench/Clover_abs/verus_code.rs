use vstd::prelude::*;

verus! {
    fn abs(x: i32) -> (y: i32)
        requires x > i32::MIN,
        ensures
            x >= 0 ==> x == y,
            x < 0 ==> x + y == 0,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}