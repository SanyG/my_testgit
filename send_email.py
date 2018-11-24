#-*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
from email.mime.application import MIMEApplication


class SendEmail():

    #取最新的测试报告
    def new_report(test_dir):


        # 列举test_dir目录下的所有文件，结果以列表形式返回
        lists=os.listdir(test_dir)

        # 按照时间顺序排序
        lists.sort(key=lambda fn:os.path.getmtime(test_dir+'/'+fn))

        # 获取最近时间的
        file_path=os.path.join(test_dir,lists[-1])

        return file_path

    def read_report(newfile):
        #打开最新测试报告文件
        f=open(newfile,'rb')

        #读取文件内容
        mail_body=f.read()

        return mail_body

        #关闭文件
        f.close()


    def send_email(reportfile,new_report_fail,now):

        # 发送者邮箱的SMTP服务器地址
        smtpserver='smtp.163.com'

        # 发送者的登陆用户名和密码
        username='xuan942458237@163.com'

        password='xuan778899'

        # 发送者邮箱
        sender='xuan942458237@163.com'

        #接收者邮箱
        receiver=['942458237@qq.com','xuan942458237@163.com']

        # 发送邮件 ，这里有三个参数
        '''
        login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文
        是一个str，as_string()把MIMEText对象变成str。
        '''

        # 构造纯文本邮件内容
        #msg = MIMEText('hello,send by Python.....','plain','utf-8')

        #mail_msg='<html><h1>你好<h1><html>'
        #msg=MIMEText(mail_msg,'html','utf-8')  #构造HTML格式邮件内容

        msg = MIMEMultipart()

        #msg['From'] = Header('xuan942458237@163.com')  #发送邮箱地址
        msg['From']=sender

        #msg['To'] = Header('942458237@qq.com') #收件邮箱地址

        #发送多人邮件
        msg['To']=','.join(receiver)

        #发送单人邮件
        #msg['To']=receiver

        subject = 'python SMTP 测试邮件'
        msg['Subject'] = Header(subject)  #邮件主题

        #邮件正文内容
        #msg.attach(MIMEText('这是一个Python发邮件的测试','plain','utf-8'))

        # 邮件内容
        text = MIMEText(reportfile,'html','utf-8')  #html格式
        msg.attach(text)

        # 发送附件
        att = MIMEApplication(open(new_report_fail, 'rb').read())
        # att = MIMEText(sendfile, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=("report.html"))
        msg.attach(att)


        smtp = smtplib.SMTP()   #实例化SMTP对象
        smtp.connect(smtpserver,25) #（缺省）默认端口是25 也可以根据服务器进行设定
        smtp.login(username,password)  #登录邮箱用户名和密码,#登陆smtp服务器
        smtp.sendmail(sender,receiver,msg.as_string())
        #print('邮件发送成功')

        #except smtplib.SMTPException:
            #print("Error: 无法发送邮件")

        smtp.quit()  # 发送完毕后退出smtp
        print('success')






