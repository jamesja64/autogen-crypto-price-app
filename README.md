# autogen-crypto-price-app

## 專案簡介

`autogen-crypto-price-app` 是一個輕量級的 Python 應用程式，用於從 CoinGecko API 獲取比特幣 (Bitcoin)、以太坊 (Ethereum) 和狗狗幣 (Dogecoin) 的即時美元價格，並將其以清晰的格式顯示在控制台上。

這個專案的特別之處在於，它的核心程式碼是由 **Microsoft AutoGen** 框架中的多個 AI 代理人（開發工程師、代碼審閱員、整合工程師）協同合作自動生成的，展示了 AI 在軟體開發流程中的潛力。

## 功能特色

*   **即時價格獲取**：從 CoinGecko API 獲取多種加密貨幣的最新價格。
*   **簡潔輸出**：將價格以易於閱讀的格式打印到控制台。
*   **錯誤處理**：包含對網路請求失敗和 API 響應格式錯誤的處理。
*   **API 快取**：利用 `cachetools` 庫對 API 響應進行快取，減少重複請求並提高效率。
*   **模組化設計**：清晰的程式碼結構，將 API 互動邏輯與主應用程式邏輯分離。

## 專案架構

本專案的檔案結構簡潔明瞭，每個檔案各司其職：

```
autogen-crypto-price-app/
├── .gitignore
├── api_client.py
├── main.py
└── requirements.txt
```

*   **`.gitignore`**:
    *   **作用**：這個檔案告訴 Git 哪些檔案或資料夾應該被忽略，不應該被追蹤或提交到版本控制中。它通常包含編譯產生的檔案、快取檔案、環境變數檔案以及其他不應共享的敏感資訊。
    *   **本專案中**：它確保像 `__pycache__`、虛擬環境資料夾 (`venv/`) 等不必要的檔案不會被提交到 GitHub。

*   **`api_client.py`**:
    *   **作用**：這個模組專門負責處理與 CoinGecko API 的所有互動。它包含了發送 HTTP 請求、解析 JSON 響應以及處理 API 相關錯誤的邏輯。
    *   **核心功能**：
        *   定義了 CoinGecko API 的 URL。
        *   `get_crypto_prices()` 函數：這是核心函數，負責發起 API 請求。
        *   **快取機制**：使用了 `cachetools` 庫的 `@cached` 裝飾器，將 API 響應快取 60 秒，避免在短時間內重複請求相同的數據，從而提高效率並減少 API 調用次數。
        *   **錯誤處理**：捕獲 `requests.exceptions.RequestException`（網路連接問題）和 `KeyError`（API 響應格式不符預期）等異常，並拋出更具描述性的錯誤。

*   **`main.py`**:
    *   **作用**：這是應用程式的入口點。它負責協調 `api_client.py` 中的功能，並將結果呈現給用戶。
    *   **核心功能**：
        *   從 `api_client` 模組導入 `get_crypto_prices` 函數。
        *   `main()` 函數：調用 `get_crypto_prices()` 獲取數據，然後格式化並打印到控制台。
        *   **通用錯誤處理**：包含一個 `try...except` 塊，用於捕獲任何未預期的錯誤，並向用戶顯示友好的錯誤訊息。
        *   `if __name__ == "__main__":` 塊：確保 `main()` 函數只在腳本直接運行時執行，而不是在被其他模組導入時執行，這是 Python 的最佳實踐。

*   **`requirements.txt`**:
    *   **作用**：這個檔案列出了專案運行所需的所有 Python 依賴套件及其版本。這使得其他開發者或部署環境可以輕鬆地安裝所有必要的庫，確保專案的可重現性。
    *   **本專案中**：列出了 `requests`（用於 HTTP 請求）和 `cachetools`（用於 API 響應快取）。

## 如何運行

要運行這個專案，請按照以下步驟操作：

1.  **克隆儲存庫**：
    ```bash
    git clone https://github.com/jamesja64/autogen-crypto-price-app.git
    cd autogen-crypto-price-app
    ```

2.  **建立並啟用虛擬環境 (推薦)**：
    ```bash
    python -m venv venv
    # 在 macOS/Linux 上
    source venv/bin/activate
    # 在 Windows 上
    .\venv\Scripts\activate
    ```

3.  **安裝依賴套件**：
    ```bash
    pip install -r requirements.txt
    ```

4.  **運行應用程式**：
    ```bash
    python main.py
    ```

    您將在控制台上看到類似以下的輸出：
    ```
    Cryptocurrency Prices (USD):
    - Bitcoin: $XXXXX.XX
    - Ethereum: $XXXX.XX
    - Dogecoin: $X.XXXX
    ```

## License

本專案採用 MIT License。這意味著您可以自由地使用、修改和分發本軟體，但必須包含原始的版權聲明和許可條款。

有關更多詳細資訊，請參閱 `LICENSE` 檔案（如果存在，我將在下一步為您創建）。

## 致謝

*   **Microsoft AutoGen**：本專案的核心程式碼由 AutoGen 框架中的 AI 代理人協同生成。
*   **CoinGecko API**：提供加密貨幣價格數據。

---
