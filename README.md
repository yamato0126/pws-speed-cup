# 処理時間を考慮に入れた匿名化コンテストの提案（情報処理学会 第86回全国大会）
Title: Proposal for an anonymization contest considering processing time

## 主催者が行う評価の手順
1. `generator.py`を実行して元データ`o.csv`を生成する．
2. 各参加者が提出したプログラムを実行して加工データ`a.csv`を得る．同時に実行時間を計測し，`time.txt`に出力する．
3. `eval_util.py`を実行して`a.csv`の有用性を評価し，`util.txt`に出力する．
4. 加工データ`a.csv`をソートして整列加工データ`b.csv`を得る．(`sort a.csv > b.csv`)
5. `o.csv`の公開部と`b.csv`から`o.csv`の秘密部を推定する攻撃プログラムを実行して安全性を評価し，`safe.txt`に出力する．

## パラメータ
- パーソナルデータの行数 n = 10\**6
- 公開部の列数 m_p = 8
- 秘密部の列数 m_r = 10
- データの各要素 (0以上c未満の整数) c = 10

## 関連リンク
- [PWSCUP 2023](https://www.iwsec.org/pws/2023/cup23.html)
- [PWSCUP 2023 チームF.SE リポジトリ](https://github.com/fseclab-osaka/pwscup2023-public)