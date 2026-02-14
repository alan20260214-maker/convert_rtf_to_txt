# 📄 RTF 轉 TXT 轉換工具

使用 `striprtf` 將 Rich Text Format (RTF) 檔案批次轉換為純文字檔案。

## ✨ 功能特點

- ✅ 支援**單一檔案**或**整個資料夾**批次轉換
- ✅ 可選擇**是否包含子資料夾**
- ✅ 自動處理編碼問題
- ✅ 保留原始檔案名稱（僅副檔名改為 `.txt`）
- ✅ 顯示轉換進度與結果

## 📋 系統需求

- **Python 版本**：3.6 或更高
- **必要套件**：`striprtf`

## 🔧 安裝步驟

### 1. 安裝必要套件

pip install striprtf

### 2. 下載程式碼

將提供的程式碼儲存為 `rtf_to_txt.py`

## 🚀 使用方法

### 基本語法

python rtf_to_txt.py <輸入路徑> [選項]

### 參數說明

| 參數 | 說明 |
|------|------|
| `path` | 輸入檔案或資料夾路徑（必要） |
| `-r, --recursive` | 是否遞迴處理子資料夾（選用） |

### 常用範例

#### 1. 轉換單一 RTF 檔案

python rtf_to_txt.py "C:\文件\報告.rtf"

#### 2. 轉換資料夾內所有 RTF 檔案（不含子資料夾）

python rtf_to_txt.py "C:\文件"

#### 3. 轉換資料夾內所有 RTF 檔案（包含子資料夾）

python rtf_to_txt.py "C:\文件" -r

#### 4. 轉換當前目錄的 RTF 檔案

python rtf_to_txt.py . -r

## 📝 輸出說明

- 轉換後的 `.txt` 檔案會**與原始 RTF 檔案在同一目錄**
- 輸出檔案名稱與原始檔案相同（僅副檔名改為 `.txt`）
- 例如：`報告.rtf` → `報告.txt`

## 📊 程式執行範例

### 範例 1：轉換單一檔案

$ python rtf_to_txt.py "C:\我的文件\報告.rtf"
成功: 報告.rtf -> 報告.txt


### 範例 2：轉換整個資料夾

$ python rtf_to_txt.py "C:\我的文件" -r
找到 5 個檔案，開始轉換...
成功: 報告1.rtf -> 報告1.txt
成功: 報告2.rtf -> 報告2.txt
成功: 文件3.rtf -> 文件3.txt
成功: 附錄A.rtf -> 附錄A.txt
成功: 附錄B.rtf -> 附錄B.txt
轉換完成！

## ❓ 常見問題

### Q1: 為什麼要使用 `errors='ignore'`？
**A:** RTF 檔案內部可能包含無法解碼的字元，`errors='ignore'` 可以跳過這些問題，確保轉換順利完成。

### Q2: 轉換後會保留格式嗎？
**A:** 不會，這是純文字轉換，只會保留文字內容，所有格式（粗體、斜體、顏色等）都會被移除。

### Q3: 可以轉換密碼保護的 RTF 檔案嗎？
**A:** 不行，需要先移除密碼保護才能轉換。

### Q4: 輸出檔案會覆蓋現有檔案嗎？
**A:** 是的，如果同名的 `.txt` 檔案已經存在，會被覆蓋。

## 📦 相依套件

- `striprtf`：RTF 解析核心套件
- `argparse`：命令列參數解析（Python 標準庫）
- `pathlib`：路徑處理（Python 標準庫）

- **本工具 (rtf_to_txt.py)**：採用 MIT 授權
- **striprtf**：[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)，版權歸原作者所有。
