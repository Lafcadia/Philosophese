import random

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)


def chs2phi(s, philo=0.1):
    words = list(pseg.cut(s))
    print(words)
    phi = []
    for word, flag in words:
        phi.append(word)
    for i in phi:
        if random.choices([0,1], [1-philo, philo])[0] and phi.index(i) != 0 and phi.index(i) != len(phi)-1:
            phi.insert(phi.index(i), '♂')
    return ''.join(phi)

if __name__ == '__main__':
    print(chs2phi('务必要结婚，娶个好女人，你会很快乐，娶个坏女人，你会成为哲学家。',0.1))
