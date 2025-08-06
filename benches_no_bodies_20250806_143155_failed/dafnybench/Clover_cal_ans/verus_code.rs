use vstd::prelude::*;

verus! {
    fn cal_div() -> (ret: (i32, i32))
        ensures
            ret.0 == 191i32 / 7i32,
            ret.1 == 191i32 % 7i32,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}