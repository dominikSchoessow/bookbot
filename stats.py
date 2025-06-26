def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lower_text = text.lower()
    ret_dic = {}
    for c in lower_text:
        if c not in ret_dic:
            ret_dic[c] = 1
        else: ret_dic[c] += 1
    return ret_dic

def sort_on(items):
    return items["num"]

def get_sorted_charakter_count(char_dic):
    ret_list = []
    for c in char_dic:
        ret_list.append({"char": c, "num": char_dic[c]})
    ret_list.sort(reverse=True, key=sort_on)
    return ret_list

