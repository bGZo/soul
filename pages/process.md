alias:: os/process, 进程

- TODO 用 go 和 docker 讲解进程????
- ## Wiki
  - 守护进程 & 僵尸进程 & 孤儿进程
    collapsed:: true
    - **守护进程(daemon)**
      - 以进程的形式初始化, 是一种在后台执行的电脑程序。进程程序的名称通常以字母“d”结尾; 很多守护进程在系统引导的时候启动，并且一直运行直到系统关闭; 如syslogd就是指管理系统日志的守护进程。
    - **僵尸进程**
      - 子进程先于父进程退出后，子进程的PCB需要其父进程释放，但是父进程并没有释放子进程的PCB，这样的子进程就称为僵尸进程。即完成执行（通过 exit 系统调用，或运行时发生致命错误或收到终止信号所致）但在操作系统的进程表中仍然有一个表项（进程控制块PCB），处于"终止状态 "的进程, 实际上是一个已经死掉的进程。对应PS里面的defunct和Top里面的zombie.下面俩个僵尸进程我居然不能杀, 太TM... 值得一提的是 WPS 退出来居然也是僵尸进程...
      - ```bash
           dfs        53396   53321  0 18:05 tty2     00:00:00 [fcitx] <defunct>
           dfs        55583   55388  0 18:07 pts/1    00:00:00 grep --color=auto defunct
        ```
    - **孤儿进程**
      - 在其父进程执行完成或被终止 后仍继续运行的一类进程。
  - 普通进程
    collapsed:: true
    - ```cpp
      #include<unistd.h>
      #include<signal.h>
      #include<stdio.h>
      #include<stdlib.h>
      #include<sys/param.h>
      #include<sys/types.h>
      #include<sys/stat.h>
      #include<time.h>
      void main(){
          FILE *fp;
          time_t t;
          while(1){
              sleep(6);
              fp=fopen("hello.log","a");
              if(fp>=0){
                  time(&t);
                  fprintf(fp,"current time is:%s\n",asctime(localtime(&t)));
                  fclose(fp);
              }
          }
          return;
      }
      ```
    - 守护进程
      - ```cpp
        #include<unistd.h>
        #include<signal.h>
        #include<stdio.h>
        #include<stdlib.h>
        #include<sys/param.h>
        #include<sys/types.h>
        #include<sys/stat.h>
        #include<time.h>
        void init_daemon(){
          int pid, ;
          pid=fork();
          if(pid<0) exit(1);
          else if(pid>0) exit(0);
          setsid();
          pid=fork();
          if(pid>0) exit(0); 
          else if(pid<0) exit(1);
          for(i=0;i<NOFILE;i++)close(i);
          chdir("/tmp");
          umask(0);
          return;
        }
        void main(){
          FILE *fp;
          time_t t;
          printf("pid = %d\n", getpid());
          init_daemon();
          while(1){
              sleep(6);
              fp=fopen("hello2.log","a");
              if(fp>=0){
                  time(&t);
                  fprintf(fp,"current time is:%s\n",asctime(localtime(&t)));
                  fclose(fp);
              }
          }
          return;
        }
        ```
    - 僵尸进程（子进程）
      - ```cpp
        #include <stdio.h>
        #include <stdlib.h>
        #include <unistd.h>
        #include <sys/wait.h>
        int main(){
         pid_t id = fork();
         if(id < 0){
            perror("fork");
            return 1;
         }
         else if(id > 0){
            printf("parent [%d] is sleeping\n",getppid());
            sleep(500);
         }
         else{
            printf("child [%d] is begining\n",getpid());
            sleep(2);
            exit(1);
         }
         return 0;
        }
        ```
    - 用到的简单命令
      - ```bash
        gcc xxx.c -o xxx #后面是指明输出文件的名字
        ./xxx 
        ps -aux | grep xxx # 
        cat /tmp/xxx.log 
        top # 不看不知道, 一看吓一跳, 我的电脑里面有两个僵尸进程, woc
        ```
- ## [[linux/kernel]] Process | Linux 操作进程
  - 进程创建运行 by [[cpp]]
    collapsed:: true
    - **fork：函数用于从已存在的进程中创建一个新进程**（新进程称为子进程，而原进程称为父进程。这个函数有两个返回值，子进程返回0，父进程返回父进程的pid，pid 是一个标志进程的数字，可以用函数getpid() 获得）
    - **exec：函数提供在进程中启动另一个程序执行的方法**。
    - **exit：函数用来进程结束**。
    - **wait：进程一旦调用了wait，就立即阻塞自己**，当发现当前进程的子进程已经exit，便会收集这个子进程的信息，然后彻底销毁，如果没有找到这样的子进程，就会一直阻塞。
    - **sleep：就是挂起进程指定的秒数**。
    - **getpid：返回当前进程（调用这一函数的进程）的ID**。
    - **getppid：返回当前进程的父进程的ID**。
    - ```c
      #include <stdio.h>
      #include <stdlib.h>
      #include <unistd.h>
      #include <sys/wait.h>
      int main(void){
          pid_t childpid;
          int status;
          childpid = fork();
          if (-1 == childpid){
              perror("fork()");
              exit(EXIT_FAILURE);
          }
          else if(0 == childpid){
              puts("In child process");
              sleep(10);
              printf("\tchild pid = %d\n", getpid());
              printf("\tchild ppid = %d\n", getppid());
              exit(EXIT_SUCCESS);
          }else{
              waitpid(childpid, &status, 0);
              puts("in parent");
              printf("\tparent pid = %d\n", getpid());
              printf("\tparent ppid = %d\n", getppid());
              printf("\tchild process exited with status %d \n", status);
          }
          exit(EXIT_SUCCESS);
      }
      ```
    -
  - 经由 [[linux/system-call]] 处理的进程操作
    - 后台进程管理 `fg`、`bg`、`jobs`、`&`、`ctrl + z`、`ctrl + c`、`ctrl + \`、`ctrl + d`
      - `&`: 加在一个命令的最后，可以把这个命令放到后台执行
        - `gftp &`
      - `ctrl + z`: 可以将一个正在前台执行的命令放到后台，并且处于暂停状态，不可执行
      - `jobs`: 查看当前有多少在后台运行的命令
        - `-l`:  选项可显示所有任务的PID
        - 3 个状态
          - running
          - stopped
          - Terminated
        - 显示的是当前shell环境中所起的后台正在运行或者被挂起的任务信息；
          - 如果任务被终止了(kill)，shell 从当前的shell环境已知的列表中删除任务的进程标识
      - `fg`: 将后台中的命令调至前台继续运行
        `bg`: 将一个在后台暂停的命令，变成继续执行 （在后台执行）
        - ` fg %jobnumber`:  后台中有多个命令, 将选中的命令调出
          - `%jobnumber`: 不是`pid`, 是通过 `jobs命令` 查到的**后台正在执行的命令的序号**
      - `ctrl+z`（挂起）, SIGTSTP 信号
      - `ctrl+c`（中断）, SIGINT 信号
      - `ctrl+\`（退出）, SIGQUIT 信号, 终止前台进程并生成 core 文件
      - `ctrl+d`（EOF）, 不发信号，特殊二进制值
    - 终止 `kill`: `ps`/`jobs`
    - 挂起 `stop`(solaris)
      - 前台挂起: `ctrl+Z`
      - `redhat`: kill -stop PID，将进程挂起；
      - 当要重新执行当前被挂起的任务时，通过bg %num 即可将挂起的job的状态由stopped改为running，仍在后台执行；当需要改为在前台执行时，执行命令fg %num即可
- ## [[ipc]] | 进程间通信
-