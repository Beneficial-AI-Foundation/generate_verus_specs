use vstd::prelude::*;

verus! {
    fn linear_search(a: &[int], e: int) -> (n: usize)
        requires a.len() <= usize::MAX,
        ensures 
            n <= a.len(),
            n == a.len() || a[n as int] == e,
            forall|i: int| 0 <= i < n ==> e != a[i],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}