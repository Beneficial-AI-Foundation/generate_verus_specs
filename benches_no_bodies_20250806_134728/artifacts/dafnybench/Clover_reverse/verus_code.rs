use vstd::prelude::*;

verus! {
    fn reverse(a: &mut Vec<i32>)
        requires old(a).len() > 0,
        ensures 
            a.len() == old(a).len(),
            forall|i: int| 0 <= i < a.len() ==> a[i] == old(a)[a.len() - 1 - i],
    {
    // TODO: Remove this comment and implement the function body
    }
}