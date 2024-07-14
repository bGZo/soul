alias:: tools/docker
icon:: 🐳
created:: [[20240524]]

- ## Why
- ## How
  - How to pull container via [[proxy]] ?
    - ```shell
      sudo mkdir -p /etc/docker
      sudo tee /etc/docker/daemon.json <<-'EOF'
      {
        "registry-mirrors": ["https://ustc-edu-cn.mirror.aliyuncs.com/"]
      }
      EOF
      sudo systemctl daemon-reload
      sudo systemctl restart docker
      ```
    - Personal mirror: ((6650a095-667c-4169-8fd8-49074f4678fc)) #[[Privacy]]
      - Get via: https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors
      - 阿里云 => 控制台 => 容器镜像服务 => 镜像加速器
    - More details via: https://docs.docker.com/engine/install
- ## What
  -
-
-
-
-
-
-
-
-
-
-
-
-
-
- ```
  bgzo@LAPTOP-CELTBLVE:~$ cat /proc/version
  Linux version 5.15.146.1-microsoft-standard-WSL2 (root@65c757a075e2) (gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37) #1 SMP Thu Jan 11 04:09:03 UTC 2024
  bgzo@LAPTOP-CELTBLVE:~$ uname -a
  Linux LAPTOP-CELTBLVE 5.15.146.1-microsoft-standard-WSL2 #1 SMP Thu Jan 11 04:09:03 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
  ```
- [[proxy]] config
  - ```shell
    $ sudo apt-get remove docker docker-engine
    $ docker-ce docker.io #卸载旧版本docker
    $ sudo apt-get remove --auto-remove docker #清空旧版docker占用的内存
    $ sudo apt-get update
    $ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common #安装环境
    $ curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add - #阿里云的docker GPG密钥
    $ sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" #阿里镜像源
    $ sudo apt-get update
    $ apt-cache madison docker-ce #查看多版本
    $ sudo apt-get install -y docker-ce #安装最新版
    $ sudo apt-get install -y docker-ce=5:19.03.6~3-0~ubuntu-bionic #安装5:19.03.6~3-0~ubuntu-bionic版
    $ sudo service docker restart
    $ sudo systemctl restart docker #重启Docker
    $ sudo docker version # Docker 版本
    ```
  - 替换成功后, 运行`sudo docker run hello-world`, 检验是否成功.
-
- Refs
  - [A Docker Tutorial for Beginners](https://docker-curriculum.com/#introduction).
  - [Ubuntu20.04 LTS国内源安装指定版本Docker/docker-compose - 放飞梦想C - 博客园](https://www.cnblogs.com/chengmf/p/13122013.html)
  - [prakhar1989/docker-curriculum: A comprehensive tutorial on getting started with Docker!](https://github.com/prakhar1989/docker-curriculum)
-