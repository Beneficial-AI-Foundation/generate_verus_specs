use vstd::prelude::*;

verus! {
    fn double_array(src: &Vec<u32>, dst: &mut Vec<u32>)
        requires 
            src.len() == old(dst).len(),
            forall|i: int| 0 <= i < src.len() ==> src[i] <= u32::MAX / 2,
        ensures
            dst.len() == old(dst).len(),
            forall|i: int| 0 <= i < src.len() ==> dst[i] == 2 * src[i],
    {
    // TODO: Remove this comment and implement the function body
    }
}