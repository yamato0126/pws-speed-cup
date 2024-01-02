## Docker環境

### 使用要件
`src/anonymize.py`の`run_anonymize()`を編集する．
すなわち`run_anonymize`関数を実行することで，データの読み込み，匿名化，書き込みが全て行われるように記述する．`main.py`は編集しない．

### 計測方法
`docker-compose run timekeeper`を実行することで時間が計測される．
計測にはPythonの標準ライブラリ関数[`time.perf_counter()`](https://docs.python.org/ja/3.11/library/time.html?highlight=time%20perf_counter)を用いる．