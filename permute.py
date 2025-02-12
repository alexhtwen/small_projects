# ChatGPT (iteration)
from typing import List

def permute(chars: str = '') -> List[str]:
    """
    將輸入字串進行全排列，生成所有可能的排列組合，使用迭代方式。

    參數:
        chars (str): 待排列的字串，預設值為空字串 ''。

    傳回值:
        List[str]: 包含所有可能排列的列表，每個元素的長度與原字串相同。
    """
    # 若字串為空，回傳空列表
    if not chars:
        return []

    # 開始時的排列僅為一個空字串
    permutations = ['']

    # 逐一將每個字元插入到當前的排列中
    for char in chars:
        new_permutations = []
        for perm in permutations:
            # 將當前字元插入到排列中每個可能的位置
            for i in range(len(perm) + 1):
                new_permutations.append(perm[:i] + char + perm[i:])
        permutations = new_permutations

    return permutations

permute('ab')   # ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']