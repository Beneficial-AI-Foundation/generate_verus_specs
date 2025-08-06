use vstd::prelude::*;

verus! {
    fn rotate_right(a: &mut Vec<i32>)
        requires old(a).len() > 0,
        ensures 
            a.len() == old(a).len(),
            forall|i: int| 1 <= i < a.len() ==> a[i] == old(a)[i - 1],
            a[0] == old(a)[old(a).len() - 1]
    {
    // TODO: Remove this comment and implement the function body
    }
}