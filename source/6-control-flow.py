
# coding: utf-8

# # 制御構造
# プログラムは入力された値に応じて, 様々な処理を行います. 制御構造を用いると, 条件分岐や反復処理などを実現できます.

# ## if 文
# if 文は条件分岐を実現します. if 文は次のように書きます.
# 
# ```
# if 条件1:
#     条件1が成立した時の処理
# elif 条件2:
#     条件1は成立しなかったが, 条件2が成立した時の処理
# else:
#     条件1も条件2も成立しなかった時の処理
# ```

# In[1]:

x = 75
if x >= 80:
    print("優")
elif x >= 70:
    print("良")
elif x >= 60:
    print("良")
else:
    print("不可")


# 条件が成立するとは条件の値が `True` であることを意味し, 条件が成立しないとは条件の値が `False` であることを意味します.
# 
# `>=` という演算子は真偽値 `True` または `False` を返すものです. 他にも `==`, `!=`, `<`, `<=`, `>` のような**比較演算子**があります.
# 
# 上の例の条件の値を実際に見てみましょう.

# In[2]:

x = 75
print(x >= 80)
print(x >= 70)
print(x >= 60)


# 前の章の `in` 演算子も真偽値 `True` または `False` を返すものでした. if 文と組み合わせて次のようなプログラムが作れます.

# In[3]:

eiwa = {
    "apple": "りんご",
    "dog": "イヌ",
    "egg": "卵"
}

if "dog" in eiwa:
    print("dog は eiwa のキーです")
else:
    print("dog は eiwa のキーではありません")

if "cat" in eiwa:
    print("cat は eiwa のキーです")
else:
    print("cat は eiwa のキーではありません")


# ## for 文
# for 文は反復処理を実現します. Python の for 文は次のように書きます.
# 
# ```
# for 変数名 in 反復するデータ:
#     処理
# ```
# 
# Python では C などのプログラミング言語と違い, リストや文字列のシーケンス型について反復処理を行えます.

# In[5]:

primes = [2, 3, 5, 7, 11, 13]
print("素数の先頭6個:")
for prime in primes:
    print(prime)

print("文字列を1文字ずつ:")
for char in "文字列":
    print(char)


# `range()` 関数を使うと, 簡単に数列を作ることができます.

# In[6]:

for i in range(10):
    print(i)


# 前の章で紹介した `dict.items()` はペア (タプル) のリストを返す関数でした. Python の for ではペアのリストについても簡単に反復処理が行えます.

# In[10]:

print(eiwa.items())

for english, japanese in eiwa.items():
    # english と japanese にペアの値がそれぞれ入ります
    print("英語: " + english)
    print("日本語: " + japanese)


# ## 練習
# - 0から100 までの数の和を表示するプログラムを作ってみましょう
# - 0から100 までの数のうち, 奇数だけを順に表示するプログラムを作ってみましょう
# - 0から100 までの数のうち, 素数だけを順に表示するプログラムを作ってみましょう