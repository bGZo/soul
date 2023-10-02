title:: linux/system-call/fork

-
- Return
  id:: 63049e75-857f-4575-b888-4008ea57c54d
  - > On success, the PID of the child process is returned in the parent, and 0 is returned in the child.  On failure, -1 is returned in the parent, no child process is created, and errno is set appropriately.
  - ==-1
    - 异常, 失败
  - == 0
    - child 返回
  - \>0
    - 父进程返回子进程 PID
-