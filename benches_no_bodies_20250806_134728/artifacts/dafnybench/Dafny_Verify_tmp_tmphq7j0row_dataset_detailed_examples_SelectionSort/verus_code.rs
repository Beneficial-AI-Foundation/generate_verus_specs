use vstd::prelude::*;

verus! {
    // Works by dividing the input list into two parts: sorted and unsorted. At the beginning, 
    // the sorted part is empty and the unsorted part contains all the elements.
    fn selection_sort(a: &mut Vec<i32>)
        requires old(a).len() > 0,
        ensures 
            // Ensures the final array is sorted in ascending order
            forall|i: int, j: int| 0 <= i < j < a.len() ==> a[i] <= a[j],
            // Ensures that the final array has the same length as the initial array
            a.len() == old(a).len(),
    {
    // TODO: Remove this comment and implement the function body
    }
}