>[!NOTE]
> 
>  The logseq behavior has changed. so this part of repo would be deprecated. 
>  No longer maintained. only archived here.

# Logseq Social Media Link Format

## Support site

- [x] http://mastodon.social
- [x] http://twitter.com
- [x] http://douban.com
- [ ] http://m.okjike.com
- [ ] http://m.weibo.com


## Usage Cases with `twitter`

Allow those formats(7 cases):

```shell
# 1. clear link
https://twitter.com/pandazhq/status/1678395427899465728
# 2. share link
https://twitter.com/pandazhq/status/1678395427899465728?s=20
# 3. share link2
https://twitter.com/pandazhq/status/1678395427899465728?s=52&t=LgI9ZHE1jAdamynKbX8X6w
# 4. link with markdown prefix
- https://twitter.com/pandazhq/status/1678395427899465728
# 5. share link with more markdown prefix
    - https://twitter.com/pandazhq/status/1678395427899465728?s=20
# 6. share link2 with more markdown prefix
    - https://twitter.com/pandazhq/status/1678395427899465728?s=52&t=LgI9ZHE1jAdamynKbX8X6w
# 7. hyberlink with more markdown prefix
    - [](https://twitter.com/pandazhq/status/1678395427899465728?s=52&t=LgI9ZHE1jAdamynKbX8X6w)
```


## Tests

```shell
python3.exe .\format_journals.py .\tests\20230722.md -o .\tests\test.md
python3.exe .\format_journals.py .\tests\20230812.md -o .\tests\test.md
```

## Notes

- 打包模块的时候需要把异常处理去掉，raise