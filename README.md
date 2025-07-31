# tron-usdt-trace

一个用于追踪 TRON 网络中 USDT（TRC20）转账来源路径的 Python 工具，基于 TronScan Open API 实现，无需 API Key，可直接使用。

## 🔍 功能特点

- 自动追踪 USDT 收款地址的来源路径，最多支持 10 层反向追踪
- 显示每一层的发送地址、接收地址、转账金额、交易哈希、时间戳
- 使用公开的 TronScan Open API，无需授权
- 轻量级命令行脚本，易于运行和修改

## 📦 依赖要求

- Python 3.7+
- 第三方库：`requests`

安装依赖：

```bash
pip install -r requirements.txt
```

## 🚀 使用方法

运行主脚本：

```bash
python trace_usdt_tronscan.py
```

然后输入：
1. 你想要追踪的 TRON 地址（例如：`TMXdkUSiKY3q...`）
2. 想要追踪的层数（建议 3~10 层）

## 📤 输出示例

```
开始追踪 10 层 USDT 来源路径...

第 1 层：TNJ4EAr3yF71... → TMXdkUSiKY3q... | 金额: 30000.0 USDT | 交易哈希: edbf39...
第 2 层：TVakEy3... → TNJ4EAr3yF71... | 金额: 30000.0 USDT | 交易哈希: 29ba91...
...
第 10 层：TDcc23... → Txxxxxxx... | 金额: 30000.0 USDT | 交易哈希: a8ee12...
```

## 📁 项目结构

```
tron-usdt-trace/
├── trace_usdt_tronscan.py    # 主脚本
├── README.md                 # 使用说明
├── requirements.txt          # Python 3.7 兼容依赖
```

## 📄 授权协议

MIT License  
本工具仅供个人学习、溯源分析与合规用途使用，请勿用于非法活动。
