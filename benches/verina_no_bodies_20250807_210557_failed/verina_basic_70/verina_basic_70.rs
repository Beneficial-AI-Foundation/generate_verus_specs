use vstd::prelude::*;

verus! {

trait Predicate {
    spec fn apply(&self, x: i32) -> bool;
    fn call(&self, x: i32) -> (result: bool)
        ensures result == self.apply(x);
}

// Precondition: there exists an index where the predicate is satisfied
spec fn linear_search3_precond<P: Predicate>(a: &[i32], p: &P) -> bool {
    return false;  // TODO: Remove this line and implement the function body
}

// Postcondition: result is valid index, predicate holds at result, and all previous elements fail predicate
spec fn linear_search3_postcond<P: Predicate>(a: &[i32], p: &P, result: usize) -> bool {
    result < a.len() && 
    p.apply(a[result as int]) && 
    (forall|k: int| 0 <= k < result ==> !p.apply(a[k]))
}

// The main linear search function
fn linear_search3<P: Predicate>(a: &[i32], p: &P) -> (result: usize)
    requires 
        linear_search3_precond(a, p),
    ensures
        linear_search3_postcond(a, p, result),
{
    return 0;  // TODO: Remove this line and implement the function body
}

fn main() {}

} // verus!