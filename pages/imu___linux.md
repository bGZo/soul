title:: imu/linux
email:: ![csxingyi@imu.edu.cn](mailto:csxingyi@imu.edu.cn)

-
- 占 80%
-
- Make
  - 手写
    - ```makefile
      mypipes: mypipes.o client.o server.o
          g++ mypipes.o client.o server.o -o mypipes 
      mypipes.o:  mypipes.cpp
          g++ -c mypipes.cpp
      client.o: client.cpp
          g++ -c client.cpp
      server.o: server.cpp
          g++ -c server.cpp
      clean:
          rm *.o
      ```
  - 自动编译
    - ```makefile
      GCC=g++
      
      CFLAG=-c
      OFLAG=-o
      
      SLIB=-pthread
      
      SEXE=serMain
      SOBJ=serMain.o server.o 
      
      CEXE=cliMain
      COBJ=cliMain.o client.o 
      
      all:${SEXE} ${CEXE}
      
      ${SEXE}:${SOBJ}
          ${GCC} ${OFLAG} $@ $^ ${SLIB}
      ${CEXE}:${COBJ}
          ${GCC} ${OFLAG} $@ $^
      
      %.o:%.cpp
          ${GCC} ${CFLAG} $^
      
      clean:
          rm *.o
          rm ${SEXE} ${CEXE}
      ```
