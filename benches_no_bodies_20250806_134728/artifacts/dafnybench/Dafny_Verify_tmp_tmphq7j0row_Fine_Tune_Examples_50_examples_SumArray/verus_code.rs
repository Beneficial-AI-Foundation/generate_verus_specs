use vstd::prelude::*;

verus! {
    spec fn sum_spec(s: Seq<i32>, len: int) -> int
        recommends 0 <= len <= s.len()
        decreases len
    {
        if len <= 0 { 
            0 
        } else { 
            s[len - 1] as int + sum_spec(s, len - 1) 
        }
    }

    fn sum_array(arr: &Vec<i32>) -> (result: i32)
        requires 
            arr.len() > 0,
            arr.len() <= 5,
            forall|j: int| 0 <= j < arr.len() ==> #[trigger] arr[j] >= -5 && arr[j] <= 5,
        ensures result as int == sum_spec(arr@, arr.len() as int)
    {
    return 0;  // TODO: Remove this line and implement the function body
    }
}