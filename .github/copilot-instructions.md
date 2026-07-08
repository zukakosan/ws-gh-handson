# Copilot Instructions — TODO App

FastAPI で作る学習用（ハンズオン）の TODO 管理 API。単一ファイル構成のミニマルなプロジェクト。詳細なセットアップ・API 一覧は [README.md](../README.md) を参照。

## 全体像

- [main.py](../main.py): API 本体。`FastAPI` アプリ、Pydantic モデル（`TodoCreate` / `Todo`）、エンドポイントをすべてここに定義。
- [test_main.py](../test_main.py): `fastapi.testclient.TestClient` を使ったテスト。
- データは DB を使わず、`main.py` 内のモジュールグローバルな `todos: list[Todo]` でインメモリ管理する。プロセス再起動で初期 3 件に戻る。

## 開発コマンド（Windows / PowerShell）

仮想環境は `.venv`。基本は仮想環境の Python を明示的に指定して実行する。

- テスト: `.\.venv\Scripts\python.exe -m pytest test_main.py -v`
- 起動: `.\.venv\Scripts\python.exe -m uvicorn main:app --reload`（→ http://127.0.0.1:8000/docs ）
- 依存追加時は [requirements.txt](../requirements.txt) を更新し `pip install -r requirements.txt`

## プロジェクト固有の重要な注意

- **意図的な未実装を勝手に埋めない**: `GET /todos/{todo_id}` はハンズオンで受講者が実装する題材。[main.py](../main.py) 末尾にコメントで雛形が残されている。**明示的に依頼されない限り、この実装やコメントを消さない・完成させない。**
- **コメントアウトされたテスト**: [test_main.py](../test_main.py) の `test_get_todo_by_id` / `test_get_todo_not_found` も同じ理由でコメントアウト済み。勝手に有効化しない。
- 有効なテストは `test_list_todos` と `test_create_todo` の 2 件のみ。この 2 件が PASS する状態を壊さない。

## コード規約

- リクエスト/レスポンスは Pydantic モデルで型付けする（`response_model=...` を明示）。
- 新規作成の ID は `max((t.id for t in todos), default=0) + 1` 方式を踏襲。
- 作成系は `status_code=status.HTTP_201_CREATED`、未検出は `HTTPException(status_code=404, ...)` を使う。
- 初期データ 3 件（`Buy groceries` / `Read a book` / `Write report`）の順序・内容はテストが依存するため変更しない。

## Coding Guidelines

- PEP 8 に従う
- Python 3.10+ のモダンな型ヒント構文を使う
  - `list[str]`, `dict[str, int]`（`from typing import List` は使わない）
  - `str | None`（`Optional[str]` は使わない）
- 公開関数には docstring を書く（PEP 257）

## Testing

- Kent Beck の TDD に従ってテスト駆動開発を行う
- テストは Arrange-Act-Assert パターンで書く
- テスト関数名は振る舞いを表す（例: `test_get_todo_by_id`）

## Git

- コミットメッセージは Conventional Commits（`feat:`, `fix:`, `test:`）
- ブランチ戦略は GitHub Flow に従う

## その他

- コメント、ドキュメント、GitHub Copilot のカスタマイズ設定は日本語
- Microsoft / Azure 関連の技術質問は `.vscode/mcp.json` で設定済みの Microsoft Learn MCP サーバーを一次情報源として利用する。
