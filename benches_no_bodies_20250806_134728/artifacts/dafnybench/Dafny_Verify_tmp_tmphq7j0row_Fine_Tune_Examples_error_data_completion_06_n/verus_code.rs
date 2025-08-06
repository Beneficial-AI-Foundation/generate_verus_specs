use vstd::prelude::*;

verus! {
    #[verifier::exec_allows_no_decreases_clause]
    fn Main() -> (ret: (u32, u32))
        ensures ret.0 == ret.1
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}