use vstd::prelude::*;

verus! {
    fn onlineMax(a: &Vec<int>, x: usize) -> (result: (Ghost<int>, usize))
        requires 
            1 <= x < a.len(),
            a.len() != 0,
        ensures ({
    return 0;  // TODO: Remove this line and implement the function body
        })
    {
        let mut p: usize = 0;
        let mut best = a[0];
        let mut i: usize = 1;
        
        // Find maximum in first x elements
        while i < x
            invariant 
                1 <= i <= x,
                x < a.len(),
                forall|j: int| 0 <= j < i ==> a[j] <= best,
                exists|j: int| 0 <= j < i && a[j] == best,
            decreases x - i,
        {
            if a[i] > best {
                best = a[i];
            }
            i = i + 1;
        }
        
        let m = Ghost(best);
        i = x;
        
        // Find first element after position x that is greater than best
        while i < a.len()
            invariant 
                x <= i <= a.len(),
                forall|j: int| x <= j < i ==> a[j] <= best,
            decreases a.len() - i,
        {
            if a[i] > best {
                p = i;
                return (m, p);
            }
            i = i + 1;
        }
        
        // If no element is greater than best, return last index
        p = a.len() - 1;
        (m, p)
    }
}

fn main() {}