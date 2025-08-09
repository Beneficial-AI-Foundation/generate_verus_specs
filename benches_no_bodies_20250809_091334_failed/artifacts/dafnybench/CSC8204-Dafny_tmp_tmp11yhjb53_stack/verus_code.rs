use vstd::prelude::*;

verus! {
    /* 
      Dafny Tutorial 2: Sequences and Stacks, Predicates and Assertions

      In this tutorial we introduce a simple stack model using the functional 
      style of programming.
      
    */
    type IntStack = Seq<int>;

    spec fn is_empty(s: IntStack) -> bool {
        s.len() == 0
    }

    spec fn push(s: IntStack, x: int) -> IntStack {
        s.push(x)
    }

    spec fn pop(s: IntStack) -> IntStack {
        if s.len() > 0 {
            s.subrange(0, s.len() - 1)
        } else {
            arbitrary()
        }
    }

    proof fn test_stack() -> (r: IntStack) {
    assume(false);  // TODO: Remove this line and implement the proof
    }

    fn main() {
    // TODO: Remove this comment and implement the function body
    }
}