use vstd::prelude::*;

verus! {
    // flips (i.e., reverses) array elements in the range [0..num]
    fn flip(a: &mut Vec<int>, num: usize)
        requires
            old(a).len() > 0,
            num < old(a).len(),
        ensures
            a.len() == old(a).len(),
            forall |k: int| 0 <= k <= num as int ==> a[k] == old(a)[num as int - k],
            forall |k: int| k > num as int && k < a.len() as int ==> a[k] == old(a)[k],
    {
    // TODO: Remove this comment and implement the function body
    }
}