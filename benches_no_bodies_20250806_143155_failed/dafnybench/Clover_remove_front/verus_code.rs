use vstd::prelude::*;

verus! {
    fn remove_front(a: &[int]) -> (c: Vec<int>)
        requires a.len() > 0,
        ensures c@ == a@.subrange(1, a.len() as int),
    {
    return Vec::new();  // TODO: Remove this line and implement the function body
    }
}