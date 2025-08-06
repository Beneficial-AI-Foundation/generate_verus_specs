use vstd::prelude::*;

verus! {
    spec fn power(n: nat) -> nat
        decreases n
    {
        if n == 0 { 1 } else { 2 * power(sub(n, 1)) }
    }

    fn compute_power(n: u32) -> (p: u32)
        requires n <= 20,  // Bound to prevent overflow
        ensures p == power(n as nat)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}