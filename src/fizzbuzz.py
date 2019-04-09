
def fizzBuzz(num):
    mod_by_3 = False if (num % 3) else True
    mod_by_5 = False if (num % 5) else True
    if mod_by_3 and mod_by_5:
        print('fizzBuzz')
    elif mod_by_3:
        print('fizz')
    elif mod_by_5:
        print('buzz')
    else:
        print(num)


def range_fizzBuzz(num):
    for i in range(1, num+1):
        fizzBuzz(i)

if __name__ == "__main__":
    num = int(input())
    range_fizzBuzz(num)
