#[allow(unused_imports)]
use vstd::prelude::*;
fn main() {}

verus! {
spec fn seq_to_set_rec<A>(seq: Seq<A>) -> Set<A>
    decreases seq.len()
{
    if seq.len() == 0 {
        Set::empty()
    } else {
        seq_to_set_rec(seq.drop_last()).insert(seq.last())
    }
}

/// helper function showing that the resulting set contains all elements of the sequence
proof fn seq_to_set_rec_contains<A>(seq: Seq<A>)
    ensures forall |a| #[trigger] seq.contains(a) <==> seq_to_set_rec(seq).contains(a)
    decreases seq.len()
{
    assume(false);  // TODO: Remove this line and implement the proof
}

/// helper function showing that the recursive definition matches the set comprehension one
proof fn seq_to_set_equal_rec<A>(seq: Seq<A>)
    ensures seq.to_set() == seq_to_set_rec(seq)
{
    assume(false);  // TODO: Remove this line and implement the proof
}

proof fn lemma_seq_push_to_set_insert<T>(s: Seq<T>, val: T)
ensures
    s.push(val).to_set() === s.to_set().insert(val),
{
    assume(false);  // TODO: Remove this line and implement the proof
}

fn remove_duplicates(nums: Vec<i32>) -> (res: Vec<i32>)
ensures
    res@.no_duplicates(),
    nums@.to_set().ext_equal(res@.to_set())
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}
}
