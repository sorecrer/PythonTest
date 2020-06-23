from socket import *


def main():
    sockfd = socket(AF_INET, SOCK_STREAM)  # 默认值其实就是这个, tcp套接字
    try:
        sockfd.connect(('127.0.0.1', 8888))
        print('连接上了服务器')  # 连接上,就显示一下, 告知操作人员
    except Exception as e:
        print('连接失败', e)  # 处理一下连接失败

    while True:
        msg = input("msg>>")
        if msg.lower() == "over":  # 输入为空就退出
            print('客户端退出')
            sockfd.close()  # 退出后随即关闭套接字
            break
        sockfd.send(msg.encode())

        data = sockfd.recv(128)
        print(data.decode())


if __name__ == '__main__':
    main()
