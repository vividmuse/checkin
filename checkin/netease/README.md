# 网易云音乐升级全家桶

<p align="center">
    <a href="https://github.com/ZainCheung"><img alt="Author" src="https://img.shields.io/badge/author-ZainCheung-blueviolet"/></a>
    <img alt="PHP" src="https://img.shields.io/badge/code-Python-success"/>
    <img src="https://github-visitor-badge.glitch.me/badge?page_id=ZainCheung.netease-cloud"/>
</p>
通过调用官方接口，每天自动刷完300首歌，借此可以达到快速升级的目的。

一个账号平均耗时为1分钟左右。放在服务器运行即可不需要人工干预，支持无服务器的云函数部署，每天自动听歌做任务，向你的微信发送任务通知。

------



### 使用文档: https://zaincheung.gitee.io/netease-cloud


### 二、设置账号密码
添加名为 **USER**、**PWD** 的变量，值分别为 **账号（仅支持手机号）**、**密码 **

> Settings-->Secrets-->New secret

支持多账号，账号之间与密码之间用 ***#*** 分隔，账号与密码的个数要对应

注:原config 多账号设置\账号\密码 设置失效(其他依然读取config设置) 需要以此设置为准

示例：**USER:13800000000#13800000001**，**PWD:cxkjntm#jntmcxk**
![image-20200727142753175](https://i.loli.net/2020/07/27/xjri3p4qdchaf2G.png)

目前已实现功能：


- [x]  每天自动升级
- [x] 任务进度推送到微信
- [x] 自定义网易云日推风格

本项目实则由三个项目组成，分别是：

- 给账号升级的Python项目：[netease-cloud](https://github.com/ZainCheung/netease-cloud)

- 使用PHP搭建的API接口：[netease-cloud-api](https://github.com/ZainCheung/netease-cloud-api)

- 使用Python开发的修改日推（每日推荐歌曲）Windows软件：[netease-cloud-fast](https://github.com/ZainCheung/netease-cloud-fastplay)

### 接口征集活动
https://github.com/ZainCheung/netease-cloud-api/issues/31
