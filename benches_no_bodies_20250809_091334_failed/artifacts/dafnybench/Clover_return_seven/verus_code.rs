use vstd::prelude::*;

verus! {
    proof fn M(x: int) -> (seven: int)
        ensures seven == 7
    {
    assume(false);  // TODO: Remove this line and implement the proof
    }
}

fn main() {}