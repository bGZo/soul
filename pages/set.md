icon:: 📄
also:: 集合 
created:: [[20240821]]
description:: 
type:: data-structure

- ## Why
  -
- ## How
  -
- ## What
  - [[cpp]]
    - set 容器内的元素会被自动排序，set 与 map 不同，set 中的元素即是键值又是实值，set 不允许两个元素有相同的键值。不能通过 set 的迭代器去修改 set 元素，原因是修改元素会破坏 set 组织。
    - 用法:
      - ``` c++
            set<int> a;
            set<int> b(a);// set<int> b(a.begin(), a.end());
            int n[] = { 1, 2, 3, 4, 5 };
            list<int> a(n, n + 5); //将数组n的前5个元素作为集合a的初值
            a.size(); //大小
            a.max_size(); //最大容量, 根据什么判断???, 我本机461168601842738790, 网上214748364
            a.empty(); //容器判空
            a.count(key); //查找键 key 的元素个数
            a.insert(const T& x); //在容器中插入元素
            a.insert(iterator it, const T& x); //任意位置插入一个元素
            a.pop_back(const T& elem); //删除容器中值为 elem 的元素
            a.erase(iterator it); //删除it迭代器所指的元素
            a.erase(iterator first, iterator last); //删除区间 [first,last] 之间的所有元素
            a.clear(); //清空所有元素
            a.find(key); //查找键 key 是否存在,若存在，返回该键的元素的迭代器；若不存在，返回set.end()
            swap(set&, set&); //lst.swap(set&); //交换两个同类型容器的元素：
        ```
      - 遍历只可以使用迭代器
      - `vector` 去重
        - ``` c++
                void removeRepeat(vector<int> &target){ // set means other function -> sort
                    set<int> temp(target.begin(), target.end());
                    target.assign(temp.begin(), temp.end());
                }
                void removeRepeat(vector<int> &target){
                    sort(vec.begin(),vec.end());
                    auto it = unique(vec.begin(), vec.end());
                    vec.erase(it, vec.end());
                }
                // unique让所有重复的数都放到最后，返回一个迭代器
          ```
      -
  -
- ## Namespace
  - {{namespace set}}
- ## ↩ Reference
  -
-