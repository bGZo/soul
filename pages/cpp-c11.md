- 新的循环
  - ```c
    int main() {
      int array[] = { 1,2,3,4,5,'\0' };
      for (int i : array)i *= 2;
      for (int i = 0; array[i] != '\0'; i++)cout << array[i] << " ";
      cout << endl;
      for (int &i : array)i *= 2;
      for (int i = 0; array[i] != '\0'; i++)cout << array[i] << " ";
    }
    ```
  - 运行结果是
    `1 2 3 4 5`
    `2 4 6 8 10`
  - 这个循环大有来历，当初问老师老师也不承认这是C++的标准写法，但是整洁度还是让我比较向往这样的写法。
  - 自己仿照这个循环自己写了一个小小的循环，这个循环叫foreach循环，是从Java引用过来的？！**是C++11的新特点**。其实还是有点懵逼
    - ```c
      void printLOVE() {
        char arr[] = { 'I','O','E','V','L',' ','U','Y','O'};
        int index[] = { 0,5,4,1,3,2,5,7,8,6 };
        for (int i : index) {
      cout << arr[i];
        }
      }
      ```
    - 把数组 a中所有的数，一一 赋给 b,并且 每赋值一个数 执行{}中的 代码一次