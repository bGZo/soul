also:: maths/scale
- Measurement Unit
  collapsed:: true
  - ((632567dc-203a-4a50-acbe-692fe9c6e248))
  - [[Chinese]] 定义非常混乱, 还是按照 [[English]] 的来吧, 我不愿意再花时间弄了...
- Convert
  collapsed:: true
  - 10 进制 to
    - N 进制
      collapsed:: true
      - 除 N 取余法
        - 如十进制整数10转化为2进制的过程
          collapsed:: true
          - ```
            10/2 = 5余0
            5/2 = 2余1
            2/2 = 1余0
            1/2 = 0余1
            ```
          - 即 `1010`
      - 降幂法
        - 将十进制整数不断减去与该整数最接近的N进制整数的位权，如果够减m次则对应N进制位上的数字为m(m<N)，否则为0。得到的差值作为新的被减数进行下一次计算，直到被减数为0.
          collapsed:: true
          - ```
            30-82=66
            66-82=2
            2-8（不够减）
            2-1=1
            1-1=1
            ```
          - 即`202`
    - 小数转换
      collapsed:: true
      - 乘 N 取整法
        - 十进制的0.54转换为16进制的过程
          - ```cpp
            0.55*16=8.8 --8
            0.8*16=12.8 --12(C)
            0.8*16=12.8 --12(C)
            0.8*16=12.8 --12(C)
            ...
            ```
          - 由于不能被精确的转换，我们可以只取前4位，为`0.8CCC`.
        - ==一般的十进制数转换为N进制数，分别转换整数和小数部分==
        - 倒序处理 -> 数组
          collapsed:: true
          - ==取模(%)出来的是从个位开始，也就是说必须从后面开始输出==。然而, 不倒序处理无法处理进位
          - ```cpp
            #include<iostream>
            using namespace std;
            int main(){
              int m,i;
              char p[1000];
              cin>>m;
              for(i=0;m!=0;i++){
                  p[i]=(m%2)+'0';
                  m=m/2;
              }
                p[i]='\0';
                for(int j=i-1;j>=0;j--)cout<<p[j];
            }//这里采取倒序输出是因为开始处理的位数是个位，所以最后输出的位数也因该是倒序输出，关于这类问题，首先着手的是自己处理的位数是哪位！是关于移位处理的进制转换问题，
            ```
          - 这是二进制转化十进制的操作！
          - ```cpp
            #include<iostream>
            #include<cstring>
            using namespace std;
            int main(){
            int sum=0;
            char p[1000];
            cin.getline(p,1000);
            int len=strlen(p);
            for(int i=0;i<len;i++){
                sum*=2;
                sum+=p[i]-'0';
            }
              cout<<sum<<endl;
            }//getline读取后的数组从最大位置开始，然后迭代算到个位结束。
            ```
          - std::bitset（转2进制），std::oct（转8进制），std::dec （转10进制），std::hex（转16进制）。另外发现的一个有趣的点是VS内置iostream是支持strlen的操作的，但是不不通用真是鸡肋的说·····
          - ```c++
            #include<cstring>
            void conversionnum(int m, int j, char p[]) {//m是原来的进制，j是转换进制，p是原来的数
              int i, sum = 0;
              char z[1000];
              for (int i = 0; i < strlen(p); i++) {
                sum *= m;
                if (p[i] >= 'A' && p[i] <= 'Z')sum += p[i] - 'A' + 10;
                else if (p[i] >= '0' && p[i] <= '9')sum += p[i] - '0';
              }//将读回来的字符数组转化成为对应十进制的数字（可不可以一步从m到j转化）
              i = 0;
              if (sum > j) {
                for (i = 0; sum != 0; i++) {
                  if ((sum % j) <= 9)z[i] = (sum % j) + '0';
                  else z[i] = (sum % j) + 'A' - 10;
                  sum = sum / j;
                }
              }//对应的进制转换（貌似不用提前讨论转换后是不是比十进制要大···以前写复杂了）
              else z[i++] = sum + '0';
              z[i] = '\0';
              for (int j = i - 1; j >= 0; j--) cout << z[j];
              cout << endl;
            }
            ```
        - 倒序处理模板类 -> 栈
          collapsed:: true
          - 栈天然具有倒序处理的能力, 所以自然很方便的可以实现, 但是因为STL里面本身不具备这样的模板函数, 所以需要自己去实现.
          - ```cpp
            const int MaxStackSize=10;//栈最大容量
            template<class T>
            class SeqStack {
                T StackList[MaxStackSize];
                int top;
            public:
                SeqStack();
                bool IsEmpty();//判断栈空
                bool IsFull() ;//判断栈满
                void Push(const T x);
                T Pop();//出栈
                void Clear() ;//置栈空
                void Conversion(int M, int N);//进制转换，并输出结果
            }; //SeqStack
            template<class T>SeqStack<T>::SeqStack(){top=-1;}
            template<class T>bool SeqStack<T>::IsEmpty(){
                if(top==-1) return true;
                else return false;
            }
            template<class T>bool SeqStack<T>::IsFull(){
                if(top==MaxStackSize-1) return true;
                else return false;
            }
            template<class T>void SeqStack<T>::Push(const T x){
                if(IsFull()) return ;
                else StackList[++top]=x;
            }
            template<class T>T SeqStack<T>::Pop(){
                if(IsEmpty()) exit(1);
                return StackList[top--];
            }
            template<class T>void SeqStack<T>::Clear(){
                top=-1;
            }
            template<class T>void SeqStack<T>::Conversion(int M,int N){
                SeqStack<T>p;
                T temp;
                while(M){
                    p.Push(M%N);
                    M/=N;
                }
                while(!p.IsEmpty()){
                    temp=p.Pop();
                    cout<<temp;
                }
                cout<<endl;
            }
            ```
          -
