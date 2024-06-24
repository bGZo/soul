alias:: python/library
icon:: 🐍
created:: [[20230627]]
title:: Python Library
- ## Why
- ## How
  - ### How to traverse?
    collapsed:: true
    - collapsed:: true
      #+BEGIN_NOTE
      遍历 `Str`, `List` 相似，一共存在 4 种方法： #.ol
      #+END_NOTE
      - `for` 循环；
      - 下标遍历；
      - `iter` 迭代器遍历
        - collapsed:: true
          #+BEGIN_NOTE
          拿到迭代器也有两种写法（while / for）
          #+END_NOTE
          - ```python
            myiter = iter(mylist)
            # 1 For
            for every_char in myiter:
             print(every_char)
            # 2 While
            while True:
              try:
                print(next(myiter))
              except StopIteration:
                break
            ```
      - `enumerate` 遍历
      - collapsed:: true
        ---
        - ```python
          demo_str = "Hello World!"
          # 1
          for i in demo_str:
            print(i)
          # 2
          for i in range(len(demo_str)):
            print(demo_str[i])
          # 3 enumerate() 返回一个 计数器 和 迭代对象
            for index, every_char in enumerate(demo_str):
            print(str(index) + every_char)
          # 4 iter() 迭代器
          for every_char in iter(demo_str):
           print(every_char)
          ```
        - ```python
          list = ['l', 'o', 'v','e', '!']
          # 1
          for i in list:
            print(i, end='')
          # 2
          for i in range(len(list)):
            print(list[i], end='')
          # 3
          for i, val in enumerate(list):
            print(list[i], end='')
          # 4
          for i, val in enumerate(list, 2):
            print(list[i-2], end='')
          # 5
          myiter = iter(list)
          for x in myiter:
            print(x)
          ```
    - collapsed:: true
      #+BEGIN_NOTE
      遍历 `dict`，一共有 3 种方法：
      #+END_NOTE
      - ```python
        mydict = {"name": "Alice", "age": 18, "gender": "female"}
        # 1
        for key in mydict:
          print(key, ":", mydict[key])
        # 2：items() 返回字典中的每个键值对元组
        for key, value in mydict.items():
          print(key, ":", value) # 输出 name : Alice 等
        # 3 keys() 返回所有键的识图对象；values 返回所有值的识图对象；
        for key in mydict.keys():
            print(key)
        for value in mydict.values():
            print(value)
        ```
    - collapsed:: true
      #+BEGIN_NOTE
      Set 遍历因为不存在下标的概念，所以不存在 `len` 函数，不支持下标遍历；
      #+END_NOTE
      - ```python
        myset = {"apple", "banana", "cherry"}
        # 1
        for item in myset:
        	print(item)
        # 2
        myiter = iter(myset)
        print(next(myiter))
        while True:
            try:
                print(next(myiter))
            except StopIteration:
                break
        # 3
        for index, value in enumerate(myset):
            print("Index:", index, "Value:", value)
        ```
  - [How to check if a list is empty in Python (tutorialspoint.com)](https://www.tutorialspoint.com/How-to-check-if-a-list-is-empty-in-Python)
    collapsed:: true
    - Using **not** operator.
    - ==Using len() function==.
    - By Comparing with an Empty List.
    - Using __len__()
    - Using NumPy Module.
  - How to traverse a path directoty?
    collapsed:: true
    - ```python
      from os import getcwd, walk
      dir_set   = set()
      file_list = []
      for root, dirs, files in walk(getcwd()):
          for file in files:
            dir_set   .add(root)
            file_list .append(os.path.join(root, file))
      ```
    - `os.walk(PATH)`
      collapsed:: true
      - ```python
        from os import getcwd, walk
        root, dirs, files = walk(getcwd())
        print(root, '\n', dirs, '\n', files, '\n')
        # ('E:\\OneDrive\\workspace\\scripts\\get_twitter_mastodon', ['utils'], ['backup_res_mastodon.json', 'backup_res_twitter.json', 'Drop me and get Twitter.bat', 'get_twitter_mastodon_content_with_logseq_format.py', 'input', 'input.txt', 'Pipfile', 'requirements.txt', 'test.py', 'tmp.py'])
        # ('E:\\OneDrive\\workspace\\scripts\\get_twitter_mastodon\\utils', ['__pycache__'], ['get_mastodon.py', 'get_twitter.py', 'template.py', 'utils.py'])
        # ('E:\\OneDrive\\workspace\\scripts\\get_twitter_mastodon\\utils\\__pycache__', [], ['template.cpython-310.pyc', 'utils.cpython-310.pyc'])
        ```
- ## What
  - ### Data  Types #.ol
    collapsed:: true
    - Number，数字
      collapsed:: true
      - `int`
      - `float`
      - `bool`
      - `complex`
      - Convertion
        collapsed:: true
        - ```python
          print('''{0}\
                   {1}\
                   {2}\
                   {3}\
                   {4}\
                   {5}
                   '''.format(str(12),\
                              int('12'),\
                              hex(12),\
                              ord('a'),\
                              chr(97),\
                              int('12', 16)))
          ```
    - String，字符串
      collapsed:: true
      - `"Hello world!"`
    - List，列表
      collapsed:: true
      - `[a, b, c]`
    - Tuple，元组
      collapsed:: true
      - `(a, b)`
    - Set，集合
      collapsed:: true
      - `{a, b, c}`
    - Frozenset，冻结集合（不可变）
    - Dict，字典
      collapsed:: true
      - `{"Hello": "World"}`
    - **Advanced**:
      collapsed:: true
      - bytes
      - bytearray
      - memoryview
  - ### `str`
    collapsed:: true
    - 种类：#.ol
      collapsed:: true
      - Unicode String / 文本字符串 / `u'xxx'` [default]
      - Byte String / 字节字符串 / `b'xxx'`
      - #+BEGIN_NOTE
        Raw String /  原始字符串 / `r'xxx'`：包含在内的字符 `\` 不具备转义功能；常用于路径或者正则表达式中；
        #+END_NOTE
    - 切片
  - ### TODO `Time` via: [Python documentation](https://docs.python.org/3/library/time.html), [zh](https://docs.python.org/zh-cn/3/library/time.html)
    collapsed:: true
    - Terminology and conventions (术语和惯例) #.ol
      collapsed:: true
      - The *==epoch==* is the point where the time starts, the return value of time.gmtime(0). It is January 1, 1970, 00:00:00 (UTC) on all platforms.
      - The term *==seconds since the epoch==* refers to the total number of elapsed seconds since the epoch, typically **excluding [leap seconds](https://en.wikipedia.org/wiki/Leap_second)**. Leap seconds are excluded from this total on all POSIX-compliant platforms.
      - The functions in this module may not handle dates and times before the [epoch](https://docs.python.org/3/library/time.html#epoch) or far in the future. The cut-off point in the future is determined by the C library; for 32-bit systems, it is typically in 2038.
      - Function [strptime()](https://docs.python.org/3/library/time.html#time.strptime) can parse 2-digit years when given %y format code. When 2-digit years are parsed, they are converted according to the POSIX and ISO C standards: values 69–99 are mapped to 1969–1999, and values 0–68 are mapped to 2000–2068.
      - UTC is Coordinated Universal Time (formerly known as Greenwich Mean Time, or GMT). The acronym UTC is not a mistake but a compromise between English and French.
      - DST is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part of the year. DST rules are magic (determined by local law) and can change from year to year. The C library has a table containing the local rules (often it is read from a system file for flexibility) and is the only source of True Wisdom in this respect.
      - The precision of the various real-time functions may be less than suggested by the units in which their value or argument is expressed. E.g. on most Unix systems, the clock “ticks” only 50 or 100 times a second.
      - On the other hand, the precision of [time()](https://docs.python.org/3/library/time.html#time.time) and [sleep()](https://docs.python.org/3/library/time.html#time.sleep) is better than their Unix equivalents: times are expressed as floating point numbers, [time()](https://docs.python.org/3/library/time.html#time.time) returns the most accurate time available (using Unix gettimeofday() where available), and [sleep()](https://docs.python.org/3/library/time.html#time.sleep) will accept a time with a nonzero fraction (Unix select() is used to implement this, where available).
      - The time value as returned by [gmtime()](https://docs.python.org/3/library/time.html#time.gmtime), [localtime()](https://docs.python.org/3/library/time.html#time.localtime), and [strptime()](https://docs.python.org/3/library/time.html#time.strptime), and accepted by [asctime()](https://docs.python.org/3/library/time.html#time.asctime), [mktime()](https://docs.python.org/3/library/time.html#time.mktime) and [strftime()](https://docs.python.org/3/library/time.html#time.strftime), is a sequence of 9 integers. The return values of [gmtime()](https://docs.python.org/3/library/time.html#time.gmtime), [localtime()](https://docs.python.org/3/library/time.html#time.localtime), and [strptime()](https://docs.python.org/3/library/time.html#time.strptime) also offer attribute names for individual fields.
      - See [struct_time](https://docs.python.org/3/library/time.html#time.struct_time) for a description of these objects.
      - *Changed in version 3.3: *The [struct_time](https://docs.python.org/3/library/time.html#time.struct_time) type was extended to provide the tm_gmtoff and tm_zone attributes when platform supports corresponding struct tm members.
      - *Changed in version 3.6: *The [struct_time](https://docs.python.org/3/library/time.html#time.struct_time) attributes tm_gmtoff and tm_zone are now available on all platforms.
      - Use the following functions to convert between time representations:
    - Data Structure
      collapsed:: true
      - [struct_time](https://docs.python.org/3/library/time.html#time.struct_time)
    - time.**strftime**(*format*[, *t*])
      collapsed:: true
      - | Directive | Meaning |
        | ---- | ---- |
        | %a | Locale’s abbreviated weekday name. |
        | %A | Locale’s full weekday name. |
        | %b | Locale’s abbreviated month name. |
        | %B | Locale’s full month name. |
        | %c | Locale’s appropriate date and time representation. |
        | %d | Day of the month as a decimal number [01,31]. |
        | %H | Hour (24-hour clock) as a decimal number [00,23]. |
        | %I | Hour (12-hour clock) as a decimal number [01,12]. |
        | %j | Day of the year as a decimal number [001,366]. |
        | %m | Month as a decimal number [01,12]. |
        | %M | Minute as a decimal number [00,59]. |
        | %p | Locale’s equivalent of either AM or PM. |
        | %S | Second as a decimal number [00,61]. |
        | %U | Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0. |
        | %w | Weekday as a decimal number [0(Sunday),6]. |
        | %W | Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0. |
        | %x | Locale’s appropriate date representation. |
        | %X | Locale’s appropriate time representation. |
        | %y | Year without century as a decimal number [00,99]. |
        | %Y | Year with century as a decimal number. |
        | %z | Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59]. |
        | %Z | Time zone name (no characters if no time zone exists). Deprecated. |
        | %% | A literal '%' character. |
  - TODO `OS`
  - TODO `Datetime`
  - TODO RE
  - TODO Requests
  -
  - collapsed:: true
    ---
    - ### 判断是不是二进制文件
      collapsed:: true
      - ```python
        textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        # is_binary_string(open('/usr/bin/python', 'rb').read(1024))
        # >>> True
        # via https://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
        # https://github.com/file/file/blob/f2a6e7cb7db9b5fd86100403df6b2f830c7f22ba/src/encoding.c#L151-L228
        ```
    - ### OS Manage
      collapsed:: true
      - os
        - os.getcwd(): 得到当前工作目录，即当前Python脚本工作的目录路径
        - os.listdir(): 返回指定目录下的所有文件和目录名
        - os.remove(): 函数用来删除一个文件
        - os.removedirs(r“c：\python”): 删除多个目录
        - os.path.isfile(): 检验给出的路径是否是一个文件
        - os.path.isdir(): 检验给出的路径是否是一个目录
        - os.path.isabs(): 判断是否是绝对路径
        - os.path.exists(): 检验给出的路径是否真地存
        - os.path.split() eg os.path.split(‘/home/swaroop/byte/code/poem.txt’) 结果：(‘/home/swaroop/byte/code’, ‘poem.txt’): 返回一个路径的目录名和文件名
        - os.path.splitext(): 分离扩展名
        - os.path.dirname(): 获取路径名
        - os.path.basename(): 获取文件名
        - os.system(): 运行shell命令
        - os.getenv() 与os.putenv(): 读取和设置环境变量
        - os.linesep Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’: 给出当前平台使用的行终止符
        - os.name 对于Windows，它是’nt’，而对于Linux/Unix用户，它是’posix’: 指示你正在使用的平台
        - os.rename(old， new): 重命名
        - os.makedirs(r“c：\python\test”): 创建多级目录
        - os.mkdir(“test”): 创建单个目录
        - os.stat(file): 获取文件属性
        - os.chmod(file): 修改文件权限与时间戳
        - os.exit(): 终止当前进程
        - os.path.getsize(filename): 获取文件大小
      - Path Manage
        - os.mkdir(“file”): 创建目录
        - shutil.copyfile(“oldfile”,”newfile”): 复制文件, oldfile和newfile都只能是文件
        - shutil.copy(“oldfile”,”newfile”): 复制文件, oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
        - shutil.copytree(“olddir”,”newdir”): 复制文件夹, olddir和newdir都只能是目录，且newdir必须不存在
        - os.rename(“oldname”,”newname”): 重命名文件(目录), 文件或目录都是使用这条命令
        - shutil.move(“oldpos”,”newpos”): 移动文件(目录)
        - os.remove(“file”): 删除文件
        - os.rmdir(“dir”) : 删除目录, 只能删除空目录
        - shutil.rmtree(“dir”):删除目录, 空目录、有内容的目录都可以删
        - os.chdir(“path”) 转换目录, 换路径
      -
      - ```shell
        Open
        os.mknod(“test.txt”)创建空文件
        fp = open(“test.txt”,w) 直接打开一个文件，如果文件不存在则创建文件
        w：以写方式打开，
        a：append, 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
        r+：以读写模式打开
        w+：以读写模式打开 (参见 w )
        a+：以读写模式打开 (参见 a )
        rb：以二进制读模式打开
        wb：以二进制写模式打开 (参见 w )
        ab：以二进制追加模式打开 (参见 a )
        rb+：以二进制读写模式打开 (参见 r+ )
        wb+：以二进制读写模式打开 (参见 w+ )
        ab+：以二进制读写模式打开 (参见 a+ )
        fp.read([size]) size为读取的长度，以byte为单位
        fp.readline([size]) 读一行，如果定义了size，有可能返回的只是一行的一部分
        fp.readlines([size]) 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
        fp.write(str) 把str写到文件中，write()并不会在str后加上一个换行符
        fp.writelines(seq) 把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
        fp.close() 关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。 如果一个文件在关闭后还对其进行操作会产生ValueError
        fp.flush() 把缓冲区的内容写入硬盘
        fp.fileno() 返回一个长整型的”文件标签“
        fp.isatty() 文件是否是一个终端设备文件(unix系统中的)
        fp.tell() 返回文件操作标记的当前位置，以文件的开头为原点
        fp.next() 返回下一行，并将件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
        fp.seek(offset[,whence]) 将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
        ```
      - from: https://blog.csdn.net/silentwolfyh/article/details/74931123
    - ### 遍历本地一级目录
      collapsed:: true
      - I am run wsl2, so `C:\Users\xxx\Pictures\pic` is not suitting me. Should use the mount path, such as `/mnt/c/Users/15517/Pictures/pic`.
      - ```python
        import os
        localDir = []
        localFile = []
        PATH = os.getcwd()
        for root,dirs,files in os.walk(PATH):
            for dir in dirs:
                for file in files:
                    localDir.append(os.path.join(root,dir))
                    localFile.append(os.path.join(root, file))
        ```
    - ### 遍历所有文件
      collapsed:: true
      - ```
        for root,dirs,files in os.walk(r"D:\test"):
            for file in files:
                print(root) # 获取文件所属目录
                print(os.path.join(root,file))# 获取文件路径
        for root,dirs,files in os.walk(r"D:\test"):
            for dir in dirs:
                print(dir) #获取目录的名称
                print(os.path.join(root,dir)) #获取目录的路径
        #递归获取该目录下所有的文件名称和目录名称
        def get_file_path(root_path,file_list,dir_list):
            dir_or_files = os.listdir(root_path)
            for dir_file in dir_or_files:
                dir_file_path = os.path.join(root_path,dir_file)
                if os.path.isdir(dir_file_path): # 判断 文件/路径
                    dir_list.append(dir_file_path)
                    get_file_path(dir_file_path,file_list,dir_list)
                else:
                    file_list.append(dir_file_path)
        ```
      - `walk all file, so the method is like os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])`
        collapsed:: true
        - top − Each directory rooted at directory, yields 3-tuples, i.e.(dirpath, dirnames, filenames)
        - topdown − If optional argument topdown is True or not specified,
        - directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.
        - onerror − This can show error to continue with the walk, or raise the exception to abort the walk.
        - followlinks − This visits directories pointed to by symlinks, if set to true.
        - refer to:
          - https://www.tutorialspoint.com/python/os_walk.htm
          - https://blog.csdn.net/sinat_29957455/article/details/82778306
    - ### 拿到所有文件名
      collapsed:: true
      - ```python
        import os
        DirList = []
        FileNameList = []
        DIR = os.getcwd()
        for root, dirs, files in os.walk(DIR):
            for file in files:
                DirList.append(os.path.join(root,file))
                nowFileName = os.path.splitext(file) # Here
                FileNameList.append(nowFileName[0])
                # from: https://www.geeksforgeeks.org/python-os-path-splitext-method/
        ```
  - ### Print
    collapsed:: true
    - 不换行打印, 参数 end=''
    - ```python
      # print(StrFormat, file=ff) # output to file using print with `file`
      ```
  - ### Re
    collapsed:: true
    - **crawler**: `re.findall()` is more better. and you should notice the usage of `re.match`.
      - **`re.match`**: match from **begin** of string!!! I support Judge is better...
      - **`re.search`**: match anywhere!
    - ```python
      import re
      target= '{"is_success": true, "message": "9a5ab695d17c3b3271ef48e825a5a52114acfecc92094986ee0ae761d9e33ed712642d6b1647434b493b850d4237cb20be2b0f7cd456d51f88f62bd82ae37518d2baae7570c49c6f59a8051c7e42e5a0395be18da9a39ccc198a8df90129cebf49373c11d9823e24f47b609b56088f039c5a1b120874822fdffa21102430a834"}'
      m =re.search(r'"(message)": "(.*)?"', target)
      print(target[m.start():m.end()])
      print(m.group(1)) # notice don not use group[1]
      print(m.group(2))
      ```
    - Flag pattern could use
      - | 修饰符 | 描述                                                         |
        | ------ | ------------------------------------------------------------|
        | re.I   | 使匹配对大小写不敏感                                          |
        | re.L   | 做本地化识别（locale-aware）匹配                              |
        | re.M   | 多行匹配，影响 ^ 和 $                                        |
        | re.S   | 使 . 匹配包括换行在内的所有字符                                |
        | re.U   | 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.        |
        | re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。    |
    - More have `split`, `finditer`, `sub` and `compile`. more see in https://docs.python.org/zh-cn/3/library/re.html
  - ### Requests
    collapsed:: true
    - test: http://icanhazip.com/
    - ### proxy
      collapsed:: true
      - urllib.urlopen: ProxyHandler -> opener -> request install, more help in
        - https://gist.github.com/bGZoCg/82a76ecbebf81b556a1d20a91a6bd21a
        - https://gohom.win/2016/01/21/proxy-py/
      - ```python
        import urllib
        proxy="http://127.0.0.1:7890"
        # Build ProxyHandler object by given proxy, wsl2 is hard...
        proxy_support=urllib.request.ProxyHandler({'http':proxy})
        # Build opener with ProxyHandler object
        opener = urllib.request.build_opener(proxy_support)
        # Install opener to request
        urllib.request.install_opener(opener)
        # Open url
        # r = urllib.request.urlopen('http://icanhazip.com',timeout = 1000)
        ```
      - requests: could use system proxy. or
      - ```
        requests.request() 	构造一个请求，支持以下各种方法
        requests.get() 		获取html的主要方法
        requests.head() 		获取html头部信息的主要方法
        requests.post() 		向html网页提交post请求的方法
        requests.put() 		向html网页提交put请求的方法
        requests.patch() 		向html提交局部修改的请求
        requests.delete() 		向html提交删除请求
        ```
  - ### Re
    collapsed:: true
    - collapsed:: true
      ```python
      import requests
      proxies = {
          "http": "http://127.0.0.1:7890",
          "https": "http://127.0.0.1:7890",
          }
      # r=requests.get("http://icanhazip.com", proxies=proxies)
      ```
      - auth: authentication, 认证
        - Basic Auth
  - ### JSON (JavaScript Object Notation)
    collapsed:: true
    - **`loads`**
    - **`dumps`**
    - ```python
      import json
      def get_json_to_dict(url):
          r = requests.get(url, auth=('user', 'pass')) # Basic Auth
          data = json.loads(r.text) # get a dict obj
          _ans = data['items']
          return _ans
      ```
    - Transform string **json to dict**: it depends on your json response, maybe its no match of key and value in raw json. So you only get very long string.
    - ```python
      def get_unend_dict(Dict):
          unendDict = {}
          index = 0
          for i in Dict:
              if i['end'] == "":
                  unendDict[index] = i
                  # FIXME: how to add sub_dict don't use index???
                  index += 1
          return unendDict
      ```
  - ### Base64
    collapsed:: true
    - ### 去掉文件开头的 `b`
    - 开头的 `b` 表示二进制文件, 解码会发生错误
      > The base64 encoding converts every 3 input bytes to 4 ASCII characters from a restricted set. -- https://stackoverflow.com/questions/58323382/binascii-error-invaild-base64-encoded-string-number-of-data-characters1957-c
    - if you don not open with 'rb', you'll get `error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte`, see more in https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
    - ```python
      import base64
      def f(PATH):
          with open(PATH, "rb") as f:
              base64_data = base64.b64encode(f.read())
              print(base64_data)
              # https://blog.csdn.net/qq_42731401/article/details/105039539
      ```
  - ### Math
    collapsed:: true
    - `math.floor()` & `//` is different. While calculating big number, you may be will see the number of `0` is much more, which must be wrong! You could use `hex()` to verify. Cause the floor return is float, is not int, the precision is bad.
    - ```python
      ans=[]
      target = 18415121715151845121548215411215820216445125484101548460051710202051815025484202061840201
      while target != 0:
          ans.append(chr(target%256))
          temp //= 256 # floor, math.floor is wrong... use gex() to verify
      ```
  - ### pyinstaller
    collapsed:: true
    - 找到程序位置执行
      pyinstaller -F xxx.py
      想去掉黑窗口(命令行窗口)
      pyinstaller -F -w xxx.py
      修改图标
      pyinstaller -F -w -i xx.ico xxx.py
      http://www.bitbug.net/  图标生成地址
      注意：打包的文件名最好不是中文的！！
