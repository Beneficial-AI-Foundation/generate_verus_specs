use vstd::prelude::*;

verus! {
    // Direct translation from Dafny method to Verus spec function
    spec fn triple(x: int) -> int {
        if x < 18 {
            let a = 2 * x;
            let b = 4 * x;
            (a + b) / 2
        } else {
            // In original Dafny: "case 0 <= x"
            // Since conditions can overlap, we use else here
            let y = 2 * x;
            x + y
        }
    }
    
    // Proof that the function correctly computes 3*x
    proof fn triple_correctness(x: int) 
        ensures triple(x) == 3 * x
    {
    assume(false);  // TODO: Remove this line and implement the proof
    }
}