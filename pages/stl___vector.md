title:: stl/vector
alias:: cpp/stl/vector
- assign: 替换旧元素为向量元素分配新值
  - ``` c++
        void assign(const_iterator first,const_iterator last); // 将区间[first,last)的元素赋值到当前的vector容器
        void assign(size_type n,const T& x = T()); //赋n个值为x的元素到vector容器中
    ```
- 遍历
  - ``` c++
        auto first = intervals.begin(), end = intervals.end(); //迭代器
        //vector<vector<int>>::iterator iter;
        while (first != end){
            cout << (*first)[0] << (*first)[1] << ' \n';//下标
            //for (int i = 0; i < (*first).size(); ++i) cout << (*first)[i] << " " ;
            ++first;
        }
    ```
- pointer
  - ```cpp
    //via: https://stackoverflow.com/questions/6946217/how-to-access-the-contents-of-a-vector-from-a-pointer-to-the-vector-in-c
    int main(int nArgs, char ** vArgs){
        vector<int> *v = new vector<int>(10);
        v->at(2); //Retrieve using pointer to member
        v->operator[](2); //Retrieve using pointer to operator member
        v->size(); //Retrieve size
        vector<int> &vr = *v; //Create a reference
        vr[2]; //Normal access through reference
        delete &vr; //Delete the reference. You could do the same with
                    //a pointer (but not both!)
    }
    ```
  -