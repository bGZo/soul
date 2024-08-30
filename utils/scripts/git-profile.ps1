# CHCP 65001 not work
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$name = git config user.name
echo "current user name => $name"

$email = git config user.email
echo "current user email => $email"

$proxy = git config http.proxy
echo "current user proxy => $proxy"

