# 課題
https://github.com/hikalium/malloc_challenge/tree/main/real_malloc

# 回答
read_malloc/malloc.cに記載しました。

## 比較結果
best-fit,worst-fit,first-fitを比較した結果、以下のようになりました。

best-fitの結果は以下のようになった
```
Challenge 1: simple malloc => my malloc
Time: 10 ms => 1795 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 9 ms => 799 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 205 ms => 933 ms
Utilization: 8% => 50%
==================================
Challenge 4: simple malloc => my malloc
Time: 24332 ms => 13133 ms
Utilization: 15% => 71%
==================================
Challenge 5: simple malloc => my malloc
Time: 16456 ms => 7162 ms
Utilization: 15% => 74%
==================================
```
worst-fitの結果は以下のようになった
```
Challenge 1: simple malloc => my malloc
Time: 11 ms => 1736 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 9 ms => 831 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 193 ms => 145343 ms
Utilization: 8% => 4%
==================================
Challenge 4: simple malloc => my malloc
Time: 20383 ms => 603509 ms
Utilization: 15% => 7%
==================================
Challenge 5: simple malloc => my malloc
Time: 20247 ms => 580099 ms
Utilization: 15% => 7%
==================================
```

## 考察

* challenge3~4において、best-fitのUtilizationの割合が、worst-fitやfirst-fitと比べ、非常に高かった
* best-fitと比べ、worst-fitのほうが時間がかかった用に思える
* best-fitと比べ、worst-fitのほうが確保可能なヒープが断片的になる

## 疑問
* Utilizationは低い方が活用されているパーセンテージが低いということだろうか
* Utilizationの値が分からないので、どちらが効率的な結果になったのかが分からない