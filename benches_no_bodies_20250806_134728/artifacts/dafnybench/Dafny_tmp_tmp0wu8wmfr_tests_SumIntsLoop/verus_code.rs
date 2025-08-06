use vstd::prelude::*;

verus! {
    spec fn sum_ints(n: int) -> int
        decreases n
    {
        if n <= 0 {
            0
        } else {
            sum_ints(n - 1) + n
        }
    }

    fn sum_ints_loop(n: u32) -> (s: u32)
        requires n >= 0,
        ensures s == sum_ints(n as int),
        ensures s == n * (n + 1) / 2,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn main() {
    // TODO: Remove this comment and implement the function body
    }
}