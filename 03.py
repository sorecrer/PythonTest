import string
import random


def main():
    # 生成随机数库
    selectWord = string.ascii_letters + "0123456789"
    # 生成密码库列表
    for x in range(10):
        # 将随机数库转换为列表，方便后续移除已调用字符
        list_selectWord = [str(i) for i in selectWord]
        re = ""
        for y in range(8):
            word = random.choice(list_selectWord)
            re += word
            list_selectWord.remove(word)
        print(re)


if __name__ == '__main__':
    main()
