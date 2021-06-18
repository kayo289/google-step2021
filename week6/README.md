# 課題
https://github.com/hikalium/malloc_challenge/tree/main/real_malloc

# 回答
read_malloc/malloc.cに記載しました
best-fitの結果は以下のようになった

```
Challenge 1: simple malloc => my malloc
Time: 10 ms => 9 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 8 ms => 8 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 198 ms => 175 ms
Utilization: 8% => 7%
==================================
Challenge 4: simple malloc => my malloc
Time: 22008 ms => 21275 ms
Utilization: 15% => 15%
==================================
Challenge 5: simple malloc => my malloc
Time: 15253 ms => 15956 ms
Utilization: 15% => 15%
==================================
```
worst-fitの結果は以下のようになった
```
Challenge 1: simple malloc => my malloc
Time: 10 ms => 10 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 8 ms => 7 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 183 ms => 184 ms
Utilization: 8% => 7%
==================================
Challenge 4: simple malloc => my malloc
Time: 19337 ms => 20434 ms
Utilization: 15% => 15%
==================================
Challenge 5: simple malloc => my malloc
Time: 15976 ms => 17174 ms
Utilization: 15% => 15%
==================================
```
