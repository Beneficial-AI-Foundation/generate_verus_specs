use vstd::prelude::*;

verus! {
    #[derive(PartialEq, Eq)]
    pub enum Exp {
        Const(int),
        Var(String),
        Plus(Box<Exp>, Box<Exp>),
        Mult(Box<Exp>, Box<Exp>),
    }

    spec fn eval(e: Exp, store: Map<String, int>) -> int
        decreases e
    {
        match e {
            Exp::Const(n) => n,
            Exp::Var(s) => if store.contains_key(s) { store[s] } else { -1 },
            Exp::Plus(e1, e2) => eval(*e1, store) + eval(*e2, store),
            Exp::Mult(e1, e2) => eval(*e1, store) * eval(*e2, store),
        }
    }

    spec fn optimize(e: Exp) -> Exp
        decreases e
    {
        match e {
            Exp::Mult(e1, e2) => match (*e1, *e2) {
                (Exp::Const(n), _) if n == 0 => Exp::Const(0),
                (_, Exp::Const(n)) if n == 0 => Exp::Const(0),
                (Exp::Const(n), e) if n == 1 => e,
                (e, Exp::Const(n)) if n == 1 => e,
                (Exp::Const(n1), Exp::Const(n2)) => Exp::Const(n1 * n2),
                _ => e,
            },
            Exp::Plus(e1, e2) => match (*e1, *e2) {
                (Exp::Const(n), e) if n == 0 => e,
                (e, Exp::Const(n)) if n == 0 => e,
                (Exp::Const(n1), Exp::Const(n2)) => Exp::Const(n1 + n2),
                _ => e,
            },
            _ => e,
        }
    }

    proof fn optimize_correct(e: Exp, s: Map<String, int>)
        ensures eval(e, s) == eval(optimize(e), s)
        decreases e
    {
    assume(false);  // TODO: Remove this line and implement the proof
    }

    proof fn optimize_simple_tests() {
    assume(false);  // TODO: Remove this line and implement the proof
    }
}