use vstd::prelude::*;

verus! {
    spec fn fib(n: nat) -> nat
        decreases n
    {
        if n == 0 {
            0
        } else if n == 1 {
            1
        } else {
            fib((n - 1) as nat) + fib((n - 2) as nat)
        }
    }

    fn fibonacci1(n: u32) -> (f: u32)
        requires n <= 10,  
        ensures f == fib(n as nat)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn fibonacci2(n: u32) -> (f: u32) 
        requires n <= 10,
        ensures f == fib(n as nat)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn fibonacci3(n: u32) -> (f: u32)
        requires n <= 10,
        ensures f == fib(n as nat)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}