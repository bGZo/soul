also:: design/photo
icon:: 📷
- [[compress]]
  collapsed:: true
  - commands
  - Webp <- `cwebp/ffmpeg`
    - [Induction](https://developers.google.com/speed/webp)
      id:: 28f3486f-45c0-4a2e-ae38-449fcaace64f
    - [download](https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html)
      id:: fc619fb7-3783-491c-9d27-db20220249d8
    - ```shell
      $ sudo apt install webp
      $ cwebp -q 50 -lossless picture.png -o picture_lossless.webp
      $ cwebp -q 70 picture_with_alpha.png -o picture_with_alpha.webp
      $ cwebp -sns 70 -f 50 -size 60000 picture.png -o picture.webp
      $ cwebp -o picture.webp -- ---picture.png
      # https://developers.google.com/speed/webp/docs/cwebp
      ```
  - Jpeg <- `jpegoptim`
    - ```shell
      jpegoptim --size=1024k ().jpg
      ```
  - Png <- optipng
-