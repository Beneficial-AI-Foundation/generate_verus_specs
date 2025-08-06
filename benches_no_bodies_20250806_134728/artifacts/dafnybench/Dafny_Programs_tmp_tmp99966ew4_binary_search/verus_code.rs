use vstd::prelude::*;

verus! {
    spec fn sorted(a: &[int]) -> bool {
        forall|j: int, k: int| 0 <= j < k < a.len() ==> a[j] <= a[k]
    }

    fn binary_search(a: &[int], value: int) -> (index: Option<usize>)
        requires 
            sorted(a)
        ensures
            match index {
    return None;  // TODO: Remove this line and implement the function body
            }
    {
        let mut low: usize = 0;
        let mut high: usize = a.len();
        
        while low < high
            invariant
                low <= high <= a.len()
            decreases high - low
        {
            let mid: usize = low + (high - low) / 2;
            let mid_val = a[mid];
            if mid_val < value {
                low = mid + 1;
            } else if value < mid_val {
                high = mid;
            } else {
                return Some(mid);
            }
        }
        None
    }
}

fn main() {}