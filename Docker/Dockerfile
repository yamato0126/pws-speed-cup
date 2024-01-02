FROM python:3
USER root

# RUN apt-get update
# RUN apt-get install -y vim less
# ライブラリインストール
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas

# srcディレクトリの作成
RUN mkdir -p /src
# ワーキングディレクトリの設定
WORKDIR /src

CMD ["python", "main.py"]