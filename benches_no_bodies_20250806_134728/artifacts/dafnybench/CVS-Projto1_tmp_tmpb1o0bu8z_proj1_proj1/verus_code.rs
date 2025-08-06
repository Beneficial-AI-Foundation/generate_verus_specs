use vstd::prelude::*;

verus! {
    // Exercise 1.a)
    spec fn sum(a: Seq<int>, i: int, j: int) -> int
        decreases j - i
    {
        recommends(0 <= i <= j <= a.len());
        if i >= j {
            0
        } else {
            a[j-1] + sum(a, i, j-1)
        }
    }

    // Exercise 1.b) - Working version with bounds checking
    fn query(a: &Vec<i32>, i: usize, j: usize) -> (s: i32)
        requires 0 <= i <= j <= a.len()
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    // Exercise 1.c)
    proof fn queryLemma(a: Seq<int>, i: int, j: int, k: int)
        requires 0 <= i <= k <= j <= a.len()
        ensures sum(a, i, k) + sum(a, k, j) == sum(a, i, j)
        decreases j - i
    {
        if i == k {
            assert(sum(a, i, k) == 0);
        } else if k == j {
            assert(sum(a, k, j) == 0);
        } else {
            queryLemma(a, i, j-1, k);
        }
    }

    spec fn is_prefix_sum_for(a: Seq<int>, c: Seq<int>) -> bool {
        a.len() + 1 == c.len()
        && c[0] == 0
        && forall|j: int| 1 <= j <= a.len() ==> c[j] == sum(a, 0, j)
    }

    fn queryFast(a: &Vec<i32>, c: &Vec<i32>, i: usize, j: usize) -> (r: i32)
        requires 
            0 <= i <= j <= a.len() < c.len()
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    // Exercise 2.
    #[derive(PartialEq, Eq)]
    enum List<T> {
        Nil,
        Cons(T, Box<List<T>>)
    }

    spec fn mem<T>(x: T, l: List<T>) -> bool
        decreases l
    {
        match l {
            List::Nil => false,
            List::Cons(y, r) => if x == y { true } else { mem(x, *r) }
        }
    }

    fn from_array<T: Copy>(a: &Vec<T>) -> (l: List<T>)
        requires a.len() > 0
    {
    assume(false);  // TODO: Replace with appropriate return value of type List<T>
    }
}