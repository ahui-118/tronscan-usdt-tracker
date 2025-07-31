
import requests
import time

TRONSCAN_API = "https://apilist.tronscan.org/api"

def get_trc20_transfers(address, limit=20, start=0):
    url = "{}/transaction/trc20".format(TRONSCAN_API)
    params = {
        "limit": limit,
        "start": start,
        "sort": "-timestamp",
        "count": True,
        "relatedAddress": address
    }
    response = requests.get(url, params=params)
    return response.json().get("data", [])

def find_latest_incoming(address, token_name="USDT", min_amount=1000):
    transfers = get_trc20_transfers(address)
    for tx in transfers:
        if tx.get("to_address") == address and tx.get("tokenName") == token_name:
            amount = float(tx.get("quant", 0)) / (10 ** int(tx.get("tokenDecimal", 6)))
            if amount >= min_amount:
                return {
                    "from": tx["from_address"],
                    "amount": amount,
                    "txid": tx["transaction_id"],
                    "timestamp": tx["block_timestamp"]
                }
    return None

def trace_usdt_path(start_address, layers=10):
    address = start_address
    path = []
    for i in range(layers):
        tx_info = find_latest_incoming(address)
        if tx_info is None:
            break
        path.append({
            "layer": i + 1,
            "from": tx_info["from"],
            "to": address,
            "amount": tx_info["amount"],
            "txid": tx_info["txid"],
            "timestamp": tx_info["timestamp"]
        })
        address = tx_info["from"]
        time.sleep(1)  # Avoid rate limit
    return path

def main():
    start_address = input("请输入目标地址 (USDT 收款地址): ").strip()
    layers = int(input("请输入要追踪的层数 (最多建议10层): ").strip() or "10")
    print("开始追踪 {} 层 USDT 来源路径...".format(layers))
    result = trace_usdt_path(start_address, layers)
    print("\n追踪结果：")
    for entry in result:
        print("第 {} 层：{} → {} | 金额: {} USDT | 交易哈希: {}".format(
            entry['layer'], entry['from'], entry['to'], entry['amount'], entry['txid']
        ))

if __name__ == "__main__":
    main()
