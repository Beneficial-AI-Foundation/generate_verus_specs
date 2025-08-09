use vstd::arithmetic::div_mod::{
    lemma_fundamental_div_mod, lemma_fundamental_div_mod_converse_div,
};
use vstd::prelude::*;

verus! {

spec fn mul(a: nat, b: nat) -> (result:nat) {
    builtin::mul(a, b)
}
// pure-end

spec fn divides(factor: nat, candidate: nat) -> (result:bool) {
    exists|k: nat| mul(factor, k) == candidate
}
// pure-end

proof fn lemma_mod_zero(a: nat, b: nat)
    // pre-conditions-start
    requires
        a > 0 && b > 0,
        a % b == 0,
    // pre-conditions-end
    // post-conditions-start
    ensures
        divides(b, a),
    // post-conditions-end
{
    assume(false);  // TODO: Remove this line and implement the proof
}
// pure-end

proof fn lemma_mod_zero_reversed(a: nat, b: nat)
    // pre-conditions-start
    requires
        a > 0 && b > 0,
        divides(b, a),
    // pre-conditions-end
    // post-conditions-start
    ensures
        a % b == 0,
    // post-conditions-end
{
    assume(false);  // TODO: Remove this line and implement the proof
}
// pure-end

proof fn lemma_one_divides_all()
    // post-conditions-start
    ensures
        forall|v: nat| divides(1 as nat, v),
    // post-conditions-end
{
    assume(false);  // TODO: Remove this line and implement the proof
}
// pure-end

fn largest_divisor(n: u32) -> (ret: u32)
    // pre-conditions-start
    requires
        n > 1,
    // pre-conditions-end
    // post-conditions-start
    ensures
        divides(ret as nat, n as nat),
        ret < n,
        forall|k: u32| (0 < k < n && divides(k as nat, n as nat)) ==> ret >= k,
    // post-conditions-end
{
    return 0;  // TODO: Remove this line and implement the function body
}

}
fn main() {}
