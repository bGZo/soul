-
- Custom Compare Function
  - > **comp** - comparison function which ==returns ​*true* if the first argument is less than the second==. The signature of the comparison function should be equivalent to the following:  `bool cmp(const Type1 &a, const Type2 &b);`
    More via: [http://en.cppreference.com/w/cpp/algorithm/sort](http://en.cppreference.com/w/cpp/algorithm/sort).
    - ```
      template< class RandomIt, class Compare >
      void sort( RandomIt first, RandomIt last, Compare comp );
      ```
  - 意思就是说, 如果 第一次参数 < 第二个参数, 那么就符合规则(`true`), 所以最终得到的结果是从大到小, 因为 不符合规则的(false) 都丢到后面去了
    - 这样我们就可以更加 #[[abstract]] 一点, 如果我们想要让某个值排得考前一点, 那么我们就可以把他写成小于的那一方
  - Custom C++14 polymorphic lambda:
    - ```
      std::sort(std::begin(container), std::end(container),
              [] (const auto& lhs, const auto& rhs) {
        return lhs.first < rhs.first;
      });
      ```
-
- Refs
  - [c++ custom compare function for std::sort() - Stack Overflow](https://stackoverflow.com/questions/16894700/c-custom-compare-function-for-stdsort)