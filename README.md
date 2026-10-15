# Q4工作规划

整装业务思考、基础数据建设与AI应用建设。包含4张思路示意图，可展开、收起事实依据，并支持打印。

## 查看

- 离线：下载项目，解压后用浏览器打开 `index.html`。
- 在线：仓库启用 GitHub Pages 后，访问其提供的 HTTPS 地址。
- 页面所需样式、脚本和图示均已内嵌，无需安装依赖或加载外部字体、图片。

## 文件

- `index.html`：完整网页，可独立使用。
- `build.py`：页面内容与样式生成脚本。
- `diagrams.py`：4张矢量示意图的生成代码。
- `.nojekyll`：按静态文件发布。

## 修改

可直接编辑 `index.html`；如使用源文件维护，修改 `build.py` 或 `diagrams.py` 后执行：

```sh
python3 build.py
```

只使用 Python 标准库。输出到项目根目录的 `index.html`。

## 发布

在仓库的 **Settings → Pages** 中，选择从分支发布，指定实际主分支和根目录 `/ (root)`，保存后等待部署完成。正式网址以 GitHub Pages 页面返回的链接为准。
