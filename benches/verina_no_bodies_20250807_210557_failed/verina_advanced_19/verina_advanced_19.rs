use vstd::prelude::*;

verus! {

// Check if a character is an uppercase alphabet letter
pub fn is_upper_alpha(c: char) -> (result: bool)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Check if a character is a lowercase alphabet letter  
pub fn is_lower_alpha(c: char) -> (result: bool)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Determine if a character is alphabetic
pub fn is_alpha(c: char) -> (result: bool)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Convert a single character to lowercase
pub fn to_lower(c: char) -> (result: char)
{
    assume(false);  // TODO: Replace with appropriate return value of type char
}

// Normalize a character: keep only lowercase letters
pub fn normalize_char(c: char) -> (result: Option<char>)
{
    return None;  // TODO: Remove this line and implement the function body
}

// Normalize a string into a vector of lowercase alphabetic characters
pub fn normalize_string(s: &str) -> (result: Vec<char>)
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}

// Check if two vectors are equal element-wise
pub fn vec_equal(v1: &Vec<char>, v2: &Vec<char>) -> (result: bool)
    ensures result == (v1@ =~= v2@)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Reverse the vector
pub fn reverse_vec(xs: &Vec<char>) -> (result: Vec<char>)
    ensures result@ == xs@.reverse()
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}

pub open spec fn is_clean_palindrome_precond(s: &str) -> bool
{
    true
}

pub fn is_clean_palindrome(s: &str) -> (result: bool)
    requires is_clean_palindrome_precond(s)
{
    return false;  // TODO: Remove this line and implement the function body
}

// Postcondition expressed directly in terms of the result
pub open spec fn is_clean_palindrome_postcond(s: &str, result: bool, norm_seq: Seq<char>) -> bool
{
    (result == true ==> (norm_seq =~= norm_seq.reverse())) && 
    (result == false ==> !(norm_seq =~= norm_seq.reverse()))
}

} // verus!

fn main() {}