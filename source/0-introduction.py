
# coding: utf-8

# # はじめに
# このチュートリアルはプログラミング初心者の方が, Python を使ってプログラミングの基礎を学ぶためのものです.
# 
# 出来る限り正確な表現を心がけていますが, 一部の表現は技術的な正確さを犠牲にして, 初心者にわかりやすいように記述している部分があります.

# ## 対話モードで遊ぶ
# `python` というコマンドを入力すると, Python インタプリタが**対話モード**で起動します.
# 対話モードを使うと, プログラムを入力して, すぐに実行することが出来ます.
# 
# 例:
# ```
# $ python
# Python 3.5.1 (default, Dec  7 2015, 21:59:10)
# [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# >>> exit()
# $
# ```

# ### 電卓
# Python インタプリタを簡単な電卓として使ってみましょう.
# 計算したい式 (プログラム) を入力して, `Enter` キーを押すと, プログラムを実行した結果が表示されます.
# 間違ったプログラムを実行すると, **エラー**の内容が表示されます.
# 
# Python では `+` や `-`, `*`, `/` などの**演算子**が利用出来ます.
# 
# 例 (`#` の後ろは入力しなくて良いです):
# ```
# >>> 1 + 1  # 加算
# 2
# >>> 123 - 32  # 減算
# 91
# >>> 6 * 3  # 乗算
# 18
# >>> 8 / 2  # 除算
# 4.0
# >>> 2 ** 8  #  2の8乗
# 256
# >>> (3 + 4) * (8 - 2)  # 丸括弧
# 42
# >>> 1.1 + 1.2  # 小数
# 2.3
# >>> 3 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>> 3 +
#   File "<stdin>", line 1
#     3 +
#       ^
# SyntaxError: invalid syntax
# ```

# ### 文字列
# **文字列**は `'おはよう'` や `"こんにちは"` のように, 引用符を使って書きます.
# 文字列は `+` を使って, 2つの文字列を結合することも出来ます.
# 
# 例:
# ```
# >>> "おはよう"
# 'おはよう'
# >>> 'こんにちは'
# 'こんにちは'
# >>> "おはよう" + "こんにちは"
# 'おはようこんにちは'
# ```

# ## スクリプトを実行する
# 実際に Python プログラムを作成する時には, ファイルにプログラムを書いておいて, そのファイルを Python インタプリタで実行することが多いです.
# Python プログラムは末尾に拡張子 **`.py`** をつけます. (例: `filename.py`)
# 
# ファイルを作成してみましょう. 例 (`0.py`):
# ```python
# print("こんにちは")
# ```
# 
# ファイルを作成したら, 実行してみましょう. 例:
# ```
# $ python 0.py
# こんにちは
# ```
# 
# 対話モード以外で文字列を表示するためには `print()` 関数を利用します.
# 
# ### コメント
# **`#`** 以降に書かれたプログラムは**コメント**と呼ばれ, プログラムとしての意味は持ちません.
# プログラマーが様々なメモをプログラム中に残すために利用します.

# In[2]:

print("ここは表示される")
# print("ここは表示されない")
print("ここも表示される")


# ## 練習
# - 対話モードで Python インタプリタを起動して, 様々な計算をしてみましょう
#   - 非常に大きい数や非常に小さい数を計算してみましょう
#   - 整数と小数 (浮動小数点数) の違いはわかりますか?
# - 適当な Python プログラムのファイルを作成して, 実行してみましょう
#   - 何かメッセージを表示できましたか?
