use vstd::prelude::*;

verus! {
    fn main_method() -> (ret: (i32, i32, i32, i32))
        ensures ret.3 >= 1
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}