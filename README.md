# 🧭 TRON USDT 来源追踪工具

这是一个基于浏览器的 USDT 资金流向追踪工具，适用于 TRON 网络。用户只需输入任意一个 TRON 地址，即可查看该地址最近接收的 USDT 的来源路径信息。

部署地址（GitHub Pages）：
👉 [点击访问工具页面](https://ahui-118.github.io/tronscan-usdt-tracker/)

---

## 🚀 功能说明

- 📥 支持用户输入 TRON 地址（以 `T` 开头的34位地址）
- 🔍 追踪该地址最近接收到的 USDT 的来源地址
- 🪜 显示路径跳数、转账金额等基础信息
- 💻 无需安装，可直接在浏览器中使用
- 📦 可本地运行，也可部署在 GitHub Pages

---

## 📂 项目结构

```bash
tronscan-usdt-tracker/
├── index.html       # 主页面（HTML + JS + CSS 内嵌）
├── README.md        # 项目说明文件
```

---

## 🔧 使用方法

### ✅ 在线使用

无需下载，点击访问：

👉 [https://ahui-118.github.io/tronscan-usdt-tracker/](https://ahui-118.github.io/tronscan-usdt-tracker/)

### 🖥 本地使用

1. 克隆或下载此仓库：

```bash
git clone https://github.com/ahui-118/tronscan-usdt-tracker.git
```

2. 使用浏览器打开本地的 `index.html` 即可运行工具。

---

## 🛠 后续计划（可选）

- ✅ 集成 TronGrid API 实时追踪交易路径
- ✅ 支持多级路径显示（转账链路跳数）
- ✅ 加入 USDT 合约验证与筛选（防钓鱼地址）
- ✅ 支持交易记录可视化图谱展示

---

## 📜 注意事项

- 本工具暂为测试版本，默认使用示例数据。
- 若需接入真实区块链数据，请在 JS 中接入 TronGrid API 或调用 TronScan Open API。
- 本项目仅供学习和技术研究使用。

---

## 🙋‍♂️ 联系与反馈

如有建议或问题，欢迎通过 Issues 提交反馈。
