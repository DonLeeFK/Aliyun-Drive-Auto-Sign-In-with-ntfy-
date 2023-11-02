# Aliyun Drive auto sign in (with ntfy as notification service)
## 阿里云盘自动签到 

Use this python script with `CRONTAB` or any other scheduled task manager of your choice. I highly recommend you to setup a self hosted [ntfy](https://github.com/binwiederhier/ntfy) notification service. 
大多数人使用的青龙面板是一个非常臃肿的方案， 使用Linux常用的`CRONTAB`即可实现相同功能， 同时搭配`ntfy`还能推送通知。

### How to run
You should first create a file under the same path named `refreshToken`, which should contain your 'refresh_token'(you can get it by typing in `JSON.parse(localStorage.getItem("token")).refresh_token` in console). Then add the script to CRONTAB. 