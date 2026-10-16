# Hokkaido 的个人作品集

个人项目网站，收录系统实验、服务端、产业链分析、数学建模和数据可视化项目。桌面端左侧为名字与项目导航，右侧直接展示项目说明和图片；手机端按顺序阅读。

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

网页不加载第三方字体、统计脚本或远程图片。全部项目链接指向相应公开仓库，系统原理实验室另有在线体验入口。

排版参考 [《排版的艺术：一条很长很长的路》](https://re.karlbaey.top/articles/typography/)：系统字体、清楚的标题层级、适当留白和常显的内容链接。正文使用相对字号，窄屏通过换行与单栏布局保持可读性。

## 图片来源

- `systems-lab.webp`：`cs-systems-lab/docs/validation/cache-comparison.png` 的 Cache 实验区域，保留参数、缓存状态和 LRU/FIFO 对照，裁切后压缩为 WebP。
- `risk-overview.webp`：`supply-chain-risk-core/assets/readme-risk-core.png`，保留合成案例的来源说明。
- `multibeam.webp`：`cumcm-2023-multibeam/assets/readme-multibeam.png`，图中覆盖结构为概念示意。
- `weather.webp`：`nanjing-weather-visualization/assets/readme-weather-overview.png`，基于保存的南京 2023 年天气数据。
- `news-portal.webp`：`campus-news-portal/docs/validation/root-portal.png` 的页面截图，来自隔离验收环境。
- `http-server.svg`、`mrp-system.svg`：根据当前项目实现绘制的结构示意；不代表性能结果或实际业务数据。

项目资料及原图仍以各自仓库为准。网站配图不会修改原项目的历史图片、数据、论文或分析成品。

如需从相邻项目重新生成 WebP，安装 Pillow 后运行 `python tools/prepare-images.py --projects-root ..`。该命令只重写本仓库的五张 WebP；原图不存在、裁切区域越界或宽高比不符合约定时会明确报错。
