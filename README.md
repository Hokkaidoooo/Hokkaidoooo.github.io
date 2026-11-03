# Hokkaido 的个人作品集

个人项目网站，收录系统实验、服务端、产业链分析、日常工具、数学建模和数据可视化项目。使用暖白与墨绿配色，按工程与系统、日常工具、建模与探索组织内容。桌面端展示图文卡片，手机端按阅读顺序展开。

网站地址：<https://hokkaidoooo.github.io/>。

学习笔记与日常文章在 [Hokkaido · 手记](https://hokkaidoooo.github.io/blog/)，也可从站内导航进入。

## 本地查看

在仓库根目录运行 Python 静态服务器，然后访问 <http://127.0.0.1:4186/>：

```powershell
python -m http.server 4186 --bind 127.0.0.1
```

也可以直接打开 `index.html`。页面由 HTML 与 CSS 组成，不需要安装前端依赖或运行构建命令。

## 更新内容

- 项目名称、介绍和链接统一维护在 `index.html`。
- 布局、配色与响应式规则在 `assets/site.css`。
- 404 页面在 `404.html`；图标和项目图片在 `assets`。
- GitHub Pages 使用 `main` 分支的仓库根目录发布。`.nojekyll` 使静态文件直接发布。

网页不加载 JavaScript、第三方字体、统计脚本或远程图片，不使用 Cookie、本地存储、表单或指纹采集。全部项目链接指向相应公开仓库，系统原理实验室另有在线体验入口。GitHub Pages 托管服务与外链目标适用各自的服务政策。

正文使用系统字体、相对字号和完整换行；内容链接常显下划线，键盘焦点可见。页面提供跳到正文入口，支持减少动态效果的系统偏好；不依赖 JavaScript 即可浏览、跳转与访问所有项目。首屏几何插画为装饰性内联 SVG，项目配图分别标明结构示意、合成案例与实际界面。

## 公开内容与隐私

网站使用公开昵称，不提供真实姓名、私人联系方式、学校、住址或简历附件。项目说明仅取自对应公开仓库，TraceDesk 展示演示业务能力，知乎导出仅面向已有阅读权限的内容。

发布前检查网页与说明、全部可达 Git 历史、提交身份、图片可见文字及 EXIF/XMP。不得把本机状态、验收日志、原始数据、账号信息、阅读记录或密钥加入公开仓库。该检查只针对本网站，不能代替对各个外链项目的独立审查。

## 图片来源

- `systems-lab.webp`：`cs-systems-lab/docs/validation/cache-comparison.png` 的 Cache 实验区域，保留参数、缓存状态和 LRU/FIFO 对照，裁切后压缩为 WebP。
- `risk-overview.webp`：`supply-chain-risk-core/assets/readme-risk-core.png`，保留合成案例的来源说明。
- `multibeam.webp`：`cumcm-2023-multibeam/assets/readme-multibeam.png`，图中覆盖结构为概念示意。
- `weather.webp`：`nanjing-weather-visualization/assets/readme-weather-overview.png`，基于保存的南京 2023 年天气数据。
- `news-portal.svg`：根据门户功能绘制的通用示意，不使用校名、人物照片或个人资料，不代表实际运行截图。
- `http-server.svg`、`mrp-system.svg`：根据当前项目实现绘制的结构示意；不代表性能结果或实际业务数据。

项目资料及原图仍以各自仓库为准。网站配图不会修改原项目的历史图片、数据、论文或分析成品。

如需从相邻项目重新生成 WebP，安装 Pillow 后运行 `python tools/prepare-images.py --projects-root ..`。该命令只重写本仓库的四张 WebP，不读取或生成门户截图；原图不存在、裁切区域越界或宽高比不符合约定时会明确报错。
