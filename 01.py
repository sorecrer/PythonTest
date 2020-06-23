import string


def main():
    str = """The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    str = str.split()
    # 去掉标点，全部变为小写，不区分大小写
    list_word = [word.strip(string.punctuation).lower() for word in str]
    # 去掉重复的单词
    set_word = set(list_word)
    # 构建字典
    dict_word = {word: list_word.count(word) for word in set_word}
    # 根据次数进行排列
    list_sorted_words = sorted(dict_word, key=lambda w: dict_word[w], reverse=True)
    for word in list_sorted_words:
        print("{} -- {} times".format(word, dict_word[word]))


if __name__ == '__main__':
    main()
