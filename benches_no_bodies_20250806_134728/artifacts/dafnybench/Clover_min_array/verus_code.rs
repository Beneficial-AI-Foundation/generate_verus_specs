use vstd::prelude::*;

verus! {
    fn minArray(a: &[int]) -> (r: int)
        requires a.len() > 0,
        ensures 
            forall|i: int| 0 <= i < a.len() ==> r <= a[i],
            exists|i: int| 0 <= i < a.len() && r == a[i]
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}