## Introduction
该项目是一个**歌曲偏好分析系统**，它可以抓取特定用户的网易云音乐数据，进行相关处理，然后在网页上将数据可视化。它还包括根据用户的喜好向他们推荐艺术家和歌单，以及分析艺术家的听众用户情况。项目中存在大量私货

## Technology Included
前端框架：bootstrap 
想做web开发，后端代码得自己实现，但是前端界面最方便的还是直接套用框架、模板之类的
当然啦，我自己现在水平还是做不出这么精美的界面，所以套用了一下模板，把他爆改了一下
https://www.bootstrapdash.com/product/celestial-admin-bootstrap-admin-template-free
演示demo：https://demo.bootstrapdash.com/celestial-free/template/index.html
地图api demo：https://lbsyun.baidu.com/jsdemo.htm#a1_2
结合echarts https://echarts.apache.org/examples/zh/editor.html?c=effectScatter-bmap
设计语言：Python + CSV + HTML + CSS + JS

数据爬虫：NeteaseCloudMusicApi + Requset + etree + json 

数据清洗：re + replace + join + spilt

可视化：Flask + Echarts + WordCloud + Html

文本分析：jieba2

数据存储：CSV


## Features

- 支持使用网易云用户id登录
- 支持查询开放数据的用户信息
- 支持对登录用户喜爱的歌手可视化展示
- 支持展示用户最喜爱的top100歌曲
- 支持展示用户听歌偏好标签统计
- 支持展示用户评论区词云图，以及相关热评信息
- 支持通过作者id搜索任意作者信息
- 支持展示作者粉丝群体性别，居住地统计
- 支持展示作者创作偏好
- 支持展示作者热门歌曲以及热门评论
- 支持为登录用户推荐歌曲以及歌单

## TODO
- [ ] 歌曲搜索页面
- [ ] 基于歌曲的用户群体分析
## 部署

下面的信息可能有一些繁琐枯燥甚至还有错误, 希望还可见谅。
+ 部署内容分为两个板块，请认真阅读。
  
### 网易云api部署
项目中使用了网易云api作为爬虫的一部分，保证了实时爬虫的稳定性同时减少了用户配置爬虫的阶段。
> 详细配置流程请[看这里](https://github.com/Binaryify/NeteaseCloudMusicApi)

部署之前请确保你拥有/完成以下能力/事情:
- Node.js / JavaScript 基础

<details>

  <summary>简略部署流程 (点击展开)</summary>

  #### 安装
```
$ git clone git@github.com:Binaryify/NeteaseCloudMusicApi.git
$ cd NeteaseCloudMusicApi
$ npm install
```

  #### 运行
```shell
$ node app.js
```

服务器启动默认端口为 3000, 若不想使用 3000 端口 , 可使用以下命令 : Mac/Linux

```shell
$ PORT=4000 node app.js
```

windows 下使用 git-bash 或者 cmder 等终端执行以下命令 :

```shell
$ set PORT=4000 && node app.js
```

服务器启动默认 host 为 localhost,如果需要更改, 可使用以下命令 : Mac/Linux

```shell
$ HOST=127.0.0.1 node app.js
```

windows 下使用 git-bash 或者 cmder 等终端执行以下命令 :

```shell
$ set HOST=127.0.0.1 && node app.js
```
</details>

### Music部署

项目使用的是python 3.10，不知道低版本会不会有什么问题。可以通过以下语句创建py 3.10的虚拟环境

```shell
conda create -n music_work python=3.10
```

都是一些很常见的库，可以通过pip来安装。不过这边建议使用虚拟环境捏~
> pip list
```shell
pip install pandas flask bs4 html5lib Jinja2 lxml requests jieba 
pip install wordcloud imageio matplotlib numpy
```
如果还有没有覆盖到的，出现报错时pip一下就可以了

## 启动流程

1. 首先参照部署一中的内容，我们cd到NeteaseCloudMusicApi的目录下，运行以下内容：
```shell
node app.js
```
出现以下内容则说明运行成功：
```powershell
server running @ http://localhost:3000
```

2. 打开新的终端，cd到项目文件夹下，开启虚拟环境，并运行以下内容：
```shell
python app.py
```
出现以下内容则说明运行成功：
```shell
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
```
在浏览器中访问[这里](http://localhost:5000)(运行成功了再点这里哦！！)

