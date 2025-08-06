use vstd::prelude::*;

verus! {
    fn swap(X: int, Y: int) -> (result: (int, int))
        ensures 
            result.0 == Y,
            result.1 == X,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}