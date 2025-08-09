use vstd::prelude::*;

verus! {

// Precondition - in the original it's just True  
spec fn only_once_precond(a: Seq<i32>, key: i32) -> bool {
    true
}

// Helper function to count occurrences
spec fn count_occurrences(a: Seq<i32>, key: i32) -> nat {
    a.fold_left(0nat, |cnt: nat, x: i32| if x == key { cnt + 1 } else { cnt })
}

// Postcondition
spec fn only_once_postcond(a: Seq<i32>, key: i32, result: bool) -> bool {
    (count_occurrences(a, key) == 1 ==> result) &&
    (count_occurrences(a, key) != 1 ==> !result)
}

// The loop function - recursive approach following the original Lean structure
fn only_once_loop_rec(a: &Vec<i32>, key: i32, i: usize, key_count: usize) -> (result: bool)
    requires i <= a.len(), key_count <= a.len()
    decreases a.len() - i
{
    return false;  // TODO: Remove this line and implement the function body
}

// The main loop function
fn only_once_loop(a: &Vec<i32>, key: i32) -> (result: bool)
    ensures result == (count_occurrences(a@, key) == 1)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Main function
fn only_once(a: &Vec<i32>, key: i32) -> (result: bool)
    requires only_once_precond(a@, key)
    ensures only_once_postcond(a@, key, result)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Specification theorem - equivalent to the Lean theorem
proof fn only_once_spec_satisfied(a: Vec<i32>, key: i32) 
    requires only_once_precond(a@, key)
    ensures only_once_postcond(a@, key, only_once(&a, key), only_once_precond(a@, key))
{
    assume(false);  // TODO: Remove this line and implement the proof
}

}