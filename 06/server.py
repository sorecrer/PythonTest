from socket import *


def main():
    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.bind(('0.0.0.0', 8888))
    sockfd.listen(3)

    while True:
        print('等待接收中...')
        try:
            connfd, addr = sockfd.accept()
            print('客户端已连接:', addr)  # 连接到客户端,就打印消息,告诉一下操作人员
        except KeyboardInterrupt:
            print('服务器退出')
            break  # 每次捕获异常, 都要做相应的处理, 不然后续代码会出问题
        except Exception as e:
            print(e)
            continue  # 每次捕获异常, 都要做相应的处理, 不然后续代码会出问题

        while True:
            data = connfd.recv(1024)  # 循环接收数据
            if not data:  # 客户端退出后,系统会自动发送空字符过来,可以据此判断客户端状态
                print('此客户端已退出, 正在等待连接下一个客户端...\n')
                connfd.close()  # 关闭对应这个客户的套接字
                break  # 退出这个客户的"循环接收发送"
            print('客户端发来:', data.decode())  # 客户端发来的消息不为空时的处理
            connfd.send(b"OK")  # 会发客户端消息
    sockfd.close()


if __name__ == '__main__':
    main()
