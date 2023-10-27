def del_me(txt: str, char: str = '') -> str:
    # return (word_list := sentence.split())[0], word_list[1:]
    return txt.replace(char, '')

txt = 'Alex Van is a Pythonista who works very hard.'

print(f'{del_me(del_me(del_me(del_me(txt, 'a'), 'n'), 'e'), 's')}')
