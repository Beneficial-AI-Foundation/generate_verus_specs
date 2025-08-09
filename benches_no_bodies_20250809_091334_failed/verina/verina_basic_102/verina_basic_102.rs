use vstd::prelude::*;

verus! {

// Precondition: array has more than 1 element and there exists a pair that sums to target
spec fn two_sum_precond(nums: Seq<int>, target: int) -> bool {
    nums.len() > 1 && exists |i: int, j: int| 
        0 <= i < j < nums.len() && nums[i] + nums[j] == target
}

// Postcondition: result is a valid pair that sums to target and is the lexicographically first such pair
spec fn two_sum_postcond(nums: Seq<int>, target: int, result: (usize, usize)) -> bool {
    let (i, j) = result;
    // Basic validity
    i < j && j < nums.len() && nums[i as int] + nums[j as int] == target &&
    // i is the first valid first index
    (forall |i0: int| #![trigger nums[i0]] 0 <= i0 < i ==> 
        (forall |j0: int| #![trigger nums[j0]] i0 < j0 < nums.len() ==> nums[i0] + nums[j0] != target)) &&
    // j is the first valid second index for the chosen i
    (forall |j0: int| #![trigger nums[j0]] (i as int) < j0 < (j as int) ==> nums[i as int] + nums[j0] != target)
}

fn two_sum_inner(nums: &Vec<int>, target: int, i: usize, j: usize) -> (result: Option<(usize, usize)>)
    requires 
        i < nums.len(),
        j <= nums.len(),
        i < j,
    ensures
        match result {
    return None;  // TODO: Remove this line and implement the function body
        }
    decreases nums.len() - j
{
    if j >= nums.len() {
        None
    } else if nums[i] + nums[j] == target {
        Some((i, j))
    } else {
        two_sum_inner(nums, target, i, j + 1)
    }
}

fn two_sum_outer(nums: &Vec<int>, target: int, i: usize) -> (result: Option<(usize, usize)>)
    requires 
        i < nums.len(),
        nums.len() > 0,
    ensures
        match result {
    return None;  // TODO: Remove this line and implement the function body
        }
    decreases nums.len() - i
{
    if nums.len() == 0 || i >= nums.len() - 1 {
        None
    } else {
        match two_sum_inner(nums, target, i, i + 1) {
            Some(pair) => Some(pair),
            None => two_sum_outer(nums, target, i + 1),
        }
    }
}

fn two_sum(nums: Vec<int>, target: int) -> (result: (usize, usize))
    requires 
        two_sum_precond(nums@, target),
    ensures 
        two_sum_postcond(nums@, target, result),
{
    return 0;  // TODO: Remove this line and implement the function body
}

}

fn main() {}