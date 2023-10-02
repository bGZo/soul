-
- ` ./gradlew bootRun` 做了什么?
- [Unable to import maven project](https://stackoverflow.com/questions/30569909/unable-to-import-maven-project-in-intellij14)
  - Set your project configuraion JDK
- idea download dependencies via proxy failed
  - Reopen project.
  - couldn't solve by reload???
- [java - Intellij "Could not find or load main class" - Stack Overflow](https://stackoverflow.com/questions/51902094/intellij-could-not-find-or-load-main-class)
  - rm `.idea/modules.xml` and run project again.
- xml mirror [将maven源改为国内阿里云镜像 - 知乎](https://zhuanlan.zhihu.com/p/71998219)
  - ```
    <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                          http://maven.apache.org/xsd/settings-1.0.0.xsd">
      <localRepository/>
      <interactiveMode/>
      <usePluginRegistry/>
      <offline/>
      <pluginGroups/>
      <servers/>
      <mirrors>
        <mirror>
         <id>aliyunmaven</id>
         <mirrorOf>central</mirrorOf>
         <name>阿里云公共仓库</name>
         <url>https://maven.aliyun.com/repository/central</url>
        </mirror>
        <mirror>
          <id>repo1</id>
          <mirrorOf>central</mirrorOf>
          <name>central repo</name>
          <url>http://repo1.maven.org/maven2/</url>
        </mirror>
        <mirror>
         <id>aliyunmaven</id>
         <mirrorOf>apache snapshots</mirrorOf>
         <name>阿里云阿帕奇仓库</name>
         <url>https://maven.aliyun.com/repository/apache-snapshots</url>
        </mirror>
      </mirrors>
      <proxies/>
      <activeProfiles/>
      <profiles>
        <profile>  
            <repositories>
               <repository>
                    <id>aliyunmaven</id>
                    <name>aliyunmaven</name>
                    <url>https://maven.aliyun.com/repository/public</url>
                    <layout>default</layout>
                    <releases>
                            <enabled>true</enabled>
                    </releases>
                    <snapshots>
                            <enabled>true</enabled>
                    </snapshots>
                </repository>
                <repository>
                    <id>MavenCentral</id>
                    <url>http://repo1.maven.org/maven2/</url>
                </repository>
                <repository>
                    <id>aliyunmavenApache</id>
                    <url>https://maven.aliyun.com/repository/apache-snapshots</url>
                </repository>
            </repositories>             
         </profile>
      </profiles>
    </settings>
    ```
  - [Gradle 比 Maven 好为什么用的人少？ - 知乎](https://www.zhihu.com/question/276078446)
  - [你们会觉得 maven 做构建比 gradle 更好用吗 - V2EX](https://www.v2ex.com/t/615200)
  - [为什么 Java 的包管理器都这么复杂？ - V2EX](https://www.v2ex.com/t/753415?p=1)
  - [灵魂拷问之是否适合 Java 开发 - V2EX](https://www.v2ex.com/t/764794#; )