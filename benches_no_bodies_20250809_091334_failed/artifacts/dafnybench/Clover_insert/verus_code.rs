use vstd::prelude::*;

verus! {
    fn insert(line: &mut Vec<char>, l: usize, nl: &Vec<char>, p: usize, at: usize)
        requires 
            l + p <= old(line).len(),
            p <= nl.len(),
            at <= l,
            l <= old(line).len(),
        ensures 
            line.len() == old(line).len(),
            forall|i: int| (0 <= i < p) ==> line[at + i] == nl[i],
            forall|i: int| (0 <= i < at) ==> line[i] == old(line)[i],
            forall|i: int| (at + p <= i < l + p) ==> line[i] == old(line)[i - p],
    {
    // TODO: Remove this comment and implement the function body
    }
}