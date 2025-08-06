use vstd::prelude::*;

verus! {
    trait Predicate<T> {
        fn test(&self, x: &T) -> (result: bool)
            ensures result == self.spec_test(*x);
        
        spec fn spec_test(&self, x: T) -> bool;
    }
    
    fn linear_search<T, P: Predicate<T>>(a: &[T], p: &P) -> (n: usize)
        ensures 
            n <= a.len(),
            n < a.len() ==> p.spec_test(a[n as int]),
            forall|i: int| 0 <= i < n ==> !p.spec_test(a[i])
    {
    return false;  // TODO: Remove this line and implement the function body
    }
}