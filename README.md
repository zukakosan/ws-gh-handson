# TODO App

FastAPI で作成したシンプルな TODO 管理 API です。ハンズオン用のベースプロジェクトとして利用します。

## 技術スタック

- FastAPI + uvicorn
- pytest + httpx（テスト）
- 依存管理: requirements.txt（pip）

## セットアップ

```bash
# 1. 仮想環境の作成
python3 -m venv .venv

# 2. 仮想環境の有効化
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 3. 依存パッケージのインストール
pip install -r requirements.txt
```

## 起動方法

```bash
uvicorn main:app --reload
```

起動後、以下の URL にアクセスできます。

- API ルート: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs

## API 一覧

| メソッド | パス | 説明 |
|---|---|---|
| GET | `/` | ウェルカムメッセージを返す |
| GET | `/todos` | TODO 一覧を返す |
| POST | `/todos` | 新しい TODO を作成する（201 を返す） |
| GET | `/todos/{todo_id}` | 個別の TODO を取得する（**未実装** / ハンズオンで実装） |

## テスト

```bash
pytest test_main.py -v
```

`test_list_todos` と `test_create_todo` が PASS することを確認してください。
個別取得（`/todos/{todo_id}`）に関するテストは、ハンズオンで実装するためコメントアウトされています。
