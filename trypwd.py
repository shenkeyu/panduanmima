"""
版本：1.0
作者：sky
作用：判断密码强度
日期：20181007
"""

def check_num(pwd_str):
    for c in pwd_str:
        if c.isnumeric():
            return True

    return False


def check_str(pwd_str):
    for c in pwd_str:
        if c.isalpha():
            return True

    return False

def main():


   trytimes = 5

   while trytimes > 0:
       pwd = input('请输入密码：')
       pwdstength = 0  # pwd强度

       #pwd > 8
       if len(pwd) >= 8:
        pwdstength += 1
       else:
        print('密码长度要大于8个字符或数字')

       #pwd has num
       if check_num(pwd):
        pwdstength += 1
       else:
        print('密码需要含有数字')

        # pwd has alpha
       if check_str(pwd):
        pwdstength += 1
       else:
        print('密码需要含有字符')

       f = open('pwd.txt', 'a')
       f.write('密码：{},强度:{}。\n'.format(pwd, pwdstength))
       f.close()

       if pwdstength == 3:
            print('密码强度合格')
            break
       else:
            print('密码强度不合格')
       trytimes -= 1

   if trytimes <=0:
        print('尝试次数太多！')

   f1 = open('pwd.txt')
   #content = f1.read()
   for line in f1.readlines():
    print(line)
   f1.close()
   #print(content)




if __name__ == '__main__':
    main()