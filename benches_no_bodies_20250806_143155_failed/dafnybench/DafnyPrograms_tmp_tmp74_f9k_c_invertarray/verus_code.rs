use vstd::prelude::*;

verus! {
    /**
      Inverts an array of ints.
     */
    fn invert_array(a: &mut Vec<int>)
        requires old(a).len() > 0,
        ensures 
            a.len() == old(a).len(),
            forall|i: int| 0 <= i < a.len() ==> a[i] == old(a)[a.len() - 1 - i],
    {
    // TODO: Remove this comment and implement the function body
    }
}