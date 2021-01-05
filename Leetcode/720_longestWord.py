"""
题目1 词典中最长的单词
给出一个字符串数组words组成的一本英语词典。
从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。
若无答案，则返回空字符串。

示例 1：
输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释：
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。

示例 2：
输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
 
提示：

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。


"""


def search_words(list_demo):
    res_list = []
    if len(list_demo) == 0:
        return ''
    for word in list_demo:
        the_word = word
        while the_word in list_demo:
            the_word = the_word[:-1]

        if not the_word:
            res_list.append(word)

    #
    res_str = ''
    for res in res_list:
        if len(res) > len(res_str) or len(res) == len(res_str):
            res_str = res

    return res_str


from typing import List


def longestWord(words: List[str]) -> str:
    words.sort()
    tmp = set()
    tmp.add("")
    res = ""
    for word in words:
        if word[:-1] in tmp:
            tmp.add(word)
            if len(word) > len(res):
                res = word
    return res


if __name__ == "__main__":
    words = ["w", "wo", "wor", "worl", "world"]
    res_one = search_words(words)
    print(res_one)
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    res_two = search_words(words)
    print(res_two)

    res_test = longestWord(words)
    print(res_test)
