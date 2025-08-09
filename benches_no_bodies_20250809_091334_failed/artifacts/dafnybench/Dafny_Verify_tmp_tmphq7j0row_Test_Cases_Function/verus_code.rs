use vstd::prelude::*;

verus! {
    spec fn average(a: int, b: int) -> int {
        (a + b) / 2
    }

    proof fn triple_conditions(x: int) -> (r: int)
        ensures r == 3 * x
    {   
    assume(false);  // TODO: Remove this line and implement the proof
    }

    proof fn triple_prime(x: int) -> (r: int) 
        ensures 
            average(r, 3 * x) == 3 * x,
            r == 3 * x
    {
    assume(false);  // TODO: Remove this line and implement the proof
    }

    proof fn prove_specifications_equivalent(x: int) {
    assume(false);  // TODO: Remove this line and implement the proof
    }
}

fn main() {}