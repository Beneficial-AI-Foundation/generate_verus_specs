use vstd::prelude::*;

verus! {
    fn min(x: int, y: int) -> (z: int)
        ensures 
            x <= y ==> z == x,
            x > y ==> z == y,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}