use vstd::prelude::*;

verus! {
    fn selection_sort(a: &mut Vec<i32>)
        ensures 
            a.len() == old(a).len(),
            forall|i: int, j: int| 0 <= i < j < a.len() ==> a[i] <= a[j],
    {
    // TODO: Remove this comment and implement the function body
    }
}