- collapsed:: true
  ---
  - Wolk 目录的格式注意: Py的默认编码是 Unicode, 所以需要加字符 **r**, 否则将报`(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape [duplicate] <generator object walk at 0x7f067f9a9820>`. 正确下写法如: `os.walk(r'/mnt/c/Users/15517/Pictures/pic')`. Alos have other char:
  - or `pandas.read_csv("C:/Users/DeePak/Desktop/myac.csv")` / `pandas.read_csv("C:\\Users\\DeePak\\Desktop\\myac.csv")` is okey. Refer to:
  - [python - Error "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape" - Stack Overflow](https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca)
  - [Project Jupyter | Home](https://jupyter.org/)
  - I'll put some code (cells)examples in here insteaded of to Gist. This are much better. It could use Cpp/Python/Java and more probablly. I used to get some help in following links, wish next time I don't need to refer to them.
  - And some tips to me, which make sense after i made a mistake.
  - Its False Not false. Its True Not ture.
  - {} 不可以声明集合, 它表示空字典, https://www.runoob.com/python3/python3-set.html
  - 导包: `import urllib.*` is okay?
      With packages, like this, you sometimes need to explicitly import the piece you want. That way, the urllib module doesn't have to load everything up just because you wanted one small part. --from: https://stackoverflow.com/questions/37042152/python-3-5-1-urllib-has-no-attribute-request
  - exist: None
  - main function: [Python 中的 if __name__ == '__main__' 该如何理解 | Huoty's Blog](https://blog.konghy.cn/2017/04/24/python-entry-program/)
  - 有一次为了避免文件创建的重名问题, 一时方便取巧, 将文件的开头加入今天的时间之后在做重命名, 但是有一个问题, **必须加到毫秒才会安全**, 因为如果最小任务单位制是毫秒级的话, 精确到秒的命名规则就会出现问题. **[FIXME]** 那么如何加毫秒呢???
  - ```python
    import time
    newDir = str(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
    ```
-