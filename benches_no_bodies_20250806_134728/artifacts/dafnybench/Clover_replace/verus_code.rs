use vstd::prelude::*;

verus! {
    fn replace(arr: &mut Vec<i32>, k: i32)
        ensures
            forall|i: int| #![auto] 0 <= i < old(arr)@.len() ==> old(arr)@.index(i) > k ==> arr@.index(i) == -1,
            forall|i: int| #![auto] 0 <= i < old(arr)@.len() ==> old(arr)@.index(i) <= k ==> arr@.index(i) == old(arr)@.index(i),
    {
    // TODO: Remove this comment and implement the function body
    }
}