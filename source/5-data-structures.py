
# coding: utf-8

# # データ構造
# これまでは数値や文字列のようなデータを扱ってきましたが, Python ではリストや辞書と呼ばれるものを使って, 複数の値を一つにまとめることが出来ます.

# ## リスト
# リストは複数の値の並びを一つにまとめることができます. リストは角括弧を使って書きます.

# In[1]:

primes = [2, 3, 5, 7, 11, 13]
print(primes)


# `primes[n]` のようにして, リスト `prime` の `n` 番目の値を取得できます. (プログラミングでは数は0から数えることが多いため, 先頭の数は0番目になります)

# In[2]:

print("0番目:")
print(primes[0])
print("1番目:")
print(primes[1])
print("2番目:")
print(primes[2])


# `primes[n]` に値を代入することで, `prime` の `n` 番目の値を変更できます.

# In[3]:

print(primes)
primes[1] = 100
print(primes)


# ## 辞書
# 辞書はその名の通り辞書のようなもので, キーと値のペアの集合です. 辞書は波括弧を使って書きます.

# In[4]:

eiwa = {
    "apple": "りんご",
    "dog": "イヌ",
    "egg": "卵"
}
print(eiwa)


# `eiwa[key]` のようにして, `eiwa` のキーが `key` である値を取得できます.

# In[5]:

print(eiwa["dog"])


# 存在しないキーの値を取得しようとするとエラーになります

# In[6]:

eiwa["cat"]


# 辞書にあるキーが存在するかどうかは**`in`**演算子でチェックできます. 存在する場合は `True` (真), 存在しない場合は `False` (偽) という真偽値が返ります.

# In[7]:

print("dog" in eiwa)
print("cat" in eiwa)


# `eiwa[key]` に値を代入することで, `eiwa` のキーが `key` である値を変更出来ます.

# In[8]:

print(eiwa["dog"])
eiwa["dog"] = "犬"
print(eiwa["dog"])


# `eiwa.keys()` でキーのリスト, `eiwa.values()` で値のリスト, `eiwa.items()` でキーと値のペア (タプル) のリストを取得できます.

# In[9]:

print(eiwa.keys())
print(eiwa.values())
print(eiwa.items())


# ## 練習
# - いろいろなリストや辞書を作って, 値を変更してみましょう.
# - リストや辞書には要素を追加したり削除したりなど, 様々な操作が可能です. 調べて試してみましょう.
