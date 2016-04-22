
# coding: utf-8

# ## input
# [`input()`](http://docs.python.jp/3/library/functions.html#input) 関数は, 入力から1行を読み込み, その結果を文字列として返します.
# 

# ## 文字列の入力

# In[1]:

name = input("名前は?")
print(name + "さん、こんにちは")


# ## 整数の入力
# `input()` 関数は入力された値を文字列として返します.
# `int()` を利用すると, 文字列を整数に変換することが出来ます.
# これらを組み合わせると, 入力された文字列を整数に変換して利用することができます.

# In[2]:

multiplier = input("2を何倍しますか?")
multiplier = int(multiplier)  # 文字列 -> 整数の変換
print(2 * multiplier)


# ## 練習
# - 2つの整数を入力して, その積 (乗算の結果) を表示するプログラムを作って実行しましょう.
# - `print(3 * input("数字を入力してください"))` を実行すると, 何が表示されるでしょうか?
