use vstd::prelude::*;

verus! {
    spec fn max(x: nat, y: nat) -> nat {
        if x < y { y } else { x }
    }

    fn slow_max(a: u32, b: u32) -> (z: u32)
        requires a < 0x80000000 && b < 0x80000000
        ensures z == max(a as nat, b as nat)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}