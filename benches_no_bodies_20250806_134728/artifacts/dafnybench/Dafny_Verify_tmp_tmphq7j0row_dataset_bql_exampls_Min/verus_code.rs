use vstd::prelude::*;

verus! {
    fn min(a: &[int], n: usize) -> (min: int)
        requires 
            0 < n <= a.len(),
        ensures
            exists|i: int| 0 <= i < n && a[i] == min,
            forall|i: int| 0 <= i < n ==> a[i] >= min,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}