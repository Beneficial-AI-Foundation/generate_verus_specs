use vstd::prelude::*;

verus! {
    spec fn sorted(s: Seq<int>) -> bool {
        forall|u: int, w: int| 0 <= u < w < s.len() ==> s[u] <= s[w]
    }

    spec fn as_int_seq(s: Seq<i32>) -> Seq<int> {
        s.map(|_i, x| x as int)
    }

    // Binary search returns index of last element <= elem, or -1 if none
    fn binary_search(v: &[i32], elem: i32) -> (p: i32)
        requires sorted(as_int_seq(v@))
        ensures 
            -1 <= p < v@.len() &&
            (forall|u: int| 0 <= u <= p ==> v@[u] <= elem) && 
            (forall|w: int| p < w < v@.len() ==> v@[w] > elem)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn search(v: &[i32], elem: i32) -> (b: bool)
        requires sorted(as_int_seq(v@))
        ensures b == as_int_seq(v@).contains(elem as int)
    {
    return false;  // TODO: Remove this line and implement the function body
    }

    fn binary_search_rec(v: &[i32], elem: i32, c: usize, f: usize) -> (p: i32)
        requires 
            sorted(as_int_seq(v@)) &&
            c <= f + 1 &&
            f < v@.len() &&
            (forall|k: int| 0 <= k < c ==> v@[k] <= elem) &&
            (forall|k: int| f < k < v@.len() ==> v@[k] > elem)
        decreases f + 1 - c
        ensures 
            -1 <= p < v@.len() &&
            (forall|u: int| 0 <= u <= p ==> v@[u] <= elem) &&
            (forall|w: int| p < w < v@.len() ==> v@[w] > elem)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn other_b_search(v: &[i32], elem: i32) -> (result: (bool, usize))
        requires sorted(as_int_seq(v@))
        ensures ({
    return false;  // TODO: Remove this line and implement the function body
        })
    {
        let p_signed = binary_search(v, elem);
        let b: bool;
        let p: usize;
        
        if p_signed == -1 {
            b = false;
            p = 0;
        } else {
            let p_unsigned = p_signed as usize;
            b = v[p_unsigned] == elem;
            p = if b { p_unsigned } else { p_unsigned + 1 };
        }
        
        (b, p)
    }
}

fn main() {}