- Refs
  collapsed:: true
  - [进位制 - OI Wiki](https://oi-wiki.org/math/base/)
  - [按照我国传统，一兆到底是表示一百万，还是表示一万亿？ - 知乎](https://www.zhihu.com/question/20602674/answer/15606415)
    collapsed:: true
    - 根据东汉时期《数术记遗》中所载：
    - > 黄帝为法，数有十等，及其用也，乃有三焉，十等者，亿、兆、京、垓、秭、穰、沟、涧、正、载。三等者，谓上中下也。其下数者，十十变之，若言十万曰亿，十亿曰兆，十兆曰京。中数者、万万变之，若言万万曰亿、万万亿曰兆、万万兆曰京。上数者数穷则变，若言万万曰亿，亿亿曰兆，兆兆曰京也。下数浅短，计事则不尽，上数宏廓，世不可用，故其传业惟以中数耳。
    - 也就是说古代对于大数的记载有亿、兆、京、垓、秭、穰、沟、涧、正、载这十个基数，后来又在“载之上”加了一个“极”。基数之间的关系有三种：
      - 十进制，十万等于一亿(10^5)，十亿等于一兆(10^6)，十兆等于一京(10^7)……
      - 万进制，万万等于一亿(10^8)，万亿等于一兆(10^12)，万兆等于一京(10^16)……
      - 平方制，万万等于一亿(10^8)，亿亿等于一兆(10^16)，兆兆等于一京(10^32)……
    - 按照我国传统，三种关系并行，第一种比较常用。这么说来，1KB 叫一千，1MB 叫一兆，1GB 应该叫一秭（zǐ），1TB 应该叫一涧，1PB应该叫一极。 那位说了，再大怎么办？没法表示了？还有办法，后来随着佛教传入中国，佛法无边，藏须弥于芥子，常常用到极大的数和极小的数，所以翻译佛经的同时，中文中又多了更多的表示数字的词语，一万万个极叫“恒河沙”，一万万个“恒河沙”叫“阿憎祗”。
    - 这是往大了说，那往小了说呢？由大到小分别是分、厘、毫、丝、忽、微、纤、沙、尘埃、渺、模糊、逡巡、须臾、瞬息、弹指、刹那、六德、虚、空、清、净等。后边有很多的词大家看着很眼熟，没错，因为微、纤之下可能就找不到与之相对应的实物了，更小的数量级往往都是用来描述极短的时间的。
    - 一九八四年二月二十七日发布的《国务院关于在我国统一实行法定计量单位的命令》中的表 5 《用于构成十进倍数和分数单位的词头》明确规定，一兆表示一百万。
    - id:: 632567dc-203a-4a50-acbe-692fe9c6e248
      |所表示的因数| 词头名称| 词头符号|
      |----------|--------|--------|
      |$10^{18}$ | 艾［可萨］ |E|
      |$10^{15}$ | 拍［它］| P|
      |$10^{12}$ | 太［拉］| T|
      |$10^9$ | 吉［咖］| G|
      |$10^6$ | 兆| **M**ega |
      |$10^3$ | 千| k|
      |$10^2$ | 百| h|
      |$10^1$ | 十| da|
      |$10^{-1}$ | 分| d|
      |$10^{-2}$ | 厘| c|
      |$10^{-3}$ | 毫| m|
      |$10^{-6}$ | 微| μ|
      |$10^{-9}$ | 纳［诺］| n|
      |$10^{-12}$ | 皮［可］| p|
      |$10^{-15}$ | 飞［母托］| f|
      |$10^{-18}$ | 阿［托］| a|
      - 周、月、年(年的符号为a)为一般常用时间单位。
      - []内的字，是在不致混淆的情况下，可以省略的字。 ……
      - $10^4$ 称为万，$10^8$ 称为亿，$10^12$ 称为万亿，这类数词的使用不受词头名称的影响，但不应与词头混淆
    - 所以现在根据我国规定，亿表示的数量竟然比兆大，真是奇怪。没有办法，晚清以降，国力积弱，方方面面都要学习外国，只能抛掉老祖宗的东西，跟着人家的规则。