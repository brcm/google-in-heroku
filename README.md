## 简易谷歌反代（Heroku版）

部署在 Heroku 中即可立即获得一个非常方便访问谷歌的方式。源代码基于 @Hsiny 的 ```google-in-heroku``` 修改而来。

### 如何部署

在 Windows 的 Git Bash 或者 Linux 的终端中运行如下命令即可。

```bash
git clone https://github.com/brcm/google-in-heroku
cd google-in-heroku
heroku create
git add -A
git commit -m "init"
git push heroku master
heroku open
```

### 更新内容

1. 修复 User-Agent 识别错误致访问到旧版谷歌
2. 修复中文搜索时，搜索结果页出现乱码问题
3. 强制设置默认搜索语言为简体中文
4. 强行关闭谷歌的安全搜索选项，可搜索额外内容
5. 强行移除多余 Javascript 脚本，例如 G+ 社区、广告等
6. 完善 HTTP 请求头，HTTP 响应头添加缓存字段

### 已知问题

1. 图片搜索无法点击查看，无法翻页加载
2. 谷歌的首页和搜索页面的 Google 标志加载慢