use vstd::prelude::*;

verus! {
    fn multiple_returns(x: int, y: int) -> (ret: (int, int))
        ensures
            ret.0 == x + y,
            ret.1 == x - y,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}