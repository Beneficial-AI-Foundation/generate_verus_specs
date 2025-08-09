use vstd::prelude::*;

verus! {
    fn longest_common_prefix(str1: Vec<char>, str2: Vec<char>) -> (prefix: Vec<char>)
        ensures
            prefix.len() <= str1.len() && prefix@ == str1@.subrange(0, prefix.len() as int),
            prefix.len() <= str2.len() && prefix@ == str2@.subrange(0, prefix.len() as int),
            prefix.len() == str1.len() || prefix.len() == str2.len() || 
                (prefix.len() < str1.len() && prefix.len() < str2.len() && str1[prefix.len() as int] != str2[prefix.len() as int])
    {
    return Vec::new();  // TODO: Remove this line and implement the function body
    }
}