use vstd::prelude::*;

verus! {
    fn sum_loop(n: u64) -> (ret: (u64, u64))
        requires 
            n >= 0,
            n <= 10  // Small upper bound to prevent overflow
        ensures 
            ret.0 >= 0,
            0 <= ret.1 <= n,
            ret.1 == n
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}