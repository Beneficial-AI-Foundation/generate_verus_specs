use vstd::prelude::*;

verus! {
    struct BoundedQueue<T> where T: Copy {
        // abstract state
        ghost contents: Seq<T>, // the contents of the bounded queue
        ghost N: nat, // the (maximum) size of the bounded queue
        
        // concrete state
        data: Vec<T>,
        wr: usize,
        rd: usize,
    }

    impl<T> BoundedQueue<T> where T: Copy {
        spec fn valid(self) -> bool {
            self.data.len() == self.N + 1 &&
            self.wr <= self.N &&
            self.rd <= self.N &&
            self.contents == if self.rd <= self.wr {
                self.data@.subrange(self.rd as int, self.wr as int)
            } else {
                self.data@.subrange(self.rd as int, self.data.len() as int) + 
                self.data@.subrange(0, self.wr as int)
            }
        }

        fn insert(&mut self, x: T)
            requires 
                old(self).valid(),
                old(self).contents.len() != old(self).N,
            ensures 
                self.contents == old(self).contents.push(x),
                self.N == old(self).N,
                self.valid(),
        {
    // TODO: Remove this comment and implement the function body
        }

        fn remove(&mut self) -> (x: T)
            requires 
                old(self).valid(),
                old(self).contents.len() != 0,
            ensures 
                self.contents == old(self).contents.drop_first(),
                old(self).contents.index(0) == x,
                self.N == old(self).N,
                self.valid(),
        {
    assume(false);  // TODO: Replace with appropriate return value of type T
        }
    }
}