import requests
import time

FILE_IDS = ["85y6RASk","ZxYAYcLD","hzDGuEG7","xkByaAPU","efuhBi2K","M6YuANet","KBxJbUVw","tUWCzwm5","ppx5cbd4","5LjkT1Wd","c9kiHEB9","MeueGJbF","nxfTFaF9","sbN4ot7y","NaeCSU7W","WC6fQWpQ","BUzbSfAa","JWCfVv7Q","HsdD9ZXS","UyFfLxjv","aRvADwbJ","wSsjTYRj","b5zpN1ht","Wc8kdwq2","rZSQ2Rxm","xARWeFb4","NF2j7v9P","RuVQtasD"] # 替換成實際的 Pixeldrain 檔案 ID

def keep_file_alive(file_id):
    url = f"https://pixeldrain.com/api/file/{file_id}"
    print(f"開始請求檔案: {file_id}")
    
    try:
        # stream=True 允許分塊讀取，避免將大檔案塞滿記憶體，也無需寫入硬碟
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=8192):
                pass # 讀取資料後直接丟棄
        print(f"檔案 {file_id} 請求完成，已重置計時器。")
    except requests.exceptions.RequestException as e:
        print(f"處理 {file_id} 時發生錯誤: {e}")

if __name__ == "__main__":
    for fid in FILE_IDS:
        keep_file_alive(fid)
        time.sleep(5) # 稍微暫停，避免短時間內頻繁請求
