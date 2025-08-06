use vstd::prelude::*;

verus! {
    fn double_quadruple(x: i32) -> (result: (i32, i32))
        requires 
            x.checked_mul(4).is_some()
        ensures 
            result.0 == x * 2 && result.1 == x * 4
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}