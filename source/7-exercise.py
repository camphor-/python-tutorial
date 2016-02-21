
# coding: utf-8

# # 練習: 英単語ゲーム
# ここまでに学んだ知識を生かして英単語ゲームを作ってみましょう.
# 単語の日本語訳を表示して, ユーザーが英単語を解答するというシンプルなゲームです.
# 
# 動作例1:
# 0. プログラムが "Q: 「りんご」" と表示
# 0. ユーザーが "apple" と入力
# 0. プログラムが "正解" と表示
# 0. 次の問題を出題
# 
# 動作例2:
# 0. プログラムが "Q: 「りんご」" と表示
# 0. ユーザーが "orange" と入力
# 0. プログラムが "不正解" と表示
# 0. 次の問題を出題
# 
# 
# 動作例3:
# ```
# Q: 「りんご」
# A: apple
# 正解
# Q: 「犬」
# A: cat
# 不正解
# ```
# 
# 
# ## 仕様
# - 問題と答えは辞書型で事前にプログラム中に準備されているものとします. 例:
# ```python
# problems = {
#     "apple": "りんご",
#     "dog": "犬"
# }
# ```
# 
# - プログラムをスタートすると, すべての問題を順に出題します. 出題順は自由です.
# - それぞれの問題について次の処理を行います
#   - 問題の表示 (例: "Q: 「りんご」")
#   - 解答の入力
#   - 解答が正しいか判定
#     - 正解なら "正解" と表示
#     - 不正解なら "不正解" と表示

# In[2]:

# 問題と答えを辞書型で準備しましょう
# 例:
# problems = {
#     "apple": "りんご",
#     "dog": "犬"
# }

# problem.items() を使って, 問題と答えについて反復処理をしましょう

# 問題を出題しましょう

# 解答の入力を受け取りましょう

# 解答が正解か判定して, メッセージを表示しましょう


# ## 拡張
# 上の仕様のプログラムができたら, さらにプログラムを拡張してみましょう!
# 
# 拡張例:
# - ゲームの最初と最後にメッセージを表示する
# - ゲームの最初に問題数を表示する
# - ゲームの最後に正答率を表示する
# - プログラムを実行するたびに出題順をランダムにする
# - すべての問題が終わった後, もう一度遊べるようにする (リプレイ)
# - 問題をプログラム中で追加できるようにする

# ## 改善
# プログラミング言語の様々な機能を使ってプログラムを改善してみましょう!
# 
# 改善例:
# - 関数を定義して処理をわかりやすくする
# - コメントを書いてプログラムをわかりやすくする
# - わかりやすい変数名に変更する
