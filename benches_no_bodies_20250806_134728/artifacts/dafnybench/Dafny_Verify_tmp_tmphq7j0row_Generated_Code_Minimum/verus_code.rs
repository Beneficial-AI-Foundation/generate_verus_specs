use vstd::prelude::*;

verus! {
    fn minimum(a: &[int]) -> (m: int)
        requires a.len() > 0,
        ensures 
            exists|i: int| 0 <= i < a.len() && m == a[i],
            forall|i: int| 0 <= i < a.len() ==> m <= a[i]
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}