# FRC 6433 HZ4Z · 27赛季招新网页

## 文件结构
- `index.html`：完整网页
- `images/`：6张网页图片
- `make_web_qr.py`：公开网页部署后，用公开网址生成海报二维码

## 本地预览
直接双击 `index.html` 即可用浏览器打开。若浏览器限制本地图片，可使用 VS Code Live Server 等本地静态服务器。

## 招新问卷
网页按钮已直接指向：
https://v.wjx.cn/vm/tBGSn9m.aspx#

## 发布成公开网址（推荐 GitHub Pages）
1. 在 GitHub 创建一个新仓库，例如 `frc6433-recruitment`。
2. 把整个文件夹里的 `index.html` 和 `images` 文件夹上传到仓库根目录。
3. 打开仓库 `Settings` → `Pages`。
4. 在 `Build and deployment` 中选择 `Deploy from a branch`。
5. Branch 选择 `main`，文件夹选择 `/ (root)`，保存。
6. 等待 GitHub Pages 部署完成，会得到一个公开网址，例如 `https://你的用户名.github.io/frc6433-recruitment/`。
7. 用这个公开网址运行 `make_web_qr.py`，生成可以贴在海报上的网页二维码。

## 重要
二维码不能在网页公开网址确定前制作最终版。因为二维码需要编码“最终公开网址”。本项目没有在网页内部放二维码，符合“网页外单独二维码”的要求。
