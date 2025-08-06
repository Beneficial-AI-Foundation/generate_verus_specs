use vstd::prelude::*;

verus! {
    // Predicate to check if element at index i is a "peek" 
    // (greater than or equal to all previous elements)
    spec fn isPeek(v: &[int], i: int) -> bool {
        &&& 0 <= i < v.len()
        &&& forall|k: int| 0 <= k < i ==> v[i] >= v[k]
    }

    // Recursive function to sum all "peek" elements up to index i
    spec fn peekSum(v: &[int], i: int) -> int 
        decreases i
    {
        if i == 0 {
            0
        } else if 0 <= i <= v.len() && isPeek(v, i - 1) {
            v[i - 1] + peekSum(v, i - 1)
        } else if 0 <= i <= v.len() {
            peekSum(v, i - 1)
        } else {
            0
        }
    }

    // O(n) algorithm to compute the sum of all peek elements
    fn mPeekSum(v: &[int]) -> (sum: int)
        requires v.len() > 0
        ensures sum == peekSum(v, v.len() as int)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}