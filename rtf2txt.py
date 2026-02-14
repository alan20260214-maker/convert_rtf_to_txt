import argparse
import os
from pathlib import Path
from striprtf.striprtf import rtf_to_text

def convert_rtf(input_path):
    """處理單個 RTF 檔案轉換並存成 TXT"""
    input_path = Path(input_path)
    
    # 檢查是否為 RTF 檔案
    if input_path.suffix.lower() != '.rtf':
        print(f"跳過非 RTF 檔案: {input_path}")
        return

    try:
        # 讀取 RTF (通常 RTF 內部編碼是 ASCII/Windows-1252，striprtf 會處理轉碼)
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 轉換為純文字
        text = rtf_to_text(content)
        
        # 產生輸出檔名 (將 .rtf 改為 .txt)
        output_path = input_path.with_suffix('.txt')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
            
        print(f"成功: {input_path.name} -> {output_path.name}")
        
    except Exception as e:
        print(f"錯誤: 處理 {input_path.name} 時發生問題: {e}")

def main():
    parser = argparse.ArgumentParser(description="使用 striprtf 批次轉換 RTF 檔案為文字檔")
    
    # 定義位置參數：可以是檔案或目錄
    parser.add_argument("path", help="輸入 RTF 檔案的路徑或資料夾路徑")
    
    # 可選參數：是否包含子目錄
    parser.add_argument("-r", "--recursive", action="store_true", help="是否遞迴搜尋子資料夾")

    args = parser.parse_args()
    target_path = Path(args.path)

    if not target_path.exists():
        print(f"錯誤: 路徑 '{args.path}' 不存在")
        return

    if target_path.is_file():
        # 如果是單一檔案
        convert_rtf(target_path)
    elif target_path.is_dir():
        # 如果是目錄，搜尋所有 .rtf 檔案
        pattern = "**/*.rtf" if args.recursive else "*.rtf"
        rtf_files = list(target_path.glob(pattern))
        
        if not rtf_files:
            print("在目錄中找不到任何 .rtf 檔案。")
            return
            
        print(f"找到 {len(rtf_files)} 個檔案，開始轉換...")
        for rtf_file in rtf_files:
            convert_rtf(rtf_file)
        print("轉換完成！")

if __name__ == "__main__":
    main()