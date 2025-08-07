use vstd::prelude::*;
use std::collections::HashMap;

verus! {

// Precondition: list is non-empty
spec fn most_frequent_precond(xs: Seq<i32>) -> bool {
    xs.len() > 0
}

// Count occurrences of value x in sequence xs
spec fn count_occurrences(xs: Seq<i32>, x: i32) -> nat {
    xs.filter(|y: i32| y == x).len()
}

// Simple contains function for Vec
fn vec_contains(v: &Vec<i32>, x: i32) -> (result: bool) 
    ensures result <==> v@.contains(x)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Build a frequency map from the list  
fn count_map(xs: &Vec<i32>) -> (result: HashMap<i32, u32>)
    requires xs.len() > 0
{
    return 0;  // TODO: Remove this line and implement the function body
}

// Compute the maximum frequency in the map
fn get_max_frequency(map: &HashMap<i32, u32>) -> (result: u32)
    requires map.len() > 0
{
    return 0;  // TODO: Remove this line and implement the function body
}

// Extract all keys whose frequency == max_freq
fn get_candidates(map: &HashMap<i32, u32>, max_freq: u32) -> (result: Vec<i32>)
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}

// Return the first candidate element from original list
fn get_first_with_freq(xs: &Vec<i32>, candidates: &Vec<i32>) -> (result: i32)
    requires 
        xs.len() > 0,
        candidates.len() > 0
{
    return 0;  // TODO: Remove this line and implement the function body
}

// Main function
fn most_frequent(xs: Vec<i32>) -> (result: i32)
    requires most_frequent_precond(xs@)
    ensures most_frequent_postcond(xs@, result)
{
    return 0;  // TODO: Remove this line and implement the function body
}

// Postcondition specification
spec fn most_frequent_postcond(xs: Seq<i32>, result: i32) -> bool {
    // result is in xs
    xs.contains(result) &&
    // all elements have frequency <= frequency of result  
    (forall |x: i32| #![auto] xs.contains(x) ==> count_occurrences(xs, x) <= count_occurrences(xs, result)) &&
    // result is the first element with maximum frequency
    (forall |i: int| #![auto] 0 <= i < xs.len() && count_occurrences(xs, xs[i]) == count_occurrences(xs, result) ==> 
        exists |j: int| 0 <= j <= i && xs[j] == result)
}

} // verus!

fn main() {}