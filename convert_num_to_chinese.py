import time


def numeral_to_chinese(numeral):
    ...  # 請完成這個函數。
    ...
    return ...


while True:
    time.sleep(1)  # 暫停一秒，以免有時輸入後看不到輸出。
    input_str = input('請輸入一個數字(exit結束)：')
    if input_str.lower().strip() == 'exit':
        print('Game over.')
    numeral = int(input_str)
    print(numeral_to_chinese(numeral))
    print()