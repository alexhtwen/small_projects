def diamond(chars: str, direction: str = 'left') -> str:
    import math
    if len(chars) <= 1:
        diamond_str = chars
    else:
        middle_layers = ''
        paired_layer_id = len(chars)
        paired_layers = math.ceil((paired_layer_id - 2) / 2)
        paired_layers = paired_layers + 1 if paired_layers % 2 == 0 else paired_layers
        chars_full = chars + chars[:paired_layers*2 + 2 - len(chars)]
        len_chars_full = len(chars_full)
        bottom_pos = int(len_chars_full/2)  # top的position一定是0，不必設變數。
        chars_paired = chars_full[1:bottom_pos] + chars_full[bottom_pos+1:]
        max_leading_spaces = int((paired_layers - 1)/2) + 1
        # print(f'{chars_paired = }  {paired_layers = }')

        for paired_layer_id in range(paired_layers):
            # 前面的空白：上半部空白數遞減，最寬那層沒空白，下半部則空白數遞增。
            leading_spaces = ' '*(max_leading_spaces - paired_layer_id - 1) if paired_layer_id <= paired_layers / 2 else ' '*(paired_layer_id - max_leading_spaces + 1)
            # 中間「空洞」的空白：上半部遞增，最寬那層空白最多，下半部則遞減。
            hollow_spaces =  ' '*(paired_layer_id*2 + 1) if paired_layer_id <= paired_layers / 2 else ' '*((paired_layers - paired_layer_id)*2 - 1)
            if direction == 'left':
                left_char = chars_paired[paired_layer_id]
                right_char = chars_paired[-paired_layer_id-1]
            else:
                left_char = chars_paired[-paired_layer_id-1]
                right_char = chars_paired[paired_layer_id]

            middle_layers += leading_spaces + left_char + hollow_spaces + right_char + '\n'

        top_layer = ' '*max_leading_spaces + chars_full[0] + '\n'
        bottom_layer = ' '*max_leading_spaces + chars_full[bottom_pos]
        diamond_str = top_layer + middle_layers + bottom_layer
    return diamond_str

print()
chars = ''
print(f'{chars = }\n')
print(f'{diamond(chars) = }\n')

chars = 'A'
print(f'{chars = }\n')
print(f'{diamond(chars)}\n\n')

chars = '01234'
print(f"diamond('{chars}', 'right')\n")
print(f"{diamond(chars, 'right')}\n\n")

chars = '*!@#$%*@#$%!'
print(f"diamond('{chars}', 'left')\n")
print(f"{diamond(chars, direction='left')}\n\n")

chars = 'abcdefghijklmnopqrstuvwxyz'
print(f"diamond('{chars}', 'right')\n")
print(f"{diamond(chars=chars, direction='right')}\n\n")

chars = '亂我心者，今日之日多煩憂。'
        # '人生在世不稱意，明朝散髮弄扁舟'
print(f"diamond('{chars}', 'left')\n")
print(f"{diamond(chars=chars, direction='left')}\n")