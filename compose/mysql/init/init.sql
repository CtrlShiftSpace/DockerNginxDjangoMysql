# 資料庫帳號密碼，需要和.env文件中相同
Alter user 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON mysite.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;