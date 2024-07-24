also:: cpp/stl/map
- map是STL的一个关联容器，它提供一对一的hash
-
- ## `map`
  id:: 625ee24d-2321-4e6a-9bcf-88bee55d83fc
-
- ## `unordered_map`
  id:: 625ee11b-c3f2-493d-ab6e-67f7b27f0d6d
  - 泛型注意不要是 `char*`
    - `key` 就会变成一个地址, 只有这个地址才会指向对应 `value`, 不会比对内存的内容的
      > The unordered_map compares only the address, not the set of characters that reside at the address.
      via: https://stackoverflow.com/a/54473240/13561253
-
- diff ((625ee24d-2321-4e6a-9bcf-88bee55d83fc)) with ((625ee11b-c3f2-493d-ab6e-67f7b27f0d6d))
  - ```
    # via: https://www.geeksforgeeks.org/map-vs-unordered_map-c/
                      | map                 | unordered_map
    ---------------------------------------------------------
    Ordering          | increasing  order   | no ordering
                      | (by default)        |
    Implementation    | Self balancing BST  | Hash Table
                      | like Red-Black Tree |
    search time       | log(n)              | O(1) -> Average
                      |                     | O(n) -> Worst Case
    Insertion time    | log(n) + Rebalance  | Same as search
    Deletion time     | log(n) + Rebalance  | Same as search
    ```
  - Use `std::map` when
    collapsed:: true
    - You need ordered data.
    - You would have to print/access the data (in sorted order).
    - You need predecessor/successor of elements.
    - See [advantages of BST over Hash Table](https://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/) for more cases.
    - ---
      `map` keeps iterators to all elements stable, in C++17 you can even move elements from one `map` to the other without invalidating iterators to them (and if properly implemented without any potential allocation).
    - `map` timings for single operations are typically more consistent since they never need large allocations.
    - `unordered_map` using `std::hash` as implemented in the libstdc++ is vulnerable to DoS if fed with untrusted input (it uses MurmurHash2 with a constant seed - not that seeding would really help, see https://emboss.github.io/blog/2012/12/14/breaking-murmur-hash-flooding-dos-reloaded/).
    - Being ordered enables efficient range searches, e.g. iterate over all elements with key ≥ 42.
      ---
      via: [c++ - Is there any advantage of using map over unordered_map in case of trivial keys? - Stack Overflow](https://stackoverflow.com/questions/2196995/is-there-any-advantage-of-using-map-over-unordered-map-in-case-of-trivial-keys)
  - Use `std::unordered_map` when
    collapsed:: true
    - You need to keep count of some data (Example – strings) and no ordering is required.
    - You need single element access i.e. no traversal.
  -