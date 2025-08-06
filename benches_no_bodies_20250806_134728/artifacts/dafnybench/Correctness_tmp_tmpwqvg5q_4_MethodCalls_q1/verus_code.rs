use vstd::prelude::*;

verus! {
    spec fn fusc(n: int) -> nat;

    proof fn rule1()
        ensures fusc(0) == 0nat
    {
        admit(); // axiom
    }

    proof fn rule2()
        ensures fusc(1) == 1nat
    {
        admit(); // axiom
    }

    proof fn rule3(n: nat)
        ensures fusc(2 * n as int) == fusc(n as int)
    {
        admit(); // axiom
    }

    proof fn rule4(n: nat)
        ensures fusc(2 * n as int + 1) == fusc(n as int) + fusc(n as int + 1)
    {
        admit(); // axiom
    }

    fn compute_fusc(N: int) -> (b: int)
        requires N >= 0
        ensures b == fusc(N)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn main() {}
}