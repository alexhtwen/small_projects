def diamond(chars: str) -> str:
    import math
    if len(chars) <= 1:
        return_str = chars
    else:
        return_str = ''
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
            return_str += leading_spaces + chars_paired[paired_layer_id] + hollow_spaces + chars_paired[-paired_layer_id-1] + '\n'
        return_str = ' '*max_leading_spaces + chars_full[0] + '\n' + return_str + ' '*max_leading_spaces + chars_full[bottom_pos]

    return return_str

chars = 'abcdefghijklmnopqrstu'  # vwxyz'
print(f'{chars = }')
print(diamond(chars))
# bb ca dr eq fp go hn im jl