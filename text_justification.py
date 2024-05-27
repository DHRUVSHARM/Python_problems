from typing import List

if __name__ == '__main__':
    arr = ['1', '2', '3', '4', '5', '6']
    print("^".join(arr))


# interesting problem with a lot of edge cases, basic idea is a greedy algo
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified_text, current_line_words, words_length = [], [], 0
        index = 0

        while index < len(words):
            if words_length + len(current_line_words) + len(words[index]) > maxWidth:
                # we have to justify this line and move to the next
                basic_spaces_length = (maxWidth - words_length) // max(len(current_line_words) - 1, 1)
                remaining_spaces = (maxWidth - words_length) % max(len(current_line_words) - 1, 1)

                # print(current_line_words)
                # print(basic_spaces_length , remaining_spaces)

                for j in range(0, len(current_line_words) - 1):
                    current_line_words[j] += (" " * basic_spaces_length)
                    if remaining_spaces:
                        current_line_words[j] += " "
                        remaining_spaces -= 1

                # adding the line
                line = "".join(current_line_words)
                line += " " * (maxWidth - len(line))
                justified_text.append(line)
                # we need to reset the line parameters
                current_line_words = []
                words_length = 0

            else:
                # we can greedily add words with a basic space of 1
                current_line_words.append(words[index])
                words_length += len(words[index])
                index += 1

        # we have exited but have not justified the last line, we have to left justify it no matter what
        if words_length:
            for j in range(0, len(current_line_words) - 1):
                current_line_words[j] += " "
            line = "".join(current_line_words)
            line += " " * (maxWidth - len(line))
            justified_text.append(line)

        return justified_text
