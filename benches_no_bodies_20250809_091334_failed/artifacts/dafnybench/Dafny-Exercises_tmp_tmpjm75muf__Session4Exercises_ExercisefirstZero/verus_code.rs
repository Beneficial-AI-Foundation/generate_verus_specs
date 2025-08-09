use vstd::prelude::*;

verus! {
    fn mfirstCero(v: &[i32]) -> (i: usize)
        ensures 
            0 <= i <= v.len(),
            forall|j: int| 0 <= j < i ==> v@[j] != 0,
            i != v.len() ==> v@[i as int] == 0
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}