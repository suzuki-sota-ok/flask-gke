# ベースイメージを取得
FROM python:3.12.0

# 作業ディレクトリを指定
WORKDIR /app

# 環境変数を定義
# FLASK_RUN_HOST：これがないとlocalhostからのみしかアクセスできない
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# pipenvのインストール
# パッケージ管理ファイルをコピーして管理ファイルを参照してパッケージをインストール
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system

# ローカルのファイルをコンテナのWORKDIRにコピー
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]