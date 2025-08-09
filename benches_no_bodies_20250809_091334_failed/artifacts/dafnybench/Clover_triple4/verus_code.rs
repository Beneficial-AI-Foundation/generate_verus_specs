use vstd::prelude::*;

verus! {
    spec fn Triple(x: int) -> int
    {
        let y = x * 2;
        y + x
    }
    
    proof fn Triple_correctness(x: int) 
        ensures Triple(x) == 3 * x
    {
    assume(false);  // TODO: Remove this line and implement the proof
    }
}