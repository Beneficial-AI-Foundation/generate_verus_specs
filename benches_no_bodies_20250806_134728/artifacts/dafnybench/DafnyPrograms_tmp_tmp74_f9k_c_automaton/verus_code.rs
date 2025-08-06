use vstd::prelude::*;

verus! {
    /**
    Consider cellular automata: a row of cells is repeatedly updated according to a rule. In this exercise I dabbled with,
    each cell has the value either false or true. Each cell's next state depends only on the immediate neighbours, in the 
    case where the cell is at the edges of the row, the inexistent neighbours are replaced by "false". The automaton table 
    will contain the initial row, plus a row for each number of steps.
     */

    /**
    This method computes the automaton.
    Provide the initial row: init, the rule and the desired number of steps
     */
    fn execute_automaton(init: Vec<bool>, rule: fn(bool, bool, bool) -> bool, steps: usize) -> (table: Vec<Vec<bool>>)
        requires 
            // we need the initial row to have the length bigger or equal to two
            init.len() >= 2,
        ensures 
            // after computation the automaton is made of the initial row plus a row for each of the steps
            table.len() == 1 + steps,
            // the automaton must have the initial row at the top
            table[0] == init,
            // all rows in the automaton must be the same length
            forall|i: int| 0 <= i < table.len() ==> table[i].len() == init.len(),
            // all the middle row elements (with existing neighbours) after a step, will be equal to the rule applied on the element in the previous state
            // and its neigbours
            forall|i: int| 0 <= i < table.len() - 1 ==>
              forall|j: int| 1 <= j <= table[i].len() - 2 ==> 
                table[i + 1][j] == rule(table[i][j - 1], table[i][j], table[i][j + 1]),
            // the corner row elements (with non-existing neighbours) after a step, will be equal to the rule applied on the element in the previous state,
            // its neighbour and false
            forall|i: int| 0 <= i < table.len() - 1 ==>
              table[i + 1][0] == rule(false, table[i][0], table[i][1]) && 
              table[i + 1][table[i].len() - 1] == rule(table[i][table[i].len() - 2], table[i][table[i].len() - 1], false),
    {
    return false;  // TODO: Remove this line and implement the function body
    }

    // example rule
    fn the_rule(a: bool, b: bool, c: bool) -> bool {
    return false;  // TODO: Remove this line and implement the function body
    }

    // example rule 2
    fn the_rule2(a: bool, b: bool, c: bool) -> bool {
    return false;  // TODO: Remove this line and implement the function body
    }

    fn test_method() {
    // TODO: Remove this comment and implement the function body
    }
}

fn main() {}