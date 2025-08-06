use vstd::prelude::*;

verus! {
    fn replace(v: &mut Vec<int>, x: int, y: int)
        requires old(v).len() >= 0,
        ensures 
            v.len() == old(v).len(),
            forall|k: int| 0 <= k < old(v).len() && old(v)[k] == x ==> v[k] == y,
            forall|k: int| 0 <= k < old(v).len() && old(v)[k] != x ==> v[k] == old(v)[k],
    {
    // TODO: Remove this comment and implement the function body
    }
}