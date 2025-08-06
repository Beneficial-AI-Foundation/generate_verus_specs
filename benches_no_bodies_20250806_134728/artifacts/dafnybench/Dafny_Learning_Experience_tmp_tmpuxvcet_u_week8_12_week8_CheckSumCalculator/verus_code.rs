use vstd::prelude::*;

verus! {
    spec fn hash(s: Seq<char>) -> int {
        sum_chars(s) % 137
    }

    spec fn sum_chars(s: Seq<char>) -> int 
        decreases s.len()
    {
        if s.len() == 0 {
            0
        } else {
            s[s.len() - 1] as int + sum_chars(s.subrange(0, s.len() - 1))
        }
    }

    struct CheckSumCalculator {
        cs: u32,
    }

    impl CheckSumCalculator {
        fn new() -> (result: CheckSumCalculator)
            ensures result.cs == 0
        {
    assume(false);  // TODO: Replace with appropriate return value of type CheckSumCalculator
        }

        fn append_single(&mut self, c: char)
            ensures self.cs < 137
        {
    // TODO: Remove this comment and implement the function body
        }

        fn checksum(&self) -> u32 {
    return 0;  // TODO: Remove this line and implement the function body
        }
    }

    fn main() {
    // TODO: Remove this comment and implement the function body
    }
}