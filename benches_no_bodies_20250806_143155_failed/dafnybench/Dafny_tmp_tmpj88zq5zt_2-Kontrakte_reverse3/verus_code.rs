use vstd::prelude::*;

verus! {
    fn swap3(a: &mut Vec<int>, h: usize, i: usize, j: usize)
        requires 
            h < old(a).len(),
            i < old(a).len(),
            j < old(a).len(),
            i != j && j != h && h != i,
        ensures
            a@[h as int] == old(a)@[i as int],
            a@[j as int] == old(a)@[h as int],
            a@[i as int] == old(a)@[j as int],
            forall|k: int| 0 <= k < old(a).len() && k != h && k != i && k != j ==> a@[k] == old(a)@[k],
    {
    // TODO: Remove this comment and implement the function body
    }

    fn test_swap3(a: &mut Vec<int>, h: usize, i: usize, j: usize)
        requires 
            h < old(a).len(),
            i < old(a).len(),
            j < old(a).len(),
            i != j && j != h && h != i,
    {
    // TODO: Remove this comment and implement the function body
    }
}