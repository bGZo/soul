alias:: tool/docker

-
- [[Proxy]] config
  collapsed:: true
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
  - 登录阿里云, 在 控制台 -> 容器镜像服务 -> 镜像加速器 [里面](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)找到对应的加速器地址. #[[Privacy]]
    collapsed:: true
    - ```shell
      $ cd /etc/docker | sudo mkdir -p /etc/docker  
      $ sudo tee /etc/docker/daemon.json <<-'EOF'
      {
        "registry-mirrors": [
          "https://9mz5nt2s.mirror.aliyuncs.com"
        ]
      }
      $ sudo systemctl daemon-reload
      $ sudo systemctl restart docker
      # more details see: https://docs.docker.com/engine/install
      ```
  - 替换成功后, 运行`sudo docker run hello-world`, 检验是否成功.
-
- Refs
  collapsed:: true
  - [A Docker Tutorial for Beginners](https://docker-curriculum.com/#introduction).
  - [Ubuntu20.04 LTS国内源安装指定版本Docker/docker-compose - 放飞梦想C - 博客园](https://www.cnblogs.com/chengmf/p/13122013.html)
  - [prakhar1989/docker-curriculum: A comprehensive tutorial on getting started with Docker!](https://github.com/prakhar1989/docker-curriculum)
-