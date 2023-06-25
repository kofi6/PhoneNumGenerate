import argparse

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser()

# 添加一个名为"-n"或"--number"的参数
parser.add_argument('-n', '--number', help='要补充的数字字符串')

# 解析命令行参数
args = parser.parse_args()

# 递归生成所有可能的11位数字
def generate_numbers(number):
    if len(number) == 11:
        return [number]
    else:
        numbers = []
        for i in range(10):
            new_number = number + str(i)
            numbers.extend(generate_numbers(new_number))
        return numbers

# 检查参数是否提供
if args.number:
    number = args.number

    # 断言数字字符串长度小于等于11
    assert len(number) <= 11, '数字字符串长度不能超过11个字符'


    # 生成所有可能的11位数字
    all_numbers = generate_numbers(number)

    # 将结果写入文件
    with open('out.txt', 'w') as f:
        for num in all_numbers:
            f.write(num + '\n')
        print('写入成功')
else:
    print('没有提供数字字符串')
