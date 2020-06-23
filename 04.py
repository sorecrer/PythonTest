# 发送邮件
import smtplib
from email.mime.text import MIMEText


def main():
    subject = "叶恒隆"  # 邮件标题
    sender = "soledad_mini@163.com"  # 发送方
    content = "Hello world！"
    recover = "qa_2020@163.com"  # 接收方
    password = "CRPFUXJEZYHUMPRS"  # 邮箱密码

    message = MIMEText(content, "plain", "utf-8")
    # content 发送内容     "plain"文本格式   utf-8 编码格式

    message['Subject'] = subject  # 邮件标题
    message['To'] = recover  # 收件人
    message['From'] = sender  # 发件人

    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recover], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()


if __name__ == '__main__':
    main()
