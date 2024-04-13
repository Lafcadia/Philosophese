import random

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)


def _convertion(x, y, philo):
    if random.random() > philo:
        return x
    if x in {'，', '。'}:
        return '♂'
    if x in {'!', '！'}:
        return '♀'
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}……{x}'
    else:
        if y == 'n' and random.random() < 0.5:
            x = '〇' * len(x)
        return f'……{x}'


def chs2yin(s, philo=0.5):
    return ''.join([_convertion(x, y, philo) for x, y in pseg.cut(s)])


if __name__ == '__main__':
    print(chs2yin('从前的哲学家们只是用不同的方式解释世界，而问题在于改变世界。'))
