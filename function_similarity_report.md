# Cross-File Function Similarity Analysis Report

*Note: This analysis only considers similarities between functions in different files.*

Total functions analyzed: 2396
Similar function groups found (cross-file only): 53

Total functions in similar groups: 1394
Percentage of functions with cross-file similarities: 58.2%

## Similar Function Groups

### Group 1 (Average Similarity: 100.00%)

Functions in this group (38 total):

- **shared_elements** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_2.rs` (line 14)
- **replace_with_colon** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_732.rs` (line 19)
- **find_odd_numbers** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_554.rs` (line 5)
- **filter_odd_numbers** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_426.rs` (line 5)
- **remove_elements** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_161.rs` (line 30)
- **element_wise_divide** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_618.rs` (line 5)
- **element_wise_division** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_261.rs` (line 5)
- **remove_chars** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_18.rs` (line 31)
- **insert_before_each** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_251.rs` (line 5)
- **intersection** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_249.rs` (line 14)
- **extract_rear_chars** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_424.rs` (line 5)
- **list_deep_clone** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_307.rs` (line 5)
- **find_negative_numbers** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_436.rs` (line 5)
- **to_lowercase** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_477.rs` (line 15)
- **difference** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_769.rs` (line 30)
- **remove_odds** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_412.rs` (line 5)
- **interleave** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_578.rs` (line 5)
- **remove_kth_element** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_610.rs` (line 5)
- **add_list** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_728.rs` (line 6)
- **element_wise_subtract** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_282.rs` (line 5)
- **rotate_right** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_743.rs` (line 10)
- **split_and_append** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_586.rs` (line 5)
- **find_even_numbers** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_629.rs` (line 6)
- **bit_wise_xor** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_399.rs` (line 5)
- **replace_chars** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_474.rs` (line 14)
- **reverse_to_k** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_644.rs` (line 5)
- **replace_blanks_with_chars** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_230.rs` (line 14)
- **element_wise_module** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_616.rs` (line 5)
- **to_toggle_case** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 36)
- **remove_duplicates** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_572.rs` (line 29)
- **element_wise_multiplication** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_445.rs` (line 5)
- **element_wise_subtract** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_273.rs` (line 5)
- **square_nums** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_8.rs` (line 6)
- **to_uppercase** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_624.rs` (line 23)
- **cube_element** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_447.rs` (line 5)
- **get_first_elements** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_460.rs` (line 5)
- **find_dissimilar** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_579.rs` (line 30)
- **replace_last_element** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_240.rs` (line 5)

**Sample code from first function:**
```rust
{
    return Vec::new();  // TODO: Remove this line and implement the function body
}
```

---

### Group 2 (Average Similarity: 100.00%)

Functions in this group (3 total):

- **is_sub_list_at_index** in `benches/VerusProofSynthesisBench/MBPP/task_id_69.rs` (line 5)
- **is_sub_list_at_index** in `benches/autoverus/MBPP/verified/task_id_69.rs` (line 13)
- **sub_array_at_index** in `benches/autoverus/MBPP/verified/task_id_576.rs` (line 24)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut i = 0;
    while i < sub.len()
        // invariants-start
        invariant
            0 <= idx <= (main.len() - sub.len()),
            0 <= i <= sub.len(),
            0 <= idx + i <= main.len(),
            forall|k: int| 0 <= k < i ==> main[idx + k] == sub[k],
            forall|k: int|
                0 <= k < i ==> (main@.subrange(idx as int, (idx + k)) =~= sub@.subrange(0, k)),
        // invariants-end
    {
        if (main[idx + i] != sub[i]) {
       ...
```

**Pairwise similarities:**
- is_sub_list_at_index vs is_sub_list_at_index: 100.00%
- is_sub_list_at_index vs sub_array_at_index: 100.00%
- is_sub_list_at_index vs sub_array_at_index: 100.00%

---

### Group 3 (Average Similarity: 100.00%)

Functions in this group (3 total):

- **is_odd_at_odd_index** in `benches/VerusProofSynthesisBench/MBPP/task_id_775.rs` (line 5)
- **is_odd_at_odd_index** in `benches/autoverus/MBPP/verified/task_id_775.rs` (line 13)
- **is_even_at_even_index** in `benches/autoverus/MBPP/verified/task_id_790.rs` (line 13)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut index = 0;
    while index < arr.len()
        // invariants-start
        invariant
            0 <= index <= arr.len(),
            forall|i: int| 0 <= i < index ==> ((i % 2) == (arr[i] % 2)),
        // invariants-end
    {
        if ((index % 2) != (arr[index] % 2)) {
            // assert-start
            assert(((index as int) % 2) != (arr[index as int] % 2));
            // assert-end
            return false;
        }
        index += 1;
    }
    true
