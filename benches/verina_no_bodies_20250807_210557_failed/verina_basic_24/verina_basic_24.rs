use vstd::prelude::*;

verus! {

// Helper functions for even/odd checking  
spec fn is_even(n: i32) -> bool {
    n % 2 == 0
}

spec fn is_odd(n: i32) -> bool {
    n % 2 != 0
}

// Precondition specification
spec fn first_even_odd_difference_precond(a: Seq<i32>) -> bool {
    &&& a.len() > 1
    &&& exists|i: int| 0 <= i < a.len() && is_even(a[i])
    &&& exists|i: int| 0 <= i < a.len() && is_odd(a[i])
}

// Postcondition specification
spec fn first_even_odd_difference_postcond(a: Seq<i32>, result: i32) -> bool {
    exists|i: int, j: int| {
        &&& 0 <= i < a.len()
        &&& 0 <= j < a.len()
        &&& is_even(a[i])
        &&& is_odd(a[j])
        &&& result == a[i] - a[j]
        &&& forall|k: int| #![auto] 0 <= k < i ==> is_odd(a[k])
        &&& forall|k: int| #![auto] 0 <= k < j ==> is_even(a[k])
    }
}

// Function to find first even index
fn find_first_even(a: &Vec<i32>) -> (result: Option<usize>)
    ensures 
        result.is_some() ==> {
    return None;  // TODO: Remove this line and implement the function body
        },
        result.is_none() ==> forall|k: int| #![auto] 0 <= k < a.len() ==> is_odd(a@[k]),
{
    for i in 0..a.len()
        invariant
            forall|k: int| #![auto] 0 <= k < i ==> is_odd(a@[k]),
    {
        if a[i] % 2 == 0 {
            return Some(i);
        }
    }
    None
}

// Function to find first odd index
fn find_first_odd(a: &Vec<i32>) -> (result: Option<usize>)
    ensures 
        result.is_some() ==> {
    return None;  // TODO: Remove this line and implement the function body
        },
        result.is_none() ==> forall|k: int| #![auto] 0 <= k < a.len() ==> is_even(a@[k]),
{
    for i in 0..a.len()
        invariant
            forall|k: int| #![auto] 0 <= k < i ==> is_even(a@[k]),
    {
        if a[i] % 2 != 0 {
            return Some(i);
        }
    }
    None
}

// Main function implementation  
fn first_even_odd_difference(a: &Vec<i32>) -> (result: i32)
    requires 
        first_even_odd_difference_precond(a@),
        // Additional bounds to prevent overflow
        forall|i: int| #![trigger a@[i]] 0 <= i < a.len() ==> -1000000000 <= a@[i] <= 1000000000,
    ensures
        first_even_odd_difference_postcond(a@, result),
{
    return 0;  // TODO: Remove this line and implement the function body
}

fn main() {}

} // verus!