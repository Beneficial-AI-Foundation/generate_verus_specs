use vstd::prelude::*;

verus! {
    fn arrayProduct(a: &Vec<i32>, b: &Vec<i32>) -> (c: Vec<i32>)
        requires a.len() == b.len(),
        ensures 
            c.len() == a.len(),
            forall|i: int| 0 <= i < a.len() ==> c[i] == a[i] * b[i]
    {
    return Vec::new();  // TODO: Remove this line and implement the function body
    }
}