...
```

**Pairwise similarities:**
- is_odd_at_odd_index vs is_odd_at_odd_index: 100.00%
- is_odd_at_odd_index vs is_even_at_even_index: 100.00%
- is_odd_at_odd_index vs is_even_at_even_index: 100.00%

---

### Group 4 (Average Similarity: 100.00%)

Functions in this group (2 total):

- **max** in `benches/RustBench/preconditions_removed/max_dafny_lsp.rs` (line 6)
- **max_dafny_lsp** in `benches/RustBench/ground_truth/max_dafny_lsp.rs` (line 6)

**Sample code from first function:**
```rust
{
    let mut x = 0;
    let mut y = a.len() - 1;

    let ghost mut m = 0;
    while x != y
        invariant
            0 <= x <= y < a.len(),
            m == x || m == y,
            forall|i: int| 0 <= i < x ==> a[i] <= a[m],
            forall|i: int| y < i < a.len() ==> a[i] <= a[m],
    {
        if a[x] <= a[y] {
            x = x + 1;
            proof {
                m = y as int;
            }
        } else {
            y = y - 1;
            proof {
                m = x as int...
```

**Pairwise similarities:**
- max vs max_dafny_lsp: 100.00%

---

### Group 5 (Average Similarity: 100.00%)

Functions in this group (2 total):

- **unique** in `benches/RustBench/preconditions_removed/unique_better.rs` (line 6)
- **unique_better** in `benches/RustBench/ground_truth/unique_better.rs` (line 6)

**Sample code from first function:**
```rust
{
    let mut result: Vec<i32> = Vec::new();
    let mut i = 0;
    while i < a.len()
        invariant
            0 <= i <= a.len(),
            forall|k: int, l: int|
                #![trigger result[k], result[l]]
                0 <= k && k < l && l < result.len() ==> result[k] < result[l],
            forall|k: int|
                #![trigger result[k]]
                0 <= k && k < result.len() ==> exists|m: int| 0 <= m < i && result[k] == a[m],
    {
        if result.len() == 0 || resu...
```

**Pairwise similarities:**
- unique vs unique_better: 100.00%

---

### Group 6 (Average Similarity: 99.83%)

Functions in this group (3 total):

- **difference_max_min** in `benches/VerusProofSynthesisBench/MBPP/task_id_588.rs` (line 29)
- **difference_max_min** in `benches/autoverus/MBPP/verified/task_id_588.rs` (line 35)
- **sum_min_max** in `benches/autoverus/MBPP/verified/task_id_476.rs` (line 35)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut min_val = arr[0];
    let mut max_val = arr[0];
    let mut index = 1;

    while index < arr.len()
        // invariants-start
        invariant
            1 <= index <= arr.len(),
            i32::MIN / 2 < min_val < i32::MAX / 2,
            i32::MIN / 2 < max_val < i32::MAX / 2,
            max_val == max_rcur(arr@.subrange(0, index as int)),
            min_val == min_rcur(arr@.subrange(0, index as int)),
        // invariants-end
    {
        if (arr[index...
```

**Pairwise similarities:**
- difference_max_min vs difference_max_min: 100.00%
- difference_max_min vs sum_min_max: 99.83%
- difference_max_min vs sum_min_max: 99.83%

---

### Group 7 (Average Similarity: 99.73%)

Functions in this group (3 total):

- **find_dissimilar** in `benches/VerusProofSynthesisBench/MBPP/task_id_579.rs` (line 44)
- **find_dissimilar** in `benches/autoverus/MBPP/verified/task_id_579.rs` (line 48)
- **difference** in `benches/autoverus/MBPP/verified/task_id_769.rs` (line 45)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut result = Vec::new();
    let ghost mut output_len: int = 0;

    let mut index = 0;
    while index < arr1.len()
        // invariants-start
        invariant
            forall|i: int|
                0 <= i < index ==> (!arr2@.contains(#[trigger] arr1[i]) ==> result@.contains(
                    arr1[i],
                )),
            forall|m: int, n: int|
                0 <= m < n < result.len() ==> #[trigger] result[m] != #[trigger] result[n],
        // i...
```

**Pairwise similarities:**
- find_dissimilar vs find_dissimilar: 100.00%
- find_dissimilar vs difference: 99.73%
- find_dissimilar vs difference: 99.73%

---

### Group 8 (Average Similarity: 98.25%)

Functions in this group (6 total):

- **sqrt** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_sqrt/verus_code.rs` (line 8)
- **new** in `benches/artifacts/dafnybench/CS5232_Project_tmp_tmpai_cfrng_LFUSimple/verus_code.rs` (line 18)
- **congruence** in `benches/artifacts/dafnybench/Dafny-VMC_tmp_tmpzgqv0i1u_src_Math_Helper/verus_code.rs` (line 16)
- **sum_range_list** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_170.rs` (line 16)
- **sum** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_798.rs` (line 16)
- **sum_negatives** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_133.rs` (line 21)

**Sample code from first function:**
```rust
{
        // This is a specification-only function - actual implementation
        // would need to compute square root
        assume(false);
        0
    }
```

---

### Group 9 (Average Similarity: 97.63%)

Functions in this group (3 total):

- **is_sub_list** in `benches/VerusProofSynthesisBench/MBPP/task_id_69.rs` (line 45)
- **is_sub_list** in `benches/autoverus/MBPP/verified/task_id_69.rs` (line 41)
- **is_sub_array** in `benches/autoverus/MBPP/verified/task_id_576.rs` (line 53)

**Sample code from first function:**
```rust
{
    // impl-start
    if sub.len() > main.len() {
        return false;
    }
    let mut index = 0;
    while index <= (main.len() - sub.len())
        // invariants-start
        invariant
            sub.len() <= main.len(),
            0 <= index <= (main.len() - sub.len()) + 1,
            forall|k: int, l: int|
                (0 <= k < index) && l == k + sub.len() ==> (#[trigger] (main@.subrange(k, l))
                    != sub@),
        // invariants-end
    {
        if (is_sub_list...
```

**Pairwise similarities:**
- is_sub_list vs is_sub_list: 100.00%
- is_sub_list vs is_sub_array: 97.63%
- is_sub_list vs is_sub_array: 97.63%

---

### Group 10 (Average Similarity: 96.59%)

Functions in this group (3 total):

- **remove_chars** in `benches/VerusProofSynthesisBench/MBPP/task_id_18.rs` (line 45)
- **remove_chars** in `benches/autoverus/MBPP/verified/task_id_18.rs` (line 39)
- **remove_elements** in `benches/autoverus/MBPP/verified/task_id_161.rs` (line 48)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut output_str = Vec::new();
    let mut index: usize = 0;
    let ghost mut output_len: int = 0;

    while index < str1.len()
        // invariants-start
        invariant
            forall|k: int|
                0 <= k < output_str.len() ==> (str1@.contains(#[trigger] output_str[k])
                    && !str2@.contains(#[trigger] output_str[k])),
            forall|k: int|
                0 <= k < index ==> (str2@.contains(#[trigger] str1[k]) || output_str@.con...
```

**Pairwise similarities:**
- remove_chars vs remove_chars: 100.00%
- remove_chars vs remove_elements: 96.59%
- remove_chars vs remove_elements: 96.59%

---

### Group 11 (Average Similarity: 96.43%)

Functions in this group (9 total):

- **shift32_spec** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_477.rs` (line 10)
- **shift32_spec** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 10)
- **shift_minus_32_spec** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 20)
- **shift_minus_32_spec** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_624.rs` (line 10)
- **shift32_spec** in `benches/VerusProofSynthesisBench/MBPP/task_id_477.rs` (line 10)
- **shift32_spec** in `benches/VerusProofSynthesisBench/MBPP/task_id_557.rs` (line 10)
- **shift_minus_32_spec** in `benches/VerusProofSynthesisBench/MBPP/task_id_557.rs` (line 20)
- **shift_minus_32_spec** in `benches/VerusProofSynthesisBench/MBPP/task_id_624.rs` (line 10)
- **shift_minus_32_spec** in `benches/HumanEval-RustBench/027-flip_case.rs` (line 21)

**Sample code from first function:**
```rust
{
    ((c as u8) + 32) as char
}
```

---

### Group 12 (Average Similarity: 96.12%)

Functions in this group (15 total):

- **min_rcur** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_588.rs` (line 18)
- **min_rcur** in `benches/VerusProofSynthesisBench/MBPP/task_id_476.rs` (line 18)
- **min_rcur** in `benches/VerusProofSynthesisBench/MBPP/task_id_588.rs` (line 18)
- **min_rcur** in `benches/autoverus/MBPP/unverified/task_id_476.rs` (line 19)
- **min_rcur** in `benches/autoverus/MBPP/unverified/task_id_588.rs` (line 19)
- **min_rcur** in `benches/autoverus/MBPP/verified/task_id_476.rs` (line 25)
- **min_rcur** in `benches/autoverus/MBPP/verified/task_id_588.rs` (line 25)
- **max_rcur** in `benches/VerusProofSynthesisBench/MBPP/task_id_476.rs` (line 7)
- **max_rcur** in `benches/VerusProofSynthesisBench/MBPP/task_id_588.rs` (line 7)
- **max_rcur** in `benches/autoverus/MBPP/unverified/task_id_476.rs` (line 9)
- **max_rcur** in `benches/autoverus/MBPP/unverified/task_id_588.rs` (line 9)
- **max_rcur** in `benches/autoverus/MBPP/verified/task_id_476.rs` (line 15)
- **max_rcur** in `benches/autoverus/MBPP/verified/task_id_588.rs` (line 15)
- **max_rcur** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_588.rs` (line 7)
- **min_rcur** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_476.rs` (line 18)

**Sample code from first function:**
```rust
{
    if seq.len() <= 1 {
        seq.first() as int
    } else {
        min(seq.last() as int, min_rcur(seq.drop_last()))
    }
}
```

---

### Group 13 (Average Similarity: 95.76%)

Functions in this group (8 total):

- **element_wise_division** in `benches/autoverus/MBPP/unverified/task_id_261.rs` (line 7)
- **list_deep_clone** in `benches/autoverus/MBPP/unverified/task_id_307.rs` (line 7)
- **add_list** in `benches/autoverus/MBPP/unverified/task_id_728.rs` (line 7)
- **element_wise_subtract** in `benches/autoverus/MBPP/unverified/task_id_282.rs` (line 7)
- **bit_wise_xor** in `benches/autoverus/MBPP/unverified/task_id_399.rs` (line 7)
- **element_wise_module** in `benches/autoverus/MBPP/unverified/task_id_616.rs` (line 7)
- **element_wise_multiplication** in `benches/autoverus/MBPP/unverified/task_id_445.rs` (line 7)
- **element_wise_subtract** in `benches/autoverus/MBPP/unverified/task_id_273.rs` (line 7)

**Sample code from first function:**
```rust
{
    let mut output_arr = Vec::with_capacity(arr1.len());
    let mut index = 0;

    while index < arr1.len() {
        output_arr.push((arr1[index] / arr2[index]));
        index += 1;
    }
    output_arr
}
```

---

### Group 14 (Average Similarity: 95.45%)

Functions in this group (2 total):

- **sum_min_max** in `benches/autoverus/MBPP/unverified/task_id_476.rs` (line 29)
- **difference_max_min** in `benches/autoverus/MBPP/unverified/task_id_588.rs` (line 29)

**Sample code from first function:**
```rust
{
    let mut min_val = arr[0];
    let mut max_val = arr[0];
    let mut index = 1;

    while index < arr.len() {
        if (arr[index] <= min_val) {
            min_val = arr[index];
        } else if (arr[index] > max_val) {
            max_val = arr[index];
        }
        index += 1;
    }
    max_val + min_val
}
```

**Pairwise similarities:**
- sum_min_max vs difference_max_min: 95.45%

---

### Group 15 (Average Similarity: 94.44%)

Functions in this group (7 total):

- **shift_minus_32_spec** in `benches/autoverus/MBPP/unverified/task_id_557.rs` (line 18)
- **shift_minus_32_spec** in `benches/autoverus/MBPP/unverified/task_id_624.rs` (line 11)
- **shift_minus_32_spec** in `benches/autoverus/MBPP/verified/task_id_557.rs` (line 24)
- **shift_minus_32_spec** in `benches/autoverus/MBPP/verified/task_id_624.rs` (line 17)
- **shift32_spec** in `benches/autoverus/MBPP/verified/task_id_477.rs` (line 17)
- **shift32_spec** in `benches/autoverus/MBPP/verified/task_id_557.rs` (line 16)
- **shift32_spec** in `benches/autoverus/MBPP/unverified/task_id_557.rs` (line 10)

**Sample code from first function:**
```rust
{
    (c - 32) as u8
}
```

---

### Group 16 (Average Similarity: 93.82%)

Functions in this group (3 total):

- **is_non_prime** in `benches/VerusProofSynthesisBench/MBPP/task_id_3.rs` (line 11)
- **is_non_prime** in `benches/autoverus/MBPP/verified/task_id_3.rs` (line 22)
- **prime_num** in `benches/autoverus/MBPP/verified/task_id_605.rs` (line 22)

**Sample code from first function:**
```rust
{
    // impl-start
    if n <= 1 {
        return true;
    }
    let mut index = 2;
    while index < n
        // invariants-start
        invariant
            2 <= index,
            forall|k: int| 2 <= k < index ==> !is_divisible(n as int, k),
        // invariants-end
    {
        if ((n % index) == 0) {
            // assert-start
            assert(is_divisible(n as int, index as int));
            // assert-end
            return true;
        }
        index += 1;
    }
    false
   ...
```

**Pairwise similarities:**
- is_non_prime vs is_non_prime: 100.00%
- is_non_prime vs prime_num: 93.82%
- is_non_prime vs prime_num: 93.82%

---

### Group 17 (Average Similarity: 93.33%)

Functions in this group (6 total):

- **is_vowel** in `benches/HumanEval-RustBench/064-vowel_count.rs` (line 5)
- **is_ascii_digit_spec** in `benches/autoverus/CloverBench/unverified/all_digits_strong.rs` (line 6)
- **is_ascii_digit** in `benches/autoverus/CloverBench/unverified/all_digits_strong.rs` (line 11)
- **is_ascii_digit_spec** in `benches/autoverus/CloverBench/verified/all_digits_strong.rs` (line 6)
- **is_ascii_digit** in `benches/autoverus/CloverBench/verified/all_digits_strong.rs` (line 11)
- **is_vowel** in `benches/HumanEval-RustBench/051-remove_vowels.rs` (line 11)

**Sample code from first function:**
```rust
{
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I'
        || c == 'O' || c == 'U'
}
```

---

### Group 18 (Average Similarity: 92.69%)

Functions in this group (3 total):

- **all_characters_same** in `benches/VerusProofSynthesisBench/MBPP/task_id_741.rs` (line 6)
- **all_characters_same** in `benches/autoverus/MBPP/verified/task_id_741.rs` (line 13)
- **has_only_one_distinct_element** in `benches/autoverus/MBPP/verified/task_id_760.rs` (line 13)

**Sample code from first function:**
```rust
{
    // impl-start
    if char_arr.len() <= 1 {
        return true;
    }
    let mut index = 1;
    while index < char_arr.len()
        // invariants-start
        invariant
            1 <= index <= char_arr.len(),
            forall|k: int| 0 <= k < index ==> char_arr[0] == #[trigger] char_arr[k],
        // invariants-end
    {
        if char_arr[0] != char_arr[index] {
            // assert-start
            assert(exists|i: int|
                1 <= i < char_arr@.len() && char_arr[0] !...
```

**Pairwise similarities:**
- all_characters_same vs all_characters_same: 100.00%
- all_characters_same vs has_only_one_distinct_element: 92.69%
- all_characters_same vs has_only_one_distinct_element: 92.69%

---

### Group 19 (Average Similarity: 90.74%)

Functions in this group (15 total):

- **element_wise_division** in `benches/VerusProofSynthesisBench/MBPP/task_id_261.rs` (line 5)
- **add_list** in `benches/VerusProofSynthesisBench/MBPP/task_id_728.rs` (line 6)
- **element_wise_subtract** in `benches/VerusProofSynthesisBench/MBPP/task_id_282.rs` (line 5)
- **element_wise_module** in `benches/VerusProofSynthesisBench/MBPP/task_id_616.rs` (line 5)
- **element_wise_multiplication** in `benches/VerusProofSynthesisBench/MBPP/task_id_445.rs` (line 5)
- **element_wise_subtract** in `benches/VerusProofSynthesisBench/MBPP/task_id_273.rs` (line 5)
- **element_wise_division** in `benches/autoverus/MBPP/verified/task_id_261.rs` (line 22)
- **add_list** in `benches/autoverus/MBPP/verified/task_id_728.rs` (line 16)
- **element_wise_subtract** in `benches/autoverus/MBPP/verified/task_id_282.rs` (line 19)
- **element_wise_module** in `benches/autoverus/MBPP/verified/task_id_616.rs` (line 22)
- **element_wise_multiplication** in `benches/autoverus/MBPP/verified/task_id_445.rs` (line 31)
- **element_wise_subtract** in `benches/autoverus/MBPP/verified/task_id_273.rs` (line 22)
- **element_wise_divide** in `benches/autoverus/MBPP/verified/task_id_618.rs` (line 16)
- **bit_wise_xor** in `benches/VerusProofSynthesisBench/MBPP/task_id_399.rs` (line 5)
- **bit_wise_xor** in `benches/autoverus/MBPP/verified/task_id_399.rs` (line 22)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut output_arr = Vec::with_capacity(arr1.len());
    let mut index = 0;
    while index < arr1.len()
        // invariants-start
        invariant
            arr1.len() == arr2.len(),
            0 <= index <= arr2.len(),
            output_arr.len() == index,
            forall|i: int| 0 <= i < arr2.len() ==> arr2[i] != 0,
            forall|m: int|
                0 <= m < arr1.len() ==> (u32::MIN <= #[trigger] arr1[m] / #[trigger] arr2[m]
                    <= u3...
```

---

### Group 20 (Average Similarity: 89.42%)

Functions in this group (50 total):

- **prime_num** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_605.rs` (line 10)
- **second_smallest** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_755.rs` (line 25)
- **any_value_exists** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_414.rs` (line 14)
- **min_sublist** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_457.rs` (line 5)
- **is_product_even** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_804.rs` (line 10)
- **sub_array_at_index** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_576.rs` (line 5)
- **is_sub_array** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_576.rs` (line 19)
- **count_identical_position** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_142.rs` (line 21)
- **split_array** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_262.rs` (line 6)
- **has_only_one_distinct_element** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_760.rs` (line 6)
- **smallest_list_length** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_95.rs` (line 6)
- **is_greater** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_433.rs` (line 5)
- **count_uppercase** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_461.rs` (line 30)
- **smallest_num** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_62.rs` (line 6)
- **all_elements_equals** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_284.rs` (line 5)
- **is_non_prime** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_3.rs` (line 11)
- **max_difference** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_145.rs` (line 5)
- **find_first_occurrence** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_733.rs` (line 5)
- **is_digit** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_113.rs` (line 10)
- **is_integer** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_113.rs` (line 19)
- **sum_min_max** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_476.rs` (line 29)
- **all_characters_same** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_741.rs` (line 6)
- **count_digits** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_764.rs` (line 26)
- **contains_z** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_454.rs` (line 5)
- **count_true** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_105.rs` (line 20)
- **is_sorted** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_567.rs` (line 5)
- **min_second_value_first** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_94.rs` (line 6)
- **contains_consecutive_numbers** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_472.rs` (line 5)
- **find_first_odd** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_807.rs` (line 17)
- **count_frequency** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_602.rs` (line 20)
- **first_repeated_char** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_602.rs` (line 42)
- **has_common_element** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_431.rs` (line 5)
- **contains_k** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_808.rs` (line 6)
- **is_smaller** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_809.rs` (line 6)
- **is_sub_list_at_index** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_69.rs` (line 5)
- **is_sub_list** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_69.rs` (line 19)
- **max_length_list** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_290.rs` (line 6)
- **is_even_at_even_index** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_790.rs` (line 6)
- **count_frequency** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_572.rs` (line 20)
- **all_sequence_equal_length** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_70.rs` (line 5)
- **sub_array_at_index** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_576_v2.rs` (line 5)
- **is_sub_array** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_576_v2.rs` (line 23)
- **difference_max_min** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_588.rs` (line 29)
- **is_odd_at_odd_index** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_775.rs` (line 5)
- **contains** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_414.rs` (line 5)
- **contains** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_161.rs` (line 21)
- **contains** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_18.rs` (line 22)
- **contains** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_249.rs` (line 5)
- **contains** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_769.rs` (line 21)
- **contains** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_579.rs` (line 21)

**Sample code from first function:**
```rust
{
    return false;  // TODO: Remove this line and implement the function body
}
```

---

### Group 21 (Average Similarity: 89.20%)

Functions in this group (9 total):

- **count_digits** in `benches/VerusProofSynthesisBench/MBPP/task_id_764.rs` (line 26)
- **count_true** in `benches/VerusProofSynthesisBench/MBPP/task_id_105.rs` (line 20)
- **count_digits** in `benches/autoverus/MBPP/verified/task_id_764.rs` (line 32)
- **count_true** in `benches/autoverus/MBPP/verified/task_id_105.rs` (line 27)
- **count_uppercase** in `benches/autoverus/MBPP/verified/task_id_461.rs` (line 35)
- **count_frequency** in `benches/VerusProofSynthesisBench/MBPP/task_id_602.rs` (line 20)
- **count_frequency** in `benches/VerusProofSynthesisBench/MBPP/task_id_572.rs` (line 20)
- **count_frequency** in `benches/autoverus/MBPP/verified/task_id_602.rs` (line 27)
- **count_frequency** in `benches/autoverus/MBPP/verified/task_id_572.rs` (line 27)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut count = 0;

    let mut index = 0;
    while index < text.len()
        // invariants-start
        invariant
            0 <= index <= text.len(),
            0 <= count <= index,
            count == count_digits_recursively(text@.subrange(0, index as int)),
        // invariants-end
    {
        if ((text[index] as u8) >= 48 && (text[index] as u8) <= 57) {
            count += 1;
        }
        index += 1;
        // assert-start
        assert(text@.subran...
```

---

### Group 22 (Average Similarity: 89.01%)

Functions in this group (3 total):

- **max_length_list** in `benches/VerusProofSynthesisBench/MBPP/task_id_290.rs` (line 6)
- **max_length_list** in `benches/autoverus/MBPP/verified/task_id_290.rs` (line 30)
- **min_sublist** in `benches/autoverus/MBPP/verified/task_id_457.rs` (line 22)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut max_list = &seq[0];
    assert(max_list@ =~= seq[0]@);
    let mut index = 1;

    while index < seq.len()
        // invariants-start
        invariant
            0 <= index <= seq.len(),
            forall|k: int| 0 <= k < index ==> max_list.len() >= #[trigger] (seq[k]).len(),
            exists|k: int| 0 <= k < index && max_list@ =~= #[trigger] (seq[k]@),
        // invariants-end
    {
        if ((seq[index]).len() > max_list.len()) {
            max_list = ...
```

**Pairwise similarities:**
- max_length_list vs max_length_list: 100.00%
- max_length_list vs min_sublist: 85.86%
- max_length_list vs min_sublist: 85.86%

---

### Group 23 (Average Similarity: 88.89%)

Functions in this group (3 total):

- **get_element_check_property** in `benches/autoverus/Misc/unverified/trigger.rs` (line 11)
- **array_append** in `benches/RustBench/invariants_removed/array_append.rs` (line 6)
- **array_append** in `benches/RustBench/ground_truth/array_append.rs` (line 6)

**Sample code from first function:**
```rust
{
    arr[i]
}
```

**Pairwise similarities:**
- get_element_check_property vs array_append: 88.89%
- get_element_check_property vs array_append: 88.89%
- array_append vs array_append: 100.00%

---

### Group 24 (Average Similarity: 88.49%)

Functions in this group (6 total):

- **array_copy** in `benches/HumanEval-RustBench/additional/array_copy.rs` (line 6)
- **array_copy** in `benches/RustBench/ground_truth/array_copy.rs` (line 6)
- **array_product** in `benches/HumanEval-RustBench/additional/array_product.rs` (line 6)
- **reverse** in `benches/HumanEval-RustBench/additional/reverse.rs` (line 5)
- **array_product** in `benches/RustBench/ground_truth/array_product.rs` (line 6)
- **reverse** in `benches/RustBench/ground_truth/reverse.rs` (line 5)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut result: Vec<i32> = Vec::new();
    let mut i = 0;
    while i < a.len()
        // invariants-start
        invariant
            0 <= i && i <= a.len(),
            result.len() == i,
            forall|j: int| 0 <= j && j < i ==> result[j] == a[j],
        // invariants-end
    {
        result.push(a[i]);
        i = i + 1;
    }
    result
    // impl-end
}
```

---

### Group 25 (Average Similarity: 88.38%)

Functions in this group (6 total):

- **sum** in `benches/HumanEval-RustBench/008-sum_product.rs` (line 4)
- **sum** in `benches/HumanEval-RustBench/004-mean_absolute_derivation.rs` (line 12)
- **sum** in `benches/HumanEval-RustBench/SubBench/008-sum_product.rs` (line 4)
- **spec_sum** in `benches/HumanEval-RustBench/not_finished_proof/072-will_it_fly.rs` (line 47)
- **product** in `benches/HumanEval-RustBench/SubBench/008-sum_product.rs` (line 9)
- **product** in `benches/HumanEval-RustBench/008-sum_product.rs` (line 9)

**Sample code from first function:**
```rust
{
    numbers.fold_left(0, |acc: int, x| acc + x)
}
```

---

### Group 26 (Average Similarity: 88.33%)

Functions in this group (8 total):

- **is_digit_sepc** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_113.rs` (line 5)
- **is_digit** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_764.rs` (line 6)
- **is_upper_case** in `benches/VerusProofSynthesisBench/MBPP/task_id_461.rs` (line 10)
- **is_digit_sepc** in `benches/VerusProofSynthesisBench/MBPP/task_id_113.rs` (line 5)
- **is_digit** in `benches/VerusProofSynthesisBench/MBPP/task_id_113.rs` (line 10)
- **is_digit** in `benches/VerusProofSynthesisBench/MBPP/task_id_764.rs` (line 6)
- **is_upper_case** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_461.rs` (line 10)
- **is_lower_case** in `benches/VerusProofSynthesisBench/MBPP/task_id_461.rs` (line 5)

**Sample code from first function:**
```rust
{
    (c as u32) >= 48 && (c as u32) <= 57
}
```

---

### Group 27 (Average Similarity: 87.72%)

Functions in this group (4 total):

- **to_uppercase** in `benches/autoverus/MBPP/unverified/task_id_624.rs` (line 15)
- **to_uppercase** in `benches/autoverus/MBPP/verified/task_id_624.rs` (line 21)
- **to_lowercase** in `benches/autoverus/MBPP/unverified/task_id_477.rs` (line 15)
- **to_lowercase** in `benches/autoverus/MBPP/verified/task_id_477.rs` (line 21)

**Sample code from first function:**
```rust
{
                shift_minus_32_spec(str1[i])
            }
```

**Pairwise similarities:**
- to_uppercase vs to_uppercase: 100.00%
- to_uppercase vs to_lowercase: 87.72%
- to_uppercase vs to_lowercase: 87.72%
- to_uppercase vs to_lowercase: 87.72%
- to_uppercase vs to_lowercase: 87.72%
- to_lowercase vs to_lowercase: 100.00%

---

### Group 28 (Average Similarity: 86.81%)

Functions in this group (12 total):

- **filter_odd_numbers** in `benches/VerusProofSynthesisBench/MBPP/task_id_426.rs` (line 5)
- **find_negative_numbers** in `benches/VerusProofSynthesisBench/MBPP/task_id_436.rs` (line 5)
- **remove_odds** in `benches/VerusProofSynthesisBench/MBPP/task_id_412.rs` (line 5)
- **find_even_numbers** in `benches/VerusProofSynthesisBench/MBPP/task_id_629.rs` (line 6)
- **remove_duplicates** in `benches/VerusProofSynthesisBench/MBPP/task_id_572.rs` (line 52)
- **filter_odd_numbers** in `benches/autoverus/MBPP/verified/task_id_426.rs` (line 19)
- **find_negative_numbers** in `benches/autoverus/MBPP/verified/task_id_436.rs` (line 13)
- **remove_odds** in `benches/autoverus/MBPP/verified/task_id_412.rs` (line 13)
- **find_even_numbers** in `benches/autoverus/MBPP/verified/task_id_629.rs` (line 13)
- **remove_duplicates** in `benches/autoverus/MBPP/verified/task_id_572.rs` (line 49)
- **find_odd_numbers** in `benches/autoverus/MBPP/verified/task_id_554.rs` (line 13)
- **find_first_odd** in `benches/VerusProofSynthesisBench/MBPP/task_id_807.rs` (line 17)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut odd_list: Vec<u32> = Vec::new();
    let input_len = arr.len();

    // assert-start
    assert(arr@.take(0int).filter(|x: u32| x % 2 != 0) == Seq::<u32>::empty());
    // assert-end
    let mut index = 0;
    while index < arr.len()
        // invariants-start
        invariant
            0 <= index <= arr.len(),
            odd_list@ == arr@.take(index as int).filter(|x: u32| x % 2 != 0),
        // invariants-end
    {
        if (arr[index] % 2 != 0) {
      ...
```

---

### Group 29 (Average Similarity: 85.60%)

Functions in this group (30 total):

- **abs** in `benches/HumanEval-RustBench/004-mean_absolute_derivation.rs` (line 25)
- **odd_or_zero** in `benches/HumanEval-RustBench/085-add.rs` (line 5)
- **max** in `benches/artifacts/dafnybench/Dafny_tmp_tmpmvs2dmry_SlowMax/verus_code.rs` (line 4)
- **compare_bool** in `benches/artifacts/dafnybench/Clover_compare/verus_code.rs` (line 5)
- **compare_int** in `benches/artifacts/dafnybench/Clover_compare/verus_code.rs` (line 15)
- **compare_nat** in `benches/artifacts/dafnybench/Clover_compare/verus_code.rs` (line 25)
- **abs_diff** in `benches/artifacts/dafnybench/Clover_has_close_elements/verus_code.rs` (line 4)
- **Max** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_Hoare/verus_code.rs` (line 5)
- **abs** in `benches/artifacts/dafnybench/Dafny_tmp_tmpmvs2dmry_examples1/verus_code.rs` (line 4)
- **Abs** in `benches/artifacts/dafnybench/Dafny_tmp_tmpmvs2dmry_examples1/verus_code.rs` (line 8)
- **Max** in `benches/artifacts/dafnybench/Dafny_tmp_tmpmvs2dmry_examples1/verus_code.rs` (line 44)
- **min** in `benches/artifacts/dafnybench/Dafny_tmp_tmpv_d3qi10_2_min/verus_code.rs` (line 5)
- **minMethod** in `benches/artifacts/dafnybench/Dafny_tmp_tmpv_d3qi10_2_min/verus_code.rs` (line 19)
- **minFunction** in `benches/artifacts/dafnybench/Dafny_tmp_tmpv_d3qi10_2_min/verus_code.rs` (line 33)
- **min** in `benches/artifacts/dafnybench/Clover_min_of_two/verus_code.rs` (line 4)
- **abs** in `benches/artifacts/dafnybench/Clover_abs/verus_code.rs` (line 4)
- **abs_spec** in `benches/HumanEval-RustBench/additional/has_close_elements.rs` (line 5)
- **abs** in `benches/HumanEval-RustBench/additional/has_close_elements.rs` (line 9)
- **abs** in `benches/HumanEval-RustBench/additional/abs.rs` (line 5)
- **abs_spec** in `benches/RustBench/preconditions_removed/has_close_elements.rs` (line 5)
- **abs** in `benches/RustBench/preconditions_removed/has_close_elements.rs` (line 9)
- **abs** in `benches/RustBench/preconditions_removed/abs.rs` (line 5)
- **abs_spec** in `benches/RustBench/invariants_removed/has_close_elements.rs` (line 5)
- **abs** in `benches/RustBench/invariants_removed/has_close_elements.rs` (line 9)
- **abs_spec** in `benches/RustBench/ground_truth/has_close_elements.rs` (line 5)
- **abs** in `benches/RustBench/ground_truth/has_close_elements.rs` (line 9)
- **abs** in `benches/RustBench/ground_truth/abs.rs` (line 5)
- **ex_saturating_sub_spec** in `benches/autoverus/interprocedural/tock/unverified/rb1.rs` (line 8)
- **ex_saturating_sub_spec** in `benches/autoverus/interprocedural/tock/verified/rb1.rs` (line 8)
- **max** in `benches/artifacts/dafnybench/Dafny_tmp_tmpj88zq5zt_2-Kontrakte_max/verus_code.rs` (line 4)

**Sample code from first function:**
```rust
{
    if n >= 0 {
        n
    } else {
        -n
    }
}
```

---

### Group 30 (Average Similarity: 84.00%)

Functions in this group (3 total):

- **inner_expr_replace_blanks_with_chars** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_230.rs` (line 5)
- **inner_expr_replace_blanks_with_chars** in `benches/VerusProofSynthesisBench/MBPP/task_id_230.rs` (line 5)
- **inner_epxr_replace_chars** in `benches/VerusProofSynthesisBench/MBPP/task_id_474.rs` (line 5)

**Sample code from first function:**
```rust
{
    if str1[i] == 32 {
        ch
    } else {
        str1[i]
    }
}
```

**Pairwise similarities:**
- inner_expr_replace_blanks_with_chars vs inner_expr_replace_blanks_with_chars: 100.00%
- inner_expr_replace_blanks_with_chars vs inner_epxr_replace_chars: 84.00%
- inner_expr_replace_blanks_with_chars vs inner_epxr_replace_chars: 84.00%

---

### Group 31 (Average Similarity: 83.55%)

Functions in this group (26 total):

- **count_uppercase_sum** in `benches/HumanEval-RustBench/066-digitSum.rs` (line 10)
- **special_filter_spec** in `benches/HumanEval-RustBench/146-specialFilter.rs` (line 75)
- **count_uppercase_recursively** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_461.rs` (line 15)
- **count_digits_recursively** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_764.rs` (line 11)
- **count_boolean** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_105.rs` (line 5)
- **count_frequency_rcr** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_602.rs` (line 5)
- **sum_negative_to** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_133.rs` (line 6)
- **count_frequency_rcr** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_572.rs` (line 5)
- **count_uppercase_recursively** in `benches/VerusProofSynthesisBench/MBPP/task_id_461.rs` (line 15)
- **count_digits_recursively** in `benches/VerusProofSynthesisBench/MBPP/task_id_764.rs` (line 11)
- **count_boolean** in `benches/VerusProofSynthesisBench/MBPP/task_id_105.rs` (line 5)
- **count_frequency_rcr** in `benches/VerusProofSynthesisBench/MBPP/task_id_602.rs` (line 5)
- **sum_negative_to** in `benches/VerusProofSynthesisBench/MBPP/task_id_133.rs` (line 6)
- **count_frequency_rcr** in `benches/VerusProofSynthesisBench/MBPP/task_id_572.rs` (line 5)
- **count_uppercase_recursively** in `benches/autoverus/MBPP/unverified/task_id_461.rs` (line 15)
- **count_digits_recursively** in `benches/autoverus/MBPP/unverified/task_id_764.rs` (line 11)
- **count_boolean** in `benches/autoverus/MBPP/unverified/task_id_105.rs` (line 7)
- **count_frequency_rcr** in `benches/autoverus/MBPP/unverified/task_id_602.rs` (line 7)
- **sum_negative_to** in `benches/autoverus/MBPP/unverified/task_id_133.rs` (line 7)
- **count_frequency_rcr** in `benches/autoverus/MBPP/unverified/task_id_572.rs` (line 7)
- **count_uppercase_recursively** in `benches/autoverus/MBPP/verified/task_id_461.rs` (line 21)
- **count_digits_recursively** in `benches/autoverus/MBPP/verified/task_id_764.rs` (line 18)
- **count_boolean** in `benches/autoverus/MBPP/verified/task_id_105.rs` (line 13)
- **count_frequency_rcr** in `benches/autoverus/MBPP/verified/task_id_602.rs` (line 13)
- **sum_negative_to** in `benches/autoverus/MBPP/verified/task_id_133.rs` (line 16)
- **count_frequency_rcr** in `benches/autoverus/MBPP/verified/task_id_572.rs` (line 13)

**Sample code from first function:**
```rust
{
    if seq.len() == 0 {
        0
    } else {
        count_uppercase_sum(seq.drop_last()) + if is_upper_case(seq.last()) {
            seq.last() as int
        } else {
            0 as int
        }
    }
}
```

---

### Group 32 (Average Similarity: 83.14%)

Functions in this group (16 total):

- **array_copy** in `benches/RustBench/invariants_removed/array_copy.rs` (line 6)
- **reverse** in `benches/RustBench/invariants_removed/reverse.rs` (line 5)
- **insert_before_each** in `benches/autoverus/MBPP/unverified/task_id_251.rs` (line 7)
- **square_nums** in `benches/autoverus/MBPP/unverified/task_id_8.rs` (line 7)
- **array_product** in `benches/RustBench/invariants_removed/array_product.rs` (line 6)
- **find_negative_numbers** in `benches/autoverus/MBPP/unverified/task_id_436.rs` (line 7)
- **cube_element** in `benches/autoverus/MBPP/unverified/task_id_447.rs` (line 7)
- **filter_odd_numbers** in `benches/autoverus/MBPP/unverified/task_id_426.rs` (line 7)
- **remove_elements** in `benches/autoverus/MBPP/unverified/task_id_161.rs` (line 21)
- **remove_odds** in `benches/autoverus/MBPP/unverified/task_id_412.rs` (line 7)
- **find_even_numbers** in `benches/autoverus/MBPP/unverified/task_id_629.rs` (line 7)
- **find_odd_numbers** in `benches/autoverus/MBPP/unverified/task_id_554.rs` (line 7)
- **remove_duplicates** in `benches/autoverus/MBPP/unverified/task_id_572.rs` (line 36)
- **remove_chars** in `benches/autoverus/MBPP/unverified/task_id_18.rs` (line 21)
- **intersection** in `benches/autoverus/MBPP/unverified/task_id_249.rs` (line 21)
- **shared_elements** in `benches/autoverus/MBPP/unverified/task_id_2.rs` (line 21)

**Sample code from first function:**
```rust
{
    let mut result: Vec<i32> = Vec::new();
    let mut i = 0;
    while i < a.len()
    {
        result.push(a[i]);
        i = i + 1;
    }
    result
}
```

---

### Group 33 (Average Similarity: 82.91%)

Functions in this group (4 total):

- **product** in `benches/autoverus/CloverBench/unverified/array_product_strong.rs` (line 6)
- **copy** in `benches/autoverus/CloverBench/unverified/array_copy_strong.rs` (line 6)
- **append** in `benches/autoverus/CloverBench/unverified/array_append_strong.rs` (line 6)
- **concat** in `benches/autoverus/CloverBench/unverified/array_concat_strong.rs` (line 6)

**Sample code from first function:**
```rust
{
    let mut c = Vec::with_capacity(a.len());
    let mut n: usize = 0;
    let len: usize = a.len();
    while n != len {
        let product: u32 = a[n] * b[n];
        c.push(product);
        n = n + 1;
    }
    c
}
```

**Pairwise similarities:**
- product vs copy: 84.89%
- product vs append: 80.24%
- product vs concat: 71.83%
- copy vs append: 89.80%
- copy vs concat: 72.16%
- append vs concat: 73.51%

---

### Group 34 (Average Similarity: 82.60%)

Functions in this group (39 total):

- **is_even** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_804.rs` (line 5)
- **is_even** in `benches/VerusProofSynthesisBench/MBPP/task_id_804.rs` (line 5)
- **is_even** in `benches/autoverus/MBPP/unverified/task_id_804.rs` (line 6)
- **is_even** in `benches/autoverus/MBPP/verified/task_id_804.rs` (line 11)
- **is_odd** in `benches/HumanEval-RustBench/146-specialFilter.rs` (line 49)
- **is_even_spec** in `benches/artifacts/dafnybench/Clover_even_list/verus_code.rs` (line 4)
- **is_odd** in `benches/artifacts/dafnybench/FMSE-2022-2023_tmp_tmp6_x_ba46_Lab10_Lab10/verus_code.rs` (line 5)
- **odd** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_partitionOddEven/verus_code.rs` (line 5)
- **even** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_partitionOddEven/verus_code.rs` (line 6)
- **odd_exec** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_partitionOddEven/verus_code.rs` (line 9)
- **even_exec** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_partitionOddEven/verus_code.rs` (line 15)
- **isEven** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session6Exercises_ExerciseCountEven/verus_code.rs` (line 10)
- **is_divisible** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_605.rs` (line 5)
- **is_divisible** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_3.rs` (line 6)
- **is_divisible** in `benches/VerusProofSynthesisBench/MBPP/task_id_605.rs` (line 5)
- **is_divisible** in `benches/VerusProofSynthesisBench/MBPP/task_id_3.rs` (line 6)
- **is_divisible** in `benches/autoverus/MBPP/unverified/task_id_605.rs` (line 7)
- **is_divisible** in `benches/autoverus/MBPP/unverified/task_id_3.rs` (line 7)
- **is_divisible** in `benches/autoverus/MBPP/verified/task_id_605.rs` (line 18)
- **is_divisible** in `benches/autoverus/MBPP/verified/task_id_3.rs` (line 18)
- **extract_last_digit_spec** in `benches/HumanEval-RustBench/146-specialFilter.rs` (line 33)
- **extract_last_digit** in `benches/HumanEval-RustBench/146-specialFilter.rs` (line 38)
- **add_one** in `benches/HumanEval-RustBench/additional/integer_square_root.rs` (line 6)
- **add_one** in `benches/RustBench/invariants_removed/integer_square_root.rs` (line 6)
- **add_one** in `benches/RustBench/ground_truth/integer_square_root.rs` (line 6)
- **index** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Index/verus_code.rs` (line 4)
- **add** in `benches/HumanEval-RustBench/additional/cubes.rs` (line 6)
- **add** in `benches/RustBench/invariants_removed/cubes.rs` (line 6)
- **square** in `benches/RustBench/invariants_removed/integer_square_root.rs` (line 14)
- **add** in `benches/RustBench/ground_truth/cubes.rs` (line 6)
- **square** in `benches/RustBench/ground_truth/integer_square_root.rs` (line 14)
- **square** in `benches/HumanEval-RustBench/additional/integer_square_root.rs` (line 14)
- **compute_avg** in `benches/artifacts/dafnybench/Clover_avg/verus_code.rs` (line 4)
- **Average** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Ghost/verus_code.rs` (line 4)
- **average** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Function/verus_code.rs` (line 4)
- **even** in `benches/HumanEval-RustBench/005-intersperse.rs` (line 17)
- **calc_power** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_week5_ComputePower/verus_code.rs` (line 10)
- **triple** in `benches/artifacts/dafnybench/Clover_triple/verus_code.rs` (line 4)
- **Mid_spec** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_F1a/verus_code.rs` (line 30)

**Sample code from first function:**
```rust
{
    (n % 2) == 0
}
```

---

### Group 35 (Average Similarity: 82.11%)

Functions in this group (44 total):

- **is_sorted** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_InsertionSortSeq/verus_code.rs` (line 9)
- **seq_equal_prefix** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_longestPrefix/verus_code.rs` (line 6)
- **pivot** in `benches/artifacts/dafnybench/CS494-final-project_tmp_tmp7nof55uq_bubblesort/verus_code.rs` (line 12)
- **sorted_seg** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session8Exercises_ExerciseInsertionSort/verus_code.rs` (line 4)
- **strict_sorted** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExerciseContained/verus_code.rs` (line 5)
- **ascending** in `benches/artifacts/dafnybench/Dafny-Practice_tmp_tmphnmt4ovh_BST/verus_code.rs` (line 50)
- **no_duplicates** in `benches/artifacts/dafnybench/Dafny-Practice_tmp_tmphnmt4ovh_BST/verus_code.rs` (line 54)
- **sorted_seg** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseSelSort/verus_code.rs` (line 5)
- **sorted_seg** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseBubbleSort/verus_code.rs` (line 5)
- **sorted_between** in `benches/artifacts/dafnybench/Dafny-programs_tmp_tmpnso9eu7u_Algorithms + sorting_bubble-sort/verus_code.rs` (line 6)
- **sorted_seq** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 94)
- **sorted_eq** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 106)
- **less_than** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 110)
- **greater_than** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 114)
- **greater_equal_than** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 118)
- **upper_bound** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_normal_data_completion_MaxPerdV2/verus_code.rs` (line 8)
- **strict_sorted** in `benches/RustBench/WIP/WIP: mcontained.rs` (line 7)
- **sorted** in `benches/artifacts/dafnybench/CS494-final-project_tmp_tmp7nof55uq_bubblesort/verus_code.rs` (line 5)
- **positive** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExerciseFirstNegative/verus_code.rs` (line 5)
- **positive** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session2Exercises_ExercisePositive/verus_code.rs` (line 5)
- **positive** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseSeparate/verus_code.rs` (line 10)
- **sorted** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 98)
- **all_equal** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExerciseAllEqual/verus_code.rs` (line 5)
- **sorted** in `benches/artifacts/dafnybench/630-dafny_tmp_tmpz2kokaiq_Solution/verus_code.rs` (line 4)
- **sorted** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_RawSort/verus_code.rs` (line 14)
- **sorted** in `benches/artifacts/dafnybench/AssertivePrograming_tmp_tmpwf43uz0e_MergeSort/verus_code.rs` (line 7)
- **sorted** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseBinarySearch/verus_code.rs` (line 4)
- **strict_negative** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseSeparate/verus_code.rs` (line 4)
- **sorted_between** in `benches/VerusProofSynthesisBench/Misc/bubble_v1.rs` (line 5)
- **sorted_between** in `benches/VerusProofSynthesisBench/Misc/bubble_v2.rs` (line 4)
- **sorted_between** in `benches/autoverus/Misc/unverified/bubble.rs` (line 5)
- **sorted_between** in `benches/autoverus/Misc/verified/bubble_v1.rs` (line 5)
- **sorted_between** in `benches/autoverus/Misc/verified/bubble_v2.rs` (line 5)
- **sorted** in `benches/artifacts/dafnybench/Dafny-demo_tmp_tmpkgr_dvdi_Dafny_BinarySearch/verus_code.rs` (line 4)
- **distinct** in `benches/artifacts/dafnybench/BPTree-verif_tmp_tmpq1z6xm1d_Utils/verus_code.rs` (line 102)
- **in_array** in `benches/HumanEval-RustBench/additional/remove_elements.rs` (line 5)
- **in_array** in `benches/HumanEval-RustBench/additional/remove_duplicates.rs` (line 5)
- **in_array** in `benches/RustBench/preconditions_removed/remove_duplicates.rs` (line 5)
- **in_array** in `benches/RustBench/invariants_removed/remove_elements.rs` (line 5)
- **in_array** in `benches/RustBench/invariants_removed/remove_duplicates.rs` (line 5)
- **in_array** in `benches/RustBench/ground_truth/remove_elements.rs` (line 5)
- **in_array** in `benches/RustBench/ground_truth/remove_duplicates.rs` (line 5)
- **in_prefix** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExerciseContained/verus_code.rs` (line 10)
- **contains** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_normal_data_completion_MaxPerdV2/verus_code.rs` (line 4)

**Sample code from first function:**
```rust
{
        forall|p: int, q: int| 0 <= p < q < s.len() ==> s[p] <= s[q]
    }
```

---

### Group 36 (Average Similarity: 81.52%)

Functions in this group (6 total):

- **max_array** in `benches/RustBench/invariants_removed/max_array.rs` (line 5)
- **find_max** in `benches/autoverus/Misc/unverified/findmax.rs` (line 6)
- **smallest_num** in `benches/autoverus/MBPP/unverified/task_id_62.rs` (line 7)
- **min_sublist** in `benches/autoverus/MBPP/unverified/task_id_457.rs` (line 7)
- **smallest_list_length** in `benches/autoverus/MBPP/unverified/task_id_95.rs` (line 7)
- **max_length_list** in `benches/autoverus/MBPP/unverified/task_id_290.rs` (line 7)

**Sample code from first function:**
```rust
{
    let mut idx = 0;

    let mut i = 1;
    while i < nums.len()
    {
        if nums[i] > nums[idx] {
            idx = i;
        }
        i = i + 1;
    }
    idx
}
```

---

### Group 37 (Average Similarity: 81.35%)

Functions in this group (89 total):

- **test** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_LinearSearch/verus_code.rs` (line 5)
- **linear_search** in `benches/artifacts/dafnybench/Clover_linear_search1/verus_code.rs` (line 4)
- **linear_search0** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_Week4__LinearSearch/verus_code.rs` (line 5)
- **linear_search1** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_Week4__LinearSearch/verus_code.rs` (line 26)
- **mfirstCero** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExercisefirstZero/verus_code.rs` (line 4)
- **linear_search** in `benches/artifacts/dafnybench/Clover_linear_search2/verus_code.rs` (line 4)
- **in_array_exec** in `benches/HumanEval-RustBench/additional/remove_elements.rs` (line 9)
- **in_array_exec** in `benches/HumanEval-RustBench/additional/remove_duplicates.rs` (line 9)
- **linear_search** in `benches/autoverus/CloverBench/verified/linear_search2.rs` (line 7)
- **in_array_exec** in `benches/RustBench/preconditions_removed/remove_duplicates.rs` (line 9)
- **in_array_exec** in `benches/RustBench/invariants_removed/remove_duplicates.rs` (line 9)
- **in_array_exec** in `benches/RustBench/ground_truth/remove_elements.rs` (line 9)
- **in_array_exec** in `benches/RustBench/ground_truth/remove_duplicates.rs` (line 9)
- **linear_search1_int** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_week4_tute_ex4/verus_code.rs` (line 30)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_414.rs` (line 5)
- **contains** in `benches/autoverus/MBPP/verified/task_id_414.rs` (line 13)
- **m_all_equal2** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExerciseAllEqual/verus_code.rs` (line 46)
- **minimum** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_Minimum/verus_code.rs` (line 4)
- **is_greater** in `benches/VerusProofSynthesisBench/MBPP/task_id_433.rs` (line 5)
- **is_greater** in `benches/autoverus/MBPP/verified/task_id_433.rs` (line 13)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_2.rs` (line 5)
- **is_product_even** in `benches/VerusProofSynthesisBench/MBPP/task_id_804.rs` (line 10)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_161.rs` (line 21)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_18.rs` (line 22)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_249.rs` (line 5)
- **all_elements_equals** in `benches/VerusProofSynthesisBench/MBPP/task_id_284.rs` (line 5)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_769.rs` (line 21)
- **contains_z** in `benches/VerusProofSynthesisBench/MBPP/task_id_454.rs` (line 5)
- **contains_k** in `benches/VerusProofSynthesisBench/MBPP/task_id_808.rs` (line 6)
- **contains** in `benches/VerusProofSynthesisBench/MBPP/task_id_579.rs` (line 21)
- **is_non_prime** in `benches/HumanEval-RustBench/additional/is_non_prime.rs` (line 6)
- **contains** in `benches/autoverus/MBPP/verified/task_id_2.rs` (line 22)
- **contains** in `benches/autoverus/MBPP/verified/task_id_161.rs` (line 31)
- **contains** in `benches/autoverus/MBPP/verified/task_id_18.rs` (line 22)
- **contains** in `benches/autoverus/MBPP/verified/task_id_249.rs` (line 22)
- **contains** in `benches/autoverus/MBPP/verified/task_id_769.rs` (line 28)
- **contains_k** in `benches/autoverus/MBPP/verified/task_id_808.rs` (line 13)
- **contains** in `benches/autoverus/MBPP/verified/task_id_579.rs` (line 31)
- **is_non_prime** in `benches/RustBench/preconditions_removed/is_non_prime.rs` (line 6)
- **is_non_prime** in `benches/RustBench/ground_truth/is_non_prime.rs` (line 6)
- **is_product_even** in `benches/autoverus/MBPP/verified/task_id_804.rs` (line 15)
- **all_elements_equals** in `benches/autoverus/MBPP/verified/task_id_284.rs` (line 13)
- **contains_z** in `benches/autoverus/MBPP/verified/task_id_454.rs` (line 13)
- **any_value_exists** in `benches/VerusProofSynthesisBench/MBPP/task_id_414.rs` (line 29)
- **is_sorted** in `benches/VerusProofSynthesisBench/MBPP/task_id_567.rs` (line 5)
- **is_smaller** in `benches/VerusProofSynthesisBench/MBPP/task_id_809.rs` (line 6)
- **any_value_exists** in `benches/autoverus/MBPP/verified/task_id_414.rs` (line 31)
- **is_integer** in `benches/VerusProofSynthesisBench/MBPP/task_id_113.rs` (line 19)
- **is_integer** in `benches/autoverus/MBPP/verified/task_id_113.rs` (line 24)
- **is_sorted** in `benches/autoverus/MBPP/verified/task_id_567.rs` (line 13)
- **is_product_even** in `benches/autoverus/MBPP/unverified/task_id_804.rs` (line 10)
- **contains_k** in `benches/autoverus/MBPP/unverified/task_id_808.rs` (line 7)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_2.rs` (line 7)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_414.rs` (line 7)
- **any_value_exists** in `benches/autoverus/MBPP/unverified/task_id_414.rs` (line 21)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_161.rs` (line 7)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_18.rs` (line 7)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_249.rs` (line 7)
- **all_elements_equals** in `benches/autoverus/MBPP/unverified/task_id_284.rs` (line 7)
- **is_non_prime** in `benches/autoverus/MBPP/unverified/task_id_3.rs` (line 11)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_769.rs` (line 7)
- **is_integer** in `benches/autoverus/MBPP/unverified/task_id_113.rs` (line 18)
- **contains_z** in `benches/autoverus/MBPP/unverified/task_id_454.rs` (line 7)
- **is_sorted** in `benches/autoverus/MBPP/unverified/task_id_567.rs` (line 7)
- **contains_consecutive_numbers** in `benches/autoverus/MBPP/unverified/task_id_472.rs` (line 7)
- **count_frequency** in `benches/autoverus/MBPP/unverified/task_id_602.rs` (line 21)
- **is_smaller** in `benches/autoverus/MBPP/unverified/task_id_809.rs` (line 7)
- **is_even_at_even_index** in `benches/autoverus/MBPP/unverified/task_id_790.rs` (line 7)
- **count_frequency** in `benches/autoverus/MBPP/unverified/task_id_572.rs` (line 21)
- **all_sequence_equal_length** in `benches/autoverus/MBPP/unverified/task_id_70.rs` (line 7)
- **is_odd_at_odd_index** in `benches/autoverus/MBPP/unverified/task_id_775.rs` (line 7)
- **contains** in `benches/autoverus/MBPP/unverified/task_id_579.rs` (line 7)
- **in_array_exec** in `benches/RustBench/invariants_removed/remove_elements.rs` (line 9)
- **is_non_prime** in `benches/RustBench/invariants_removed/is_non_prime.rs` (line 6)
- **linear_search** in `benches/autoverus/CloverBench/unverified/linear_search2.rs` (line 7)
- **sub_array_at_index** in `benches/autoverus/MBPP/unverified/task_id_576.rs` (line 7)
- **is_greater** in `benches/autoverus/MBPP/unverified/task_id_433.rs` (line 7)
- **count_true** in `benches/autoverus/MBPP/unverified/task_id_105.rs` (line 21)
- **is_sub_list_at_index** in `benches/autoverus/MBPP/unverified/task_id_69.rs` (line 7)
- **has_only_one_distinct_element** in `benches/autoverus/MBPP/unverified/task_id_760.rs` (line 7)
- **prime_num** in `benches/autoverus/MBPP/unverified/task_id_605.rs` (line 11)
- **count_uppercase** in `benches/autoverus/MBPP/unverified/task_id_461.rs` (line 29)
- **count_digits** in `benches/autoverus/MBPP/unverified/task_id_764.rs` (line 25)
- **sum** in `benches/autoverus/MBPP/unverified/task_id_798.rs` (line 17)
- **sum_negatives** in `benches/autoverus/MBPP/unverified/task_id_133.rs` (line 21)
- **all_characters_same** in `benches/autoverus/MBPP/unverified/task_id_741.rs` (line 7)
- **choose_odd** in `benches/autoverus/Misc/unverified/choose_odd.rs` (line 5)
- **count_identical_position** in `benches/autoverus/MBPP/unverified/task_id_142.rs` (line 22)
- **sum_range_list** in `benches/autoverus/MBPP/unverified/task_id_170.rs` (line 17)

**Sample code from first function:**
```rust
{
        let mut n: usize = 0;
        while n != a.len()
            invariant 
                n <= a.len(),
                forall|i: int| 0 <= i < n ==> !p.spec_test(a[i])
            decreases a.len() - n
        {
            if p.test(&a[n]) {
                return n;
            }
            n = n + 1;
        }
        n
    }
```

---

### Group 38 (Average Similarity: 80.98%)

Functions in this group (5 total):

- **spec_prime** in `benches/HumanEval-RustBench/075-is_multiply_prime.rs` (line 6)
- **spec_prime_helper** in `benches/HumanEval-RustBench/059-largest-prime-factor.rs` (line 4)
- **prime** in `benches/artifacts/dafnybench/DafnyPrograms_tmp_tmp74_f9k_c_prime-database/verus_code.rs` (line 5)
- **is_prime_pred** in `benches/HumanEval-RustBench/additional/largest_prime_factor.rs` (line 37)
- **is_prime_pred** in `benches/RustBench/ground_truth/largest_prime_factor.rs` (line 29)

**Sample code from first function:**
```rust
{
    p > 1 && forall|k: int| 1 < k < p ==> #[trigger] (p % k) != 0
}
```

**Pairwise similarities:**
- spec_prime vs spec_prime_helper: 72.31%
- spec_prime vs prime: 85.93%
- spec_prime vs is_prime_pred: 82.17%
- spec_prime vs is_prime_pred: 82.17%
- spec_prime_helper vs prime: 69.63%
- spec_prime_helper vs is_prime_pred: 82.17%
- spec_prime_helper vs is_prime_pred: 82.17%
- prime vs is_prime_pred: 76.12%
- prime vs is_prime_pred: 76.12%
- is_prime_pred vs is_prime_pred: 100.00%

---

### Group 39 (Average Similarity: 80.76%)

Functions in this group (16 total):

- **spec_sum_to_n** in `benches/HumanEval-RustBench/060-sum_to_n.rs` (line 5)
- **power** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_week5_ComputePower/verus_code.rs` (line 4)
- **power** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_AI_agent_verify_examples_ComputePower/verus_code.rs` (line 4)
- **fact** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_fact/verus_code.rs` (line 5)
- **factAcc** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_fact/verus_code.rs` (line 12)
- **power** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_Power/verus_code.rs` (line 14)
- **power** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_AI_agent_validation_examples/verus_code.rs` (line 2)
- **triangle** in `benches/VerusProofSynthesisBench/Misc/tail_triangle.rs` (line 5)
- **triangle** in `benches/autoverus/Misc/unverified/tail_triangle.rs` (line 9)
- **triangle** in `benches/autoverus/Misc/verified/tail_triangle.rs` (line 9)
- **sum_ints** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_SumIntsLoop/verus_code.rs` (line 4)
- **arith_sum_int** in `benches/autoverus/Misc/unverified/sum.rs` (line 8)
- **arith_sum_int** in `benches/autoverus/Misc/verified/sum.rs` (line 8)
- **power** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_ComputePower/verus_code.rs` (line 4)
- **sub1** in `benches/artifacts/dafnybench/DafnyExercises_tmp_tmpd6qyevja_QuickExercises_testing2/verus_code.rs` (line 173)
- **modp_rec** in `benches/HumanEval-RustBench/049-modp.rs` (line 5)

**Sample code from first function:**
```rust
{
    if (n == 0) {
        0
    } else {
        n + spec_sum_to_n((n - 1) as nat)
    }
}
```

---

### Group 40 (Average Similarity: 80.01%)

Functions in this group (30 total):

- **is_paren_char** in `benches/HumanEval-RustBench/001-separate-paren-groups.rs` (line 23)
- **is_upper_case** in `benches/HumanEval-RustBench/066-digitSum.rs` (line 5)
- **is_upper_case** in `benches/HumanEval-RustBench/027-flip_case.rs` (line 6)
- **is_lower_case** in `benches/HumanEval-RustBench/027-flip_case.rs` (line 11)
- **is_upper_case** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_477.rs` (line 5)
- **is_upper_case** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 5)
- **is_lower_case** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 15)
- **is_lower_case** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_624.rs` (line 5)
- **is_upper_case** in `benches/VerusProofSynthesisBench/MBPP/task_id_477.rs` (line 5)
- **is_upper_case** in `benches/VerusProofSynthesisBench/MBPP/task_id_557.rs` (line 5)
- **is_lower_case** in `benches/VerusProofSynthesisBench/MBPP/task_id_557.rs` (line 15)
- **is_lower_case** in `benches/VerusProofSynthesisBench/MBPP/task_id_624.rs` (line 5)
- **is_lower_case** in `benches/autoverus/MBPP/unverified/task_id_461.rs` (line 7)
- **is_digit_spec** in `benches/autoverus/MBPP/unverified/task_id_113.rs` (line 7)
- **is_digit** in `benches/autoverus/MBPP/unverified/task_id_113.rs` (line 11)
- **is_digit** in `benches/autoverus/MBPP/unverified/task_id_764.rs` (line 7)
- **is_lower_case** in `benches/autoverus/MBPP/unverified/task_id_557.rs` (line 14)
- **is_lower_case** in `benches/autoverus/MBPP/unverified/task_id_624.rs` (line 7)
- **is_lower_case** in `benches/autoverus/MBPP/verified/task_id_461.rs` (line 13)
- **is_digit_sepc** in `benches/autoverus/MBPP/verified/task_id_113.rs` (line 13)
- **is_digit** in `benches/autoverus/MBPP/verified/task_id_113.rs` (line 17)
- **is_digit** in `benches/autoverus/MBPP/verified/task_id_764.rs` (line 14)
- **is_lower_case** in `benches/autoverus/MBPP/verified/task_id_557.rs` (line 20)
- **is_lower_case** in `benches/autoverus/MBPP/verified/task_id_624.rs` (line 13)
- **is_upper_case** in `benches/autoverus/MBPP/unverified/task_id_461.rs` (line 11)
- **is_upper_case** in `benches/autoverus/MBPP/unverified/task_id_477.rs` (line 7)
- **is_upper_case** in `benches/autoverus/MBPP/unverified/task_id_557.rs` (line 6)
- **is_upper_case** in `benches/autoverus/MBPP/verified/task_id_461.rs` (line 17)
- **is_upper_case** in `benches/autoverus/MBPP/verified/task_id_477.rs` (line 13)
- **is_upper_case** in `benches/autoverus/MBPP/verified/task_id_557.rs` (line 12)

**Sample code from first function:**
```rust
{
    c == '(' || c == ')'
}
```

---

### Group 41 (Average Similarity: 80.00%)

Functions in this group (2 total):

- **get_xs** in `benches/artifacts/dafnybench/CS5232_Project_tmp_tmpai_cfrng_test/verus_code.rs` (line 83)
- **get_size** in `benches/artifacts/dafnybench/DafnyExercises_tmp_tmpd6qyevja_QuickExercises_testing2/verus_code.rs` (line 96)

**Sample code from first function:**
```rust
{
            &self.xs
        }
```

**Pairwise similarities:**
- get_xs vs get_size: 80.00%

---

### Group 42 (Average Similarity: 79.96%)

Functions in this group (802 total):

- **array_facts** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session5Exercises_ExerciseSumElems/verus_code.rs` (line 95)
- **main** in `benches/HumanEval-RustBench/042-incr-list.rs` (line 34)
- **main** in `benches/HumanEval-RustBench/052-below-threshold.rs` (line 27)
- **main** in `benches/HumanEval-RustBench/082-prime_length.rs` (line 46)
- **main** in `benches/HumanEval-RustBench/035-max-element.rs` (line 34)
- **main** in `benches/HumanEval-RustBench/037-sort_even.rs` (line 190)
- **main** in `benches/HumanEval-RustBench/018-how_many_times.rs` (line 170)
- **main** in `benches/HumanEval-RustBench/073-smallest_change.rs` (line 62)
- **main** in `benches/HumanEval-RustBench/054-same-chars.rs` (line 112)
- **main** in `benches/HumanEval-RustBench/056-correct_bracketing.rs` (line 71)
- **main** in `benches/HumanEval-RustBench/025-factorize.rs` (line 456)
- **main** in `benches/HumanEval-RustBench/048-is-palindrome.rs` (line 30)
- **main** in `benches/HumanEval-RustBench/011-string_xor.rs` (line 59)
- **main** in `benches/HumanEval-RustBench/053-add.rs` (line 17)
- **main** in `benches/HumanEval-RustBench/009-rolling_max.rs` (line 48)
- **main** in `benches/HumanEval-RustBench/070-strange_sort_list.rs` (line 193)
- **main** in `benches/HumanEval-RustBench/008-sum_product.rs` (line 75)
- **main** in `benches/HumanEval-RustBench/139-special_factorial.rs` (line 160)
- **main** in `benches/HumanEval-RustBench/049-modp.rs` (line 59)
- **main** in `benches/HumanEval-RustBench/061-correct_bracketing.rs` (line 68)
- **main** in `benches/HumanEval-RustBench/087-get_row.rs` (line 192)
- **main** in `benches/HumanEval-RustBench/014-all_prefixes.rs` (line 70)
- **main** in `benches/HumanEval-RustBench/015-string_sequence.rs` (line 192)
- **main** in `benches/HumanEval-RustBench/004-mean_absolute_derivation.rs` (line 446)
- **main** in `benches/HumanEval-RustBench/030-get-positive.rs` (line 35)
- **main** in `benches/HumanEval-RustBench/085-add.rs` (line 67)
- **main** in `benches/HumanEval-RustBench/034-unique.rs` (line 230)
- **main** in `benches/HumanEval-RustBench/068-pluck.rs` (line 63)
- **main** in `benches/HumanEval-RustBench/001-separate-paren-groups.rs` (line 192)
- **main** in `benches/HumanEval-RustBench/026-remove_duplicates.rs` (line 96)
- **main** in `benches/HumanEval-RustBench/057-monotonic.rs` (line 43)
- **main** in `benches/HumanEval-RustBench/003-below_zero.rs` (line 101)
- **main** in `benches/HumanEval-RustBench/062-derivative.rs` (line 43)
- **main** in `benches/HumanEval-RustBench/000-has_close_elements.rs` (line 69)
- **main** in `benches/HumanEval-RustBench/024-largest-divisor.rs` (line 125)
- **main** in `benches/HumanEval-RustBench/080-is_happy.rs` (line 59)
- **main** in `benches/HumanEval-RustBench/005-intersperse.rs` (line 134)
- **main** in `benches/HumanEval-RustBench/075-is_multiply_prime.rs` (line 149)
- **main** in `benches/HumanEval-RustBench/136-largest_smallest_integers.rs` (line 52)
- **main** in `benches/HumanEval-RustBench/055-fib.rs` (line 88)
- **main** in `benches/HumanEval-RustBench/066-digitSum.rs` (line 68)
- **main** in `benches/HumanEval-RustBench/012-longest.rs` (line 53)
- **main** in `benches/HumanEval-RustBench/027-flip_case.rs` (line 71)
- **main** in `benches/HumanEval-RustBench/023-strlen.rs` (line 17)
- **main** in `benches/HumanEval-RustBench/051-remove_vowels.rs` (line 58)
- **main** in `benches/HumanEval-RustBench/045-triangle_area.rs` (line 30)
- **main** in `benches/HumanEval-RustBench/060-sum_to_n.rs` (line 42)
- **main** in `benches/HumanEval-RustBench/063-fibfib.rs` (line 37)
- **main** in `benches/HumanEval-RustBench/043-pairs-sum-to-zero.rs` (line 51)
- **main** in `benches/HumanEval-RustBench/146-specialFilter.rs` (line 125)
- **main** in `benches/HumanEval-RustBench/064-vowel_count.rs` (line 74)
- **main** in `benches/HumanEval-RustBench/050-encode_shift.rs` (line 134)
- **main** in `benches/HumanEval-RustBench/059-largest-prime-factor.rs` (line 80)
- **main** in `benches/HumanEval-RustBench/033-sort_third.rs` (line 151)
- **main** in `benches/HumanEval-RustBench/007-filter_by_substring.rs` (line 110)
- **main** in `benches/artifacts/dafnybench/Clover_linear_search3/verus_code.rs` (line 29)
- **main** in `benches/artifacts/dafnybench/Dafny_Programs_tmp_tmp99966ew4_binary_search/verus_code.rs` (line 39)
- **main** in `benches/artifacts/dafnybench/Clover_all_digits/verus_code.rs` (line 33)
- **main** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week8_12_a3_search_findPositionOfIndex/verus_code.rs` (line 58)
- **main** in `benches/artifacts/dafnybench/Clover_avg/verus_code.rs` (line 12)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_38/verus_code.rs` (line 33)
- **main** in `benches/artifacts/dafnybench/Dafny-VMC_tmp_tmpzgqv0i1u_src_Math_Exponential/verus_code.rs` (line 108)
- **main** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_week5_ComputePower/verus_code.rs` (line 34)
- **main** in `benches/artifacts/dafnybench/Correctness_tmp_tmpwqvg5q_4_HoareLogic_exam/verus_code.rs` (line 108)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session2Exercises_ExerciseSquare_root/verus_code.rs` (line 83)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_InsertionSortSeq/verus_code.rs` (line 53)
- **main** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_longestPrefix/verus_code.rs` (line 50)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_error_data_completion_11/verus_code.rs` (line 28)
- **main** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_week4_tute_ex4/verus_code.rs` (line 114)
- **main** in `benches/artifacts/dafnybench/Clover_compare/verus_code.rs` (line 35)
- **main** in `benches/artifacts/dafnybench/Correctness_tmp_tmpwqvg5q_4_Sorting_Tangent/verus_code.rs` (line 90)
- **main** in `benches/artifacts/dafnybench/703FinalProject_tmp_tmpr_10rn4z_gaussian/verus_code.rs` (line 60)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_error_data_completion_06_n/verus_code.rs` (line 49)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_11/verus_code.rs` (line 29)
- **main** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_sqrt/verus_code.rs` (line 51)
- **main** in `benches/artifacts/dafnybench/Clover_selectionsort/verus_code.rs` (line 52)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmpmvs2dmry_examples2/verus_code.rs` (line 90)
- **main** in `benches/artifacts/dafnybench/CS494-final-project_tmp_tmp7nof55uq_bubblesort/verus_code.rs` (line 61)
- **main** in `benches/artifacts/dafnybench/Clover_find/verus_code.rs` (line 28)
- **main** in `benches/artifacts/dafnybench/Clover_even_list/verus_code.rs` (line 50)
- **main** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week1_7_A2_Q1_trimmed copy - 副本/verus_code.rs` (line 137)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_Search1000/verus_code.rs` (line 91)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session8Exercises_ExerciseInsertionSort/verus_code.rs` (line 46)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_error_data_real_error_IsEven_success_1/verus_code.rs` (line 38)
- **main** in `benches/artifacts/dafnybench/Clover_binary_search/verus_code.rs` (line 37)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Ghost/verus_code.rs` (line 95)
- **m1** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_Hoare/verus_code.rs` (line 21)
- **main** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_Hoare/verus_code.rs` (line 79)
- **main** in `benches/artifacts/dafnybench/Correctness_tmp_tmpwqvg5q_4_MethodCalls_q1/verus_code.rs` (line 164)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmpmvs2dmry_examples1/verus_code.rs` (line 58)
- **main** in `benches/artifacts/dafnybench/Clover_triple/verus_code.rs` (line 12)
- **main** in `benches/artifacts/dafnybench/Clover_online_max/verus_code.rs` (line 60)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_15/verus_code.rs` (line 31)
- **main** in `benches/artifacts/dafnybench/CS5232_Project_tmp_tmpai_cfrng_LFUSimple/verus_code.rs` (line 87)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Triple/verus_code.rs` (line 60)
- **main** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_partitionOddEven/verus_code.rs` (line 64)
- **main** in `benches/artifacts/dafnybench/Clover_is_even/verus_code.rs` (line 15)
- **main** in `benches/artifacts/dafnybench/Clover_cal_sum/verus_code.rs` (line 23)
- **main** in `benches/artifacts/dafnybench/Clover_double_array_elements/verus_code.rs` (line 29)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_AI_agent_verify_examples_CopyMatrix/verus_code.rs` (line 62)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseSelSort/verus_code.rs` (line 63)
- **main** in `benches/artifacts/dafnybench/DafnyPrograms_tmp_tmp74_f9k_c_automaton/verus_code.rs` (line 118)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session2Exercises_ExercisePositive/verus_code.rs` (line 138)
- **M** in `benches/artifacts/dafnybench/Clover_return_seven/verus_code.rs` (line 4)
- **main** in `benches/artifacts/dafnybench/Clover_return_seven/verus_code.rs` (line 11)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseSeparate/verus_code.rs` (line 35)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Function/verus_code.rs` (line 33)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session10Exercises_ExerciseBarrier/verus_code.rs` (line 45)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_AI_agent_verify_examples_ComputePower/verus_code.rs` (line 33)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseBubbleSort/verus_code.rs` (line 95)
- **main** in `benches/artifacts/dafnybench/Clover_canyon_search/verus_code.rs` (line 45)
- **main** in `benches/artifacts/dafnybench/Clover_triple3/verus_code.rs` (line 18)
- **main** in `benches/artifacts/dafnybench/Clover_copy_part/verus_code.rs` (line 50)
- **max_sum** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Index/verus_code.rs` (line 39)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_Index/verus_code.rs` (line 82)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_bql_exampls_Min/verus_code.rs` (line 31)
- **main** in `benches/artifacts/dafnybench/Clover_match/verus_code.rs` (line 29)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_rand/verus_code.rs` (line 43)
- **main** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_fact/verus_code.rs` (line 135)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_28/verus_code.rs` (line 28)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_41/verus_code.rs` (line 30)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmpj88zq5zt_2-Kontrakte_max/verus_code.rs` (line 30)
- **main** in `benches/artifacts/dafnybench/Clover_swap_sim/verus_code.rs` (line 15)
- **main** in `benches/artifacts/dafnybench/703FinalProject_tmp_tmpr_10rn4z_DP-GD/verus_code.rs` (line 63)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_Heimaverkefni 8_H8/verus_code.rs` (line 51)
- **main** in `benches/artifacts/dafnybench/Dafny-Practice_tmp_tmphnmt4ovh_Pattern Matching/verus_code.rs` (line 104)
- **main** in `benches/artifacts/dafnybench/Clover_array_append/verus_code.rs` (line 26)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session6Exercises_ExerciseCountEven/verus_code.rs` (line 76)
- **main** in `benches/artifacts/dafnybench/Clover_convert_map_key/verus_code.rs` (line 36)
- **main** in `benches/artifacts/dafnybench/Clover_count_lessthan/verus_code.rs` (line 40)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session4Exercises_ExerciseAllEqual/verus_code.rs` (line 143)
- **main** in `benches/artifacts/dafnybench/Clover_integer_square_root/verus_code.rs` (line 28)
- **main** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_searchSort/verus_code.rs` (line 72)
- **main** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week8_12_week9_lemma/verus_code.rs` (line 69)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session2Exercises_ExerciseExp/verus_code.rs` (line 56)
- **main** in `benches/artifacts/dafnybench/Clover_swap_arith/verus_code.rs` (line 20)
- **main** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_findMax/verus_code.rs` (line 62)
- **main** in `benches/artifacts/dafnybench/Dafny_Programs_tmp_tmp99966ew4_mymax/verus_code.rs` (line 22)
- **main** in `benches/artifacts/dafnybench/630-dafny_tmp_tmpz2kokaiq_Solution/verus_code.rs` (line 39)
- **main** in `benches/artifacts/dafnybench/DafnyProjects_tmp_tmp2acw_s4s_RawSort/verus_code.rs` (line 99)
- **main** in `benches/artifacts/dafnybench/Clover_update_array/verus_code.rs` (line 18)
- **main** in `benches/artifacts/dafnybench/DafnyPrograms_tmp_tmp74_f9k_c_map-multiset-implementation/verus_code.rs` (line 78)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_37/verus_code.rs` (line 34)
- **F_spec** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_F1a/verus_code.rs` (line 5)
- **F** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_F1a/verus_code.rs` (line 10)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_F1a/verus_code.rs` (line 56)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_LoopInvariant/verus_code.rs` (line 89)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session9Exercises_ExerciseSeqMaxSum/verus_code.rs` (line 132)
- **main** in `benches/artifacts/dafnybench/Dafny_Programs_tmp_tmp99966ew4_trig/verus_code.rs` (line 17)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session7Exercises_ExerciseBinarySearch/verus_code.rs` (line 124)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_23_x/verus_code.rs` (line 31)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_01/verus_code.rs` (line 30)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Generated_Code_15/verus_code.rs` (line 30)
- **main** in `benches/artifacts/dafnybench/Clover_linear_search2/verus_code.rs` (line 28)
- **main** in `benches/artifacts/dafnybench/Clover_test_array/verus_code.rs` (line 15)
- **main** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_Heimaverkefni 1_LinearSearch/verus_code.rs` (line 62)
- **main** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_07/verus_code.rs` (line 42)
- **main** in `benches/artifacts/dafnybench/Clover_bubble_sort/verus_code.rs` (line 53)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/brs3.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/ms2.rs` (line 53)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s42if.rs` (line 72)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/sina2.rs` (line 66)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s3lif.rs` (line 68)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s12if.rs` (line 71)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s1if.rs` (line 53)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/sina1.rs` (line 48)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s3if.rs` (line 56)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s52if.rs` (line 73)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s22if.rs` (line 71)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/conda.rs` (line 67)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/ms3.rs` (line 54)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s32if.rs` (line 71)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/res2o.rs` (line 108)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/condg.rs` (line 67)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s1lif.rs` (line 67)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s5if.rs` (line 55)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/ms4.rs` (line 54)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/condn.rs` (line 47)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/ms5.rs` (line 55)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s4if.rs` (line 54)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s2lif.rs` (line 67)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s5lif.rs` (line 68)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/brs2.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/brs1.rs` (line 56)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s4lif.rs` (line 69)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/sina3.rs` (line 79)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/res1o.rs` (line 78)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/ms1.rs` (line 52)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/condm.rs` (line 49)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/sina4.rs` (line 81)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/sina5.rs` (line 94)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/res1.rs` (line 81)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/brs5.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/s2if.rs` (line 54)
- **main** in `benches/VerusProofSynthesisBench/SVComp-Array-fpi-nonl/brs4.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/Misc/choose_odd.rs` (line 34)
- **main** in `benches/VerusProofSynthesisBench/Misc/len_intersect.rs` (line 36)
- **main** in `benches/VerusProofSynthesisBench/Misc/bubble_v1.rs` (line 69)
- **main** in `benches/VerusProofSynthesisBench/Misc/filter_v2.rs` (line 78)
- **main** in `benches/VerusProofSynthesisBench/Misc/arg_free.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/Misc/filter.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/Misc/bubble_v2.rs` (line 73)
- **main** in `benches/VerusProofSynthesisBench/Misc/max_index.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/Misc/filter_weak.rs` (line 35)
- **main** in `benches/VerusProofSynthesisBench/Misc/simple_nested.rs` (line 53)
- **main** in `benches/VerusProofSynthesisBench/Misc/linearsearch.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/Misc/map.rs` (line 34)
- **main** in `benches/VerusProofSynthesisBench/Misc/remove_all_greater_v2.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/Misc/tail_triangle.rs` (line 62)
- **main** in `benches/VerusProofSynthesisBench/Misc/basic_nonlinear.rs` (line 27)
- **main** in `benches/VerusProofSynthesisBench/Misc/remove_all_greater.rs` (line 41)
- **main** in `benches/VerusProofSynthesisBench/Misc/trigger.rs` (line 34)
- **main** in `benches/VerusProofSynthesisBench/Misc/fib.rs` (line 81)
- **main** in `benches/VerusProofSynthesisBench/Misc/findmax.rs` (line 37)
- **main** in `benches/VerusProofSynthesisBench/Misc/conditional_average.rs` (line 65)
- **main** in `benches/VerusProofSynthesisBench/Misc/cell_2_sum.rs` (line 53)
- **main** in `benches/VerusProofSynthesisBench/Misc/binary_search.rs` (line 39)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_2.rs` (line 29)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_605.rs` (line 25)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_755.rs` (line 46)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_732.rs` (line 32)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_554.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_414.rs` (line 25)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_426.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_457.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_804.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_576.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_161.rs` (line 48)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_618.rs` (line 25)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_142.rs` (line 37)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_261.rs` (line 26)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_262.rs` (line 23)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_18.rs` (line 49)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_170.rs` (line 32)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_798.rs` (line 27)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_251.rs` (line 18)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_249.rs` (line 29)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_424.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_760.rs` (line 17)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_95.rs` (line 24)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_433.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_461.rs` (line 42)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_62.rs` (line 22)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_307.rs` (line 17)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_436.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_477.rs` (line 71)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_284.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_3.rs` (line 26)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_145.rs` (line 22)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_769.rs` (line 49)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_733.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_113.rs` (line 30)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_476.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_412.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_741.rs` (line 18)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_764.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_454.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_578.rs` (line 24)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_105.rs` (line 32)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_610.rs` (line 23)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_567.rs` (line 20)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_94.rs` (line 24)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_728.rs` (line 25)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_472.rs` (line 22)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_282.rs` (line 24)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_807.rs` (line 27)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_602.rs` (line 53)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_743.rs` (line 28)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_586.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_629.rs` (line 17)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_431.rs` (line 17)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_808.rs` (line 17)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_399.rs` (line 23)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_809.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_474.rs` (line 27)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_644.rs` (line 23)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_230.rs` (line 27)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_616.rs` (line 25)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 49)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_133.rs` (line 32)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_69.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_290.rs` (line 22)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_790.rs` (line 17)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_572.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_445.rs` (line 24)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_273.rs` (line 24)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_8.rs` (line 23)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_624.rs` (line 36)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_70.rs` (line 23)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_576_v2.rs` (line 35)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_447.rs` (line 27)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_588.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_460.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_775.rs` (line 16)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_579.rs` (line 50)
- **main** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_240.rs` (line 21)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_2.rs` (line 69)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_605.rs` (line 46)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_755.rs` (line 87)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_732.rs` (line 56)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_554.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_414.rs` (line 55)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_426.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_457.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_804.rs` (line 36)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_576.rs` (line 85)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_161.rs` (line 91)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_618.rs` (line 46)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_142.rs` (line 69)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_261.rs` (line 47)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_262.rs` (line 51)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_18.rs` (line 90)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_170.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_798.rs` (line 51)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_251.rs` (line 35)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_249.rs` (line 68)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_424.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_760.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_95.rs` (line 42)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_433.rs` (line 31)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_461.rs` (line 66)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_62.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_307.rs` (line 32)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_436.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_477.rs` (line 71)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_284.rs` (line 31)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_3.rs` (line 47)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_145.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_769.rs` (line 130)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_733.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_113.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_476.rs` (line 74)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_412.rs` (line 42)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_741.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_764.rs` (line 62)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_454.rs` (line 31)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_578.rs` (line 46)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_105.rs` (line 56)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_610.rs` (line 56)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_567.rs` (line 35)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_94.rs` (line 51)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_728.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_472.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_282.rs` (line 44)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_807.rs` (line 50)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_602.rs` (line 108)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_743.rs` (line 66)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_586.rs` (line 49)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_629.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_431.rs` (line 43)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_808.rs` (line 32)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_399.rs` (line 40)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_809.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_474.rs` (line 51)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_644.rs` (line 52)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_230.rs` (line 51)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_616.rs` (line 45)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_557.rs` (line 76)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_133.rs` (line 59)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_69.rs` (line 85)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_290.rs` (line 41)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_790.rs` (line 35)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_572.rs` (line 96)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_445.rs` (line 43)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_273.rs` (line 43)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_8.rs` (line 41)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_624.rs` (line 75)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_70.rs` (line 38)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_576_v2.rs` (line 73)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_447.rs` (line 48)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_588.rs` (line 74)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_460.rs` (line 41)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_775.rs` (line 34)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_579.rs` (line 133)
- **main** in `benches/VerusProofSynthesisBench/MBPP/task_id_240.rs` (line 54)
- **main** in `benches/HumanEval-RustBench/not_finished_proof/072-will_it_fly.rs` (line 159)
- **main** in `benches/HumanEval-RustBench/not_finished_proof/134-check_if_last_char_is_a_letter.rs` (line 54)
- **main** in `benches/HumanEval-RustBench/not_finished_proof/076-is_simple_power.rs` (line 47)
- **main** in `benches/HumanEval-RustBench/not_finished_proof/077-is_cube.rs` (line 163)
- **main** in `benches/HumanEval-RustBench/additional/array_copy.rs` (line 31)
- **main** in `benches/HumanEval-RustBench/additional/replace_chars.rs` (line 30)
- **main** in `benches/HumanEval-RustBench/additional/barrier.rs` (line 52)
- **main** in `benches/HumanEval-RustBench/additional/has_close_elements.rs` (line 64)
- **main** in `benches/HumanEval-RustBench/additional/max_array.rs` (line 37)
- **main** in `benches/HumanEval-RustBench/additional/remove_element.rs` (line 49)
- **main** in `benches/HumanEval-RustBench/additional/smallest_list_length.rs` (line 37)
- **main** in `benches/HumanEval-RustBench/additional/abs.rs` (line 25)
- **main** in `benches/HumanEval-RustBench/additional/array_product.rs` (line 35)
- **main** in `benches/HumanEval-RustBench/additional/index_wise_addition.rs` (line 61)
- **main** in `benches/HumanEval-RustBench/additional/unique.rs` (line 42)
- **main** in `benches/HumanEval-RustBench/additional/is_sorted.rs` (line 38)
- **main** in `benches/HumanEval-RustBench/additional/rolling_max.rs` (line 49)
- **main** in `benches/HumanEval-RustBench/additional/max_dafny_lsp.rs` (line 47)
- **main** in `benches/HumanEval-RustBench/additional/has_only_one_distinct_element.rs` (line 38)
- **main** in `benches/HumanEval-RustBench/additional/arithmetic_weird.rs` (line 28)
- **main** in `benches/HumanEval-RustBench/additional/remove_elements.rs` (line 61)
- **main** in `benches/HumanEval-RustBench/additional/replace.rs` (line 34)
- **main** in `benches/HumanEval-RustBench/additional/reverse.rs` (line 30)
- **main** in `benches/HumanEval-RustBench/additional/two_sum.rs` (line 56)
- **main** in `benches/HumanEval-RustBench/additional/largest_prime_factor.rs` (line 65)
- **main** in `benches/HumanEval-RustBench/additional/remove_duplicates.rs` (line 65)
- **main** in `benches/HumanEval-RustBench/additional/binary_search_recursive.rs` (line 45)
- **main** in `benches/HumanEval-RustBench/additional/is_non_prime.rs` (line 34)
- **main** in `benches/HumanEval-RustBench/additional/two_way_sort.rs` (line 66)
- **main** in `benches/HumanEval-RustBench/additional/intersperse.rs` (line 37)
- **main** in `benches/HumanEval-RustBench/additional/last_position.rs` (line 37)
- **main** in `benches/HumanEval-RustBench/additional/smallest_missing_number.rs` (line 45)
- **main** in `benches/HumanEval-RustBench/additional/cubes.rs` (line 51)
- **main** in `benches/HumanEval-RustBench/additional/array_concat.rs` (line 46)
- **main** in `benches/HumanEval-RustBench/additional/string_xor.rs` (line 39)
- **main** in `benches/HumanEval-RustBench/additional/integer_square_root.rs` (line 48)
- **main** in `benches/HumanEval-RustBench/additional/unique_better.rs` (line 45)
- **main** in `benches/HumanEval-RustBench/additional/array_append.rs` (line 32)
- **main** in `benches/HumanEval-RustBench/additional/binary_search.rs` (line 43)
- **main** in `benches/HumanEval-RustBench/SubBench/008-sum_product.rs` (line 73)
- **main** in `benches/autoverus/Diffy/unverified/brs3.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/ms2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s42if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/sina2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s3lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s12if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s1if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/sina1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s3if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s52if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s22if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/conda.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/ms3.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s32if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/res2o.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/condg.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s1lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s5if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/res2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/ms4.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/condn.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/ms5.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s4if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s2lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s5lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/brs2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/brs1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s4lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/sina3.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/res1o.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/ms1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/condm.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/sina4.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/sina5.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/res1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/brs5.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/s2if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/unverified/brs4.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/brs3.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/ms2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s42if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/sina2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s3lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s12if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s1if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/sina1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s3if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s52if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s22if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/conda.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/ms3.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s32if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/res2o.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/condg.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s1lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s5if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/res2.rs` (line 4)
- **main** in `benches/autoverus/Diffy/verified/ms4.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/condn.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/ms5.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s4if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s2lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s5lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/brs2.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/brs1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s4lif.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/sina3.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/res1o.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/ms1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/condm.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/sina4.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/sina5.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/res1.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/brs5.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/s2if.rs` (line 2)
- **main** in `benches/autoverus/Diffy/verified/brs4.rs` (line 2)
- **main** in `benches/autoverus/interprocedural/tock/unverified/rb1.rs` (line 4)
- **main** in `benches/autoverus/interprocedural/tock/verified/rb1.rs` (line 4)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifeqn4.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/brs3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/modp.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ms2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/eqn5.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/eqn3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s42if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sina2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s3lif.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s12if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s1if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/mods.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sina1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s3if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s52if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s22if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ncomp.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/indp4.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/conda.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifcomp.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ms3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s32if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/modn.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/res2o.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/condg.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifeqn5.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sqm.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/nsqm-if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s1lif.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s5if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/res2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ms4.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/condn.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/pcomp.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/indp1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ms5.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/indp3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s4if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/indp2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s2lif.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s5lif.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifncomp.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifeqn3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/brs2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/brs1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifeqn1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/eqn2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/eqn4.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/indp5.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s4lif.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ss3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sina3.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sqm-if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ss2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/res1o.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ms1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/nsqm.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/condm.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sina4.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/sina5.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ifeqn2.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/res1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ss4.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ssina.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/brs5.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/s2if.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/eqn1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/ss1.rs` (line 2)
- **main** in `benches/autoverus/SVComp-Array-fpi/unverified/brs4.rs` (line 2)
- **main** in `benches/autoverus/CloverBench/unverified/array_sum_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/cal_div.rs` (line 21)
- **main** in `benches/autoverus/CloverBench/unverified/array_product_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/array_concat_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/array_copy_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/all_digits_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/two_sum.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/array_append_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/linear_search2.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/is_prime.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/unverified/binary_search.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/array_sum_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/cal_div.rs` (line 24)
- **main** in `benches/autoverus/CloverBench/verified/array_product_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/array_concat_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/array_copy_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/all_digits_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/two_sum.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/array_append_strong.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/linear_search2.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/is_prime.rs` (line 3)
- **main** in `benches/autoverus/CloverBench/verified/binary_search.rs` (line 3)
- **main** in `benches/autoverus/Misc/unverified/deduplicate.rs` (line 3)
- **main** in `benches/autoverus/Misc/unverified/choose_odd.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/len_intersect.rs` (line 4)
- **main** in `benches/autoverus/Misc/unverified/bubble.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/arg_free.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/filter.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/max_index.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/filter_weak.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/simple_nested.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/linearsearch.rs` (line 4)
- **main** in `benches/autoverus/Misc/unverified/map.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/reverse.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/tail_triangle.rs` (line 5)
- **main** in `benches/autoverus/Misc/unverified/basic_nonlinear.rs` (line 4)
- **main** in `benches/autoverus/Misc/unverified/remove_all_greater.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/havoc_inline_post.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/trigger.rs` (line 4)
- **main** in `benches/autoverus/Misc/unverified/fib.rs` (line 3)
- **main** in `benches/autoverus/Misc/unverified/findmax.rs` (line 3)
- **main** in `benches/autoverus/Misc/unverified/sum.rs` (line 4)
- **main** in `benches/autoverus/Misc/unverified/conditional_average.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/cell_2_sum.rs` (line 2)
- **main** in `benches/autoverus/Misc/unverified/binary_search.rs` (line 3)
- **main** in `benches/autoverus/Misc/verified/deduplicate.rs` (line 3)
- **main** in `benches/autoverus/Misc/verified/choose_odd.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/len_intersect.rs` (line 4)
- **main** in `benches/autoverus/Misc/verified/bubble_v1.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/filter_v2.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/arg_free.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/filter.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/bubble_v2.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/max_index.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/filter_weak.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/simple_nested.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/linearsearch.rs` (line 4)
- **main** in `benches/autoverus/Misc/verified/map.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/remove_all_greater_v2.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/tail_triangle.rs` (line 5)
- **main** in `benches/autoverus/Misc/verified/basic_nonlinear.rs` (line 4)
- **main** in `benches/autoverus/Misc/verified/remove_all_greater.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/havoc_inline_post.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/trigger.rs` (line 4)
- **main** in `benches/autoverus/Misc/verified/fib.rs` (line 3)
- **main** in `benches/autoverus/Misc/verified/findmax.rs` (line 3)
- **main** in `benches/autoverus/Misc/verified/sum.rs` (line 4)
- **main** in `benches/autoverus/Misc/verified/conditional_average.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/cell_2_sum.rs` (line 2)
- **main** in `benches/autoverus/Misc/verified/binary_search.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_2.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_605.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_755.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_732.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_554.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_414.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_426.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_457.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_804.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_576.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_161.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_618.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_142.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_261.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_262.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_18.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_170.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_798.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_251.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_249.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_424.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_760.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_95.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_433.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_461.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_62.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_307.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_436.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_477.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_284.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_3.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_145.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_769.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_733.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_113.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_476.rs` (line 5)
- **main** in `benches/autoverus/MBPP/unverified/task_id_412.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_741.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_764.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_454.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_578.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_105.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_610.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_567.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_94.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_728.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_472.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_282.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_807.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_602.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_743.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_586.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_629.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_431.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_808.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_399.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_809.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_474.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_644.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_230.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_616.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_557.rs` (line 2)
- **main** in `benches/autoverus/MBPP/unverified/task_id_133.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_69.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_290.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_790.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_572.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_445.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_273.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_8.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_624.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_70.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_447.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_588.rs` (line 5)
- **main** in `benches/autoverus/MBPP/unverified/task_id_460.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_775.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_579.rs` (line 3)
- **main** in `benches/autoverus/MBPP/unverified/task_id_240.rs` (line 3)
- **main** in `benches/RustBench/preconditions_removed/barrier.rs` (line 41)
- **main** in `benches/RustBench/preconditions_removed/has_close_elements.rs` (line 51)
- **main** in `benches/RustBench/preconditions_removed/remove_element.rs` (line 37)
- **main** in `benches/RustBench/preconditions_removed/smallest_list_length.rs` (line 27)
- **main** in `benches/RustBench/preconditions_removed/abs.rs` (line 17)
- **main** in `benches/RustBench/preconditions_removed/index_wise_addition.rs` (line 42)
- **main** in `benches/RustBench/preconditions_removed/unique.rs` (line 30)
- **main** in `benches/RustBench/preconditions_removed/max_dafny_lsp.rs` (line 37)
- **main** in `benches/RustBench/preconditions_removed/two_sum.rs` (line 39)
- **main** in `benches/RustBench/preconditions_removed/remove_duplicates.rs` (line 49)
- **main** in `benches/RustBench/preconditions_removed/binary_search_recursive.rs` (line 31)
- **main** in `benches/RustBench/preconditions_removed/is_non_prime.rs` (line 24)
- **main** in `benches/RustBench/preconditions_removed/last_position.rs` (line 26)
- **main** in `benches/RustBench/preconditions_removed/smallest_missing_number.rs` (line 33)
- **main** in `benches/RustBench/preconditions_removed/string_xor.rs` (line 27)
- **main** in `benches/RustBench/preconditions_removed/unique_better.rs` (line 33)
- **main** in `benches/RustBench/preconditions_removed/binary_search.rs` (line 33)
- **main** in `benches/RustBench/invariants_removed/array_copy.rs` (line 21)
- **main** in `benches/RustBench/invariants_removed/replace_chars.rs` (line 20)
- **main** in `benches/RustBench/invariants_removed/barrier.rs` (line 34)
- **main** in `benches/RustBench/invariants_removed/has_close_elements.rs` (line 46)
- **main** in `benches/RustBench/invariants_removed/max_array.rs` (line 25)
- **main** in `benches/RustBench/invariants_removed/remove_element.rs` (line 35)
- **main** in `benches/RustBench/invariants_removed/smallest_list_length.rs` (line 25)
- **main** in `benches/RustBench/invariants_removed/array_product.rs` (line 23)
- **main** in `benches/RustBench/invariants_removed/index_wise_addition.rs` (line 40)
- **main** in `benches/RustBench/invariants_removed/is_sorted.rs` (line 26)
- **main** in `benches/RustBench/invariants_removed/unique_no_hints.rs` (line 29)
- **main** in `benches/RustBench/invariants_removed/rolling_max.rs` (line 37)
- **main** in `benches/RustBench/invariants_removed/max_dafny_lsp.rs` (line 34)
- **main** in `benches/RustBench/invariants_removed/has_only_one_distinct_element.rs` (line 27)
- **main** in `benches/RustBench/invariants_removed/arithmetic_weird.rs` (line 20)
- **main** in `benches/RustBench/invariants_removed/remove_elements.rs` (line 42)
- **main** in `benches/RustBench/invariants_removed/replace.rs` (line 22)
- **main** in `benches/RustBench/invariants_removed/reverse.rs` (line 20)
- **main** in `benches/RustBench/invariants_removed/two_sum.rs` (line 37)
- **main** in `benches/RustBench/invariants_removed/remove_duplicates.rs` (line 51)
- **main** in `benches/RustBench/invariants_removed/is_non_prime.rs` (line 23)
- **main** in `benches/RustBench/invariants_removed/two_way_sort.rs` (line 46)
- **main** in `benches/RustBench/invariants_removed/intersperse.rs` (line 26)
- **main** in `benches/RustBench/invariants_removed/last_position.rs` (line 26)
- **main** in `benches/RustBench/invariants_removed/smallest_missing_number.rs` (line 32)
- **main** in `benches/RustBench/invariants_removed/cubes.rs` (line 38)
- **main** in `benches/RustBench/invariants_removed/array_concat.rs` (line 34)
- **main** in `benches/RustBench/invariants_removed/string_xor.rs` (line 27)
- **main** in `benches/RustBench/invariants_removed/integer_square_root.rs` (line 37)
- **main** in `benches/RustBench/invariants_removed/array_append.rs` (line 22)
- **main** in `benches/RustBench/invariants_removed/unique_with_hint.rs` (line 31)
- **main** in `benches/RustBench/invariants_removed/binary_search.rs` (line 31)
- **main** in `benches/RustBench/WIP/WIP: max_segment_sum.rs` (line 78)
- **main** in `benches/RustBench/WIP/WIP: mcontained.rs` (line 50)
- **main** in `benches/RustBench/WIP/WIP: transpose_matrix.rs` (line 53)
- **main** in `benches/RustBench/ground_truth/array_copy.rs` (line 25)
- **main** in `benches/RustBench/ground_truth/replace_chars.rs` (line 24)
- **main** in `benches/RustBench/ground_truth/barrier.rs` (line 42)
- **main** in `benches/RustBench/ground_truth/has_close_elements.rs` (line 54)
- **main** in `benches/RustBench/ground_truth/max_array.rs` (line 29)
- **main** in `benches/RustBench/ground_truth/remove_element.rs` (line 39)
- **main** in `benches/RustBench/ground_truth/smallest_list_length.rs` (line 29)
- **main** in `benches/RustBench/ground_truth/abs.rs` (line 19)
- **main** in `benches/RustBench/ground_truth/array_product.rs` (line 27)
- **main** in `benches/RustBench/ground_truth/index_wise_addition.rs` (line 51)
- **main** in `benches/RustBench/ground_truth/unique.rs` (line 34)
- **main** in `benches/RustBench/ground_truth/is_sorted.rs` (line 30)
- **main** in `benches/RustBench/ground_truth/rolling_max.rs` (line 43)
- **main** in `benches/RustBench/ground_truth/max_dafny_lsp.rs` (line 39)
- **main** in `benches/RustBench/ground_truth/has_only_one_distinct_element.rs` (line 30)
- **main** in `benches/RustBench/ground_truth/arithmetic_weird.rs` (line 22)
- **main** in `benches/RustBench/ground_truth/remove_elements.rs` (line 49)
- **main** in `benches/RustBench/ground_truth/replace.rs` (line 28)
- **main** in `benches/RustBench/ground_truth/reverse.rs` (line 24)
- **main** in `benches/RustBench/ground_truth/two_sum.rs` (line 46)
- **main** in `benches/RustBench/ground_truth/largest_prime_factor.rs` (line 57)
- **main** in `benches/RustBench/ground_truth/remove_duplicates.rs` (line 51)
- **main** in `benches/RustBench/ground_truth/binary_search_recursive.rs` (line 37)
- **main** in `benches/RustBench/ground_truth/is_non_prime.rs` (line 26)
- **main** in `benches/RustBench/ground_truth/two_way_sort.rs` (line 52)
- **main** in `benches/RustBench/ground_truth/intersperse.rs` (line 31)
- **main** in `benches/RustBench/ground_truth/last_position.rs` (line 29)
- **main** in `benches/RustBench/ground_truth/smallest_missing_number.rs` (line 37)
- **main** in `benches/RustBench/ground_truth/cubes.rs` (line 45)
- **main** in `benches/RustBench/ground_truth/array_concat.rs` (line 38)
- **main** in `benches/RustBench/ground_truth/string_xor.rs` (line 31)
- **main** in `benches/RustBench/ground_truth/integer_square_root.rs` (line 40)
- **main** in `benches/RustBench/ground_truth/unique_better.rs` (line 37)
- **main** in `benches/RustBench/ground_truth/array_append.rs` (line 26)
- **main** in `benches/RustBench/ground_truth/binary_search.rs` (line 35)
- **main** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session5Exercises_ExerciseSumElems/verus_code.rs` (line 148)
- **string_xor** in `benches/HumanEval-RustBench/additional/string_xor.rs` (line 6)
- **string_xor** in `benches/RustBench/preconditions_removed/string_xor.rs` (line 6)
- **string_xor** in `benches/RustBench/invariants_removed/string_xor.rs` (line 6)
- **string_xor** in `benches/RustBench/ground_truth/string_xor.rs` (line 6)

**Sample code from first function:**
```rust
{
        // Basic facts about arrays and their sequence views
    }
```

---

### Group 43 (Average Similarity: 79.61%)

Functions in this group (3 total):

- **length** in `benches/artifacts/dafnybench/FMSE-2022-2023_tmp_tmp6_x_ba46_Lab10_Lab10/verus_code.rs` (line 141)
- **is_empty** in `benches/artifacts/dafnybench/CSC8204-Dafny_tmp_tmp11yhjb53_stack/verus_code.rs` (line 13)
- **empty2** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week8_12_a3 copy 2/verus_code.rs` (line 161)

**Sample code from first function:**
```rust
{
            self.vec.len()
        }
```

**Pairwise similarities:**
- length vs is_empty: 64.71%
- length vs empty2: 75.00%
- is_empty vs empty2: 84.21%

---

### Group 44 (Average Similarity: 79.38%)

Functions in this group (7 total):

- **sum_chars** in `benches/artifacts/dafnybench/Dafny_Learning_Experience_tmp_tmpuxvcet_u_week8_12_week8_CheckSumCalculator/verus_code.rs` (line 8)
- **sum_spec** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_SumArray/verus_code.rs` (line 4)
- **recursive_sum_down** in `benches/artifacts/dafnybench/Dafny-Practice_tmp_tmphnmt4ovh_Pattern Matching/verus_code.rs` (line 5)
- **recursive_sum_up** in `benches/artifacts/dafnybench/Dafny-Practice_tmp_tmphnmt4ovh_Pattern Matching/verus_code.rs` (line 15)
- **sum_r** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session5Exercises_ExerciseSumElems/verus_code.rs` (line 5)
- **sum_l** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session5Exercises_ExerciseSumElems/verus_code.rs` (line 16)
- **sum** in `benches/HumanEval-RustBench/003-below_zero.rs` (line 6)

**Sample code from first function:**
```rust
{
        if s.len() == 0 {
            0
        } else {
            s[s.len() - 1] as int + sum_chars(s.subrange(0, s.len() - 1))
        }
    }
```

---

### Group 45 (Average Similarity: 79.07%)

Functions in this group (4 total):

- **max_segment_sum** in `benches/RustBench/WIP/WIP: max_segment_sum.rs` (line 26)
- **two_sum** in `benches/RustBench/preconditions_removed/two_sum.rs` (line 6)
- **two_sum** in `benches/RustBench/invariants_removed/two_sum.rs` (line 6)
- **two_sum** in `benches/RustBench/ground_truth/two_sum.rs` (line 6)

**Sample code from first function:**
```rust
{ let (i, j) = p; 0 <= i <= j <= a.len() }
```

**Pairwise similarities:**
- max_segment_sum vs two_sum: 79.07%
- max_segment_sum vs two_sum: 79.07%
- max_segment_sum vs two_sum: 79.07%
- two_sum vs two_sum: 100.00%
- two_sum vs two_sum: 100.00%
- two_sum vs two_sum: 100.00%

---

### Group 46 (Average Similarity: 77.70%)

Functions in this group (8 total):

- **main_method** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_C_convert_examples_11/verus_code.rs` (line 4)
- **main_fn** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Fine_Tune_Examples_50_examples_41/verus_code.rs` (line 5)
- **is_even** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_dataset_error_data_real_error_IsEven_success_1/verus_code.rs` (line 17)
- **sum** in `benches/artifacts/dafnybench/Clover_cal_sum/verus_code.rs` (line 4)
- **up_while_less** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_LoopInvariant/verus_code.rs` (line 4)
- **up_while_not_equal** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_LoopInvariant/verus_code.rs` (line 18)
- **down_while_greater** in `benches/artifacts/dafnybench/Dafny_Verify_tmp_tmphq7j0row_Test_Cases_LoopInvariant/verus_code.rs` (line 46)
- **sum_ints_loop** in `benches/artifacts/dafnybench/Dafny_tmp_tmp0wu8wmfr_tests_SumIntsLoop/verus_code.rs` (line 14)

**Sample code from first function:**
```rust
{
        let mut i: i32 = 0;
        let mut j: i32 = 0;

        while i < x
            invariant 
                0 <= i <= x,
                j == 2 * i,
                x <= 1073741823,
            decreases x - i,
        {
            j = j + 2;
            i = i + 1;
            assert(j == 2 * i);
        }

        (j, i)
    }
```

---

### Group 47 (Average Similarity: 76.82%)

Functions in this group (2 total):

- **split_and_append** in `benches/autoverus/MBPP/unverified/task_id_586.rs` (line 6)
- **reverse_to_k** in `benches/autoverus/MBPP/unverified/task_id_644.rs` (line 6)

**Sample code from first function:**
```rust
{
    let mut new_list = Vec::new();
    let mut index = n;
    while index < list.len() {
        new_list.push(list[index]);
        index += 1;
    }
    let mut index = 0;
    while index < n {
        new_list.push(list[index]);
        index += 1;
    }
    new_list
}
```

**Pairwise similarities:**
- split_and_append vs reverse_to_k: 76.82%

---

### Group 48 (Average Similarity: 76.50%)

Functions in this group (7 total):

- **spec_fibfib** in `benches/HumanEval-RustBench/063-fibfib.rs` (line 5)
- **fib** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_Hoare/verus_code.rs` (line 29)
- **fib** in `benches/artifacts/dafnybench/Dafny-Exercises_tmp_tmpjm75muf__Session2Exercises_ExerciseFibonacci/verus_code.rs` (line 4)
- **power** in `benches/artifacts/dafnybench/Dafny-VMC_tmp_tmpzgqv0i1u_src_Math_Helper/verus_code.rs` (line 4)
- **fibo** in `benches/VerusProofSynthesisBench/Misc/fib.rs` (line 4)
- **fibo** in `benches/autoverus/Misc/unverified/fib.rs` (line 6)
- **fibo** in `benches/autoverus/Misc/verified/fib.rs` (line 6)

**Sample code from first function:**
```rust
{
    if (n == 0) {
        0
    } else if (n == 1) {
        0
    } else if (n == 2) {
        1
    } else {
        spec_fibfib((n - 1) as nat) + spec_fibfib((n - 2) as nat) + spec_fibfib((n - 3) as nat)
    }
}
```

---

### Group 49 (Average Similarity: 76.13%)

Functions in this group (2 total):

- **add_list** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_Hoare/verus_code.rs` (line 45)
- **length** in `benches/artifacts/dafnybench/CVS-Projto1_tmp_tmpb1o0bu8z_fact/verus_code.rs` (line 70)

**Sample code from first function:**
```rust
{
        match l {
            List::Nil => 0,
            List::Cons(head, tail) => head as int + add_list(*tail),
        }
    }
```

**Pairwise similarities:**
- add_list vs length: 76.13%

---

### Group 50 (Average Similarity: 76.00%)

Functions in this group (3 total):

- **arithmetic** in `benches/RustBench/invariants_removed/arithmetic_weird.rs` (line 6)
- **arithmetic_weird** in `benches/HumanEval-RustBench/additional/arithmetic_weird.rs` (line 6)
- **arithmetic_weird** in `benches/RustBench/ground_truth/arithmetic_weird.rs` (line 6)

**Sample code from first function:**
```rust
{
    let mut x = 0;
    let mut y = 0;
    while x <= 10
    {
        y = 10 - x;
        x = x + 1;
    }
    y
}
```

**Pairwise similarities:**
- arithmetic vs arithmetic_weird: 76.00%
- arithmetic vs arithmetic_weird: 76.00%
- arithmetic_weird vs arithmetic_weird: 100.00%

---

### Group 51 (Average Similarity: 75.63%)

Functions in this group (5 total):

- **remove_duplicates** in `benches/HumanEval-RustBench/additional/remove_duplicates.rs` (line 34)
- **remove_duplicates** in `benches/RustBench/preconditions_removed/remove_duplicates.rs` (line 28)
- **remove_duplicates** in `benches/RustBench/invariants_removed/remove_duplicates.rs` (line 28)
- **remove_duplicates** in `benches/RustBench/ground_truth/remove_duplicates.rs` (line 28)
- **remove_elements** in `benches/RustBench/ground_truth/remove_elements.rs` (line 28)

**Sample code from first function:**
```rust
{
    // impl-start
    let mut result: Vec<i32> = Vec::new();
    let mut i = 0;
    while i < a.len()
        // invariants-start
        invariant
            0 <= i <= a.len(),
            forall|k: int| #![auto] 0 <= k < result.len() ==> in_array(a@, result[k]),
            forall|k: int, l: int| 0 <= k < l < result.len() ==> result[k] != result[l],
        // invariants-end
    {
        if !in_array_exec(&result, a[i]) {
            result.push(a[i]);
        }
        i = i + 1;
    }
  ...
```

**Pairwise similarities:**
- remove_duplicates vs remove_duplicates: 100.00%
- remove_duplicates vs remove_duplicates: 100.00%
- remove_duplicates vs remove_duplicates: 100.00%
- remove_duplicates vs remove_elements: 75.19%
- remove_duplicates vs remove_duplicates: 100.00%
- remove_duplicates vs remove_duplicates: 100.00%
- remove_duplicates vs remove_elements: 75.19%
- remove_duplicates vs remove_duplicates: 100.00%
- remove_duplicates vs remove_elements: 75.19%
- remove_duplicates vs remove_elements: 75.19%

---

### Group 52 (Average Similarity: 0.00%)

Functions in this group (4 total):

- **to_toggle_case_spec** in `benches/VerusProofSynthesisBench/MBPP_no_bodies/task_id_557.rs` (line 25)
- **to_toggle_case_spec** in `benches/VerusProofSynthesisBench/MBPP/task_id_557.rs` (line 25)
- **to_toggle_case_spec** in `benches/autoverus/MBPP/unverified/task_id_557.rs` (line 22)
- **to_toggle_case_spec** in `benches/autoverus/MBPP/verified/task_id_557.rs` (line 28)

**Sample code from first function:**
```rust
{
    if is_lower_case(s) {
        shift_minus_32_spec(s)
    } else if is_upper_case(s) {
        shift32_spec(s)
    } else {
        s
    }
}
```

**Pairwise similarities:**
- to_toggle_case_spec vs to_toggle_case_spec: 100.00%
- to_toggle_case_spec vs to_toggle_case_spec: 100.00%
- to_toggle_case_spec vs to_toggle_case_spec: 100.00%
- to_toggle_case_spec vs to_toggle_case_spec: 100.00%
- to_toggle_case_spec vs to_toggle_case_spec: 100.00%
- to_toggle_case_spec vs to_toggle_case_spec: 100.00%

---

### Group 53 (Average Similarity: 0.00%)

Functions in this group (2 total):

- **minArray** in `benches/artifacts/dafnybench/Clover_min_array/verus_code.rs` (line 4)
- **minArray** in `benches/artifacts/dafnybench/Dafny_tmp_tmpv_d3qi10_2_min/verus_code.rs` (line 47)

**Sample code from first function:**
```rust
{
        let mut r = a[0];
        let mut i = 1;
        while i < a.len()
            invariant 
                0 <= i <= a.len(),
                forall|x: int| 0 <= x < i ==> r <= a[x],
                exists|x: int| 0 <= x < i && r == a[x]
            decreases a.len() - i
        {
            if r > a[i] {
                r = a[i];
            }
            i = i + 1;
        }
        r
    }
```

**Pairwise similarities:**
- minArray vs minArray: 72.65%

---

