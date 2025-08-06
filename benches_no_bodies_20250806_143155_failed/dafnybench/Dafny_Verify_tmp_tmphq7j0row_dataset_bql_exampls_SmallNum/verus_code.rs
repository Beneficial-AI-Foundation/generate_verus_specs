use vstd::prelude::*;

verus! {
    fn add_small_numbers(a: &[i32], n: usize, max: i32) -> (r: i32)
        requires
            n > 0,
            n <= a.len(),
            forall|i: int| 0 <= i && i < n ==> a[i] <= max,
            max >= 0,
            n <= 100,
            max <= 100,
        ensures
            r <= max * (n as i32),
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}