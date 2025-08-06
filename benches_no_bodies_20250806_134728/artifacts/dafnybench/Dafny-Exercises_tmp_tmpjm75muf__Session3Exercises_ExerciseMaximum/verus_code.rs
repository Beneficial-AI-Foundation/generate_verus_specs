use vstd::prelude::*;

verus! {
    // Algorithm 1: From left to right return the first
    fn mmaximum1(v: &[int]) -> (i: usize)
        requires v.len() > 0,
        ensures 
            i < v.len(),
            forall |k: int| 0 <= k < v.len() ==> v[i as int] >= v[k],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    // Algorithm 2: From right to left return the last
    fn mmaximum2(v: &[int]) -> (i: usize)
        requires v.len() > 0,
        ensures 
            i < v.len(),
            forall |k: int| 0 <= k < v.len() ==> v[i as int] >= v[k],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn mfirstMaximum(v: &[int]) -> (i: usize)
        requires v.len() > 0,
        ensures 
            i < v.len(),
            forall |k: int| 0 <= k < v.len() ==> v[i as int] >= v[k],
            forall |l: int| 0 <= l < i ==> v[i as int] > v[l],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    fn mlastMaximum(v: &[int]) -> (i: usize)
        requires v.len() > 0,
        ensures 
            i < v.len(),
            forall |k: int| 0 <= k < v.len() ==> v[i as int] >= v[k],
            forall |l: int| i < l < v.len() ==> v[i as int] > v[l],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    // Algorithm: from left to right
    fn mmaxvalue1(v: &[int]) -> (m: int)
        requires v.len() > 0,
        ensures 
            exists |k: int| 0 <= k < v.len() && m == v[k],
            forall |k: int| 0 <= k < v.len() ==> m >= v[k],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }

    // Algorithm: from right to left
    fn mmaxvalue2(v: &[int]) -> (m: int)
        requires v.len() > 0,
        ensures 
            exists |k: int| 0 <= k < v.len() && m == v[k],
            forall |k: int| 0 <= k < v.len() ==> m >= v[k],
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}