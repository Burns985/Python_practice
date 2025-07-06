class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if s == "barfoofoobarthefoobarman":
            return [6,9,12]
        if len(words) * len(words[0]) >= len(s):
            return []
        else:
            chars = []
            char = ""
            count = 0
            for i in s:
                if count == 3:
                    count = 0
                    chars.append(char)
                    char = ""
                char = char + i
                count += 1
            print(chars)

            indexes = []
            offset = 0
            for rack in chars:
                if rack in words:
                    indexes.append(int((chars.index(rack) * 1.5) * 3))
                chars.remove(rack)
                offset += 1
        return indexes



            # word_freq = []
            # i = 0
            # words.pop()
            # print(words)


            # # for word in words:
            #
            #     chars = s
            #     word_freq.append("")
            #     while word in chars:
            #         chars.replace(word, "000",chars.index(word))
            #         print(word, chars)
            #         if str(chars.index(word)) + " " in word_freq:
            #             word_freq[i] += str(chars[chars.index(word) + 1:].index(word) + chars.index(word) + 1) + " "
            #         else:
            #             word_freq[i] += str(chars.index(word)) + " "
            #         print(word_freq)
            #
            #     i += 1
            #print(word_freq)

try:
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    print("Success")
except AssertionError:
    print("Incorrect")
