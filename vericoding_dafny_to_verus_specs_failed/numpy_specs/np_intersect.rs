use vstd::prelude::*;

verus! {

fn intersect(a: &[i32], b: &[i32]) -> (ret: Vec<i32>)
    ensures 
        ret.len() < a.len() && ret.len() < b.len(),
        forall|i: int, j: int| 
            0 <= i < a.len() && 0 <= j < b.len() ==>
                if a[i] == b[j] {
    return Vec::new();  // TODO: Remove this line and implement the function body
                } else {
                    !exists|k: int| 0 <= k < ret.len() && ret[k] == a[i]
                }
{
    assume(false);
    Vec::new()
}

}

fn main() {}