icon:: 📄
also:: 字节序, 端序, 尾序
created:: [[20240713]]

- ## Why
- ## How
- ## What
  - > 小人国为水煮蛋该从大的一端 (Big-End) 剥开还是小的一端 (Little-End) 剥开而争论，争论的双方分别被称为 "大端派 (Big-End·ians)" 和 "小端派 (Little-Endians)"  -- Gulliver's Travels
  - 小端 / 小尾序 / Little-endian
    - 低位字节在前 (地址较小处)，高位字节在后 (地址较大处)
  - 大端 / 大尾序 / Big-endian
    - 高位字节在前，低位字节在后
  - ![image.png](../assets/encoding/image_1654676187458_0.png){:height 471, :width 289}
  - ![https://www.figma.com/file/ufL3Sy24q450XODURO2SD5/endian%2Fbig%2Flittle?node-id=0%3A1](../assets/encoding/image_1654698703359_0.png){:height 544, :width 360}
    - So to be sure about the ARM endianness, you need to refer to the reference manual from the manufacturer. via: [Is ARM big endian or little endian? - Quora](https://www.quora.com/Is-ARM-big-endian-or-little-endian)
      id:: 62a0b386-30b3-4feb-b427-f953042fca53
- ## Reference
  - https://www.ruanyifeng.com/blog/2016/11/byte-order.html
-