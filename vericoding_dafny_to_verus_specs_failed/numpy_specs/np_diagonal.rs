use vstd::prelude::*;

verus! {

// SPEC  
#[verifier::external_body]
        if k > 0 { ret.len() == arr.len() - k } else { ret.len() == arr.len() + k },
        forall|i: int| 0 <= i < ret.len() ==> 
            if k >= 0 { 
                ret@[i] == arr@[i]@[i + k]
            } else { 
                ret@[i] == arr@[i - k]@[i]
            }
{
    unimplemented!()
}

fn main() {}

}