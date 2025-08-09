use vstd::prelude::*;

verus! {
    fn linear_search3<T>(a: &[T], Ghost(p): Ghost<spec_fn(T) -> bool>) -> (n: usize)
        requires 
            a.len() > 0,
            exists|i: int| 0 <= i < a.len() && p(a[i]),
        ensures 
            0 <= n < a.len(),
            p(a[n as int]),
            forall|k: int| 0 <= k < n ==> !p(a[k]),
    {
    return false;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}