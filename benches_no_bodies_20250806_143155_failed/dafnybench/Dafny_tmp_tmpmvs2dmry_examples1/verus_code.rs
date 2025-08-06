use vstd::prelude::*;

verus! {
    spec fn abs(x: int) -> int {
        if x > 0 { x } else { -x }
    }

    fn Abs(x: i32) -> (y: i32)
        requires x > i32::MIN,
        ensures 
            y >= 0,
            x >= 0 ==> x == y,
            x < 0 ==> -x == y,
            y == abs(x as int)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn Testing() {
    // TODO: Remove this comment and implement the function body
    }

    fn MultiReturn(x: i32, y: i32) -> (ret: (i32, i32))
        requires 
            y >= 0,
            x - y >= i32::MIN,
            x + y <= i32::MAX,
        ensures 
            ret.1 <= x,
            x <= ret.0,
            ret.1 <= ret.0
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn Max(x: i32, y: i32) -> (a: i32)
        ensures 
            a == x || a == y,
            x > y ==> a == x,
            x <= y ==> a == y
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}

fn main() {}