-
- 进程间通信
  - 同一台机器通信
    - 有血缘
      - 父子进程
        - [[linux/system-call/fork]]
          collapsed:: true
          - {{embed ((63049e75-857f-4575-b888-4008ea57c54d))}}
          - Cases
            - **进程链** => 父进程退出循环，子进程继续做循环
              collapsed:: true
              - ```cpp
                int n = 4;
                pid_t pid;
                
                for (int i=0; i<n; i++){
                    pid=fork();
                
                    if(pid < 0){
                        exit(-1);
                        printf("fork error");
                    } else if (pid > 0) // 子进程跳出循环
                        break;
                }
                printf("My pid is %ld,My parent pid is %ld\n",(long)getpid(),(long)getppid());
                sleep(1);
                ```
            - **进程扇** => 子进程退出循环，父进程继续做循环
              collapsed:: true
              - ```cpp
                int n = 4;
                pid_t pid;
                
                for (int i=0; i<n; i++){
                    pid=fork();
                
                    if(pid < 0){
                        printf("fork error");
                        exit(-1);
                    } else if (pid == 0) // 子进程跳出循环
                        break;
                }
                printf("My pid is %ld,My parent pid is %ld\n",(long)getpid(),(long)getppid());
                sleep(1);
                ```
            - **进程树** => 父子同时创建进程, 仅把循环号赋给孩子作标注
              collapsed:: true
              - ```cpp
                int n = 2;
                int id = 0;
                pid_t pid;                        // 创建一个进程，给他一个pid
                for (int i=0; i<n; ++i){
                    pid = fork();                 // 创建子进程
                
                    if(pid == 0)
                        id = i;                    // 把 i 赋值给 id 表示树的第几个孩子
                }
                printf("#%d is process %ld with parent %ld\n", 
                       id, (long)getpid(), (long)getppid());
                ```
    - !无血缘
      - pipe
        - 匿名管道
          collapsed:: true
          - More see ((630374b6-6f4c-4536-af7f-23530c6f3b75))
          - 0 为标准输出; 1 为标准输入;
          - Cases
            - 单管道 父子进程读写
              collapsed:: true
              - ```cpp
                #include <stdio.h>
                #include <stdlib.h>
                #include <string.h>
                #include <unistd.h>
                #include <sys/types.h>
                #include <sys/wait.h>
                
                int main(){
                    int fd[2];
                    int pid,line;
                    char msg[BUFSIZ];
                    //阻塞标志
                
                    int parentFlag = 1;// 1阻塞 2不阻塞
                    int childFlag = 1;// 2阻塞 1不阻塞
                
                    printf( "程序开始 \n ");
                    if( pipe(fd) < 0 ){
                        perror( "建立管道失败:");
                    }
                    printf( "建立管道成功 \n ");
                
                    pid = fork();
                    if( pid < 0){
                    perror( "建立进程失败");
                    exit( 1);
                    } else if(pid == 0){
                        printf( "子进程开始 \n ");
                        printf( "1子进程写入: \n ");
                        while( 1 ){
                            if(childFlag== 2){
                                childFlag= 1;
                                printf( "子进程阻塞,进入父进程 \n\n ");
                            } else{
                                childFlag++;
                            }
                            scanf( "%s",msg);
                
                            close(fd[ 0]); //关闭读
                            write(fd[ 1],msg, strlen(msg)+ 1); //开始写
                            printf( "子进程写入完成 \n\n ");
                            if ( strcmp(msg, "EOF") == 0){
                                printf( "子进程结束通讯 \n ");
                                break;
                            }
                        } //while
                
                        printf( "子进程结束 \n ");
                        _exit( 0);
                    } else{
                        printf( " \n 父进程开始 \n ");
                    while( 1 ){
                        if(parentFlag== 1){
                            parentFlag++;
                            printf( "父进程阻塞,进入子进程 \n\n ");
                        }
                        if(childFlag== 2) {
                            printf( "2子进程写入: \n ");
                        } else{
                            childFlag= 2;
                        }
                
                        close(fd[ 1]); //关闭写
                        read(fd[ 0],msg,BUFSIZ); //开始读
                
                        if(parentFlag== 2){
                            parentFlag= 1;
                            printf( "父进程解除阻塞 \n ");
                            printf( "父进程开始读取 \n ");
                            printf( "父进程读取:%s \n ",msg);
                
                            if ( strcmp(msg, "EOF") == 0){
                                printf( "父进程结束通讯 \n ");
                                break;
                            }
                            printf( "父进程读取完成 \n\n ");
                        }
                    } //while
                    wait( NULL); //等待子进程执行完
                    printf( "父进程结束 \n ");
                    }
                    printf( "程序结束 \n ");
                    return 0;
                }
                
                ```
            - 双管道读写
              collapsed:: true
              - ```cpp
                #include <stdio.h>
                #include <stdlib.h>
                #include <string.h>
                #include <unistd.h>
                #include <sys/types.h>
                #include <sys/wait.h>
                
                int main(){
                    int fd[2];
                    int pid,line;
                    char msg[BUFSIZ];
                    //阻塞标志
                
                    int parentFlag = 1;// 1阻塞 2不阻塞
                    int childFlag = 1;// 2阻塞 1不阻塞
                
                    printf( "程序开始 \n ");
                    if( pipe(fd) < 0 ){
                        perror( "建立管道失败:");
                    }
                    printf( "建立管道成功 \n ");
                
                    pid = fork();
                    if( pid < 0){
                    perror( "建立进程失败");
                    exit( 1);
                    } else if(pid == 0){
                        printf( "子进程开始 \n ");
                        printf( "1子进程写入: \n ");
                        while( 1 ){
                            if(childFlag== 2){
                                childFlag= 1;
                                printf( "子进程阻塞,进入父进程 \n\n ");
                            } else{
                                childFlag++;
                            }
                            scanf( "%s",msg);
                
                            close(fd[ 0]); //关闭读
                            write(fd[ 1],msg, strlen(msg)+ 1); //开始写
                            printf( "子进程写入完成 \n\n ");
                            if ( strcmp(msg, "EOF") == 0){
                                printf( "子进程结束通讯 \n ");
                                break;
                            }
                        } //while
                
                        printf( "子进程结束 \n ");
                        _exit( 0);
                    } else{
                        printf( " \n 父进程开始 \n ");
                    while( 1 ){
                        if(parentFlag== 1){
                            parentFlag++;
                            printf( "父进程阻塞,进入子进程 \n\n ");
                        }
                        if(childFlag== 2) {
                            printf( "2子进程写入: \n ");
                        } else{
                            childFlag= 2;
                        }
                
                        close(fd[ 1]); //关闭写
                        read(fd[ 0],msg,BUFSIZ); //开始读
                
                        if(parentFlag== 2){
                            parentFlag= 1;
                            printf( "父进程解除阻塞 \n ");
                            printf( "父进程开始读取 \n ");
                            printf( "父进程读取:%s \n ",msg);
                
                            if ( strcmp(msg, "EOF") == 0){
                                printf( "父进程结束通讯 \n ");
                                break;
                            }
                            printf( "父进程读取完成 \n\n ");
                        }
                    } //while
                    wait( NULL); //等待子进程执行完
                    printf( "父进程结束 \n ");
                    }
                    printf( "程序结束 \n ");
                    return 0;
                }
                
                ```
              - `client`
                ```cpp
                #include"client.h"
                #include <string.h>
                #include <stdio.h>
                #include <unistd.h>
                
                #define MAXLINE 4096
                
                void client(int readfd,int writefd){
                    size_t len;
                    char buf[MAXLINE];
                    fgets(buf,MAXLINE,stdin);
                    len = strlen(buf);
                    if(buf[len-1] == '\n')
                          --len;
                    write(writefd,buf,len);
                    while( (len = read(readfd,buf,MAXLINE)) > 0)
                          write(STDOUT_FILENO,buf,len);
                }
                ```
              - `server`
                ```cpp
                #include "server.h"
                #include <string.h>
                #include <stdio.h>
                #include <unistd.h>
                #include <stdlib.h>
                #include <cerrno>
                #include <sys/types.h>
                #include <sys/stat.h>
                #include <fcntl.h>
                
                #define MAXLINE 4096
                
                void server(int readfd,int writefd){
                    char buf[MAXLINE];
                    ssize_t n = read(readfd,buf,MAXLINE);
                    if(n ==0){
                        fprintf(stderr,"error\n");
                        exit(-1);
                    }
                    buf[n] = '\0';
                    int fd = open(buf,O_RDONLY);
                    if(fd < 0){
                        snprintf(buf+n,sizeof(buf)-n,"can't open: %s\n",strerror(errno));
                        n = strlen(buf);
                        write(writefd,buf,n);
                    } else {
                        while( (n = read(fd,buf,MAXLINE)) > 0)
                            write(writefd,buf,n);
                    }
                    close(fd);
                }
                ```
              - `mypipes`
                ```cpp
                #include <unistd.h>
                #include <stdio.h>
                #include <fcntl.h>
                #include <string.h>
                #include <stdlib.h>
                #include <error.h>
                #include <sys/types.h>
                #include <sys/wait.h>
                
                #include "client.h"
                #include "server.h"
                
                int main(){
                    int fd1[2], fd2[2];
                
                    pipe(fd1);
                    pipe(fd2);
                
                    int pid = fork();
                
                    if(pid < 0){
                        fprintf(stderr,"fork error\n");
                        exit(-1);
                    }else if(pid == 0){
                        //子进程
                        close(fd1[1]);
                        close(fd2[0]);
                        server(fd1[0],fd2[1]);
                
                    }else{
                        //父进程
                        close(fd1[0]);
                        close(fd2[1]);
                        client(fd2[0],fd1[1]);
                
                        waitpid(pid,NULL,0);
                
                    }
                
                    exit(0);
                }
                ```
            - 利用匿名管道实现 `cat filename | more | wc`
              collapsed:: true
              - 关键思路
                collapsed:: true
                - `i=1` 的时候, 事先对 `fd[0]` 的输出 和 `fd[1]` 的输入进行绑定; 然后在最后一个进程完全关闭对 `fd` 的读写.
              - ```cpp
                #include<unistd.h>
                #include<stdlib.h>
                #include<signal.h>
                #include<unistd.h>
                #include<unistd.h>
                
                #include<iostream>
                #include<sys/types.h>
                #include<sys/wait.h>
                
                void handle_child(int signo){
                  pid_t child;
                  while((child=waitpid(-1,NULL,WNOHANG)) > 0){
                    std::cerr<<child<<" finish\n";
                  }
                }
                
                int main(int argc,char* argv[]){
                  signal(SIGCHLD,handle_child);
                  int fd[2], fd2[2];
                
                    pipe(fd);
                  pipe(fd2);
                
                  int i=0;
                  for(;i<3;i++){
                    pid_t child=fork();
                    if(child==0) break;
                  }
                  if(i==0){
                    close(fd2[0]);
                    close(fd2[1]);
                
                    close(fd[0]);
                        dup2(fd[1],1);
                      execlp(argv[1], argv[1], argv[2], NULL);
                
                    exit(0);
                  }else if(i==1){
                        close(fd2[0]);
                    close(fd[1]);
                
                      dup2(fd[0], 0); // 0
                      dup2(fd2[1], 1);  //***
                
                      execlp(argv[3], argv[3], NULL); //***
                    exit(0);
                  }else if(i==2){
                        close(fd[0]);
                        close(fd[1]);
                
                    close(fd2[1]);
                      dup2(fd2[0], 0);
                
                        // printf("test");
                
                      execlp(argv[4], argv[4], NULL);
                
                        exit(0);
                
                  }else{
                    close(fd[0]);
                    close(fd[1]);
                    close(fd2[0]);
                    close(fd2[1]);
                    while(true){
                    }
                  }
                  return 0;
                }
                // RUN: ./a.out cat passwd more wc
                // FIXME: 切分 client & server 会有问题
                ```
        - TODO 命名管道
      - TODO 消息队列
      - TODO 共享内存
  - 不同机器通信
    - !socket
      - TODO TCP
        - `server`
          - ```cpp
            #include <iostream>
            #include <sys/types.h>
            #include <sys/socket.h>
            #include <unistd.h>
            #include <arpa/inet.h>
            #include <error.h>
            #include <string.h>
            #include <ctype.h>
            
            #include "server.h"
            
            using SAI = struct sockaddr_in;
            using SA = struct sockaddr;
            
            const int LEN = 4096;
            
            void handle_msg(const int confd){
                while(true){
                    char buf[LEN];
                    bool flag = true;
                    memset(buf, '\0', sizeof(buf));
                    ssize_t s = read(confd, buf, sizeof(buf));
                    if(s == 0){
                        std::cout << "client quit" << std::endl;
                        break;
                    } else if(s < 0){
                        std::cout << "read error" << std::endl;
                        break;
                    } else{
                        std::cout << "read " << s << " bytes: " << buf << std::endl;
                        for(int i=0;i<strlen(buf);i++){
                            if (!isdigit(buf[i])) {  // for(auto i: buf) ????
                                flag = false; 
                                std::cout<<"error"<< i <<std::endl;
                                break; 
                            }
                        }
                    }
                    int tmp;
                    if(flag) tmp = atoi(buf);
            
                    std::cout<<"flag:"<<flag <<"; tmp:"<<tmp<<std::endl;
            
                    memset(buf, '\0', sizeof(buf));
            
                    if (flag) {
                        if( tmp%2 == 0) strcpy(buf, "Yes");
                        else strcpy(buf, "No");
                    } else {
                        strcpy(buf, "No");
                    }
                    write(confd, buf , strlen(buf));
            
                }
            }
            
            void process(const int listenfd){
                while(true){
                    int confd = accept(listenfd, nullptr, nullptr);
                    if(confd == -1){
                        std::cerr << "accept error" << std::endl;
                        exit(EXIT_FAILURE);
                    }
                    handle_msg(confd);
                }
            }
            
            void server(int port){
                int listenfd;
                do{
                    listenfd = socket(PF_INET, SOCK_STREAM, 0);
                    // tcp transform to stream
                    if (listenfd < 0) { // -1
                        std::cerr << "ERROR opening socket" << std::endl;
                        break;
                    }
                    SAI saddr;
                    saddr.sin_family = AF_INET; // IP, PF_INET == AF_INET
                    saddr.sin_addr.s_addr = htonl(INADDR_ANY); // all IP address okey; network byte order; INADDR_ANY == 0
                    saddr.sin_port = htons(port); // port
                    if(bind(listenfd, (SA*)&saddr, sizeof(saddr)) < 0){ //-1
                        std::cerr << "ERROR on binding" << std::endl;
                        break;
                    }
                    if(listen(listenfd, 5) < 0){ //-1, queue length==5
                        std::cerr << "ERROR on listen" << std::endl;
                        break;
                    }
                    process(listenfd);
                }while(0); //via: https://www.cnblogs.com/lizhenghn/p/3674430.html & https://www.zhihu.com/question/24386599
                close(listenfd);
            }
            ```
        - `client`
          - ```cpp
            #include <iostream>
            #include <sys/types.h>
            #include <sys/socket.h>
            #include <unistd.h>
            #include <arpa/inet.h>
            #include <string.h>
            #include <error.h>
            #include "client.h"
            
            using SAI = struct sockaddr_in;
            using SA = struct sockaddr;
            
            const int LEN = 4096;
            
            void process(const int confd){
                while(true){
                    char buf[LEN];
                    memset(buf, '\0', sizeof(buf));
                    std::cout << " plz enter:";
                    std::cin>>buf;
                    if(strcmp(buf, "quit") == 0){
                        break;
                    }
                    if(std::cin.eof()){
                        break;
                    }
                    write(confd, buf, strlen(buf));
            
                    memset(buf, '\0', sizeof(buf));
                    ssize_t s = read(confd, buf, sizeof(buf));
                    if(s == 0){
                        std::cout << "server quit" << std::endl;
                        break;
                    } else if(s < 0){
                        std::cout << "read error" << std::endl;
                        break;
                    } else{
                        std::cout << "read " << s << " bytes: " << buf << std::endl;
                    }
            
                }
            }
            
            void client(const char* ip, const int port){
                int confd;
                do{
                    confd = socket(PF_INET, SOCK_STREAM, 0);
                    if (confd < 0) { // -1
                        std::cerr<<"ERROR opening socket" << std::endl;
                        break;
                    }
                    SAI saddr;
                    saddr.sin_family = AF_INET;
                    inet_pton(AF_INET, ip, &saddr.sin_addr );
                    saddr.sin_port = htons(port); 
                    if(connect(confd, (SA*)&saddr, sizeof(saddr)) < 0){ //-1
                        std::cerr << "ERROR on binding" << std::endl;
                        break;
                    }
                    process(confd);
                }while(0); //via: https://www.cnblogs.com/lizhenghn/p/3674430.html & https://www.zhihu.com/question/24386599
                close(confd);
               
            }
            ```
      - TODO UDP
        - `server`
          collapsed:: true
          - ```cpp
            #include <iostream>
            #include <sys/types.h>
            #include <sys/socket.h>
            #include <unistd.h>
            #include <arpa/inet.h>
            #include <string.h>
            
            #include "server.h"
            #include "message.h"
            
            using SAI = struct sockaddr_in;
            using SA = struct sockaddr;
            
            const int LEN = 4096;
            
            void process(const int confd) {
                char buf[LEN];
            
                while(true){
                    memset(buf, 0, LEN);
            
                    SAI caddr;
                    memset (&caddr, 0, sizeof(caddr));
                    socklen_t calen = sizeof(caddr);
                    recvfrom(confd, buf, LEN-1, 0, (SA *)&caddr, &calen); //  LEN-1
                    // handle_msg(confd);
                    sendto(confd, buf, strlen(buf), 0, (SA *)&caddr, calen);
                }
            }
            
            void server(const int port){
                // udp just have a port
                int confd;
            
                do{
                    confd = socket(PF_INET, SOCK_DGRAM, 0);
                    if(confd == -1) {
                        std::cerr<<"socket error"<<std::endl;
                        break;
                    }
                    // bind address 
                    SAI saddr;
                    memset(&saddr, 0, sizeof(saddr));
                    saddr.sin_family = AF_INET;
                    saddr.sin_addr.s_addr = htonl(INADDR_ANY);
                    saddr.sin_port = htons(port);
                    if(bind(confd, (SA*)&saddr, sizeof(saddr)) == -1) {
                        std::cerr<<"bind error"<<std::endl;
                        break;
                    }
                    process(confd);
                }while(0);
                close(confd);
            }
            ```
        - `client`
          collapsed:: true
          - ```cpp
            #include <iostream>
            #include <sys/types.h>
            #include <sys/socket.h>
            #include <unistd.h>
            #include <arpa/inet.h>
            #include <string.h>
            #include <error.h>
            #include "client.h"
            // #include "message.h"
            
            using SAI = struct sockaddr_in;
            using SA = struct sockaddr;
            
            const int LEN = 4096;
            
            void process (const int confd, SAI& saddr){
                char buf[LEN];
            
                while(true){
                    memset(buf, 0, LEN);
                    // std::cin.clear();
                    std::cin>>buf;
            
                    sendto(confd, buf, strlen(buf), 0, (SA*)&saddr, sizeof(saddr));
            
                    recvfrom(confd, buf, LEN, 0, NULL, NULL); // LEN-1
                    std::cout<<buf<<std::endl;
                }
            }
            
            void client(const char* ip, const int port){
                int confd;
                do{
                    confd = socket(PF_INET, SOCK_DGRAM, 0);
                    if (confd < 0) { // -1
                        std::cerr<<"ERROR opening socket" << std::endl;
                        break;
                    }
                    // udp don't bind , don't connect
                    SAI saddr;
                    saddr.sin_family = AF_INET;
                    inet_pton(AF_INET, ip, &saddr.sin_addr );
                    saddr.sin_port = htons(port);
                    process(confd, saddr);
                }while(0);
                close(confd);
            }
            ```
