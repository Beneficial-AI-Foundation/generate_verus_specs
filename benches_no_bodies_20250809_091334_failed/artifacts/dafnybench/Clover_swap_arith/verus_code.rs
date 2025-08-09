use vstd::prelude::*;

verus! {
    fn SwapArithmetic(X: int, Y: int) -> (ret: (int, int))
        ensures
            ret.0 == Y,
            ret.1 == X,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}