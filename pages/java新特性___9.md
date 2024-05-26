## 概述
  - 经过4次推迟，历经曲折的Java9最终在2017年9月21日发布。因为里面加入的模块化系统，在最初设想的时候并没有想过那么复杂，花费的时间超出预估时间。距离java8大约三年时间。
  - Java 9提供了超过150项新功能特性，包括备受期待的模块化系统、可交互的REPL工具: jshell, JDK编译工具，语法层面的改变：Java公共API和私有代码，以及安全增强、扩展提升、性能管理改善等。可以说Java 9是一个庞大的系统工程，完全做了一个整体改变。
  - 但是这个巨大改变的功劳，都给了java11了，**目前oracle对8,11都长期支持，9,10不支持了**，只能从[历史版本](http://jdk.java.net/)中下载，Java 11 将会获得 Oracle 提供的长期支持服务，直至2026年9月。
  - 从Java9这个版本开始，Java 的计划发布周期是6个月，下一个Java的主版本将于2018年3月发布，命名为Java18.3(java10)， 紧接着再过六个月将发布Java18.9 (java11).
  - 这意味着Java的更新**从传统的以特性驱动的发布周期，转变为以时间驱动的(6个月为周期)发布模式**（更快的时间周期,oracle的理念就是小步快跑，快速迭代，像IBM（DB2数据库，保守型内部测试才投入市场）），并逐步的将Oracle JDK原商业特性进行开源。针对企业客户的需求，Oracle将以三年为周期发布长期支持版本(long term support)
  - 重大改变：
    - 模块化系统
      logseq.order-list-type:: number
    - jShell命令
      logseq.order-list-type:: number
  - 语法层面改变：
    - 接口私有方法
      logseq.order-list-type:: number
    - 钻石操作符（泛型<>）使用升级
      logseq.order-list-type:: number
    - 语法改进：try语句
      logseq.order-list-type:: number
  - API层面变化：
    - String存储结构变更 （从char类型数组变为byte类型数组）
        logseq.order-list-type:: number
    - 集合特性：of()
        logseq.order-list-type:: number
    - 增强的Stream API(不断迭代，要重视这个Stream)
        logseq.order-list-type:: number
    - 全新的HTTP客户端API（不仅支持HTTP1.1而且还支持HTTP2：从
        logseq.order-list-type:: number
    - 以前的HttpUrlConnection-变为现在的HttpClient）
        logseq.order-list-type:: number
    - Deprecated的 API
        logseq.order-list-type:: number
  - 其它变化：
    - javadoc的HTML5支持
        logseq.order-list-type:: number
    - Js引擎升级：Nashorn（9对8升级了，但是11里又没有了）
        logseq.order-list-type:: number
    - java的动态编译器
        logseq.order-list-type:: number
    - 多版本兼容jar包
        logseq.order-list-type:: number
  - 官方提供的新特性的列表
    - https://docs.oracle.com/javase/9/whatsnew/toc.htm#JSNEW-GUID-C23AFD78-C777-460B-8ACE-58BE5EA681F6
  - openJDK  可参考源码
    - http://openjdk.java.net/projects/jdk9/
  - 在线 OracleJDK Documentation 在线文档
    - https://docs.oracle.com/javase/9/
  - JDK和JRE的目录的改变
    - JDK8
      - ```shell
        [bgzo@LAPTOP 8u342-b07]$ tree -L 2
        .
        ├── ASSEMBLY_EXCEPTION
        ├── bin # 命令行开发和调试工具
        │   ├── appletviewer.exe
        │   ├── clhsdb.exe
        │   ├── extcheck.exe
        │   ├── hsdb.exe
        │   ├── idlj.exe
        │   ├── jabswitch.exe
        │   ├── jar.exe
        │   ├── jarsigner.exe
        │   ├── javac.exe
        │   ├── javadoc.exe
        │   ├── java.exe
        │   ├── javah.exe
        │   ├── javap.exe
        │   ├── java-rmi.exe
        │   ├── javaw.exe
        │   ├── jcmd.exe
        │   ├── jconsole.exe
        │   ├── jdb.exe
        │   ├── jdeps.exe
        │   ├── jfr.exe
        │   ├── jhat.exe
        │   ├── jinfo.exe
        │   ├── jjs.exe
        │   ├── jli.dll
        │   ├── jmap.exe
        │   ├── jps.exe
        │   ├── jrunscript.exe
        │   ├── jsadebugd.exe
        │   ├── jstack.exe
        │   ├── jstatd.exe
        │   ├── jstat.exe
        │   ├── keytool.exe
        │   ├── kinit.exe
        │   ├── klist.exe
        │   ├── ktab.exe
        │   ├── msvcr100.dll
        │   ├── native2ascii.exe
        │   ├── orbd.exe
        │   ├── pack200.exe
        │   ├── policytool.exe
        │   ├── rmic.exe
        │   ├── rmid.exe
        │   ├── rmiregistry.exe
        │   ├── schemagen.exe
        │   ├── serialver.exe
        │   ├── servertool.exe
        │   ├── tnameserv.exe
        │   ├── unpack200.exe
        │   ├── wsgen.exe
        │   ├── wsimport.exe
        │   └── xjc.exe
        ├── demo
        │   ├── applets
        │   ├── jfc
        │   ├── jpda
        │   ├── jvmti
        │   ├── management
        │   ├── nbproject
        │   ├── nio
        │   ├── README
        │   └── scripting
        ├── include # 编译本地代码时使用的c/c++头部文件
        │   ├── classfile_constants.h
        │   ├── jawt.h
        │   ├── jdwpTransport.h
        │   ├── jni.h
        │   ├── jvmticmlr.h
        │   ├── jvmti.h
        │   └── win32
        ├── jre
        │   ├── ASSEMBLY_EXCEPTION
        │   ├── bin # 包含基本指令, windows 上,它包含系统的运行时动态链接
        │   │   ├── attach.dll
        │   │   ├── awt.dll
        │   │   ├── dt_shmem.dll
        │   │   ├── dt_socket.dll
        │   │   ├── fontmanager.dll
        │   │   ├── freetype.dll
        │   │   ├── hprof.dll
        │   │   ├── instrument.dll
        │   │   ├── j2pcsc.dll
        │   │   ├── j2pkcs11.dll
        │   │   ├── jaas_nt.dll
        │   │   ├── jabswitch.exe
        │   │   ├── JavaAccessBridge-64.dll
        │   │   ├── java_crw_demo.dll
        │   │   ├── java.dll
        │   │   ├── java.exe
        │   │   ├── java-rmi.exe
        │   │   ├── javaw.exe
        │   │   ├── JAWTAccessBridge-64.dll
        │   │   ├── jawt.dll
        │   │   ├── jdwp.dll
        │   │   ├── jjs.exe
        │   │   ├── jli.dll
        │   │   ├── jpeg.dll
        │   │   ├── jsdt.dll
        │   │   ├── jsound.dll
        │   │   ├── jsoundds.dll
        │   │   ├── keytool.exe
        │   │   ├── kinit.exe
        │   │   ├── klist.exe
        │   │   ├── ktab.exe
        │   │   ├── lcms.dll
        │   │   ├── management.dll
        │   │   ├── mlib_image.dll
        │   │   ├── msvcr100.dll
        │   │   ├── net.dll
        │   │   ├── nio.dll
        │   │   ├── npt.dll
        │   │   ├── orbd.exe
        │   │   ├── pack200.exe
        │   │   ├── policytool.exe
        │   │   ├── rmid.exe
        │   │   ├── rmiregistry.exe
        │   │   ├── sawindbg.dll
        │   │   ├── server
        │   │   ├── servertool.exe
        │   │   ├── splashscreen.dll
        │   │   ├── sunec.dll
        │   │   ├── sunmscapi.dll
        │   │   ├── tnameserv.exe
        │   │   ├── unpack200.exe
        │   │   ├── unpack.dll
        │   │   ├── verify.dll
        │   │   ├── w2k_lsa_auth.dll
        │   │   ├── WindowsAccessBridge-64.dll
        │   │   └── zip.dll
        │   ├── lib # 包含用户可编辑的配置文件
        │   │   ├── accessibility.properties
        │   │   ├── amd64
        │   │   ├── applet
        │   │   ├── calendars.properties
        │   │   ├── charsets.jar
        │   │   ├── classlist
        │   │   ├── cmm
        │   │   ├── content-types.properties
        │   │   ├── currency.data
        │   │   ├── ext
        │   │   ├── flavormap.properties
        │   │   ├── fontconfig.bfc
        │   │   ├── fontconfig.properties.src
        │   │   ├── hijrah-config-umalqura.properties
        │   │   ├── images
        │   │   ├── jce.jar
        │   │   ├── jfr
        │   │   ├── jfr.jar
        │   │   ├── jsse.jar
        │   │   ├── jvm.hprof.txt
        │   │   ├── logging.properties
        │   │   ├── management
        │   │   ├── management-agent.jar
        │   │   ├── meta-index
        │   │   ├── net.properties
        │   │   ├── psfontj2d.properties
        │   │   ├── psfont.properties.ja
        │   │   ├── resources.jar
        │   │   ├── rt.jar # 包含运行时的java类和资源文件
        │   │   ├── security
        │   │   ├── sound.properties
        │   │   ├── tzdb.dat
        │   │   └── tzmappings
        │   ├── LICENSE
        │   └── THIRD_PARTY_README
        ├── lib # JDK工具的几个jar和其他类型的文件
        │   ├── ct.sym
        │   ├── dt.jar
        │   ├── ir.idl
        │   ├── jawt.lib
        │   ├── jconsole.jar
        │   ├── jvm.lib
        │   ├── orb.idl
        │   ├── sa-jdi.jar
        │   └── tools.jar # 含javac编译器的java类
        ├── LICENSE
        ├── manifest.json
        ├── release
        ├── sample
        │   ├── annotations
        │   ├── forkjoin
        │   ├── jmx
        │   ├── lambda
        │   ├── nbproject
        │   ├── nio
        │   ├── README
        │   ├── scripting
        │   └── try-with-resources
        ├── src.zip
        └── THIRD_PARTY_README
        ```
    - JDK9 从9开始以后的JDK目录结构都是如此
      - ```shell
        [bgzo@LAPTOP 9.0.4-12]$ tree -L 2
        .
        ├── bin # 包含所有指令,在windows平台上,他继续包含系统的运行时动态链接
        │   ├── appletviewer.exe
        │   ├── attach.dll
        │   ├── awt.dll
        │   ├── dt_shmem.dll
        │   ├── dt_socket.dll
        │   ├── fontmanager.dll
        │   ├── freetype.dll
        │   ├── idlj.exe
        │   ├── instrument.dll
        │   ├── j2pcsc.dll
        │   ├── j2pkcs11.dll
        │   ├── jaas_nt.dll
        │   ├── jabswitch.exe
        │   ├── jaccessinspector.exe
        │   ├── jaccesswalker.exe
        │   ├── jar.exe
        │   ├── jarsigner.exe
        │   ├── javaaccessbridge.dll
        │   ├── javac.exe
        │   ├── java.dll
        │   ├── javadoc.exe
        │   ├── java.exe
        │   ├── javah.exe
        │   ├── javajpeg.dll
        │   ├── javap.exe
        │   ├── javaw.exe
        │   ├── jawt.dll
        │   ├── jcmd.exe
        │   ├── jconsole.exe
        │   ├── jdb.exe
        │   ├── jdeprscan.exe
        │   ├── jdeps.exe
        │   ├── jdwp.dll
        │   ├── jhsdb.exe
        │   ├── jimage.dll
        │   ├── jimage.exe
        │   ├── jinfo.exe
        │   ├── jjs.exe
        │   ├── jli.dll
        │   ├── jlink.exe
        │   ├── jmap.exe
        │   ├── jmod.exe
        │   ├── jps.exe
        │   ├── jrunscript.exe
        │   ├── jshell.exe
        │   ├── jsound.dll
        │   ├── jsoundds.dll
        │   ├── jstack.exe
        │   ├── jstatd.exe
        │   ├── jstat.exe
        │   ├── keytool.exe
        │   ├── kinit.exe
        │   ├── klist.exe
        │   ├── ktab.exe
        │   ├── lcms.dll
        │   ├── le.dll
        │   ├── management_agent.dll
        │   ├── management.dll
        │   ├── management_ext.dll
        │   ├── mlib_image.dll
        │   ├── msvcp120.dll
        │   ├── msvcr120.dll
        │   ├── net.dll
        │   ├── nio.dll
        │   ├── orbd.exe
        │   ├── pack200.exe
        │   ├── policytool.exe
        │   ├── prefs.dll
        │   ├── rmic.exe
        │   ├── rmid.exe
        │   ├── rmi.dll
        │   ├── rmiregistry.exe
        │   ├── sawindbg.dll
        │   ├── schemagen.exe
        │   ├── serialver.exe
        │   ├── server
        │   ├── servertool.exe
        │   ├── splashscreen.dll
        │   ├── sunec.dll
        │   ├── sunmscapi.dll
        │   ├── tnameserv.exe
        │   ├── unpack200.exe
        │   ├── unpack.dll
        │   ├── verify.dll
        │   ├── w2k_lsa_auth.dll
        │   ├── windowsaccessbridge-64.dll
        │   ├── wsgen.exe
        │   ├── wsimport.exe
        │   ├── xjc.exe
        │   └── zip.dll
        ├── conf # 包含用户可编辑的配置文件,例如之前位于jre/lib目录中的.properties和policy
        │   ├── logging.properties
        │   ├── management
        │   ├── net.properties
        │   ├── security
        │   └── sound.properties
        ├── include # 包含在以前编译本地代码时使用c/c++头文件,他只存在于JDK中
        │   ├── classfile_constants.h
        │   ├── ir.idl
        │   ├── jawt.h
        │   ├── jdwpTransport.h
        │   ├── jni.h
        │   ├── jvmticmlr.h
        │   ├── jvmti.h
        │   ├── orb.idl
        │   └── win32
        ├── install.json
        ├── jmods # 包含JMOD格式的平台模块,创建自定义运行时映像需要他,它只存在于jdk中
        │   ├── java.activation.jmod
        │   ├── java.base.jmod
        │   ├── java.compiler.jmod
        │   ├── java.corba.jmod
        │   ├── java.datatransfer.jmod
        │   ├── java.desktop.jmod
        │   ├── java.instrument.jmod
        │   ├── java.logging.jmod
        │   ├── java.management.jmod
        │   ├── java.management.rmi.jmod
        │   ├── java.naming.jmod
        │   ├── java.prefs.jmod
        │   ├── java.rmi.jmod
        │   ├── java.scripting.jmod
        │   ├── java.security.jgss.jmod
        │   ├── java.security.sasl.jmod
        │   ├── java.se.ee.jmod
        │   ├── java.se.jmod
        │   ├── java.smartcardio.jmod
        │   ├── java.sql.jmod
        │   ├── java.sql.rowset.jmod
        │   ├── java.transaction.jmod
        │   ├── java.xml.bind.jmod
        │   ├── java.xml.crypto.jmod
        │   ├── java.xml.jmod
        │   ├── java.xml.ws.annotation.jmod
        │   ├── java.xml.ws.jmod
        │   ├── jdk.accessibility.jmod
        │   ├── jdk.attach.jmod
        │   ├── jdk.charsets.jmod
        │   ├── jdk.compiler.jmod
        │   ├── jdk.crypto.cryptoki.jmod
        │   ├── jdk.crypto.ec.jmod
        │   ├── jdk.crypto.mscapi.jmod
        │   ├── jdk.dynalink.jmod
        │   ├── jdk.editpad.jmod
        │   ├── jdk.hotspot.agent.jmod
        │   ├── jdk.httpserver.jmod
        │   ├── jdk.incubator.httpclient.jmod
        │   ├── jdk.internal.ed.jmod
        │   ├── jdk.internal.jvmstat.jmod
        │   ├── jdk.internal.le.jmod
        │   ├── jdk.internal.opt.jmod
        │   ├── jdk.internal.vm.ci.jmod
        │   ├── jdk.jartool.jmod
        │   ├── jdk.javadoc.jmod
        │   ├── jdk.jcmd.jmod
        │   ├── jdk.jconsole.jmod
        │   ├── jdk.jdeps.jmod
        │   ├── jdk.jdi.jmod
        │   ├── jdk.jdwp.agent.jmod
        │   ├── jdk.jlink.jmod
        │   ├── jdk.jshell.jmod
        │   ├── jdk.jsobject.jmod
        │   ├── jdk.jstatd.jmod
        │   ├── jdk.localedata.jmod
        │   ├── jdk.management.agent.jmod
        │   ├── jdk.management.jmod
        │   ├── jdk.naming.dns.jmod
        │   ├── jdk.naming.rmi.jmod
        │   ├── jdk.net.jmod
        │   ├── jdk.pack.jmod
        │   ├── jdk.policytool.jmod
        │   ├── jdk.rmic.jmod
        │   ├── jdk.scripting.nashorn.jmod
        │   ├── jdk.scripting.nashorn.shell.jmod
        │   ├── jdk.sctp.jmod
        │   ├── jdk.security.auth.jmod
        │   ├── jdk.security.jgss.jmod
        │   ├── jdk.unsupported.jmod
        │   ├── jdk.xml.bind.jmod
        │   ├── jdk.xml.dom.jmod
        │   ├── jdk.xml.ws.jmod
        │   └── jdk.zipfs.jmod
        ├── legal # 法律声明
        │   ├── java.activation
        │   ├── java.base
        │   ├── java.compiler
        │   ├── java.corba
        │   ├── java.datatransfer
        │   ├── java.desktop
        │   ├── java.instrument
        │   ├── java.logging
        │   ├── java.management
        │   ├── java.management.rmi
        │   ├── java.naming
        │   ├── java.prefs
        │   ├── java.rmi
        │   ├── java.scripting
        │   ├── java.se
        │   ├── java.security.jgss
        │   ├── java.security.sasl
        │   ├── java.se.ee
        │   ├── java.smartcardio
        │   ├── java.sql
        │   ├── java.sql.rowset
        │   ├── java.transaction
        │   ├── java.xml
        │   ├── java.xml.bind
        │   ├── java.xml.crypto
        │   ├── java.xml.ws
        │   ├── java.xml.ws.annotation
        │   ├── jdk.accessibility
        │   ├── jdk.attach
        │   ├── jdk.charsets
        │   ├── jdk.compiler
        │   ├── jdk.crypto.cryptoki
        │   ├── jdk.crypto.ec
        │   ├── jdk.crypto.mscapi
        │   ├── jdk.dynalink
        │   ├── jdk.editpad
        │   ├── jdk.hotspot.agent
        │   ├── jdk.httpserver
        │   ├── jdk.incubator.httpclient
        │   ├── jdk.internal.ed
        │   ├── jdk.internal.jvmstat
        │   ├── jdk.internal.le
        │   ├── jdk.internal.opt
        │   ├── jdk.internal.vm.ci
        │   ├── jdk.jartool
        │   ├── jdk.javadoc
        │   ├── jdk.jcmd
        │   ├── jdk.jconsole
        │   ├── jdk.jdeps
        │   ├── jdk.jdi
        │   ├── jdk.jdwp.agent
        │   ├── jdk.jlink
        │   ├── jdk.jshell
        │   ├── jdk.jsobject
        │   ├── jdk.jstatd
        │   ├── jdk.localedata
        │   ├── jdk.management
        │   ├── jdk.management.agent
        │   ├── jdk.naming.dns
        │   ├── jdk.naming.rmi
        │   ├── jdk.net
        │   ├── jdk.pack
        │   ├── jdk.policytool
        │   ├── jdk.rmic
        │   ├── jdk.scripting.nashorn
        │   ├── jdk.scripting.nashorn.shell
        │   ├── jdk.sctp
        │   ├── jdk.security.auth
        │   ├── jdk.security.jgss
        │   ├── jdk.unsupported
        │   ├── jdk.xml.bind
        │   ├── jdk.xml.dom
        │   ├── jdk.xml.ws
        │   └── jdk.zipfs
        ├── lib # 包含非windows平台上的动态链接本地库,其子目录和文件不应由开发人员直接编译或使用
        │   ├── classlist
        │   ├── ct.sym
        │   ├── fontconfig.bfc
        │   ├── fontconfig.properties.src
        │   ├── jawt.lib
        │   ├── jrt-fs.jar
        │   ├── jvm.cfg
        │   ├── jvm.lib
        │   ├── modules
        │   ├── psfontj2d.properties
        │   ├── psfont.properties.ja
        │   ├── sawindbg.dll.manifest
        │   ├── security
        │   ├── server
        │   ├── src.zip
        │   ├── tzdb.dat
        │   └── tzmappings
        ├── manifest.json
        └── release
        ```
- ## 一 语法层次的改变
  - ### 1_钻石操作符号语法升级
    - >钻石操作符,就是我们泛型使用的符号<>
      >
      >JAVA8 中,匿名内部类不能使用钻石操作符,如下代码在JAVA8 中是报错的,匿名内部类这里不支持泛型推断,重写的方法不明确泛型
      - ![1629966490626](../assets/mashibing/1629966490626.png)
    - > 这里匿名内部类中的<>号里必须要和前面的声明保持一致,不能空着不写,这样重写的方法就根据匿名内部类的泛型
    - ![1629966550374](../assets/mashibing/1629966550374.png)
    - > 但是这种写法在JAVA9 中就允许了
    - ![1629966634077](../assets/mashibing/1629966634077.png)
    - > 而且在JAVA9中,匿名内部类的语法不仅仅可以用于接口和抽象类,普通类也可以通过匿名内部类写法,在某个实例上完成对某个方法的重写
    - ``` java
      public class Demo1 {
        public static void main(String[] args) {
          /*
            * 匿名内部类仅仅在接口和抽象类上使用,作为一种快速的实现方式
            * JAVA9中,普通类也可以借助这种语法形式实现对方法的快速临时的重写
            * */
          Person<String> person=new Person<>(){
            @Override
            public void eat(String s) {
              super.eat(s);
            }
          };
          person.eat("包子");
        }
      }
      class Person<T>{
        public void eat(T t){
          System.out.println("Person eat");
        }
      }
      ```
  - ### 2_try结构语法升级
    - 原始：普通的try catch finally语句  要释放的资源可以放到finally语句块中
      - ``` java
        InputStreamReader reader =null;
        try{
          reader =new InputStreamReader(System.in);
          int read = reader.read();
        }catch (Exception e){
          throw new RuntimeException(e);
        }finally {
          // 这里可以释放资源
          if(null != reader){
            try {
              reader.close();
            } catch (IOException e) {
              e.printStackTrace();
            }
          }
        }
        ```
    - 改进：JAVA 7中已经对try语法进行了升级,可以将要释放的资源放到try后面的小括号中,这样就不用通过finally语句块释放资源了,**但是要求执行后必须关闭的资源一定要放在try子句中进行初始化,否则编译不通过.** 下面的案例中,reader必须放在try后面的小括号中进行初始化
      - ``` java
              try( InputStreamReader reader=new InputStreamReader(System.in) ){
                  int read = reader.read();
              }catch (Exception e){
                  throw new RuntimeException(e);
              }
        ```
    - JAVA ： 资源的关闭操作,我们可以在try子句中使用已经初始化的资源但是此时的资源必须 是final修饰的,final可以省略不写
      - ``` java
        public class Demo2 {
          public void testx(){
            // 传统的 try catch finally语句块
            InputStreamReader isr =null;
            try{
              isr =new InputStreamReader(new FileInputStream("d:/aaa.txt"));
              isr.read();
            }catch (Exception e){
              e.printStackTrace();
            }finally {
              if(null != isr){
                try {
                  isr.close();
                } catch (IOException e) {
                  e.printStackTrace();
                }
              }
            }
          }
          // JAVA7 try语法升级
          public void testa(){
            // JAVA7 try catch finally语句块
            try( InputStreamReader isr =new InputStreamReader(new FileInputStream("d:/aaa.txt"));){
              isr.read();
            }catch (Exception e){
              e.printStackTrace();
            }
          }
          // JAVA9 try语法升级
          public void testb() throws FileNotFoundException {
            // JAVA9 try catch finally语句块
            InputStreamReader isr =new InputStreamReader(new FileInputStream("d:/aaa.txt"));
            OutputStreamWriter isw =new OutputStreamWriter(new FileOutputStream("d:/aaa.txt"));
            try( isr; isw){
              isr.read();
            }catch (Exception e){
              e.printStackTrace();
            }
          }
        }
        ```
  - ### 3_下划线命名标识符的使用限制
    - 标识符命名组成：字母，数字，下划线，美元符
      - JAVA8 中,可以使用一个 _ 作为标识符的命名
        - ``` java
          String  _  ="宇智波赵四儿";
          ```
      - JAVA9 中,就不可以使用一个_ 作为标识符的命名了,不通过编译,但是标识符中仍然可以使用_,必须配合其他内容
        - ``` java
          String stu_name="旋涡刘能";
          ```
    - 小细节,注意一下即可,一般也没人直接单独用一个_ 作为标识符的命名
- ## 二 API层次的改变
  - ### 1_接口中的私有方法
    collapsed:: true
    - JAVA7 中,接口只能有抽象方法
    - JAVA8 中,接口中static(静态不可重写)和default(可以重写)修饰的方法可以拥有方法体
      - ```shell
        > static和default的生命周期有什么区别？
        在Java 8中，接口中的静态方法和默认方法具有不同的生命周期：
        1. **Static 方法**：静态方法是接口的一部分，它们属于接口的类加载时期。它们在接口被加载时就被解析。这意味着你可以直接通过接口名称调用静态方法，而不需要实例化接口的任何实现类。静态方法在编译期就已经确定，因此无法在实现类中被重写。静态方法的调用是通过接口名称直接调用，例如`InterfaceName.staticMethod()`。
        2. **Default 方法**：默认方法是接口的一部分，但它们的实现在实现类被加载时期之后。默认方法允许在接口中提供默认的实现，但仍然可以在实现类中重写。这为向现有接口添加新功能提供了一种方式，而不会破坏现有的实现类。如果实现类没有提供自己的实现，将会使用默认方法的实现。调用默认方法通常是通过接口的实例调用，例如`interfaceInstance.defaultMethod()`。
        ```
        #[[chatGPT]]
    - JAVA9 中,接口中可以使用private修饰方法,并拥有方法体,但是接口中的成员变量仍然不能用private修饰
      - ```java
        interface MyInter{
          // private 修饰的私有方法
          private int add(int a, int b){
            return a+b;
          }
        }
        ```
    - 感觉: 接口中的代码越来越靠近抽象类,但是仍然是支持多继承的
    - ``` java
      public class Demo4 {
        // 接口,是一种规范和要求
        // 实现多继承
      }
      // java7 接口中的方法必须都是抽象的
      interface  Inter1{
        void methoda();
      }
      // java8接口可以定义static/default修饰的非抽象方法
      interface  Inter2{
        void methoda();
        static void methodB(){
        }
        default void methodC(){
        }
      }
      // java9 允许定义私有的非抽象方法
      interface  Inter3{
        void methoda();
        static void methodB(){
        }
        default void methodC(){
          methodD();
        }
        private void methodD(){
        }
      }
      ```
  - ### 2_String底层存储结构的变更
    - Java 8
      - String类内部维护的是一个final修饰的私有char数组,说明String的底层是通过char数组存储字符串的
      - ```java
        public final class String
          implements java.io.Serializable, Comparable<String>, CharSequence {
            private final char value[];
        }
        ```
    - Java 9
      - String类内部维护的是一个final修饰的私有byte数组,说明String的底层是通过byte数组存储字符串的
      - ```java
        public final class String
          implements java.io.Serializable, Comparable<String>, CharSequence,
        Constable, ConstantDesc {
          @Stable
          private final byte[] value;
        }
        ```
      - 这么做的原因:
        - 大多数String对象只包含latin-1字符。 这样的字符只需要一个字节的存储空间，因此这样的String对象的内部字符数组中有一半的空间没有使用 , 我们建议将String类的内部表示形式从UTF-16字符数组更改为一个字节数组加上一个结束编码标志字段
  - ### 3_Stream新增4个API
    - JAVA9 中,Stream接口添加了4个新方法,`takeWhile`,`dropWhile`,`ofNullable`,还有一个`iterate` 方法的新重载方法,可以通过一个`Predicate`来指定什么时候结束迭代
      - ``` java
        /**
         * 测试Stream新增takeWhile方法
         * takeWhile  从流中的头开始取元素,直到不满足条件为止
         */
        public static void testTakeWhile(){
          List<Integer> list = Arrays.asList(1, 89, 63, 45, 72, 65, 41, 65, 82, 35, 95, 100);
          // 从头开始取所有奇数,直到遇见一个偶数为止
          list.stream().takeWhile(e-> e%2==1).forEach(System.out::println);
        }
        /**
         * 测试Stream新增dropWhile方法
         * dropWhile  从头开始删除满足条件的数据,直到遇见第一个不满足的位置,并保留剩余元素
         */
        public static void testDropWhile(){
          List<Integer> list = Arrays.asList(2, 86, 63, 45, 72, 65, 41, 65, 82, 35, 95, 100);
          // 删除流开头所有的偶数,直到遇见奇数为止
          list.stream().dropWhile(e-> e%2==0 ).forEach(System.out::println);
        }
        /**
         * 测试Stream新增ofNullable方法
         * ofNullable 允许创建Stream流时,只放入一个null
         */
        public static void testOfNullable(){
          // of方法获取流 ,允许元素中有多个null值
          Stream<Integer> stream1 = Stream.of(10, 20, 30, null);
          // 如果元素中只有一个null,是不允许的
          Stream<Integer> stream2 = Stream.of(null);
          // JAVA9中,如果元素为null,返回的是一个空Stream,如果不为null,返回一个只有一个元素的Stream
          Stream<Integer> stream3 = Stream.ofNullable(null);
        }
        /**
         * 测试Stream新增iterate方法
         * iterate指定种子数,指定条件和迭代方式来获取流
         */
        public static void testNewIterate(){
          //JAVA8通过 generate方法获取一个Stream
         Stream.generate(Math::random).limit(10).forEach(System.out::println);
          //JAVA8 通过iterate获取一个Stream
          Stream.iterate(0,t-> t+2).limit(10).forEach(System.out::println);
          //JAVA9通过重载iterate获取Stream
          Stream.iterate(0,t -> t<10,t-> t+1).forEach(System.out::println);
        }
        ```
    - 除了`Stream`本身的扩展,`Optional`和`Stream`之间的结合也得到了改进,现在可以通过`Optional`的新方法将一个`Optional`对象转换为一个`Stream`对象(可能是空的)
      - ```  java
        /**
         * Optional类新增Stream方法,可以将一个Optional转换为Stream
         */
        public static void testOptionalStream(){
          List<Integer> list =new ArrayList<>();
          Collections.addAll(list,10,5,45,95,36,85,47);
          Optional<List<Integer>> optional=Optional.ofNullable(list);
          // 通过optional的Stream方法获取一个Stream
          Stream<List<Integer>> stream = optional.stream();
          // 以为内部的每个元素也是一个List,通过flatMap方法,将内部的List转换为Stream后再放入一个大Stream
          stream.flatMap(x->x.stream()).forEach(System.out::println);
        }
        ```
  - ### 4_InputStream新增transferTo方法
    - `InputStream`新增`transferTo`方法,可以用来将数据直接传输到OutpuStream,这是在处理原始数据时非常常见的一种方法
      - ``` java
        InputStream inputStream =new FileInputStream("d:/aaa.txt");
        OutputStream outputStream=new FileOutputStream("d:/bbb.txt");
        try (inputStream;outputStream){
          inputStream.transferTo(outputStream);
        } catch (IOException e) {
          e.printStackTrace();
        }
        ```
  - ### 5_只读集合的创建
    - JAVA8 要创建一个只读,不可改变的集合,必须构造和分配他,然后添加元素,然后再包装成一个不可修的集合。 放入数据后,然后要通过unmodifiableList才能让集合变为只读集合,不能表达为单个的表达式
      - ``` java
        List<String> list= new ArrayList<>();
        list.add("Tom");
        list.add("Jerry");
        list.add("Mark");
        list.add("Jhon");
        list = Collections.unmodifiableList(list);
        System.out.println(list);
        ```
    - JAVA9 通过集合工厂方法,创建一个只读集合,只要通过新增的of方法即可完成创建
      - ``` java
        List<String> list= List.of("TOM","Jerry","Mark","Ben");
        System.out.println(list);
        ```
    - ![image.png](../assets/image_1711113031874_0.png){:height 258, :width 691}
      - 上面是List接口的of方法, 同样的,Set接口和Map接口下也新增了of方法,也是返回一个只读集合
- ## 三 其他变化
  - ### 1_JAVA9 模块化
    - 谈到Java9大家往往第一个想到的就是Jigsaw项目（后改名为Modularity）。众所周知，Java已经发展超过20年(`95`年最初发布)，Java和相关生态在不断丰富的同时也越来越暴露出一些问题:
      - 1Java运行环境的膨胀和臃肿。**每次JVM启动的时候，至少会有30~ 60MB的内存加载，主要原因是`JVM`需要加载`rt.jar`**,不管其中的类是否被`classloader`加载，第一步整个`jar`都会被`JVM`加载到内存当中去(而模块化可以根据模块的需要加载程序运行需要的`class`)
      - 2当代码库越来越大，创建复杂，盘根错节的“意大利面条式代码”的几率呈指数级的增长。不同版本的类库交叉依赖导致让人头疼的问题，这些都阻碍了Java 开发和运行效率的提升。
      - 3很难真正地对代码进行封装,而系统并没有对不同部分(也就是JAR文件)之间的依赖关系有个明确的概念。每一个公共类都可以被类路径之下任何其它的公共类所访问到，这样就会导致无意中使用了并不想被公开访问的API.
    - 本质上讲，模块化，就是在package外面包裹一层->>>说白了项目下有众多 模块
      进行项目管理，管理各个模块，比如一个电商项目  下面有支付模块 购物模块，，，模块跟模块之间相互调用，这样代码就更安全，可以指定哪些暴露 哪些隐藏！
    - 模块之间的可访问性是所使用的模块和使用模块之间的双向协议：模块明确地使其公共类型可供其他模块使用，而且使用这些公共类型的模块明确声明对第一个模块的依赖，模块中所有未导出的软件包都是模块的私有的，他们不能在模块之外使用.之前做不到，现在可以考虑这个事了
    - 在jdk9中,项目模块之间的依赖
      - 在JDK9 先准备一个项目,普通java项目即可,然后再项目下准备两个模块,名字为jdk9module1和jdk9module2,如下图
        - ![1629959034495](../assets/mashibing/1629959034495.png)
      - jdk9module1中添加一些类
        - ![1629959219122](../assets/mashibing/1629959219122.png)
      - 如何在jdk9module2中使用这个类? 或者说是使用模块1中的类,第一步,在两个模块的src下创建各自的module-info.java
        - ![1629959400483](../assets/mashibing/1629959400483.png)
      - 创建完毕后,结构如下
        - ![1629959441838](../assets/mashibing/1629959441838.png)
      - 在jdk9module1的module-info.java文件中,设置哪些包可以向外暴露
        - ![1629959666167](../assets/mashibing/1629959666167.png)
      - 在jdk9module2的module-info.java中引入模块1
        - ![1629959723837](../assets/mashibing/1629959723837.png)
      - 但是发现报错了,原因是,我们要把模块1添加为模块2的运行环境,具体操作如下
        - project structure > modules > jdk9module2 >dependencies  >>+module lib > jdk9module1 > apply >>ok
        - ![引入模块依赖](../assets/mashibing/引入模块依赖.gif)
      - 这个是时候,我们在模块2中就可以使用模块1 中的类了
        - ![使用模块一中的代码](../assets/mashibing/使用模块一中的代码.gif)
  - ### 2_可交互的REPL工具:jshell
    - 像Python和Scala 之类的语言早就有交互式编程环境REPL (read evaluate print loop)了，以交互式的方式对语句和表达式进行求值。开发者只需要输入一些代码，就可以在编译前获得对程序的反馈。而之前的Java 版本要想执行代码，必须创建文件、声明类、提供测试方法方可实现。
    - 要想实现REPL，需要一个命令：JShell命令
    - ![1629877864498](../assets/mashibing/1629877864498.png)
    - 将环境变量配置为java9，就可以在控制命令台使用jshell命令了：如果电脑上安装了其他版本的JDK,环境变量也是其他版本,大家可以在dos上通过cd 切换到指定版本的bin目录下,就可以使用该版本的jshell了
      collapsed:: true
      - ![1629962311415](../assets/mashibing/1629962311415.png)
    - > 案例：简单输出语句：
      - ![1629877895300](../assets/mashibing/1629877895300.png)
    - > 案例：变量定义
      - ![1629877926195](../assets/mashibing/1629877926195.png)
    - > 案例：方法定义和调用：
      - ![1629877952559](../assets/mashibing/1629877952559.png)
      - ![1629877968367](../assets/mashibing/1629877968367.png)
    - > 导包：
      - ![1629877991221](../assets/mashibing/1629877991221.png)
    - > 其实jshell中有默认的导入一些包（除了java.lang之外，以下包也可以直接用），可以直接使用不用导包，查看有哪些：
      - ![1629878023330](../assets/mashibing/1629878023330.png)
    - > 常用命令：
      - ![1629878047871](../assets/mashibing/1629878047871.png)
      - ![1629878065195](../assets/mashibing/1629878065195.png)
    - > 可以将某些常用命令持久化在硬盘上：
      - ![1629878182887](../assets/mashibing/1629878182887.png)
      - ![1629878211555](../assets/mashibing/1629878211555.png)
    - > jshell不用编译时异常处理：
      - ![1629878234271](../assets/mashibing/1629878234271.png)
    - > 退出jshell
      - ![1629878258920](../assets/mashibing/1629878258920.png)