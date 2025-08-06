use vstd::prelude::*;

verus! {
    fn process_values(x: u32, y: u32) -> (r: (u32, u32, u32))
        requires
            x == y,
        ensures
            r.1 == r.2,
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}