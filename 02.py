import datetime as dt


def main():
    # 获取当前时间,%F是年月日,%T是时分秒
    now_time = str(dt.datetime.now().strftime('%F %T'))
    # 在同级目录下如果有time.txt则打开，没有则新建
    with open('time.txt', 'a') as t:
        # 将数据写入
        t.write(now_time+"\n")
        t.close()


if __name__ == '__main__':
    main()