-
- 多线程
  - 线程基础使用
    - ```cpp
      #include <iostream>
      #include <thread>
      #include <stdlib.h>
      
      class ThreadGuard{ 
          std::thread t_;
      public:
          ThreadGuard (std::thread t):t_(std::move(t)){}
          ~ThreadGuard (){ // 析构一定会被调用
              if(t_.joinable()){
                  t_.join();
              }
          }
          ThreadGuard(ThreadGuard&) = delete;
          ThreadGuard operator =(ThreadGuard&)= delete;
      };
      
      class Perfect{
          int n;
          int factorSum(int n){
              int sum=0;
              for(int i=1; i<n; i++){
                  if(n%i==0) sum +=i;
              }
              return sum;
          }
      public:
          Perfect(int n):n(n){}
          void operator()(){
              if(factorSum(n) == n){
                  std:: cout<< "yes\n";
              }else{
                  std:: cout<< "no\n";
              }
          }
      
      };
      
      
      int main(int argc, char* argv[]){
          int n = atoi (argv[1]);
          // std::cout << (isPerfect(n)? "Yes\n" : "No\n") <<std::endl;
          // std::thread t(isPerfect, n);
          // t 线程对象 管理
          // function 真正的线程, 后面跟参数
          Perfect pf(n);
          std::thread t(pf);
          ThreadGuard tg(std::move(t)); //t对应的线程移动到 t -> t_
      
          //t.join();
          return 0;
      }
      ```
  - 买票
    - `std::lock_guard<std::mutex>` 可以减少上锁, 消锁的操作
    - ```cpp
      #include <stdlib.h>
      #include <iostream>
      #include <thread>
      #include <atomic>
      #include <mutex>
      
      std::mutex tmutex;
      
      void sellref(int& tickets, int num){
          for(int i = 0; i < num; i++){
              std::lock_guard<std::mutex> lg(tmutex);
      
              if(tickets == 0){
                  std::cout << "Sold Out " << i << " Tickets\n";
                  break;
              }
              tickets--;
          }
      }
      
      void refund(int& tickets, int num){
          for(int i = 0; i < num; i++){
              std::lock_guard<std::mutex> lg(tmutex);
              tickets++;
          }
      }
      
      int main(int argc, char * argv[]){
          int total = atoi(argv[1]),
              back = atoi(argv[2]),
              tickets = total;
      
          // std::thread w1(sell, &tickets, total);              // 传指针
          std::thread w1(sellref, std::ref(tickets), total);
          std::thread w2(sellref, std::ref(tickets), total);  // 传引用
          std::thread w3(sellref, std::ref(tickets), total);
          std::thread w4(refund, std::ref(tickets), back);
      
          w1.join();
          w2.join();
          w3.join();
          w4.join();
      
          std::cout<<tickets<<std::endl;
          return 0;
      }
      // RUN: ./a.out 10000 50000
      ```
  - 哲学家吃饭
    - ```cpp
      #include<iostream>
      #include<thread>
      #include<mutex>
      
      //via: https://www.cnblogs.com/pigdragon/p/6951475.html
      const int NUM_THREADS = 5;
      
      std::mutex chopstick[NUM_THREADS];
      
      void philosopher(int id){
          while(true){
      
              int left = id;
              int right = (id + 1) % NUM_THREADS;
      
              std::this_thread::sleep_for(std::chrono::milliseconds(1000));
              std::cout<<"Philosopher "<<id<<" is thinking\n";
      
              if (try_lock(chopstick[left], chopstick[right]) == -1){
                  //via: https://stackoverflow.com/questions/4362459/check-to-see-if-a-pthread-mutex-is-locked-or-unlocked-after-a-thread-has-locked & http://www.cplusplus.com/reference/mutex/try_lock/
                  std::cout<<"Philosopher "<<id<<" is eating\n";
              }else{
                  chopstick[left].lock();
                  chopstick[right].lock();
                  continue;
              }
      
              chopstick[left].unlock();
              chopstick[right].unlock();
      
              std::cout<<"Philosopher "<<id<<" is putting down chopstick\n";
          }
      }
      
      
      int main(int argc, char * argv[]){
      
          std::thread philosophers[NUM_THREADS];
      
          for(int i = 0; i < NUM_THREADS; i++){
              philosophers[i] = std::thread(philosopher, i);
          }
      
          for(int i = 0; i < NUM_THREADS; i++){
              philosophers[i].join();
          }
      
          return 0;
      }
      ```
  - 存钱取钱
    - ```cpp
      #include<iostream>
      #include <stdlib.h>
      #include <thread>
      #include <atomic>
      #include <mutex>
      
      std::mutex tmutex;
      
      struct Account{
          int balance;
          std::string aid;
          // Account():balance(0){}
          Account(std::string id, int balance):aid(id), balance(balance){}
      };
      
      std::ostream& operator <<(std::ostream& os, const Account& acc){
          os << "Balance: " << acc.balance << " Account ID: " << acc.aid;
          return os;
      }
      
      void withdraw(Account& acc, int amount){
          std::lock_guard<std::mutex> lg(tmutex);
          if(acc.balance < amount){
              std::cout << "Insufficient Funds\n";
              return;
          }
          acc.balance -= amount;
          std::cout << "Withdrawal Successful"<<acc<<"\n";
      }
      
      
      void deposit(Account& acc, int amount){
          std::lock_guard<std::mutex> lg(tmutex);
          acc.balance += amount;
          std::cout << "Deposit Successful "<<acc<<" \n";
      }
      
      int main(int argc, char* argv[]){
          Account account("100001", 50000);
          std::thread t1(withdraw, std::ref(account), 60000);
          std::thread t2(withdraw, std::ref(account), 30000);
          std::thread t3(deposit, std::ref(account), 10000);
          std::thread t4(deposit, std::ref(account), 5000);
      
          t1.join();
          t2.join();
          t3.join();
          t4.join();
      
          std::cout<<account<<std::endl;
      }
      
      ```
