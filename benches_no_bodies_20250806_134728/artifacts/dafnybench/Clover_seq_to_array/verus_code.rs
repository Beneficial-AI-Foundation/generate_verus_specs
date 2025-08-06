use vstd::prelude::*;

verus! {
    fn to_array<T>(xs: Seq<T>) -> (a: Vec<T>)
        ensures
            a.len() == xs.len(),
            a.view() == xs,
    {
    return Vec::new();  // TODO: Remove this line and implement the function body
    }
}