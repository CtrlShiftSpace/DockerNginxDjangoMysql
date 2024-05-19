# 使用Docker 建立 Nginx + Django + Mysql + Redis

## 使用說明
將 mysite目錄下的 .env.example 更名為.env
```
cd ./mysite
mv .env.example .env
```

到docker-compose.yml的目錄下，啟動背景服務
```
docker-compose up -d
```
