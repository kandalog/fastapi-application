# Fast API を用いたアプリケーション開発

## 目的

FastAPI を学習する必要が出てきたので Udemy を教材を購入して学習

## アプリの内容

予約管理ツールを作成

## 学習教材にテコ入れした点

_自分で考えた点_

- Docker 化
- ディレクトリ構成を変更
- SQLite ではなく Mysql を使用
- sqlAlchemy で scoped_session を利用
- ユーザが存在しない時に発生するバグを修正
- 会議室が存在しない時に発生するバグを修正
- 予約済みのデータが存在しない時に発生するバグを修正

## 導入方法

_Docker app を立ち上げ、ログインしていることを確認してください_

3: `docker compose build --no-cache`
4: `docker compose up -d`
5: `タブを２つ開く`
6: `./script/fastapi`
7: `./script/streamlit`
