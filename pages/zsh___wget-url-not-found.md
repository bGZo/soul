- This is a common problem when working with urls as well.
- ```shell
  curl http://www.google.com/search?q=rails
  # => zsh: no matches found: http://www.google.com/search?q=rails
  ```
- However, you can escape it with a backslash or quote it.
- ```shell
  curl "http://www.google.com/search?q=rails"
  ```
- I don't know of any config to change this on a case-by-case basis (to keep the wildcard working). Do you?
- **双引网址** 即可.