use vstd::prelude::*;

verus! {
    fn binary_search(a: &[int], key: int) -> (n: usize)
        requires 
            forall|i: int, j: int| 0 <= i < j < a.len() ==> a[i] <= a[j],
        ensures 
            0 <= n <= a.len(),
            forall|i: int| 0 <= i < n ==> a[i] < key,
            forall|i: int| n <= i < a.len() ==> key <= a[i],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}