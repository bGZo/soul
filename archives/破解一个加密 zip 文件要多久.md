icon:: 💾
author:: 时国怀
created:: [[20240727]]
exclude-from-graph-view:: true
source:: https://www.zhihu.com/question/23728226/answer/25530432
type:: archives-web

- 做过AES加密，隐约记得AES-256的处理速度好像是10MB/s，假设破解ZIP文件需要读一个扇区的数据，那么一秒能处理20480个扇区，24小时一共能处理:
- 20480*3600*24=1769472000 = 1.769472e+9
- 按照你说的组合：假设只包括大小写和数字，一共是62个字符，9位的总组合数是：
- 62^9 = 13537086546263552 = 1.3537086546263552e+16
- 数量级差了7个，就算处理速度提高1000倍，还需要1万天左右才能破解，所以，放弃吧。
- 另外，我不清楚如果用硬件加速计算以后会怎么样，我的时间是按照CPU时间算的。
- 补充，我自己测试的结果：基于openssl 1.0.1g的AES-256-ECB，外层封装XTS算法，
- **每512字节换一次key**
- ，16字节为一组，一秒钟处理数据约40MB/s，C语言代码，gcc编译，运行环境debian，CPU是I7-3770，主频3.4G，单线程，无硬件优化。
- 我这个配置算是很高的配置，如果用显卡加速，加上各种优化，多线程一起跑，速度应该能提高1-2个数量级，但我觉得每秒处理速度要超过1GB还是有困难的，那么一秒钟能跑200万个密码，如果跑字典的话，这个速度足够了，但就看题主自己的密码有多复杂了，万一字典里没有，那就没办法了。
- 另外，有人说的用CRC校验，是个不错的思路。