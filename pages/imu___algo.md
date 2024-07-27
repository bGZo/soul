tags:: TODO

- 各种函数的增长趋势的排序：c < log2n < n < nlog2n < n2 < n3 < 2n < 3n < n!
- 当T(n)为对数函数(log2n)，幂函数(n2,n3…)或它们的乘积(nlog2n)时，算法的运行时间是可以接受的，我们称这些算法为有效的算法。 当T(n)为指数函数(2n)或阶乘函数(n!)时，算法的运行时间随n而迅速增大，是不可接受的。我们称这些算法是“坏”的算法或无效的算法。
- ![image.png](https://cdn.nlark.com/yuque/0/2021/png/1114914/1609986890233-b44d3803-7d5d-4f8b-bfde-2400729f0a74.png#align=left&display=inline&height=265&margin=%5Bobject%20Object%5D&name=image.png&originHeight=529&originWidth=897&size=59930&status=done&style=none&width=448.5)
- # 栈与队列
- ## 栈
- ### ADT栈 
  栈是一种操作受限的线性表，它的插入和删除操作只允许在表的同一端进行。  
  允许插入和删除    的一端称为栈顶 (top)，另一端称为栈底(bottom)。 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600946665186-527a5f75-9035-4ca6-bc3c-06e027427933.png#align=left&display=inline&height=170&margin=%5Bobject%20Object%5D&name=image.png&originHeight=339&originWidth=385&size=18804&status=done&style=none&width=192.5)
  栈结构的特点：先进后出(First In Last Out, FILO)或者后进先出(Last In First Out, LIFO)。 
  栈结构的特点：先进后出(First In Last Out, FILO)或者后进先出(Last In First Out, LIFO)。
- 假设栈S=(a0, a1, …, an-1)，a0是栈底元素，an-1是栈顶元素。
- 入栈（插入操作）的顺序为a0, a1, …, an-1
- 出栈（删除操作）的顺序为an-1, an-2, …, a0 
  ```cpp
  ADT Stack {
     Data
        数据元素表
        top: 栈顶位置
     Operations
         Constructor
              Process: 创建一个空栈
         IsEmpty
              Process: 判断栈是否为空
              Output: 如果栈为空，则返回true，否则返回false
         GetTop
              Process: 取栈顶元素
              Output: 返回栈顶元素
       Push      // 入栈
             Input: 要添加的数据元素
             Process: 向栈中添加元素x
         Pop       // 出栈
              Process: 删除栈顶元素
              Output: 返回栈顶元素
         Clear
              Process: 删除栈中所有元素并置新的栈顶
   } //Stack
  ```
- ### 栈的实现
  栈结构的实现方式：
- 顺序存储
  - 一维数组，栈有大小限制。
- 链式存储
  - 链表实现，栈无大小限制。
- #### 栈的顺序（数组）存储表示 — 顺序栈 
  定义顺序栈时，应包括以下内容：
- 顺序表（数组）：StackList
- 栈顶下标：top
  - 当栈为空时，top=-1；
  - 每当一个元素入栈，top的值增1；
  - 每当一个元素出栈，top的值减1。 
    ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600946846205-4764f62b-b257-4024-8652-12d7858220d5.png#align=left&display=inline&height=87&margin=%5Bobject%20Object%5D&name=image.png&originHeight=173&originWidth=918&size=18029&status=done&style=none&width=459)
    ```cpp
    const int MaxStackSize=50; //栈最大容量
    class SeqStack {
        DataType StackList[MaxStackSize];
        int top;	             //栈顶指针
     public:
        SeqStack( );                  //构造函数
        bool IsEmpty( );
        bool IsFull( ) ;
        DataType GetTop( );        //取栈顶
        void Push(const DataType x);       //入栈
        DataType Pop( );              //出栈	
        void Clear( ) ;                 //置栈空
    }; //SeqStack
     SeqStack::SeqStack( ) {  //构造函数，初始化一个空栈
       StackList = new DataType[MaxStackSize];
       top=-1;
        } //SeqStack
       bool SeqStack::IsEmpty( ) {  //判断栈是否为空
      if(top==-1)     return true;
      else      return false;
        } //IsEmpty
    bool SeqStack::IsFull( ) //判断栈是否已满
    {
     if(top==MaxStackSize-1)
          return true;
     else
         return false;
     } //IsFull
    DataType SeqStack::GetTop( ) //取栈顶元素
    {
     if (IsEmpty( ))
    {
          cout<<"栈空!"<<endl;
          return nulldata;
     }
     return StackList[top];
    } //GetTop
    void SeqStack::Push(DataType x) //入栈
    {
     if (IsFull( ))
         cout<<"栈满!"<<endl;
    else
        StackList[++top] = x;
    } //Push
    DataType SeqStack::Pop( )   //出栈
    {
        if (IsEmpty( ))
        {
       cout<<"栈空!"<<endl;
       return nulldata;
        }
        return StackList[top--];
    } //Pop
    ```
    ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600946919009-1ec8a4c8-cf30-4e08-a259-d125dfaf8e27.png#align=left&display=inline&height=288&margin=%5Bobject%20Object%5D&name=image.png&originHeight=576&originWidth=943&size=49897&status=done&style=none&width=471.5)
    ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600946986766-8872f5b7-0a29-4f7b-b2e9-61d779c43bdf.png#align=left&display=inline&height=290&margin=%5Bobject%20Object%5D&name=image.png&originHeight=580&originWidth=730&size=40062&status=done&style=none&width=365)
    算法分析：
- 以上有关栈的各种操作与栈中元素个数无关。 时间复杂度均为**O(1)**。
- 定义顺序栈时，应该知道所需的最大栈长度。 如果事先无法预知栈的最大长度，可以采用**链式栈**。
- #### 栈的链式存储表示 — 链式栈 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947057982-d080100c-8d79-4b6b-a24f-48903dd32cb3.png#align=left&display=inline&height=36&margin=%5Bobject%20Object%5D&name=image.png&originHeight=72&originWidth=779&size=4163&status=done&style=none&width=389.5)
- 链式栈空间可扩充，无栈满(溢出)问题；
- 插入与删除仅在栈顶处执行；
- 链式栈的栈顶在**链表头**；
- 对于**带头结点**的链式栈，栈空的条件是**top->next==NULL**。 
  ```cpp
  class StackNode {
       DataType data;           //结点数据	
       StackNode *next;       //结点指针	
  public:
      StackNode( DataType d=nulldata )
      {  data=d; next=NULL; }
       friend class LinkStack;
  }; //StackNode
  class LinkStack {
      StackNode *top;            //栈顶指针
  public:
      LinkStack( )
      { top=new StackNode(); top->next=NULL; } //创建头结点
      void Push(DataType data);   //入栈
      DataType Pop( );                   //出栈
  DataType GetTop( );           // 读栈顶元素
  void Clear( ); //清空栈
  bool IsEmpty( ) {return top->next == NULL; } //判栈空
  };  //LinkStack
  void LinkStack:: Push(DataType item)
  { //入栈操作
     p=new StackNode (item);
     p->next=top->next; //类似于头插法
     top->next=p;
  } //Push
  DataType LinkStack:: Pop( )
  {//出栈操作
    if ( top->next!=NULL ){
         p = top->next;
         retvalue = p->data;	      //暂存栈顶数据
         top ->next= p->next;         //修改栈顶指针
         delete p;
         return retvalue;
    }//释放，返回数据
    else{//栈空的情况
        cout<<"The stack is empty!"<<endl;
        return nulldata;
    }
  } //Pop
  DataType LinkStack:: GetTop( ) //取栈顶元素操作
  {
    if (top->next!=NULL)
        return top->next->data;
    else //栈空的情况
    {
        cout<<"The stack is empty!"<<endl;
        return nulldata;
    }
  } //GetTop
  ```
- ## 队列 ( Queue ) 
  一种操作受限的线性表，只允许在一端删除，在另一端插入。 允许删除的一端叫做队头(front)，允许插入的一端叫做队尾(rear)。 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947211887-7860137c-364b-4d76-98df-13439a7b80b3.png#align=left&display=inline&height=87&margin=%5Bobject%20Object%5D&name=image.png&originHeight=173&originWidth=605&size=8986&status=done&style=none&width=302.5)
  **特性** 先进先出(FIFO, First In First Out)
- ### ADT 队列 
  ```cpp
  ADT Queue {
  Data
       数据项列表
       front: 队列中第一个元素的位置
       rear:  队列中最后一个元素的位置
  Operations
       Constructor
         Process: 初始化队首和队尾
  IsEmpty
   Process: 判断是否为空队列
   Output: 若队列空，返回true，否则返回false
  Front
   Process: 取出队头元素
   Output: 返回队头元素
  ClearQueue
   Process: 删除队列中所有元素并设置初始状态
  IsFull
   Process: 判断队列是否已满
   Output: 若队列已满，返回true，否则返回false
  Enter
    Input: 要进入队列的元素
     Process: 在队尾插入新的元素
  Leave
    Process: 删除队头元素
    Output: 返回队头元素
  } //Queue
  ```
- ### 队列的实现 
  队列的实现方式：（类似于线性表、栈）
- 顺序存储
  - 一维数组，队列长度有限制。
- 链式存储
  - 链表实现，队列长度无限制。 
    在队列的顺序存储表示中：
- 用一维数组来存放数据元素：
  - 一维数组：QueueList[MaxQSize]
- 设置两个变量分别指向队头和队尾的位置：
  - 队头位置：front
  - 队尾位置：rear 
    顺序队列的定义如下：
    ```cpp
    const int MaxQSize=50; //队列中数据元素的上限
    class SeqQueue {
        DataType QueueList[MaxQSize]; //数据元素列表
        int front, rear; //指向队头和队尾位置的变量
      public:
        SeqQueue( ); //构造函数，建立空队列
        void Enter(DataType item); //入队列
    DataType Leave( );  //出队列
        void Clear( );  //清空队列
        DataType Front( ); //取出队头元素
        bool IsEmpty( );  //判断队列是否为空
        bool IsFull( );  //判断队列是否已满
    }; //SeqQueue
    ```
    **入队原则** : 入队时，先将新元素放入 rear 指示的位置，再将尾指针增1.   rear = rear + 1。rear始终指示队尾元素的下一个位置。 
    **出队原则** :出队时，先将下标为 front 的元素取出，再将头指针增一 front = front + 1。front始终指示队头元素的位置。 
    **空队列和满队列的条件**
- 空队列的条件：front == rear == 0;
- 满队列的条件：rear == MaxQSize; 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947462220-4c59618d-0eb6-4b41-ad7f-afa6f3236701.png#align=left&display=inline&height=251&margin=%5Bobject%20Object%5D&name=image.png&originHeight=501&originWidth=938&size=51151&status=done&style=none&width=469)
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947496249-f09e8424-6e8f-49ae-8187-cce91677bd1b.png#align=left&display=inline&height=270&margin=%5Bobject%20Object%5D&name=image.png&originHeight=540&originWidth=945&size=71247&status=done&style=none&width=472.5)
  “假溢出”的解决方法 
  1. 固定队头
   1. 出队方式发生改变：一个数据出队后，队列中其余数据均向前移动（包括rear）。
   1. 入队方式不变。
  2. 固定队尾
   1. 入队方式发生改变：一个数据入队时，队列中其余数据先向前移动（包括front），然后该数据入队尾。
   1. 出队方式不变。
  上述两种方法的缺点：在入队和出队时需要移动队列中的所有数据元素。 
  3. 循环队列
   1. 基本思想：为了不移动数据，将队列设想成环形（首尾相接）。
   1. 让QueueList[0]接在QueueList[MaxQSize-1]之后，若rear==MaxQSize，则令rear=0。 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947598665-a0e39ec6-a544-46e5-bb68-427e29fe1e8b.png#align=left&display=inline&height=135&margin=%5Bobject%20Object%5D&name=image.png&originHeight=269&originWidth=394&size=21462&status=done&style=none&width=197)
   1. 初始队列：front = rear = 0。
   1. 入队方式变为：当一个数据入队时，仍先将数据存入队尾rear指示的位置，然后rear执行如下操作：rear = (rear + 1) % MaxQSize。
   1. 出队方式变为：当一个数据出队时，仍先将队头front指示的数据取出，然后front执行如下操作：front = (front +1) % MaxQSize。 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947663222-48e9df6c-cba4-466f-9d16-e2764a218ee3.png#align=left&display=inline&height=281&margin=%5Bobject%20Object%5D&name=image.png&originHeight=561&originWidth=950&size=88915&status=done&style=none&width=475)
  约定
  1. front==rear时，表示队空
  1. 队尾的位置加1等于队头位置（队尾rear指向队头front的前一个位置）为队满的情况，因此队满的条件是(rear+1) % MaxQSize==front
  说明：这种处理方法使得队列中存在一个空单元。
- 队列初始化：front = rear = 0;
- 队空条件：front == rear;
- 队满条件：(rear + 1) % MaxQSize == front; 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947757894-a97dfc4e-ab5c-4a52-8ba2-974a2fda534d.png#align=left&display=inline&height=176&margin=%5Bobject%20Object%5D&name=image.png&originHeight=351&originWidth=928&size=123435&status=done&style=none&width=464)
  ```cpp
  SeqQueue::SeqQueue( ){//构造函数，初始化一个空队列
      front=rear=0;
  } //SeqQueue
  void SeqQueue::ClearQueue( ) {  //清空队列
      rear=front;
  } //ClearQueue
  bool SeqQueue::IsEmpty( ) {    //判断队列是否为空
  if(rear==front)
      return true;
  else  return false;
  } //IsEmpty
  bool SeqQueue::IsFull( ) {    //判断队列是否已满
    if((rear+1)%MaxQSize==front)
        return true;
    else  return false;
  } //IsFull
  void SeqQueue::Enter(DataType item) {   //入队操作
       if(IsFull( )) //判断是否队满
               cout<<"队列已满，不能入队!"<<endl;
      else {
          QueueList[rear]=item;
          rear = (rear+1)%MaxQSize;
       }
  } //Enter
  DataType SeqQueue::Leave( ) {    //出队操作
  　if(IsEmpty( )) {     //判断是否队空
         cout<<"队列已空，不能出队!"<<endl;
         return nulldata;
     }
     retvalue = QueueList[front];
     front = (front+1)%MaxQSize;
     return retvalue;
  } //Leave
  ```
  算法分析:
- 以上有关循环队列的各种操作与队列中元素个数无关。
  - 它们的时间复杂度均为O(1)。
- 定义顺序队列时，应该知道所需的最大队列长度。
  - 如果事先无法预知队列的最大长度，可以采用链式队列。
- #### 队列的链式存储表示 — 链式队列 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600947884020-87fc1239-8f8b-49a7-935b-2c0afb5e9101.png#align=left&display=inline&height=56&margin=%5Bobject%20Object%5D&name=image.png&originHeight=112&originWidth=769&size=9686&status=done&style=none&width=384.5)
- 队头在链表头，队尾在链表尾。
- 链式队列在入队时无队满问题，但出队有队空问题。
- 对于带有头结点的链式队列的队空条件是 front->next == NULL 或者 front == rear。 
  ```cpp
  class QNode {  //链队列的结点类
    DataType  data;
    QNode *next;
   public:
     QNode(DataType item=nulldata) {
           data= item;
           next=NULL;
     }
     friend class LinkQueue;
  }; //QNode
  class LinkQueue {
     QNnode *front, *rear; //front指向头结点，rear指向真正队尾
  public:
      LinkQueue( ) { rear = front = new QNode( );  }
      void Enter(DataType item );   //入队
      DataType Leave( );		//出队		
      DataType Front( );		//取队头元素
      void Clear( ); //清空队列
      bool IsEmpty() { return front –>next == NULL; }
   }; //LinkQueue
  void LinkQueue::Enter( DataType item ) {  //入队操作
     //将新元素item插入到队列的队尾
     rear->next = new QNode (item);
     rear=rear->next;
  }  //Enter
  DataType LinkQueue::Leave( ) {  //出队操作, 删去队头结点
      if(!IsEmpty( )){	//队不空
         p = front->next;		
         DataType retvalue = p->data;	//保存队头的值
         front->next = p->next;
         delete p;
         if(front->next==NULL) //删除队列中唯一结点后，重新设置rear
               rear=front;
         return retvalue;
      }
      else   { cout<<"队列空!"<<endl;     return nulldata;   }
  }  //Leave
  DataType LinkQueue::Front( ) {       //取队头元素
      if(!IsEmpty( ))			
         return front->next->data;	
     else {
        cout<<"队列空，无队头元素!"<<endl;
        return nulldata;
    }
  } //Front
  void LinkQueue::Clear( ) {   //清空队列
     p=front->next;
     while(p) {
           front->next=p->next;
           delete p;
           p=front->next;
    }
    rear=front;
  }
  ```
- ## 栈与队列的应用
- ### 栈的应用
- #### 数制转换问题
  将十进制数N转换为r进制的数，其转换方法利用辗转相除法：以N=3467，r=8为例转换方法如下： 
  得到的8进制数是按低位到高位的顺序产生的，而通常的输出是从高位到低位的，恰好与计算过程相反，因此转换过程中每得到一位8进制数可进栈保存，转换完毕后依次出栈即为转换结果。 
  当N>0时重复(1)和(2)
  1. 若N≠0，则将N % r 压入栈s中，执行(2)；若N=0，则将栈s中的内容依次出栈，算法结束。
  1. 用N / r的结果代替 N，返回(1)。 
  算法描述如下：
  ```cpp
  void conversion(int N，int r) {
   SeqStack  s;  int  x;
   while( N ) {
         s.Push(N % r);
         N=N / r ;
    } //while
    while (! s.IsEmpty( )) {
       x=s.Pop( );
       cout<<x;
    } //while
  } //conversion
  ```
- #### 表达式求值—中缀算术表达式
- 一个表达式由操作数(亦称运算对象)、操作符(亦称运算符)和分界符组成。
- 运算符从操作数的个数上分为单目、双目和三目；从类型上分为算术运算符、关系运算符、逻辑运算符等。
- 在本应用中，只讨论由双目算术运算符构成的算术表达式的求值问题。 
  在计算机中，算术表达式有三种表示形式：
  1. 中缀(infix)表示: <操作数> <操作符> <操作数>，如 A+B；
  1. 前缀(prefix)表示     <操作符> <操作数> <操作数>，如 +AB；
  1. 后缀(postfix)表示       <操作数> <操作数> <操作符>，如 AB+； 
  中缀表达式    a + b * ( c - d ) - e / f
  后缀表达式    a b c d - * + e f / -
- 中缀算术表达式：每个双目算术运算符在两个操作数中间，假设此处讨论的双目算术运算符仅包括：+、-、*、/、^(乘方)和括号( )。
- 表达式中相邻两个运算符的计算次序为： 优先级高的先计算；
  - 优先级相同的自左向右计算； 当使用括号时从最内层括号开始计算; 乘方连续出现时先算最右面的。 
    运算符间的优先关系(1和2相继出现的运算符) 
    ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600948756876-412527c0-cdc0-4ba1-9ba9-1363805782d3.png#align=left&display=inline&height=245&margin=%5Bobject%20Object%5D&name=image.png&originHeight=490&originWidth=688&size=25608&status=done&style=none&width=344)
    算法思想：
    设定两个栈：操作数栈 OPND，操作符栈 OPTR；
- 栈初始化：置操作数栈 OPND 为空；操作符栈 OPTR 中预设一个优先级最低的操作符'#'；
- 自左向右依次读入表达式的每个字符：是操作数则入OPND栈，是操作符则要进行如下判断：
  - 如果OPTR的栈顶元素(1)＜读入的操作符(2) ，则将操作符(2)入OPTR栈
  - 如果OPTR的栈顶元素(1)==读入的操作符(2) 且1不为'#'，则从OPTR栈中弹出栈顶元素（括号运算符）；否则，算法结束（ 1= 2='#'）
  - 如果OPTR的栈顶元素(1)＞读入的操作符(2) ，则操作数栈 OPND弹出两个操作数，OPTR栈弹出一个操作符进行计算，并将结果压入 OPND栈。此时，不读取表达式，而是直接判断（1）~（3）。 
    计算中缀表达式：3*2^(4+2*1)-5\#的值 
    | **读入的字符** | **  操作数栈s1** | ** 运算符栈s2** | **           说明** |
    | --- | --- | --- | --- |
    | **3** | **3** | **#** | **3入栈s1** |
    | ***** | **3** | **#*** | ***入栈s2** |
    | **2** | **3，2** | **#*** | **2入栈s1** |
    | **^** | **3，2** | **#*^** | **^入栈s2** |
    | **(** | **3，2** | **#*^(** | **(入栈s2** |
    | **4** | **3，2，4** | **#*^(** | **4入栈s1** |
    | **+** | **3，2，4** | **#*^(+** | **+入栈s2** |
    | **2** | **3，2，4，2** | **#*^(+** | **2入栈s1** |
    | ***** | **3，2，4，2** | **#*^(+*** | ***入栈s2** |
    ```cpp
    void EvaluateExpression(OperandType &result) {
      //s1为操作数栈，s2为操作符栈，OP为运算符集合
       //OP={‘^’, ‘*’, ‘/’, ‘+’, ‘-’, ‘(’, ‘)’, ‘#’};
     SeqStack s1, s2;
     s2.Push('#');     ch=cin.get( );
     while((ch!='#')||(s2.GetTop( )!='#')) {
         if (!In(ch,OP)) {
              s1.Push(ch);
              ch=cin.get( );
         }
        else
        switch(compare(s2.GetTop( ), ch) //s2.GetTop( )为1, ch为2
        {        case '<':  s2.Push(ch); ch=cin.get( ); break;
                  case '=': s2.Pop( ); ch=cin.get( ); break;
                  case '>':  temat=s2.Pop( );
                                  b=s1.Pop( ); a=s1.Pop( );
                                  result= Operate(a, temat, b);
                                  s1.Push(result);
                                  break;
        } //switch
        } //while
        result=s1.GetTop( );
    } //EvaluateExpression
    ```
- #### 表达式求值—后缀算术表达式
  后缀表达式：是运算符在操作数之后的形式，也称“逆波兰式”。
- 在编译器中，通常先将表达式的中缀形成转成后缀形式，然后再进行计算。
- 好处：后缀表达式无需括号，并且表达式的计算只需按运算符出现的顺序（从左至右）依次进行，不用考虑运算符的优先级。
- 如何得到后缀表达式？（这个问题留给大家去解决。）
- 在后缀表达式中，变量和数字仍然按其出现的顺序依次输入，而操作符（运算符）是在其操作数都已输入后再输入。
- 例如：表达式“a+b*c”的后缀形式“abc*+” 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600949099317-76f0b10e-81be-41cc-88a8-f3cd95326372.png#align=left&display=inline&height=95&margin=%5Bobject%20Object%5D&name=image.png&originHeight=190&originWidth=643&size=15268&status=done&style=none&width=321.5)
  只需设定一个栈结构，并顺序扫描表达式的每一项，根据它的类型做如下相应操作：
- 若该项是操作数，则将其入栈；
- 若该项是操作符<op>，则连续从栈中退出两个操作数Y和X，形成运算指令X<op>Y，并将计算结果重新入栈。
- 当表达式的所有项都扫描并处理完后，栈顶存放的就是最后的计算结果。
- 例： ABCD- * + EF ^G / - 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600949159393-c82cdf2a-841e-4db5-b1e9-7dde8787324d.png#align=left&display=inline&height=314&margin=%5Bobject%20Object%5D&name=image.png&originHeight=628&originWidth=802&size=91911&status=done&style=none&width=401)
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600949181171-1631a5a7-f910-4713-b711-ef7005939515.png#align=left&display=inline&height=265&margin=%5Bobject%20Object%5D&name=image.png&originHeight=529&originWidth=802&size=82571&status=done&style=none&width=401)
  ```cpp
  void CalcuPostfix( OperandType &result) {
    //OP={‘^’, ‘*’, ‘/’, ‘+’, ‘-’, ‘#’};
    SeqStack s;    ch=cin.get( );
    while(ch!='#') {
          if (!In(ch, OP))      s.Push(ch);
          else  {
                    b=s.Pop( ); a=s.Pop( );
                    result= Operate(a, ch, b);
                    s.Push(result);
                    } //end else
         ch=cin.get( );
    } //end while
    return result;
  }
  ```
- ### 队列的应用
- #### 舞伴问题
  舞会在星期五晚举行。舞会开始之前，参加舞会的男士和女士各自排队进入舞厅。舞会开始，从两队中按顺序组成舞伴开始跳舞。一曲结束后，男士和女士分别再进入各自队列。如果男士和女士人数不等，则多出的人只能等到下一舞曲开始。
  要求用算法来模拟一支舞曲开始后男士和女士组成舞伴的情况，以及多少人在等待的情况。 
  用两个队列来表示男士和女士等待队列，舞会开始前时，按其性别加入不同队列，舞曲开始后，顺序地同时删除两个队列的元素来组成舞伴，直到某一队列为空。 
  ```cpp
  class  Person{               //Person为跳舞人的类
    char *name;
    char sex;                //F为男，M为女
  };
  void Dance_parnter() {
    SeqQueue  M_Dancer, F_Dancer;
    // M_Dancer为男士队列，F_Dancer为女士队列
    Person p;                  //Person为跳舞人的类
    Person_arrive(p,name,sex);
     //有人到达舞会，将其姓名和性别赋给p
     //p.name=name; p.sex=sex;
  //根据来人的性别建立男士队列和女士队列
  while(strcmp(p.name,"#")<>0) {
   //将男士和女士分别入各自队列
   if (p.sex= ='F')
       F_Dancer.Enter(p);
   else
       M_Dancer.Enter(p);
   Person_arrive(p, name, sex);
  } //while
  if(!M_Dancer.IsEmpty( )){    //女士队列为空
         cout<<"There are "<<M_Dancer.Length( )<<
              " men  waiting for the next round."<<endl;
  }
  else if(!F_Dancer.IsEmpty( )){   //男士队列为空
         cout<<"There are "<<F_Dancer.Length( )<<
              " women waiting for the next round."<<endl;
  }
  } //Dance_partner
  ```
  P76: 2 P77: 4，5-(1) 上机实验：实验2、实验3 
  ```cpp
  练习题1
  void  main( )  {
      Queue  Q;
      char  x='e';  y='c';
       Q.Enter('h');  Q.Enter('r');
       Q.Enter(y);   x=Q.Leave();
       Q.Enter(x);   x=Q.Leave();
       Q.Enter('a');
       while(!Q.IsEmpty())  {
           y=Q.Leave();
           cout<<y;    }
        cout<<x;
  }
  ```
- # 线性表
- ## 线性结构
  线性表，数组和第三章中的栈、队列都属于线性结构。
- #### 特点
  1. 具有唯一的第一个数据元素(无前驱)；
  1. 具有唯一的最后一个数据元素(无后继) ；
  1. 其他数据元素都有且仅有一个前驱和一个后继。
- ## 线性表 (Linear List) 
  由n(>=0)个性质相同的数据元素组成的有限序列，记作：L=（a1, a2, …, an）其中：ai是表中的第i个数据元素，n是表长度。 
  注意： 数据元素的个数n被定义为表的长度。当n=0时，称为空表。 这里的数据元素ai(1in)只是一个抽象的符号，其具体含义在不同情况下可以不同。
- ### 特点（非空线性表）：
  1. 有且仅有一个开始结点a1，它没有(直接)前趋，但仅有一个(直接)后继a2；
  1. 有且仅有一个终端结点an，它没有(直接)后继，但仅有一个(直接)前趋an-1；
  1. 其余的内部结点ai(2<= i <=n-1)都有且仅有一个(直接)前趋ai-1和一个(直接)后继ai+1。
  线性表是一种典型的线性结构。
- ### 抽象数据类型（ADT）线性表：
  ```cpp
  ADT List{
  Data //数据元素表：是n(n  0)个数据元素的一个有限序列，其中每个数据元素的数据类型为
  DataType
      size//数据元素的个数
  Operation
      Constructor
      Process//创建空表
  Clear
      Process//清空线性表  　
  IsEmpty
      Process//判断线性表是否为空
      Output//若线性表为空, 返回true, 否则返回false
   Length
      Process//求线性表中元素个数
      Output//返回线性表中元素个数
   Get
      Input//要取出的元素的位置
      Process//取出指定位置上的元素
      Output//返回取出的元素值
   Locate
      Input//要定位的元素
      Process//为指定元素定位
      Output//若线性表中有给定元素，返回元素位置,否则返回-1
   Insert
      Input//被插入元素值及其位置  　
      Process//将给定元素插入指定位置
   Delete  　
      Input//被删除元素的位置  　
      Process//若线性表中有给定元素，则删除它
  Prior
      Input//要求前驱的元素
      Process//求给定元素的直接前驱
  Next
  Input//要求后继的元素    　
      Process: 求给定元素的直接后继
  } //List
  ```
- ### 顺序表(SeqList)
  把线性表的元素按逻辑顺序依次存放在一组地址连续的存储单元里。
- #### 存储结构与逻辑结构的0关系：
  以“存储位置相邻”表示有序对<ai-1，ai>，即：
  LOC(ai)=LOC(ai-1)+m。
  任一个数据元素的存储位置均取决于第一个数据元素的存储位置：
  LOC(ai) = LOC(a1) + (i -1)×m
- #### 存储结构与逻辑结构的关系
  一维数组在内存中都对应着一组连续的存储单元，因此常用一维数组来表示线性表的顺序存储结构。
- #### 顺序表(SeqList)实现 
  ```cpp
  const  int  MaxListSize=100;
  class SeqList{
  DataType data[MaxListSize]; //一维数组实现的线性表 && 实际问题中数据元素的类型。
  int size;            //元素的个数
  public:
  SeqList( ){size = 0;}     //构造一个空线性表
  void Clear( );        //清空表
  bool IsEmpty( );     //判断如果为空表，返回true，否则返回false
  DataType Get(int k){return data[k];}    //返回第k个元素
  int Locate(DataType e);      //返回第一个与元素e匹配的元素位序
  DataType Prior(DataType e);   //返回元素e 的前驱
  DataType Next(DataType e);    //返回元素e 的后继
  void Insert(DataType e, int i);   //在表中第 i 个位置插入新元素e
  DataType Delete(int i);        //删除第i个元素，并返回其值
  }; //SeqList
  ```
  1. 插入算法
  ```cpp
  void Insert(DataType e, int i){
  if ( i < 0 || i >size || size = = MaxListSize  )
  // i不合法或顺序表已满;
   exit;
  else {
   size++;							
   for (j=size-1; j>i; j-- )
       data[j] = data[j-1];	
   data[i] = e;  //插入成功
  }
  } //Insert
  ```
  插入算法的时间复杂度: (n-1)/2
  该算法的时间主要消耗在移动元素上。 
  平均情况：设插入每个位置的概率相等，则数据元素的平均移动次数： 
  插入算法的时间复杂度为：O(n)
  2. 删除算法 
  ```cpp
  DataType Delete( int i ){
  if (i<0 || i>= size)
      return nulldata; //被删除元素的下标不合法
  else{
       e=data[i];
   for ( int j=i; j<size; j++ )
            data[j] = data[j+1];
       size--;
       return e;	
   } 	
  } //Delete
  ```
  删除算法的时间复杂度:  (n-1)/2
  平均情况：设删除每个数据元素的概率相等，则移动数据元素的平均次数为： 
  删除算法的时间复杂度为：O(n)
  3. 查找(定位)算法
  ```cpp
  int Locate(DataType e){
  int  i = 0;
  while ( i<size && data[i]!=e )
       i++;	
  if ( i >=size )
     return -1; //没有找到
  else
      return i; //找到此元素，返回其下标
  } //Locate
  ```
  基本操作:比较 
  查找不成功: 比较 n 次 
  最好情况: 比较1次, O(1) 
  最坏情况:比较n次, O(n) 
  成功时:
  平均情况:设查找每个数据元素的概率相等，则 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600145930893-3d7e4f27-45ac-4ff5-a345-1de6291a364f.png#align=left&display=inline&height=61&margin=%5Bobject%20Object%5D&name=image.png&originHeight=122&originWidth=393&size=6338&status=done&style=none&width=196.5)
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1600145935424-15f184fd-339a-49d1-baf6-f9135d7e3a07.png#align=left&display=inline&height=120&margin=%5Bobject%20Object%5D&name=image.png&originHeight=239&originWidth=700&size=16154&status=done&style=none&width=350)
  时间复杂度：O(n)
- #### 优点
  1. 无需为表示数据元素之间的逻辑关系而增加额       外存储空间。
  1. 可方便地随机存取表中任一元素。 顺序表的缺点：
- #### 缺点
  1. 预先为数据元素分配空间。
  1. 插入和删除时必须移动大量元素。
- ### 链式存储
  逻辑上相邻的元素，其物理位置不一定相邻。
- 数据元素之间可以连续存储，也可以不连续存储;
- 数据元素的逻辑顺序与物理顺序可以不一致;
- 特点：长度可扩充。
- #### 单链表 
  1. 每个结点只有一个指针域且最后一个结点的指针域为空。
  1. 整个单链表可由头指针唯一确定。 
  1. 为了操作（插入和删除）方便，增设一个头结点。 
  注意区分: 头结点 && 首结点 && 头指针
  ```cpp
  class Node {  //结点类
    DataType  data;
    Node   *next;
  public:
    Node( ) { next=NULL; }
    friend class LinkList; //声明友元类
  }; //Node
  class  LinkList {             //链表类
    Node *head;          //头指针
    int size;                  //结点个数，头结点不计入其中
  public:
    LinkList( ) { head=new Node(); size=0; }
    void Create(int n);     //创建长度为n的单链表
    DataType Get(int i);    //返回第i个元素值
    Node* Locate(DataType e); //返回第一个与e匹配的
                                                       //元素结点指针
    bool IsEmpty( ) //判断是否为空链表
    {  return (head->next==NULL); }
  void Insert(DataType x, int i);  //在第i个结点之前插入元素值为x的结点
  Datatype Delete(int i); //删除第i个结点
  void Clear( ); //清空链表
  DataType Prior(DataType e); //返回e的前驱结点元素
  DataType Next(DataType e); //返回e的后继结点元素
  }; //LinkList
  DataType LinkList::Get(int i){ //取元素
  if( head->next==NULL)    //空链表，返回空值
    return nulldata;
  else {
    p=head; k=0;
    while(p&&k<i)
    {  p=p->next;  k++;  }
    if(!p || k==0)  return nulldata;  // i超出链表的范围
    else  return  p->data;
  }
  } //Get
  ```
- #### 插入结点 
  1. 在链表最前端插入
  ```cpp
  newnode->next = head->next;
  head->next = newnode;
  ```
  2. 在链表中间插入
  ```cpp
  newnode->next = p->next;	
  p->next = new node；
  ```
  3. 在链表末尾插入
  ```cpp
  newnode->next = p->next;	
  p->next = newnode；
  ```
  ```cpp
  void LinkList:: Insert ( DataType x, int i ) {
  //在第i个结点之前插入元素值为x的结点
  Node* p = head;  int k = 0;
  if(i<1 || i>size) exit; // 插入位置错误
  while ( p && k< i -1 )
  { p = p->next;  k++; }  //找到插入位置
  if(!p) exit;   //插入位置无效
  Node* newnode= new Node( );
  newnode->data=x;
  newnode->next=p->next;
  p->next=newnode;  size++;
  } //Insert
  ```
- #### 删除结点
  删除操作是将表的第i个结点删去。 删除过程：1）定位；2）删除。
  p→next = q→next;  delete q; 
  ```cpp
  DataType LinkList::Delete(int i)
  { //删除第i个结点
  Node* p = head; int k=0;
  if(i<1 ||i>size)     // 结点序号i超出链表结点范围，返回空值
  return nulldata;
  while ( p && k< i-1 )   //找到被删除结点的前一个元素
  { p = p->next;  k++; }
  if ( !p ) {
  cout << “Invalid position for Deletion!\n”;
  return nulldata;
  } 	
  q = p->next;    p->next = q->next;
  e= q->data;
  delete q;
  size--;    return e;
  } //Delete
  ```
- #### 建立单链表
  建立单链表的常用方法有如下两种： 头插法建表     该方法从一个空表开始，重复读入数据，生成新结点，将读入数据存放到新结点的数据域中，然后将新结点插入到当前链表的表头上，直到读入结束标志为止。 
  ```cpp
  void LinkList::Create( DataType  endTag){ //头插法建表   DataType  value;    head=new Node( );   //创建头结点
  head->next=NULL;
   cin>>value;
  while (value!=endTag) {
      size++;
      Node *p=new Node( );
      p->data=value;
      p->next=head->next;
      head->next=p;
      cin>>value;      }//while
  }
  ```
- ##### 尾插法建表    
  头插法建立链表虽然算法简单，但生成的链表中结点的次序和输入的顺序相反。若希望二者次序一致，可采用尾插法建表。 该方法是将新结点插入到当前链表的表尾上，为此必须增加一个尾指针r，使其始终指向当前链表的尾结点。
  1. 创建头指针head，使尾指针r=head；
  1. 新建结点p，如果head-> next = NULL, 则head-> next =p;r=p;
  1. 否则，r-> next =p; r=p;重复（2）、（3）实现尾插法；
  1. 如果r!= NULL; 则r-> next =NULL;
- ##### 尾插法建立单链表 
  ```cpp
  void LinkList:: Create(DataType  endTag) {
    Node  *p, *r;      head=new Node( );
    head->next=NULL;    r=head;          //尾指针
    cin>>value;
    while (vauel!=endTag) {
       size++;
       p=new Node( );
       p–>data=value;
       r–>next=p;
       r=p;
       cin>>value;   }//while
       r-> next =NULL;
  } //Create
  ```
- #### (单)循环链表 
  循环链表基本操作的实现 基本操作与单链表类似  考虑在循环链表中如何判断遍历链表的终止条件？        
  p->next==NULL? 
  应该是 p->next==head
- #### 双向链表
  双向链表：在单链表的每个结点里再增加一个指向其直接前趋结点的指针域，这样形成的链表中有两个不同方向的链，故称为双向链表。 
  双向链表的结点结构：
- ##### 双向循环链表 
  双向循环链表：首尾相连的双向链表。 
  双向循环链表的结点结构与双向链表一致：
- ##### 带头结点的双向循环链表    
  结点指向p
  ```cpp
  p→prior→next
  p→next →prior
  ```
- ##### 带头结点的双向循环链表类的定义 
  ```cpp
  class DNode{     //双向循环链表中结点定义
  DataType data;
  DNode *prior;               //指向前驱的指针
  DNode *next;                //指向后继的指针
  public:
  DNode(DataType d=nulldata)
  {
     data=d;
     prior=next=NULL;
  }
  friend class DBList;
  }; //DNode
  class DBList{                   //双向循环链表的定义
   DNode *head;
   int size;
  public:
  DBList(){head=new DNode(); size=0;}   //构造函数，创建空链表
  void Create(int n);             //创建长度为n的双链表
  DataType GetElem(int i);       //取得第i个元素
  DNode* Locate(DataType e); //返回第一个与e匹配的结点指针
  bool IsEmpty( );        //判断是否为空链表
  void Insert(DataType e, int i);  //在第i个结点前插入元素为e的结点
  DataType Delete(int i);       //删除第i个结点，并返回其元素值
  void Clear( );                //清空链表
  }; //DBList
  ```
- ##### 查找算法 
  搜索成功 
  搜索不成功
- ##### 删除算法
  ```cpp
  current ->prior->next= current ->next;
  ```
  1. current ->prior->next= current ->next; 
  2. current ->next->prior= current ->prior; 
  1. current ->prior->next= current ->next; 
  2. current ->next->prior= current ->prior; 
  3.  delete current ;
- ##### 双向循环链表的插入算法 
  1. p->prior=current; 
  2. p->next= current ->next;  
  3. current->next->prior=p; 
  4. current->next=p; 
  交换语句3和语句4将导致反向链表连接不正常。 
  3. current->next=p; 4. current->next->prior=p; 
  注意： 与单链表的插入和删除操作不同 的是，在双向（循环）链表中插入和删除必须同时修改两个方向上的指针。
- ### 顺序表和链表的比较 
  顺序表
- 没有附加存储空间开销
- 随机取得任一元素
- 预先申请固定长度的数组
- 插入、删除需要移动元素，运算时间代价O(n)
  链表
- 插入、删除运算时间代价O(1)
- 在运行时动态为表中新的元素分配存储空间
- 顺序取得某一元素
- 每个元素都有附加存储空间开销（指向下一个结点的指针） 
  **根据实际应用选择顺序表和链表**
  顺序表
- 结点总数目大概可以估计
- 表中结点比较稳定（插入、删除操作少）  
  链表
- 结点数目无法预知
- 线性表中结点动态变化（插入、删除操作多）
- ### 一元多项式求和算法 
  实例：一元多项式的链表表示 
  在一元多项式的链表表示中每个结点包含三个数据成员：  
  优点：  多项式的项数可以动态增长，不存在存储溢出问题。  插入、删除方便，不移动元素。 扫描两个多项式链表（多项式链表按指数递增排序），若都未检测完：  若当前被检测项指数相等，则系数相加，若不为0，则将结果添加到结果多项式；并且两个多项式指针均后移。  若当前被检测项指数不等，则将指数小者加到结果多项式，并且指针后移。 若一个多项式已检测完，则将另一个多项式剩余部分全部复制到结果多项式。 
  ```cpp
  下面给出一元多项式的结构说明。
  class PNode
  { //结点的定义
   float coef;  //系数
  int expn;  //指数
   PNode * next;
  public:
   PNode(float c＝0, int e＝0)
   {
  coef=c; expn=e; next=NULL;
   }
  friend class PolynList;  //友元类
  }; //PNode
  class PolynList{            //多项式链表定义
      PNode* head;
      int len;
  public:
  PolynList( ){head=new PNode();} //构造空的多项式链表
  void Create(int m);        //创建m项多项式
  void AddPolyn(PolynList&); //多项式相加
  void PrintPolyn( );          //显示多项式
  void SubstractPolyn(PolynList&); // 多项式相减
  void MultiplyPolyn(PolynList&); // 多项式相乘
  }; //PolynList
  void PolynList::Create(int m)
  {
  float  c;  	int e;
  p=head;
  for(int i=0; i<m; i++)
      {
            cin>>c>>e; //假设输入的多项式按指数递增
     p->next=new  PNode(c, e);
             p=p->next;  //尾插法
  }
  }
  两个多项式相加算法（多项式B加到A上）：
  void PolynList::AddPolyn (PolynList &bh) {
   pc=this->head;  pa=this->head->next;  pb=bh.head->next;
   delete bh.head;
   while (pa && pb) {
      a=pa->term.expn; b=pb->term.expn;    //指数
      if (a<b){    // 多项式ah(this指针)中当前结点的指数值小
           pc->next=pa; pc=pa; pa=pa->next; //pa指针后移
        }
       else  if (a>b){  //多项式bh中当前结点的指数值小
           pc->next=pb; pc=pb; pb=pb->next; //pb指针后移
        }
  else if(pa->term.coef+pb->term.coef==0){
         //两个结点系数之和为0，分别删除这两个结点；
         p=pa; pa=pa->next; delete p;
         p=pb; pb=pb->next; delete p;
   }
   else{ //将pb结点的系数加入pa结点
          pa->term.coef=pa->term.coef+pb->term.coef;
          pc->next=pa; pc=pa; pa=pa->next;
          p=pb; pb=pb->next; delete p;
    }
  } //while
  if(pa) pc->next=pa; //pb遍历完毕，将pa加到pc上
  else pc->next=pb; //pa遍历完毕，将pb加到pc上
  }
  ```
- ## 数组(Array)
  由一组类型相同的数据元素构成的有限序列，且该有限序列是存储在一块地址连续的内存单元中。 数据元素可以是整数、实数等简单数据类型，也可以是结构体、类等构造数据类型。 在数组中的各数据元素是由其下标来区分的。 当数组中的每个数据元素只有一个下标时，这样的数组称为一维数组。 将一维数组中各数据元素的下标按顺序变成线性表中的序号，则一维数组就是一个线性表（顺序表）。 当一个数组的每个数据元素都含有两个下标时，该数组称为二维数组。 当一个数组的每个数据元素都含有n个下标时，该数组称为n维数组。 
  特别地，
  一个二维数组可以看作每个数据元素都是一个一维数组的一维数组。 
  一个二维数组可以看作每个数据元素都是一个一维数组的一维数组。
  二维数组中的每个元素aij都属于两个线性表：第i行的线性表Bi和第j列线性表Aj。 
  因此，受两个下标的约束，二维数组中的每个元素aij最多有两个直接前驱和两个直接后继. a00没有直接前驱，称之为开始结点，an-1,m-1没有直接后继，称之为终端结点。 第0行的元素a0j (j=1,…,m-1)和第0列的元素ai0 (i=1,…,n-1)都只有一个直接前驱。 第n-1行的元素an-1,j(j=1,…,m-2)和第m-1列的元素ai,n-1(i=1,…,n-2)都只有一个直接后继。aij(1≤i ≤n-2,1 ≤j ≤m-2)都有两个直接前驱结点ai,j-1, ai-1,j和两个直接后继结点ai,j+1, ai+1,j。
- ### 三维数组和N维数组 
  同理，三维数组Am×n × l中每个元素属于三个线性表，每个元素最多有三个直接前驱和三个直接后继。 Ai1,i2,i3   前驱： Ai1-1,i2,i3 , Ai1,i2-1,i3, Ai1,i2,i3-1
  后继： Ai1+1,i2,i3 , Ai1,i2+1,i3, Ai1,i2,i3+1  
  推而广之 ，n维数组Ab1 ×b2 ×… ×bn中每个元素属于n个线性表，每个元素最多有n个直接前驱和n个直接后继。 Ai1,i2,…,in
  前驱：Ai1-1,i2,…,in, Ai1,i2-1,…,in,…, Ai1,i2,…,in-1
  后继：Ai1+1,i2,…,in, Ai1,i2+1,…,in,…, Ai1,i2,…,in+1
- #### 存储 
  在计算机中通常都采用顺序存储——数组的定义。 由于计算机中的存储空间（地址）是一维的，因此存放多维数组时，必须按照某种次序将数据元素排成一个一维序列。 对于多维数组，有一个次序约定的问题。 例如：二维数组可以按行顺序存储，即：先存放第0行元素，再存放第1行元素，依次类推；也可以按列顺序存储。 规定好次序，所有数据元素都可依次存放到一块地址连续的存储空间中。 只要给出一组下标，便可求出相应数据元素的存储地址（位置）。
- ### 用处
  1. 在图像处理中，经常开辟一个一维数组来存放图像数据；
  1. 为了能按图像中像素的坐标获得像素的颜色，需要计算存储地址。
- ### 方法
  每个元素占用l的存储单元。
  1. 一维数组：顺序存储 
  1. a
  1. LOC(i) = LOC(i-1)+l = a+i*l 
  2. 二维数组：
  - 顺序存储  行优先存放：设数组开始存放位置 LOC(0,0)=a,  每个元素占用 l 个存储单元，则数据元素(i, j)的存储地址为
  - LOC ( i, j ) = a + ( i * m + j ) * l
  - 列优先存放：设数组开始存放位置 LOC(0,0) = a,  每个元素占用 l 个存储单元，则数据元素(i, j)的存储地址为
  - LOC ( i, j ) = a + ( j * n + i ) * l 
    3. 三维数组: 各维元素个数为  m1, m2, m3。  下标为 i1, i2, i3的数据元素的存储地址：（按页/行/列存放）
  - LOC ( i1, i2, i3 ) = a +    ( i1* m2 * m3 + i2* m3 + i3 ) * l
  - LOC ( i1, i2, …, in ) = a +( i1_m2_m3_…_mn + i2_m3_m4_…_mn+……+ in-1_mn + in ) _ l
- #### 特殊矩阵
  非零元素或零元素的分布有一定规律的矩阵。
  对称矩阵；
  对角矩阵（带状矩阵）；
  稀疏矩
- ####
- #### 与压缩存储 
  压缩存储主要是针对特殊矩阵，为节省存储空间，对可以不存储的元素，如零元素或对称元素，不再存储。  对称矩阵的压缩存储 
  设有一个 nn 的对称矩阵 A。 在矩阵中，aij = aji 
  为了节约存储，只存对角线及对角线以上的元素，或者只存对角线及对角线以下的元素。前者称为上三角矩阵，后者称为下三角矩阵。 为了节约存储，只存对角线及对角线以上的元素，或者只存对角线及对角线以下的元素。前者称为上三角矩阵，后者称为下三角矩阵。 
  把所需元素按行存放于一个一维数组 B 中，称之为对称矩阵的压缩存储。 一维数组 B 共有 n + ( n - 1 ) +  + 1 =               n*(n+1)/2 个元素。 问题：压缩存储之后，如何在一维数组B中定位矩阵中的任意数据元素？ 
  若i ≤ j，数组元素a[i][j]在数组B中的存放位置为                                  +  j-i 
  若 i  j, 数组元素a[i][j]在数组B中的存放位置为 1 + 2 +  + i + j = (i + 1)* i / 2 + j
- ### 稀疏矩阵 (Sparse Matrix) 
  矩阵A中有s个非零元素，若s远远小于矩阵元素的总数（即s << m×n），而且这些非零元素的分布也没有规律。
  优点：  节省了存储单元
  缺点：  失去了随机存取功
- #### 实现
  存储稀疏矩阵时，为了节省存储单元，可采用只存储非零元素的压缩存储方法。 有两种实现方式：  
  1. 三元组顺序表——顺序存储
  1. 由于非零元素的分布没有规律，所以在存储非零元素时，需要同时存储该非零元素的行下标 row、列下标 col、值 value。 每一个非零元素可由一个三元组唯一确定
  1. 元素按行递增排序存放的，当行相等时是按列递增排序存放的。
  2. 十字链表——链式存储  
  ```cpp
  const int SMax=1024;
  class  SPNode{        //三元组类
   int i, j;                //非零元素的行、列
   DataType  v;    //非零元素值
   friend class SPMatrix;   //声明友元类
  }; //SPNode
  class SPMatrix{       //三元组表类
   int rn, cn, en;    //矩阵的行、列及非零元素的个数
   SPNode data[SMax];   //三元组顺序表
  public:
    SPMatrix( );
    SPMatrix(int m, int n, int s); //构造m行n列含s个非零元素的稀疏矩阵
    SPMatrix Transpose( );          //求转置矩阵
    SPMatrix Add(SPMatrix&);   //求矩阵的和
    SPMatrix Multiply(SPMatrix&);   //求矩阵的乘积
  }; //SPMatrix
  求转置矩阵算法
  for (col=0; col<nu; ++col)
      for (row=0; row<mu; ++row)
          b[col][row] = a[row][col];
  nu是a的列数(b的行数) mu是a的行数(b的列数)
  其时间复杂度为: O(mu×nu)
  ```
- #### 转置
  问题：若采用三元组顺序表存储稀疏矩阵，只要把每个元素的行下标和列下标互换，就完成了对该矩阵的转置运算，这种说法正确吗？ 
  思路:
  1. 每个元素的行下标和列下标互换（即三元组中的i和j互换）
  1. a的总行数mu和总列数nu赋为b的总列数和总行数
  1. 重排三元组表内元素的顺序，使转置后的三元组也按行（或列）优先顺序排列。 
  实现：压缩转置 
  思路：反复扫描a.smArray中的列序,从小到大依次进行转置。 
  ```cpp
  稀疏矩阵的压缩转置算法:
  SPMatrix SPMatrix::Transpose( ){
  SPMatrix T;
  T.rn=cn; T.cn=rn; T.en=en;  //将行数、列数、非零元个数赋给T
  if(en){
   q=0;
   for(col=0;col<cn;++col)
      for(p=0;p<en;++p)
         if(data[p].j==col){
            T.data[q].i= data[p].j;  T.data[q].j= data[p].i;
            T.data[q].v=data[p].v;
             ++q;
        }     }
  return T;
  }  //Transpose
  ```
  主要时间消耗在查找data[p].j==col元素， 由双重循环完成: for(col=0;col<cn;++col)    循环次数＝cn   //cn为列数         for(p=0;p<en;++p)    循环次数＝en  //en为非零元素个数     所以该算法的时间复杂度为O(cn*en)         ----即 a的列数与a中非零元素的个数之积 最坏情况：a中全是非零元素，此时en=cn*rn， //rn为行数             时间复杂度为 O(cn2*rn) 而用非压缩传统转置算法的时间复杂度也不过是O(cn*rn) 结论：压缩转置算法不能滥用。 前提：仅适用于非零元素个数很少（即en<<rn*cn）的情况。 
  稀疏矩阵的十字链表 
  三元组顺序表能够实现稀疏矩阵的压缩存储，并且适用于求稀疏矩阵的转置等运算，但对于另外一些运算，如矩阵加法、乘法等，在运算的过程中矩阵的非零元素的个数和位置经常发生改变，因此三元组顺序表不适合这些运算。 可采用链式存储结构——十字链表来实现稀疏矩阵的压缩存储。 
  十字链表 每个非零元素用一个含5个域的结点表示：     其中：row、col和val三个域分别表示该非零元素所在的行、列以及它的值；right域用来指向同一行中的下一个非零元素；down域用来指向同一列中的下一个非零元素。 
  每个非零元素用一个含5个域的结点表示：     这样，right域可将稀疏矩阵中同一行上的非零元素链接成一个链表；down域可将稀疏矩阵中同一列上的非零元素链接成一个链表。 
  每个非零元素用一个含5个域的结点表示：     每个非零元素既是某个行链表上的结点，同时又是某个列链表上的结点，整个稀疏矩阵将构成一个十字交叉的链表——十字链表。 
  课后习题： p51：2                      p53：5-(1), 5-(2), 5-(5) 上机实验：实验1
- # 树
- ### 树的定义
  树是由 n (n ≥ 0) 个结点组成的有限集合。树是一种典型的“层次结构”，体现出“一对多”的关系。
- 如果 n = 0，称为空树；
- 如果 n > 0，则
  - 有一个特定的称之为根(root)的结点，它只有直接后继，没有直接前驱;
  - 除根以外的其他结点被划分到 m (m ≥ 0) 个 互不相交的子集T1, T2, …, Tm中，每个子集又都构成一棵树，称之为根的子树(sub tree)。
- ### 相关术语
- 直接前驱 / 直接后继。
- 双亲、子女（parent, child）
- 结点的度（degree）
- 叶子（leaf）
- 分枝结点（branch node）
- 树的度
- 结点所在的层次(level)
- 深度或高(depth): 深度自上到下, 高自下而上.
- 兄弟(sibling)
- 堂兄弟(cousin)
- 祖先（descendant） 、子孙（ancestor）
- 路径（path）
- 有序树（ordered  tree）
- 森林(Forest)
- ### 二叉树 (Binary Tree) 
  一个结点的有限集合，该集合或者为空，或者是由一个根结点加上两棵分别称为左子树和右子树的、互不相交的二叉树组成。
- #### ADT描述
  ```cpp
  ADT BinaryTree {
  Data   是有限个结点的集合D。当D非空时，其中
           有一个根结点t，其余结点被分为t的左子树和
           右子树。
  Operations
     Constructor
         Process: 建立一棵空二叉树
     Delete
         Process: 删除二叉树
  IsEmpty	
    Process: 判断二叉树是否是空
    Output: 若二叉树为空，则返回true, 否则返回false
  Size
    Process: 计算二叉树的结点个数size
    Output: size
  Height
    Process: 计算二叉树的高度height
    Output: height
  Root
    Process: 取二叉树根结点的值x
    Output: 根结点的值x
  Parent
    Input: node是二叉树中的一个结点
    Process: 求node的双亲p，若node 是根，则p为空
    Output: p
  CreateBinaryTree
    Input: 二叉树的某种形式的定义
    Process: 根据此定义构造二叉树
  MakeTree
    Input: data是根结点值，left是左子树，right是右子树
    Process: 创建二叉树，data是根结点值，left是其左子树，
                    right是其右子树
  BreakTree
    Process: 拆分二叉树，data是根结点数据，left是左子树，
                    right是右子树
    Output: data, left, right
  PreOrder
    Input: Visit( )是结点访问函数
    Process: 前序遍历，对二叉树中每个结点仅调用一次Visit( )
    Output: 根据Visit( )，得到前序遍历的结果
  InOrder
    Input: Visit( )是结点访问函数
    Process: 中序遍历，对二叉树中每个结点仅调用一次Visit( )
    Output: 根据Visit( )，得到中序遍历的结果
  PostOrder
    Input: Visit( )是结点访问函数
    Process: 后序遍历，对二叉树中每个结点仅调用一次Visit( )
    Output: 根据Visit( )，得到后序遍历的结果
  LevelOrder
    Input: Visit( )是结点访问函数
    Process: 按层次对二叉树中每个结点仅调用一次Visit( )
    Output: 根据Visit( )，得到层次遍历的结果
  } //BinaryTree
  ```
- #### 完全二叉树 (Complete Binary Tree)
  若设二叉树的高度为h，则共有h层。除第 h 层外，其它各层 (1 - h-1) 的结点数都达到最大个数，第 h 层是将满二叉树从右向左连续去除若干结点，这就是完全二叉树。
- 叶结点仅在层次数最大的两层出现；
- 对任一结点，若其右子树的高度为l，则其左子树的高度为l或l+1。
- #### 遍历
- ##### 1. 前序(VLR)
- ##### 2. 中序(LVR)
- ##### 3. 后序(LRV)
- #### 性质
  1. 若二叉树的层次从1开始, 则在二叉树的第 i 层最多有 2个结点。(i ≥ 1)        
  1. **[证明用数学归纳法]**
  2. 深度为 k 的二叉树最多有 2个结点, 最少会有 k 个结点。(k ≥ 1)        ** [证明用求等比数列前k项和的公式]**
  1. 20 + 21 + … + 2k-1 = 2k-1 
  3. 对任何一棵二叉树，如果其叶结点有 n 个，度为2的非叶结点有 n 个，则有 **n****0****＝n****2****＋1 **
  1. **证明**：若设度为1的结点有 n 个，总结点个数为 n，总边数为 e，则根据二叉树的定义，n = n + n + n     e = 2n + n = n - 1 因此，有  2n2 + n1 = n0 + n1 + n2 - 1        n2 = n0 - 1         n0 = n2 + 1  
  4. 具有 n (n >= 0) 个结点的完全二叉树的高度为 [log(n+1)]
  4. 满二叉树可以用顺序结构实现
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1604830698428-aae81f37-8329-4226-8ff7-2e28f3e81343.png#align=left&display=inline&height=391&margin=%5Bobject%20Object%5D&name=image.png&originHeight=782&originWidth=1045&size=161044&status=done&style=none&width=522.5)
  补充:
- n个结点的完全二叉树的最大树枝节点:(n-1)／2
  - 满二叉树是完全二叉树的特殊形态, 即如果一棵二叉树是满二叉树, 则它必定是完全二叉树。
- #### 实现
- #### 顺序实现
- ##### 链式实现
  二叉链表中结点的定义如下：
  ```cpp
  class BinaryTreeNode {
   DataType data;
   BinaryTreeNode *leftChild, *rightChild; //左右指针
  public :
   BinaryTreeNode(DataType &e, BinaryTreeNode
                     *l=NULL, BinaryTreeNode *r=NULL)
  { data = e; leftChild = l; rightChild = r; }
   friend class BinaryTree; //声明友元类
  }; //BinaryTreeNode
  class BinaryTree {
   BinaryTreeNode *root;               //根结点指针
  public :
   BinaryTree( ) { root = NULL; }  //创建一个空的二叉树
   //如果二叉树为空，则返回true，否则返回false
   bool IsEmpty( );
    //置x为根结点值；若操作失败，则返回false，否则返回true
    bool Root(DataType &x);
   //创建二叉树
  void CreateBinaryTree(BinaryTreeNode *&t=root);
  void PreOrder(BinaryTreeNode *&t=root);
  void InOrder(BinaryTreeNode *&t=root);
  void PostOrder(BinaryTreeNode *&t=root);
  void LevelOrder( ); //逐层遍历
  //删除一棵二叉树，释放其结点。
  void Delete(BinaryTreeNode *&t=root);
  //返回二叉树的结点个数。
  int Size(BinaryTreeNode *&t=root);			
  //返回二叉树的高度。
  int Height(BinaryTreeNode *&t=root);		
  }; //BinaryTree
  二叉链表中基本操作的实现：
  bool BinaryTree::IsEmpty( ) {
  //如果二叉树为空，则返回true，否则返回false
  return (root ? true : false);
  }
  bool BinaryTree::Root(DataType &x) {
  //置x为根结点值，如果没有根结点，则返回false
  if (root) { root->data= x; return true;}
  return false; // 没有根结点
  }
  二叉链表中基本操作的实现：
  void BinaryTree::PreOrder(BinaryTreeNode * &t=root)
  { //前序遍历二叉树（递归算法）
   if (t)
  {
       cout<<t->data; //访问结点内容
       PreOrder(t->leftChild);
       PreOrder(t->rightChild);
  }
  }
  二叉链表中基本操作的实现：
  void BinaryTree::InOrder(BinaryTreeNode * &t=root)
  { //中序遍历二叉树（递归算法）
   if (t)
  {
       InOrder(t->leftChild);
       cout<<t->data; //访问结点内容
       InOrder(t->rightChild);
  }
  }
  二叉链表中基本操作的实现：
  void BinaryTree::PostOrder(BinaryTreeNode * &t=root)
  { //后序遍历二叉树（递归算法）
   if (t)
  {
       PostOrder(t->leftChild);
       PostOrder(t->rightChild);
       cout<<t->data; //访问结点内容
  }
  }
  ```
- #### 线索二叉树
  非线性结构(树形结构) -> 线性结构(前驱, 后继)
- 二叉树结点之间的前驱和后继关系只有在某种次序（前序、中序、后序）的遍历过程中才能确定。
  - 如果能事先知道二叉树结点之间在某种遍历次序（前序、中序、后序）下的前驱和后继关系，那么根据这些前驱和后继即可获得该次序（前序、中序、后序）下的遍历结果。
  - ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1603797620179-b8f0fca1-cf4d-48c0-9da5-246bca0a8e54.png#align=left&display=inline&height=47&margin=%5Bobject%20Object%5D&name=image.png&originHeight=94&originWidth=767&size=49748&status=done&style=none&width=383.5)
  - **Pre和Succ，分别指向该结点在某种次序下遍历时的前驱和后继(无孩子, 指针域为空)。 **
  - lTag=0，leftChild指向左子女
  - lTag=1，leftChild指向前驱
  - rTag=0，rightChild指向右子女
  - rTag=1，rightChild指向后继
  - 缺点：浪费存储空间。**有n+1个指针域是空的**。
- #### 三序线索二叉树
- **设指针pre始终指向刚刚访问过的结点（pre的初值为NULL）；若pre的右指针域为空，则令其指向它的后继p（即当前访问的结点）**
  ```cpp
  class ThrBNode{
    DataType data;
    ThrBNode *leftChild, *rightChild;
    bool  lTag, rTag;
  public:
    ThrBNode(DataType d){
        data=d;
        leftChild= rightChild=NULL;
        lTag=rTag=false;
    }
    friend class InThrBTree;
  }; //ThrBNode
  class InThrBTree {   //线索二叉树类
     ThrBNode *thrt;   //头指针，指向根结点
     ThrBNode *GetFirstNode(ThrBNode *);
     ThrBNode *GetNextNode(ThrBNode *);
  public:
     //创建一个带表头，但不带线索的空二叉树
     InThrBTree() { thrt=new ThrBNode(); }
     //创建一个带表头，但不带线索的二叉树
     void CreateBTree(ThrBNode *&t=thrt);
    //创建一个带表头，但不带线索的二叉树，其中：
       //data为根结点值，left和right是左右子树
    void MakeTree(DataType &data,
             InThrBTree &left, InThrBTree &right);
    //中序线索化
    void InOrderThreading(ThrBNode *&bt);
    void InOrder( );
  }; //InThrBTree
  void InOrderThreading(ThrBNode *p, ThrBNode *pre=NULL) {
     if (p == NULL) return;
     InOrderThreading(p->leftChild, pre);
     if (p->leftChild == NULL) {   //对p的左指针进行处理
         p->lTag = 1;
         p->leftChild = pre; } //设置p的前驱线索
     if (p->rightChild == NULL)
         p->rTag = 1; //对p的右标志进行处理
     if (pre->rTag == 1)
         pre->rightChild = p;  //设置pre的后继线索
     pre = p;
     InOrderThreading(p->rightChild, pre);
  }
  ThrBNode* InThrBTree::GetFirstNode(ThrBNode *p) {
    //求中序序列中的第一个结点
   while (!p->lTag)   p=p->leftChild;
     //沿左链走直到无左子女的结点
   return p;
  }
  ThrBNode* InThrBTree::GetNextNode(ThrBNode *p ) {  //求p在中序序列中的后继
    if (p->rTag)  return p->rightChild;  //P无右子女
    r=p->rightChild;  //r指向p的右子树的根
    r=GetFirstNode(r);  //求右子树中序的第一个结点
    return r;
  }
  void InThrBTree::InOrder( ){
     p=thrt;	//取根结点
     if(p==NULL)
         return;
     p=GetFirstNode(p);
     cout<<p->data;
     while(p->rightChild!=NULL) {
         p=GetNextNode(p);
         cout<<p->data;
     }
  } //InOrder
  ```
- #### 遍历的非递归实现 
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1603798889521-11a371c0-9508-48fb-8708-b14e04254eb9.png#align=left&display=inline&height=224&margin=%5Bobject%20Object%5D&name=image.png&originHeight=448&originWidth=629&size=43359&status=done&style=none&width=314.5)![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1603798905416-788ffa48-3d8a-48b3-8672-7c173c0e6d15.png#align=left&display=inline&height=230&margin=%5Bobject%20Object%5D&name=image.png&originHeight=460&originWidth=629&size=47906&status=done&style=none&width=314.5)![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1603798919386-15339511-ea27-4655-9741-4a50b74e6e34.png#align=left&display=inline&height=230&margin=%5Bobject%20Object%5D&name=image.png&originHeight=460&originWidth=629&size=49841&status=done&style=none&width=314.5)
- 递归算法在执行的过程中会使用到栈结构——隐式栈。
- 递归算法转成非递归算法时，也需要使用到栈结构——显式栈。
  - 栈结构需要手动开辟。
  - 二叉树遍历的非递归实现需要手动开辟栈结构，完成遍历过程。 
    ```cpp
    void PreOrder(BinaryTreeNode *＆p=root) {
        Stack  stack; //建立栈
        while (p || !stack.IsEmpty( )) {
         if(p) {
             cout<<p->data;
             stack.Push(p);
             p=p->leftChild;
         } //向左走
         else {
             p=stack.Pop( );
             p=p->rightChild; } //向右走		
       } //while
    } //PreOrder
    void InOrder(BinaryTreeNode *＆p=root) {
        Stack  stack; //建立栈
        while (p || !stack.IsEmpty()){
         if (p) {
             stack.Push(p);
             p=p->leftChild;
         }   //向左走
         else {
             p=stack.Pop();
             cout<<p->data; 	
             p=p->rightChild;
         }      //向右走		
        } //while
    } //InOrder
    void BinaryTree::PostOrder(BinaryTreeNode *＆p=root)){//后序遍历
        Stack stack;             //建立栈
        while (p || !stack.IsEmpty()){
         if (p) {
             stack.Push((p, 'L')); //(p, L)入栈
             p=p->leftChild;    //p向左走
         }
       else {
           e=stack.Pop(); //弹出栈顶元素到e中
           p=e.p;
           tag=e.tag;
           if (tag=='R') {
               cout<<p->data;
               p=NULL;
           }
           else {
               stack.Push((p, 'R'));
               p=p->rightChild;   //p向右走
           }		
    	   } //end else
       } //end while
    } //PostOrder
    ```
- #### 层次遍历算法LevelOrder的非递归实现
  ```cpp
  void BinaryTree::LevelOrder( ) {
  //层次遍历二叉树的非递归算法
  LinkedQueue   q; //链式队列
  BinaryTreeNode  *p=root;
  q.Enter(p);
  while(!q.IsEmpty( )) {
     p=q.Leave( );
     cout<<p->data;
     if(p->leftChild)  q.Enter(p->leftChild);
     if(p->rightChild)  q.Enter(p->rightChild);
  } //end while
  } //LevelOrder
  ```
- ### 树和森林
- #### 存储
- 双亲表示法——顺序结构
  - **特别适合求结点双亲的操作**
  - **不适用求结点子女等操作。 存在“上限”问题。 **
    ```cpp
    class NodeType {
        DataType data;
        int parent;
    }; //NodeType
    class PTree {
        NodeType nodes[MAX_TREE_SIZE];
        int n; //已存储的结点个数
      public:  ……
    }; //PTree
    ```
- 子女表示法——顺序结构+链式结构
- **适合求结点子女的操作**
- **不适合求结点双亲等操作。 存在“上限”问题。 **
  ```cpp
  class CNode {  //孩子结点
    int child;
    CNode *next;
  }; //CNode
  class CList {  //孩子链表
    DataType data;
    CNode *firstChild;
  }; //CList
  class CTree {  //结点的指针数组
    CList nodes[MAX_TREE_SIZE];
    int n, r;  //结点个数及根的位置
  }; //CTree
  ```
- 子女兄弟表示法——链式结构
  - **不但能够求结点的子女，而且能够求结点的兄弟**
  - **适合树的大部分操作**
  - **无“上限”问题**
  - **不适合求结点的双亲**
    ```cpp
    class CSNode {  //二叉链表的结点
        DataType data;
        CSNode *firstChild, *nextSibling;
      public:
        CSNode( ) { firstChild=nextSibling=NULL }
    }; //CSNode
    ```
- #### 先根次序遍历
- 当树非空时访问根结点；依次先根遍历根的各棵子树。
- #### 后根次序遍历
- 当树非空时依次后根遍历根的各棵子树；访问根结点。
- 没有中序是因为不是二叉树. 有多个子女, 根节点不知道从哪里输出
- ### 森林与二叉树的关系
- 链表的结构是完全一致
- 两种二叉链表中指针的含义不同：
  - **树**：左指针指向第一个子女，右指针指向下一个兄弟。
  - **二叉树**：左指针指向左子女，右指针指向右子女。
- **森林到二叉树**：凡是“兄弟”用线连起来，然后仅保留双亲到其第一个子女的连线，去掉双亲到其他子女的连线。
- **二叉树到森林**：若某结点是其双亲的左孩子，则该结点的右孩子、右孩子的右孩子 …，都与该结点的双亲连接起来，最后去掉所有双亲到右孩子的连线。
- ### Huffman树与编码
- **结点之间的路径长度 (Path Length)**：两个结点之间的路径长度是连接这两个结点的路径上的分支个数。
- 叶子结点的权值
- 二叉树的带权路径长度:     ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1603800788578-c0124af2-b3c3-49b7-ab89-fb3ed7a2dcdf.png#align=left&display=inline&height=105&margin=%5Bobject%20Object%5D&name=image.png&originHeight=209&originWidth=794&size=23804&status=done&style=none&width=397)
- **哈夫曼树**：给定一组具有确定权值的叶子结点，使得带权路径长度达到最小的那棵二叉树。
  - 权值越大的叶子结点越靠近根结点，而权值越小的叶子结点越远离根结点。
  - 只有度为0（叶子结点）和度为2（分支结点）的结点，不存在度为1的结点。
  - 一种 **前缀编码(任一字符的编码都不是其它字符的编码的前缀)**。解码时 不会出现混淆。 例如：设有abcd需要编码表示（其中，a=0、b=10、c=110、d=11,则**表示 110的编码 可以是c或者da，不唯一**）
- n个叶子结点构造出的Huffman树共有多少个结点？
  - 因为n=n+1，所以n=n-1，又由于在Huffman树中没有度为1的结点，所以在Huffman树中结点总数为： n+n-1=2n-1
- 一棵哈夫曼树共有215个结点,对其进行哈夫曼编码,共能得到()个不同的码字
  - 除了树根总共有 n-1 = 214个  ,   叶子节点为214的一半再加一个
  - ![图片.png](https://cdn.nlark.com/yuque/0/2021/png/1114914/1610625450242-6d33e9cd-a6b7-4c7c-8f10-7a72b8cb2d8a.png#align=left&display=inline&height=1093&margin=%5Bobject%20Object%5D&name=%E5%9B%BE%E7%89%87.png&originHeight=1093&originWidth=1536&size=293594&status=done&style=none&width=1536)
- #### 求每个字符的哈夫曼编码算法
  ```cpp
  void GetCode( ) {
  code=new String[n];
  for (k=0; k<n; k++) { //从叶子到根逆向求编码
    p=k;
    while ((q=tree[p].parent)!=-1) {
        if(tree[q]. leftChild ==p) code[k]+="0";
        else code[k]+="1";
        p=q;
    } //end while
    code[k].reverse(); //字符串反序
  } //end for
  } //GetCode
  ```
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1603766733598-d95424ec-0b3c-43b2-bb02-5d8a09b249f0.png#align=left&display=inline&height=285&margin=%5Bobject%20Object%5D&name=image.png&originHeight=570&originWidth=951&size=93550&status=done&style=none&width=475.5)
- # 图
  ![图片.png](https://cdn.nlark.com/yuque/0/2021/png/1114914/1610023827489-085f9229-3e04-4b8a-aa08-5c80bc07f73c.png#align=left&display=inline&height=2843&margin=%5Bobject%20Object%5D&name=%E5%9B%BE%E7%89%87.png&originHeight=5686&originWidth=5336&size=1654582&status=done&style=none&width=2668)
  [map.zip](https://www.yuque.com/attachments/yuque/0/2021/zip/1114914/1610023909255-d4b4c0c6-aa46-4815-afaf-74e754384a57.zip?_lake_card=%7B%22uid%22%3A%221610023908611-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2021%2Fzip%2F1114914%2F1610023909255-d4b4c0c6-aa46-4815-afaf-74e754384a57.zip%22%2C%22name%22%3A%22map.zip%22%2C%22size%22%3A115105%2C%22type%22%3A%22application%2Fzip%22%2C%22ext%22%3A%22zip%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22F2BVL%22%2C%22card%22%3A%22file%22%7D)
- ## 定义 & 基本术语
- 图是由 **顶点集合(Vertex)** 及 **顶点间的关系** 集合组成的一种**数据结构 **G＝(V, E)
  - V = { x | x ∈ 某个数据对象} 是**顶点的有穷非空集合**；
  - E = {(x, y) | x, y∈V} 是边(Edge)的集合
  - E = {<x, y> | x, y ∈ V && Path<x, y>} 是弧 (Arc)的集合, Path<x, y>表示从顶点 x 到 y 的一条单向通路，它是有方向的。
- 权
- 带权图（或网)
- 顶点的度(D(v)) : 与顶点v所关联的边数
- 自环
- 多重边（或弧）
- **简单图:** 不含自环和多重边（或弧）的图
- **路径**
- **回路**：起点和终点相同回路：起点和终点相同的路径
  - **简单路径**:  若一条路径上各顶点V, V, …,V均不相同
  - **简单回路（简单圈）:  **起点和终点相同的简单路径，称为简单回路
- **路径长度**：沿路径边的数目或沿路径各边权值之和
- **子图**：已知图G(V, E)和图G'(V', E')，若满足：V'∈V且E'∈E，则称图G'为图G的子图。
- **连通图: **
  - **连通分量**: 极大连通子图
  - **强连通图: **
    - 任意一对顶点 v和 v，都存在一条从 v到 v和从vj到vi的(有向)路径。
  - **强连通分量**：有向图中的极大强连通子图称为该有向图的强连通分量。
- 生成森林：在非连通图中，每个连通分量可生成一棵树，所有连通分量生成的树可组成生成森林。 
  ```cpp
  class Graph {
   public:
     Graph ( );
    void InsertVertex( Type & vertex );
     void InsertEdge( int v1,  int v2,  int weight );
     void RemoveVertex( int v );
     void RemoveEdge( int v1,  int v2 );
     int GetFirstNeighbor( int v );
     int GetNextNeighbor( int v1,  int v2 );
    …… //其他成员函数
  	};
  ```
- ### 邻接矩阵
- ### 邻接表
- ### 遍历
- #### 深度优先遍历(Depth-First Search, DFS)
- 时间复杂度： 设有n个顶点，e条边（或弧）的无（或有）向图。
  - 如果用邻接矩阵存储图：（邻接矩阵与e无关） 在DFSTraverse( )函数中，
    - 初始化visited数组所需时间为O(n)，并调用n次DFS( )函数；
    - 在DFS( )函数中，需要遍历邻接矩阵的一行才能得到邻接点，因此循环将执行n次；
  - 综上，无向图深度优先遍历算法的时间复杂度为O(n)+O(n*n)=O(n+n2)，即：O(n2)。 有向图的深度优先遍历算法的时间复杂度也为O(n2)。
  - 如果用邻接表存储图：
    - 在DFSTraverse( )函数中，初始化visited数组所需时间为O(n)，并调用n次DFS( )函数；
    - 在DFS( )函数中，每个顶点对应链表中边结点的个数为该顶点的度，因此循环将执行D(V)次。
  - 综上，无向图深度优先遍历算法的时间复杂度为O(n)+O(2e)=O(n+2e)，即：O(n+2e)。 有向图的深度优先遍历算法的时间复杂度为O(n+e)。（只有出度邻接表的情况） 
    ```cpp
    void  DFSTraverse( ) {  //深度优先遍历算法
        int  visited[n];       //开辟访问标志数组
       for (int v=0; v<n; v++)
       visited[v]=0;      //初始化访问标志数组
       for (v=0; v<n; v++)
           if (!visited[v])
               DFS(v);  //每次从尚未访问过的顶点中
                 //选取一个顶点v，从顶点v出发调用DFS(v)
    } //DFSTraverse
    void  DFS(int v) {
      //从顶点v出发访问包含该顶点v的最大连通子图中的所有顶点
        visited[v]=1;
        visit(v);      //或cout<<v;
        for(w=FirstAdjVex(v); w!=-1; w=NextAdjVex(v, w))
        if (!visited[w])
            DFS(w); //递归调用
    } //DFS
    //假定以邻接矩阵存储图：
    int  FirstAdjVex(int v) {
        int w=0;
        while(w<n && matrix[v][w]==0)
    　　  w++;
        if(w<n)
         return w;
    else return -1;  //v没有邻接点
    }
    //假定以邻接矩阵存储图：
    int  NextAdjVex(int v, int w) {
        u=w+1;
        while(u<n && matrix[v][u]==0)
    　　  u++;
        if(u<n)
         return u;
    else return -1;  //v没有邻接点
    }
    int FirstAdjVex(int v) {
    	if(ghead[v]->firstout)
        return ghead[v]->firstout.adjvex;
        else
        return -1;
    }
    int NextAdjVex(int v, int w) {
        p=ghead[v]->firstout;
        while (p && p->adjvex!=w)
        p=p->link;
        if (!p || !p->link)   return -1; 	
        else   return p->link->adjvex;
    }
    ```
    这里面的记忆数组在那里.
- ####  广度优先遍历(Breadth-First Search, BFS) 
  ```cpp
  void  BFSTraverse( ){  //广度优先遍历算法
   int  visited[n];              //设置访问标志数组
  for (v=0; v<n; v++)
      visited[v]=0；             //初始化访问标志
  for (v=0; v<n; v++)
        if (!visited[v])
           BFS(v);
  } //BFSTraverse
  void BFS(int v) {
   Q=new Queue( ); //清空队列Q
   Q.Enter(v);         //将起始顶点v入队
   visited[v]=1;        //标记v
   while (!Q.IsEmpty()) {       //队列Q不空
        u=Q.Leave( );               //出队头元素到u
        visited(u);                    //访问u
        for (w=FirstAdjVex(u); w!=-1; w=NextAdjVex(u, w))
            if (!visited[w]) {
                Q.Enter(w);  //将u的每个未被访问的邻接点w入队
                visited[w]=1;
            }
    }	
  } //BFS
  ```
- ### 无向图
  n-1 <= 网络 <=Cn2=n(n-1)/2
- ## 最小生成树
  - **邻接矩阵**存储连通无向网
  - 最小生成树 不唯一！ Kruskal（克鲁斯卡尔）算法
  - 设一个含有n个顶点的连通无向网N = { V, E }，最初先构造一个只有n个顶点，没有边的非连通图T = { V, (空集) }，图中每个顶点自成一个连通分量。
  - 当在E中选到一条具有最小权值的边时，若该边的两个顶点落在不同的连通分量上，则将此边加入到T中；否则，将此边舍去，重新选择一条权值最小的边。
  - 按上述方式重复下去，直到所有顶点都在同一个连通分量上为止。
  - **时间复杂度: **O(elog2e)
    - 仅与边的数目有关，而与顶点的数目无关
    - 适用求边稀疏的连通无向网的最小生成树
      ```cpp
      //Prim（普里姆）算法
      #include <iostream>
      #include <cstring>
      using namespace std;
      const int MaxSize=201;
      const int IV=1000000;
      class AddArray { //辅助数组类
          int  adjvex;//对应下标所要组合的边
          int lowcost;//组合的代价
      public:
          AddArray():adjvex(0),lowcost(IV){}
          friend class MST;
      };
      class MST{
          int n;//需要处理的顶点
          int m;//边数
          int start;//开始的地方
          bool AdjMatrix[MaxSize][MaxSize];//邻接矩阵存图
          int Cost[MaxSize][MaxSize];//权值
          AddArray closedge[MaxSize];//辅助数组
          AddArray edge[MaxSize];//结果保存到数组edge中。
          int *U;//顶点标记数组, 下标表示边
      public:
          MST(int,int);
          void Setclosedge();
          int Minimum();// 求下个顶点
          void MST_Prim(int u);
          void Print();
          bool JudgeIegal();
      };
      MST::MST(int a,int b):n(a),m(b){
          U=new int [a+1];//下标从0开始,   实际多输入一组边
          memset(U,0, sizeof(U));
          memset(AdjMatrix,false,sizeof(AdjMatrix));
          for(int i=0;i<=a;i++){
      for(int j=0;j<=a;j++){
          Cost[i][j]=IV;
      }
          }//初始化 Cost, 忌用 memset
      };
      void MST::Setclosedge() {
          int temp1,temp2;
          int temp3;
          for(int i=m;i>0;i--) {
      cin >> temp1 >> temp2 >> temp3;
      AdjMatrix[temp1][temp2] = true;
      AdjMatrix[temp2][temp1] = true;
      Cost[temp1][temp2] = temp3;
      Cost[temp2][temp1] = temp3;
          }
      }
      int MST::Minimum() {
          int min=IV;
          int target=-1;
          for(int i=n;i>=0;--i){//遍历节点找到身边最小的节点
      //        cout<<min<<" "<<closedge[i].lowcost<<"\n";
      if( !(U[i]) && closedge[i].adjvex && closedge[i].lowcost < min){
          min=closedge[i].lowcost;
          target=i;
      }// 在没有选中的数组里挑一个最小的
          }
          return target;
      }
      void MST::MST_Prim(int u) {
          start=u;
          if(!u){
      return;
          }
          U[u]=1; //从顶点u开始
          for (int v=1; v<=n; v++) //初始化辅助数组closedge为第一个节点的距离和权值
      if (AdjMatrix[u][v] && u != v){
          closedge[v].adjvex=u;
          closedge[v].lowcost=Cost[u][v];
      }
          for (int t=1; t<=n; t++) {//选择其余的n-1个顶点
      int k=Minimum(); //求出下一个顶点k
      if(k==-1){
      //            cout<<"没有找到应该进行的下一个节点\n";
          return ;
      }
      //        else cout<<"找到最小的下标"<<k<<"\n";
      u=closedge[k].adjvex;
      edge[k].lowcost=Cost[k][u];//保存选中边的权值
      edge[k].adjvex=u;//保存选中边的顶点
      U[k]=1;
      for (int j=1; j<=n; j++) //更新新点k以及k的关系权值
          if (Cost[k][j] < closedge[j].lowcost){
              closedge[j].lowcost=Cost[k][j];
              closedge[j].adjvex=k;
          }
          }
      }
      void MST::Print() {
          if(!JudgeIegal()) {
      cout<<"最小生成树长度为-1, 连通分支大于1";
      return;
          }
          cout<<"边的关系为:\n";
          for (int l = 1; l <= n; ++l) {
      if(l==start) continue;
      cout<<l<<" & "<<edge[l].adjvex<<" : "<<edge[l].lowcost<<"\n";
          }
          int step=0;
          cout<<"最小生成树长度为:\n";
          for (int l = 2; l <= n; ++l) {
      step+=edge[l].lowcost;
          }
          cout<<step<<endl;
      }
      bool MST::JudgeIegal(){
          for(int i=1; i<=n; ++i){
      if(!U[i]) return false;
          }
          return true;
      }
      int main(){
          int n,m;
          cout<<"输入节点的个数\n";
          cin>>n;
          cout<<"输入边的数量\n";
          cin>>m;
          MST temp(n,m);
          temp.Setclosedge();//初始化
          temp.MST_Prim(1);
          temp.Print();
      }
      /*
      6
      输入边的数量
      10
      1 2 6
      2 3 5
      1 3 1
      3 4 5
      2 5 3
      5 3 6
      1 4 5
      4 6 2
      6 5 6
      3 6 4
       *
       * */
      //Kruskal（克鲁斯卡尔）算法
      #include<iostream>
      #include<algorithm>
      #include<fstream>
      using namespace std;
      int n, m;
      class Road {
      	int x, y, l;
      public:
      	friend class Tree;
      };
      class Tree {
      	Road road[1000];
      	int root[1000];
      public:
      	void in(int x, int y, int l,int i);
      	int getRoot(int x);
      	int Kruskal();
      };
      void Tree::in(int x, int y, int l,int i) {
      	road[i].x = x;
      	road[i].y = y;
      	road[i].l = l;
      }
      int Tree::getRoot(int x) {
      	if (root[x] != x) root[x] = getRoot(root[x]);
      	return root[x];
      }
      int Tree::Kruskal() {
      	for (int i = 1; i <= n; i++) root[i] = i;
      	sort(road, road + m, [](const Road& x, const Road& y)->bool {return x.l < y.l; });
      	int ans = 0;
      	int j=0;
      	cout << "路径为：" << endl;
      	for (int i = 0; i < m; i++) {
      		int x = road[i].x;
      		int y = road[i].y;
      		if (getRoot(x) != getRoot(y)) {
      			ans += road[i].l;
      			j++;
      			cout << x << ' ' << y << ' ' << road[i].l << endl;
      			root[root[x]] = root[y];//合并并查集
      		}
      	}
      	if (j < (n - 1)) {
      		cout << "-1 无法构成最小生成树";
      	}
      	else
      	cout << "最短路径长度为:" <<ans << endl;
      	return ans;
      }
      int main() {
      	cin >> n >> m;
      	if(m < (n - 1)) cout << -1<<endl;
      	Tree A;
      	for (int i = 0; i < m; i++) {
      		int x1, y1, l1;
      		cin >> x1 >> y1 >> l1;
      		A.in(x1,y1,l1,i);
      	}
      	A.Kruskal();
      }
      ```
- ## 最短路径
- ### Dijkstra（迪杰斯特拉）算法
- 单源最短路径：某个顶点到其他顶点间的最短路径。
- 算法描述: 以邻接矩阵存储图，依次执行以下步骤：
  - **初始化** 设源点为v0，则find[0]=1; 其他find[1..n-1]=0;
    - dist[i] ← cost[0][i],   i= 1, 2, …, n-1;
  - 求出长度最短的路径 dist[k] ← min{ dist[i] },  i  V- S; find[k]=1;
  - 修改dist数组 对于每一个 i  V- S，即：find[i]==0，更新其dist[i] ← min{ dist[i], dist[k](倒数第二个顶点) + cost[k][i] }；若S = V，则算法结束；否则，转(2)。 
    ```cpp
    const  int  Vexnum=20；//图中最大顶点个数
    const  int  max=9999;     //9999表示无穷大
    class Graph {	//图的类定义
        float cost[Vexnum][Vexnum]; //邻接矩阵
        float dist[Vexnum];   //最短路径长度数组
        int path[Vexnum];     //最短路径顶点序列数组
        int find[Vexnum];     //最短路径顶点集	
    public:
        void ShortestPath_DIJ(int, float*);
        int mininum(int);
    }; //Graph
    void Graph::ShortestPath_DIJ(int v0, float *dist) {//求从源点v0到其它顶点的最短路经。
         for(v=0; v<Vexnum; v++){ //初始化
      find[v]=0;
      path[v]=0;
      dist[v]=cost[v0][v];
         }
         find[v0]=1;
        for(i=1; i<Vexnum; i++){
    k=mininum(dist); //求出当前路径中的最小值
    find[k]=1;
    for(w=1; w<Vexnum; w++)
       if(!find[w] && cost[k][w]<max)
           if(dist[k]+cost[k][w]<dist[w]){//更新dist数组元素, V0VkVw替代V0Vw
               dist[w]=dist[k]+cost[k][w];
               path[w]=k;
           }
        }
    } //ShortestPath_DIJ
    ```
    ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605228236874-49743c23-3eb5-42e5-801f-7884c625e8a1.png#align=left&display=inline&height=267&margin=%5Bobject%20Object%5D&name=image.png&originHeight=534&originWidth=932&size=86500&status=done&style=none&width=466)
- ### Floyd（弗洛伊德）算法
  ```cpp
  #mark::   MAX_VERVEX_NUM  20
  #mark::   max  9999
  VextexType  PathMatrix[MAX_VERVEX_NUM, MAX_VERVEX_NUM];
  VRType  DistMatrix[MAX_VERVEX_NUM, MAX_VERVEX_NUM];
  void ShortestPath_Floyd(PathMatrix &path, DistMatrix &A) {//用邻接矩阵存储图
  for(v=0; v<n; v++)
      for(w=0; w<n; w++){ //初始化path
          A[v][w]= DistMatrix[v][w];
          if (A[v][w]<max) path[v][w]=v；
              else  path[v][w]=-1;
      }
  for(u=0; u<n; u++)
      for(v=0; v<n; v++)
          for(w=0; w<n; w++)
              if(A[v][u]+A[u][w]<A[v][w]){ //更新最短路径及其长度
                  A[v][w]=A[v][u]+A[u][w];
                  path[v][w]=path[u][w];
              }
  } //ShortestPath_Floyd
  ```
- ## 有向图应用
- ### 拓扑排序 :
- 在AOV网络中，寻找一个拓扑有序序列的过程。
  - 活动网络（Activity Network） : 在一个表示工程的有向图中：
    - 顶点：表示活动；
    - 弧：表示**活动之间的优先关系**；例如：**<Vi, Vj> 表示活动Vi必须先于活动Vj进行**。
    - 这种有向图被称为顶点表示活动的网络(Activity On Vertices, AOV)，简称AOV网络。
    - 例如：计算机专业学生攻读学位的过程就是一个工程。
      - 每一门课程的学习是整个工程中的一个活动。
      - 有些课程要求有先修课程，有些则不要求。
      - 这样，课程之间可能存在先后关系。
      - ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605231595543-f0f6fdd9-d3bf-4711-8ce8-1de253b0206c.png#align=left&display=inline&height=224&margin=%5Bobject%20Object%5D&name=image.png&originHeight=448&originWidth=924&size=80975&status=done&style=none&width=462)
      - 拓扑有序序列：在AOV网络中，若将各个顶点 （代表各个活动）排列成一个线性有序的序列v1, v2, …, vn，使得若从顶点vi到vj有一条有向路径，则在序列中顶点vi必须排在顶点vj之前。
      - 在AOV网络中不能出现有向回路。
        - 如果出现了有向回路，则意味着某项活动将以自己作为先决条件或者活动之间互为条件。
        - 如果AOV网络中存在有向回路，则此AOV网络所代表的工程是不可行的。
        - 因此，对给定的AOV网络，必须先判断它是否存在有向回路。
  - 关键路径
  - 例: ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605582928667-b7bd9b2a-615e-475e-aa9f-f1ef1453e1e2.png#align=left&display=inline&height=180&margin=%5Bobject%20Object%5D&name=image.png&originHeight=360&originWidth=700&size=25514&status=done&style=none&width=350)
  - 事件Vi的最早开始时间ve[i]：从起点V0到顶点Vi的最长路径长度。
  - 活动ak的最早开始时间ee[k]：设活动ak在弧<Vi, Vj>上，则ee[k]是**从起点V0到顶点Vi的最长路径长度**。
    - ee[k] = ve[i]，它等于活动ak所在弧的起点事件Vi的最早开始时间。
  - 活动ak的最迟开始时间 **el[k] = vl[j] - len(<i, j>)**
  - 活动ak的时间余量el[k]-ee[k]：表示活动ak的最迟开始时间和最早开始时间之间的时间差。
    - 当el[k] == ee[k]时，表示活动ak没有时间余量，即：ak是关键活动。
    - 为了找出AOE网络中的关键活动，需要计算出各活动的ee[k]与el[k]，以判别是否满足el[k] == ee[k]。
    - 为求得ee[k]与el[k]，需要先计算出各顶点Vi的ve[i]和vl[i]。 
      ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605583367519-0a9d3eff-4eb6-4262-bd53-b37016a5f8b5.png#align=left&display=inline&height=269&margin=%5Bobject%20Object%5D&name=image.png&originHeight=537&originWidth=942&size=66034&status=done&style=none&width=471)
      ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605583338226-59d3432f-4169-4be4-a165-08f73fe63ec9.png#align=left&display=inline&height=265&margin=%5Bobject%20Object%5D&name=image.png&originHeight=530&originWidth=940&size=66570&status=done&style=none&width=470)
      ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605583346562-3ab7ee4d-5c78-4c9b-af6c-74f7cb5b423f.png#align=left&display=inline&height=261&margin=%5Bobject%20Object%5D&name=image.png&originHeight=522&originWidth=915&size=43046&status=done&style=none&width=457.5)
      ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1605583775631-ea571f7c-2c2a-4ef0-8d5a-12c6c59ea82a.png#align=left&display=inline&height=592&margin=%5Bobject%20Object%5D&name=image.png&originHeight=728&originWidth=917&size=107306&status=done&style=none&width=746)
- # 查找技术
  ![图片.png](https://cdn.nlark.com/yuque/0/2021/png/1114914/1610018683898-b5b9ab3a-4041-438f-8475-ff18874aa0be.png#align=left&display=inline&height=2350&margin=%5Bobject%20Object%5D&name=%E5%9B%BE%E7%89%87.png&originHeight=4699&originWidth=4912&size=1053652&status=done&style=none&width=2456)
  [hash.zip](https://www.yuque.com/attachments/yuque/0/2021/zip/1114914/1610018851249-df859c93-b87d-49aa-a904-85a52e1a0d1a.zip?_lake_card=%7B%22uid%22%3A%221610018850462-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2021%2Fzip%2F1114914%2F1610018851249-df859c93-b87d-49aa-a904-85a52e1a0d1a.zip%22%2C%22name%22%3A%22hash.zip%22%2C%22size%22%3A63965%2C%22type%22%3A%22application%2Fzip%22%2C%22ext%22%3A%22zip%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22IEVZB%22%2C%22card%22%3A%22file%22%7D)
- 平均查找长度：查找算法中关键码比较次数的数学期望值，即：
  - n：问题规模，查找集合中的数据元素个数；
  - pi：查找第i个数据元素的概率；
  - ci：查找第i个数据元素所需的关键码的比较次数
  - 更多关于折半查找的例子: [https://www.cnblogs.com/ygsworld/p/10238729.html](https://www.cnblogs.com/ygsworld/p/10238729.html)
    ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1606406657970-244f794a-29c4-4416-b29d-fe137a525568.png#align=left&display=inline&height=52&margin=%5Bobject%20Object%5D&name=image.png&originHeight=104&originWidth=261&size=4586&status=done&style=none&width=130.5)
- ## 线性表
- ### 顺序查找 （线性查找）
- ### 折半查找
- ### 分块查找
- 要求将查找表分成 若干个子表，并对子表建立索引表，查找表的每一个子表由索引表中的索引项确定。
- 索引项包括两个字段：关键码字段(存放对应子表中的最大关键码值) ；指针字段(存放指向对 应子表的指针)
- 索引项按关键码字段有序
  - 查找时，先用给定值key 在索引表中 检测索引项，以确定所要进行的查找在查找表中的查找分块(由于索引项按关键码字段有序，可用顺序查找或折半查找)
  - 然后，再对该分块进行顺序查找。
- 代码: [https://blog.csdn.net/hbtj_1216/article/details/50267977](https://blog.csdn.net/hbtj_1216/article/details/50267977)
- ## 树表
- ### 二叉查找树 
  ```cpp
  class BiSortTree{
  public:
   BiSortTree(int a[ ], int n);
   ~ BiSortTree( );
   void InsertBST(BiNode<int> *root , BiNode<int> *s);
  //若二叉查找树为空树，则新插入的结点为新的根结点；
  //否则，新插入的结点必为一个新的叶子结点，其插入位置由查找过程得到
   void DeleteBST(BiNode<int> *p, BiNode<int> *f );
   BiNode<int> *SearchBST(BiNode<int> *root, int k);
  private:
    BiNode<int> *root;
  };
  void BiSortTree::InsertBST(BiNode<int> *root, BiNode<int> *s){
  if (root == NULL)  root = s;
  else
      if (s->data < root->data) InsertBST(root->leftChild, s); //递归
      else InsertBST(root->rightChild, s); //递归
  }
  BiSortTree::BiSortTree(int r[ ], int n){ //构造函数
  for (i = 0; i < n; i++){
     s = new BiNode<int>;
     s->data = r[i];
     s->leftChild = s->rightChild = NULL;
     InsertBST(root, s);
  }
  }
  ```
- #### 平衡二叉树
  ![image.png](https://cdn.nlark.com/yuque/0/2020/png/1114914/1607162250150-e7e7f482-29d0-4bd3-8378-f85e54468421.png#align=left&display=inline&height=468&margin=%5Bobject%20Object%5D&name=image.png&originHeight=936&originWidth=1771&size=146793&status=done&style=none&width=885.5)