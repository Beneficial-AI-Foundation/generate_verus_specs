use vstd::prelude::*;

verus! {
    // returns an index of the largest element of array 'a' in the range [0..n)
    fn findMax(a: &[int], n: usize) -> (r: usize)
        requires 
            a.len() > 0,
            0 < n <= a.len(),
        ensures 
            0 <= r < n <= a.len(),
            forall|k: int| 0 <= k < n ==> a[r as int] >= a[k],
            // Array is unchanged (implicit in Rust with & reference)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}