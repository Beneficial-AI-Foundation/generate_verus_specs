use vstd::prelude::*;

verus! {
    fn find_max(a: &[int]) -> (i: usize)
        requires a.len() > 0,
        ensures 
            i < a.len(),
            forall|k: int| 0 <= k < a.len() ==> a[k] <= a[i as int],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}