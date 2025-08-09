use vstd::prelude::*;

verus! {
    spec fn has_count(v: int, a: &[int], n: int) -> int
        decreases n
    {
        if n <= 0 {
            0
        } else {
            if a[n-1] == v {
                has_count(v, a, n-1) + 1int
            } else {
                has_count(v, a, n-1)
            }
        }
    }

    fn count(v: int, a: &[int], n: usize) -> (r: i32)
        requires 
            n <= a.len(),
            n < 1000000000,
        ensures 
            r == has_count(v, a, n as int),
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}