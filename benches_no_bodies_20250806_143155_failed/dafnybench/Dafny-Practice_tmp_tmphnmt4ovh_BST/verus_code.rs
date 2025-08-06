use vstd::prelude::*;

verus! {
    #[derive(PartialEq, Eq)]
    pub enum Tree {
        Empty,
        Node(int, Box<Tree>, Box<Tree>),
    }

    pub fn main() {
    // TODO: Remove this comment and implement the function body
    }

    pub fn print_tree_numbers_inorder(t: &Tree)
        decreases t
    {
    // TODO: Remove this comment and implement the function body
    }

    pub open spec fn numbers_in_tree(t: Tree) -> Set<int> {
        numbers_in_sequence(inorder(t))
    }

    pub open spec fn numbers_in_sequence(q: Seq<int>) -> Set<int> {
        Set::new(|x: int| q.contains(x))
    }

    pub open spec fn bst(t: Tree) -> bool {
        ascending(inorder(t))
    }

    pub open spec fn inorder(t: Tree) -> Seq<int>
        decreases t
    {
        match t {
            Tree::Empty => Seq::empty(),
            Tree::Node(n, nt1, nt2) => inorder(*nt1) + seq![n] + inorder(*nt2),
        }
    }

    pub open spec fn ascending(q: Seq<int>) -> bool {
        forall|i: int, j: int| 0 <= i < j < q.len() ==> q[i] < q[j]
    }

    pub open spec fn no_duplicates(q: Seq<int>) -> bool {
        forall|i: int, j: int| 0 <= i < j < q.len() ==> q[i] != q[j]
    }

    pub fn build_bst(q: Vec<int>) -> (t: Tree)
        requires no_duplicates(q@),
        ensures bst(t) && numbers_in_tree(t) == numbers_in_sequence(q@)
    {
    assume(false);  // TODO: Replace with appropriate return value of type Tree
    }

    pub fn insert_bst(t0: Tree, x: int) -> (t: Tree)
        requires bst(t0) && !numbers_in_tree(t0).contains(x),
        ensures bst(t) && numbers_in_tree(t) == numbers_in_tree(t0).insert(x),
        decreases t0
    {
    assume(false);  // TODO: Replace with appropriate return value of type Tree
    }

    pub proof fn lemma_binary_search_subtree(n: int, left: Tree, right: Tree)
        requires bst(Tree::Node(n, Box::new(left), Box::new(right))),
        ensures bst(left) && bst(right)
    {
        assert(ascending(inorder(Tree::Node(n, Box::new(left), Box::new(right)))));
        let qleft = inorder(left);
        let qright = inorder(right);
        let q = qleft + seq![n] + qright;
        assert(q == inorder(Tree::Node(n, Box::new(left), Box::new(right))));
        assert(ascending(qleft + seq![n] + qright));
        lemma_ascending_subsequence(q, qleft, 0);
        assert(ascending(qleft));
        lemma_ascending_subsequence(q, qright, qleft.len() as int + 1);
        assert(ascending(qright));
    }

    pub proof fn lemma_ascending_subsequence(q1: Seq<int>, q2: Seq<int>, i: int)
        requires 
            i <= q1.len() - q2.len() && 
            q2 == q1.subrange(i, i + q2.len()) &&
            ascending(q1),
        ensures ascending(q2)
    {}

    pub proof fn lemma_all_small(q: Seq<int>, i: int)
        requires 
            forall|k: int| numbers_in_sequence(q).contains(k) ==> k < i,
            forall|k: int| 0 <= k < q.len() ==> numbers_in_sequence(q).contains(q[k]),
        ensures forall|j: int| 0 <= j < q.len() ==> q[j] < i
    {}

    pub proof fn lemma_all_big(q: Seq<int>, i: int)
        requires 
            forall|k: int| numbers_in_sequence(q).contains(k) ==> k > i,
            forall|k: int| 0 <= k < q.len() ==> numbers_in_sequence(q).contains(q[k]),
        ensures forall|j: int| 0 <= j < q.len() ==> q[j] > i
    {}
}