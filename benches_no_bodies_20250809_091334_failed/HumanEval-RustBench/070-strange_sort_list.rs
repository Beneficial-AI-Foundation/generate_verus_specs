use vstd::calc;
use vstd::prelude::*;
use vstd::seq_lib::lemma_multiset_commutative;

verus! {

proof fn swap_preserves_multiset_helper(s: Seq<i32>, i: int, j: int)
    // pre-conditions-start
    requires
        0 <= i < j < s.len(),
    // pre-conditions-end
    // post-conditions-start
    ensures
        (s.take(j + 1)).to_multiset() =~= s.take(i).to_multiset().add(
            s.subrange(i + 1, j).to_multiset(),
        ).insert(s.index(j)).insert(s.index(i)),
    // post-conditions-end
{
    assume(false);  // TODO: Remove this line and implement the proof
}
// pure-end

proof fn swap_preserves_multiset(s1: Seq<i32>, s2: Seq<i32>, i: int, j: int)
    // pre-conditions-start
    requires
        0 <= i < j < s1.len() == s2.len(),
        forall|x: int| 0 <= x < s1.len() && x != i && x != j ==> s1.index(x) == s2.index(x),
        s1.index(i) == s2.index(j),
        s1.index(j) == s2.index(i),
    // pre-conditions-end
    // post-conditions-start
    ensures
        s1.to_multiset() == s2.to_multiset(),
    // post-conditions-end
{
    assume(false);  // TODO: Remove this line and implement the proof
}
// pure-end

fn sort_seq(s: &Vec<i32>) -> (ret: Vec<i32>)
    // post-conditions-start
    ensures
        forall|i: int, j: int| 0 <= i < j < ret@.len() ==> ret@.index(i) <= ret@.index(j),
        ret@.len() == s@.len(),
        s@.to_multiset() == ret@.to_multiset(),
    // post-conditions-end
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}

fn strange_sort_list_helper(s: &Vec<i32>) -> (ret: (Vec<i32>, Vec<i32>))
    // post-conditions-start
    ensures
        s@.to_multiset() == (ret.0)@.to_multiset(),
        s@.len() == (ret.0)@.len() == (ret.1)@.len(),
        forall|i: int|
            0 <= i < s@.len() && i % 2 == 0 ==> (ret.1)@.index(i) == (ret.0)@.index(i / 2),
        forall|i: int|
            0 <= i < s@.len() && i % 2 == 1 ==> (ret.1)@.index(i) == (ret.0)@.index(
                s@.len() - (i - 1) / 2 - 1,
            ),
    // post-conditions-end
{
    return 0;  // TODO: Remove this line and implement the function body
}

fn strange_sort_list(s: &Vec<i32>) -> (ret: Vec<i32>)
    // post-conditions-start
    ensures
        s@.len() == ret@.len(),
    // post-conditions-end
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}

}
fn main() {}
