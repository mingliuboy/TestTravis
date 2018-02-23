#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import smtplib
import socket
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 自动发送邮件
def send_email(new_report):
    # 读取测试报告中的内容作为邮件的内容
    with file(new_report, 'r') as f:
        mail_body = f.read()

    # mail_body = "<html>Test</html>"
    # 发件人地址
    from_addr = 'mingeasilydo@naver.com'
    # 收件人地址 weicheng@edison.tech
    to_addr = "testeda@163.com"
#"ming@edison.tech; weicheng@edison.tech; jing.zhang@edison.tech"
    # 发送邮箱的服务器地址
    mail_server = 'smtp.naver.com'
    # 邮件的标题
    subject = 'chat Server 测试报告'
    # 发件人的邮箱地址
    username = 'mingeasilydo@naver.com'
    password = 'Ming@2016'
    # 邮箱的内容和标题
    message = MIMEText(mail_body, 'html', 'utf8')
    message['Subject'] = Header(subject, charset='utf8')
    message['To'] = to_addr
    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username, password)
        smtp.sendmail(from_addr, to_addr.split(','), message.as_string())
        smtp.quit()
        print('发送成功')
    except smtplib.SMTPException as e:
        print('smtp can\'t send mail  %s' % e)
    except socket.error as e:
        print('could not connect to server %s ' % e)
    except Exception as e:
        print('发送失败: %s ' % e)


# 获取最新报告的地址
def acquire_report_address(reports_address):
    # 测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(reports_address)
    # 按照升序排序生成新的列表
    new_test_reports_list = sorted(test_reports_list)
    # 获取最新的测试报告
    the_last_report = new_test_reports_list[-1]
    # 最新的测试报告的地址
    the_last_report_address = os.path.join(reports_address, the_last_report)
    return the_last_report_address


if __name__ == '__main__':
    pass
    # 生成测试报告并发送邮件
    # 测试报告文件夹地址

    test_file = './testReport/testReport.html'
    setup_file = './'

    # test_cases_dir = os.path.abspath(os.path.dirname(setup_file))
    
    # os.system("pytest runRestAPI.py --html=%s" % test_file)

    test_reports_dir = os.path.abspath(os.path.dirname(test_file))

    new_report_addr = acquire_report_address(test_reports_dir)

    send_email(new_report_addr)
