# python-tutorial
この資料は Jupyter Notebook で作成されています.

## 環境構築
- Python 3.5 の環境を準備してください. 仮想環境を作成することを推奨します.
- `requirements.txt` のパッケージをインストールしてください
  - pip を用いる場合: `pip install -U -r requirements.txt`
  - pip-tools を用いる場合: `pip-sync`
- Jupyter Notebook を起動してください: `jupyter notebook`

## ファイル構成
```
- notebooks/   --- Jupyter Notebook
- source/      --- Jupyter Notebook から生成した Python ソースコード
- build.sh     --- Jupyter Notebook から Python ソースコードを生成するスクリプト
```
