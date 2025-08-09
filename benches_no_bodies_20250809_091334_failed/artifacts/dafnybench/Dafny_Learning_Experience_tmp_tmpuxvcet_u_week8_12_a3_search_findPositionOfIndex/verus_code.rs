use vstd::prelude::*;

verus! {
    fn find_position_of_element(a: &Vec<i32>, element: i32, n1: usize, s1: Seq<i32>) -> (result: (i32, usize))
        requires
            n1 == s1.len() && 0 <= n1 <= a.len(),
            forall|i: int| 0 <= i < s1.len() ==> a[i] == s1[i],
        ensures
            result.0 == -1 || result.0 >= 1,
            s1.len() != 0 && result.0 >= 1 ==> exists|i: int| 0 <= i < s1.len() && s1[i] == element,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn main() {
    // TODO: Remove this comment and implement the function body
    }
}

fn main() {}