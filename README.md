# PWS SPEED CUP

## ファイルの配置
```
├── Admin
│   ├── attack_1.py
│   ├── common.py
│   ├── eval_util.py
│   └── generator.py
└── Docker
    ├── src
    ├── docker-compose.yml
    └── Dockerfile
```

## 主催者が行う評価の手順
1. generator.pyを実行して元データo.csvを生成する．
2. 各参加者が提出したソースコードを実行して加工データa.csvを得る．同時に実行時間を計測し，time.txtに出力する．
3. eval_util.pyを実行してa.csvの有用性を評価し，util.txtに出力する．
4. 加工データa.csvをソートして整列加工データb.csvを得る．
5. o.csvの公開部とb.csvからo.csvの秘密部を推定する攻撃によって安全性を評価し，safe.txtに出力する．なお，攻撃プログラムはattack_1.pyなど数種類存在する．

## パラメータについて
- データの行数 n = 10\**5 or 10\**6
- 公開データの列数 m_p = 8
- 秘密データの列数 m_r = 10
- データの各要素 (0以上c未満の整数) c = 10

## 議論
- 最終スコアの算出方法