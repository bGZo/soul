# CHCP 65001 not work
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

git pull origin main

# git add .

git add ../../logseq/
git add ../../pages/
git add ../../utils/


git commit -am "docs: a commit a day keeps the girl friend away"

git push origin main