-
- Other
  - [[vim]]
  - [[command/exec]] 系统调用
    collapsed:: true
    - ```cpp
      pid_t child=fork();
      if(child==0){
          execlp("/bin/mkdir", "mkdir", "-v", "createdByChild", NULL);
          exit(0);
      }else{
          printf("%d", child);
          wait(NULL);
      }
      return 0;
      ```
    - `file1(main)`
      ```cpp
      #include <stdio.h>
      #include <stdlib.h>
      #include <sys/types.h>
      #include <unistd.h>
      
      extern int create_process (char* program, char** arg_list);
      
      int main (){
          char* arg_list[] = {
              "ls",
              "-l",
              "/home/bgzocg/",
              NULL
          };
          create_process("ls", arg_list);
          return 0;
      }
      ```
      ---
      `file2`
      ```cpp
      #include <stdio.h>
      #include <stdlib.h>
      #include <sys/types.h>
      #include <unistd.h>
      
      extern int create_process (char* program, char** arg_list);
      
      int create_process (char* program, char** arg_list){
          pid_t child_pid;
          child_pid = fork();
          if (child_pid != 0)
              return child_pid;
          else {
              execvp (program, arg_list);
              abort ();
          }
      }
      
      ```
  - [[command/tar]] 打包
  -
- Refs
  - [Linux创建进程链、进程扇、进程树_小咸鱼一条的博客-CSDN博客_进程树怎么画](https://blog.csdn.net/weixin_45907789/article/details/109256707)