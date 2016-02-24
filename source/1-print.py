
# coding: utf-8

# # print
# [`print()`](http://docs.python.jp/3/library/functions.html#print) 関数を利用すると, 数値や文字列を画面に表示することが出来ます.

# ## 文字列の表示
# `print()` を用いて, 文字列を表示出来ます.
# 
# Python で複数の文を記述するときは, 間に改行を記述します.

# In[1]:

print("こんにちは")
print("CAMPHOR-")
print("CAMPHOR- HOUSE")


# ## 数値の表示
# `print()` を用いて数値を表示することも出来ます.

# In[2]:

print(1 + 2)
print(2 * 3)
print("2の16乗は:")
print(2 ** 16)


# ## フォーマット
# `str.format()` 関数を利用すると文字列フォーマット処理ができます. 様々な文字列や数値を1つの文字列に結合できます.

# In[3]:

# {} の部分に .format() で指定した文字列や数値が順に入ります
print("{}と{}".format("日本語", "英語"))
print("{} 足す {} は {}".format(1, 2, 3))
print("文字列: {}, 数値: {}".format("文字列", 123))
# {n} とすると, n 番目に指定したものを表示できます
print("{1} {0} {2}".format("零", "一", "二"))
print("{1} {0} {2} {0}".format("零", "一", "二"))


# ## 練習
# - 様々な文字列や計算結果を表示する Python スクリプトを作成して, 実行してみましょう.
