use vstd::prelude::*;

verus! {

spec fn sum_and_average_precond(n: nat) -> bool {
    true
}

spec fn sum_and_average_postcond(n: nat, result: (u32, u32)) -> bool {
    (n == 0 ==> result.0 == 0) &&
    (n == 1 ==> result.0 == 1) &&
    (n == 2 ==> result.0 == 3) &&
    (n == 3 ==> result.0 == 6) &&
    (n == 4 ==> result.0 == 10) &&
    (n == 5 ==> result.0 == 15) &&
    result.1 == result.0  // second component same as first (represents average numerator)
}

fn sum_and_average(n: u32) -> (result: (u32, u32))
    requires 
        sum_and_average_precond(n as nat),
        n <= 5u32
    ensures sum_and_average_postcond(n as nat, result)
{
    return 0;  // TODO: Remove this line and implement the function body
}

fn main() {
    // TODO: Remove this comment and implement the function body
}

} // verus!