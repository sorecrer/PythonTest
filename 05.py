import os


def main():
    path = 'C:\Program Files (x86)'
    # 将目录下所有的文件夹名打印出来
    print(os.listdir(path))


if __name__ == '__main__':
    main()
