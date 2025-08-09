use vstd::prelude::*;

verus! {
    /**
     * Proves the correctness of a "raw" array sorting algorithm that swaps elements out of order, chosen randomly.
     * FEUP, MFES, 2020/21.
     * Translated from Dafny to Verus.
     */

    // Type of each array element; can be any type supporting comparison operators.
    type T = int;

    // Checks if array 'a' is sorted by non-descending order.
    spec fn sorted(a: Seq<T>) -> bool {
        forall|i: int, j: int| 0 <= i < j < a.len() ==> a[i] <= a[j]
    }

    // Obtains the set of all inversions in an array 'a', i.e., 
    // the pairs of indices i, j such that i < j and a[i] > a[j]. 
    spec fn inversions(a: Seq<T>) -> Set<(nat, nat)> {
        Set::new(|p: (nat, nat)| {
            let (i, j) = p;
            0 <= i < j < a.len() && a[i as int] > a[j as int]
        })
    }

    // Helper function to find an inversion pair
    fn find_inversion(a: &Vec<T>) -> (result: Option<(usize, usize)>)
        ensures match result {
    return None;  // TODO: Remove this line and implement the function body
        }
    {
        for i in 0..a.len() {
            for j in (i + 1)..a.len() {
                if a[i] > a[j] {
                    return Some((i, j));
                }
            }
        }
        None
    }

    // Sorts an array by simply swapping elements out of order, chosen randomly.
    fn rawsort(a: &mut Vec<T>)
        requires old(a).len() > 0,
        ensures 
            sorted(a@),
            a@.to_multiset() == old(a)@.to_multiset(),
        decreases inversions(old(a)@).len(),
    {
    // TODO: Remove this comment and implement the function body
    }

    // States and proves (by induction) the following property: given sets 'a' and 'b' and an injective
    // and non-surjective mapping 'm' from elements in 'a' to elements in 'b', then |a| < |b|.
    // To facilitate the proof, it is given an element 'k' in 'b' that is not an image of elements in 'a'.   
    proof fn mappingProp<T1, T2>(a: Set<T1>, b: Set<T2>, k: T2, m: Map<T1, T2>)
        requires 
            b.contains(k),
            forall|x: T1| a.contains(x) ==> m.dom().contains(x) && b.remove(k).contains(m[x]),
            forall|x: T1, y: T1| a.contains(x) && a.contains(y) && x != y ==> m[x] != m[y],
        ensures a.len() < b.len(),
        decreases a.len(),
    {
    assume(false);  // TODO: Remove this line and implement the proof
    }
}

fn main() {}