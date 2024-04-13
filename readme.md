# 哲♂学翻译机

能把中文翻译成哲♂学的翻译机！

<sub>(鸣谢伟大的 <a href="https://github.com/RimoChan/yinglish">RimoChan 的淫语翻译机</a> )</sub>


## 样例

```python
import philosophese

s = '你已经站在宏观的角度进行哲学思考了。'
print(philosophese.chs2phi(s))
# 你已经站在宏观的角度进行哲♂学思考了。

s2 = '务必要结婚，娶个好女人，你会很快乐，娶个坏女人，你会成为哲学家。'
print(philosophese.chs2phi(s2))
# 务必要结婚，娶个好女人，你会很快乐，娶个坏女人，你会成为哲♂学家。
```


## 接口说明

```python
def chs2phi(s, philo=0.5):
```

s是原字符串，philo是0~1之间的实数，越大越哲♂学，表示每个词语被转化的概率。


## 安装

```bash 
pip install philosophese
```


