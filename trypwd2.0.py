"""
版本：2.0
作者：sky
作用：判断密码强度
日期：20181008
"""

class PwdTool:
    def __init__(self, pwd):
        self.pwd_str = pwd
        self.pwdstrength = 0

    def check_num(self):
        for c in self.pwd_str:
            if c.isnumeric():
                return True
        return False

    def check_str(self):
        for c in self.pwd_str:
            if c.isalpha():
                return True
        return False

    def process(self):
        # pwd > 8
        if len(self.pwd_str) >= 8:
            self.pwdstrength += 1
        else:
            print('密码长度要大于8个字符或数字')

        # pwd has num
        if self.check_num():
            self.pwdstrength += 1
        else:
            print('密码需要含有数字')

            # pwd has alpha
        if self.check_str():
            self.pwdstrength += 1
        else:
            print('密码需要含有字符')

def main():

   trytimes = 5

   while trytimes > 0:
       pwd = input('请输入密码：')
       tool = PwdTool(pwd)
       tool.process()

       f = open('pwd.txt', 'a')
       f.write('密码：{},强度:{}。\n'.format(pwd, tool.pwdstrength))
       f.close()

       if tool.pwdstrength == 3:
            print('密码强度合格')
            break
       else:
            print('密码强度不合格')
       trytimes -= 1

   if trytimes <=0:
        print('尝试次数太多！')


if __name__ == '__main__':
    main()