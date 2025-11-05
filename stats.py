def f_num_words(file_contents):
    word_cnt = len(file_contents.split())
    
    return word_cnt

def f_num_letters(file_contents):
    letter_counts = {}
    cln_txt = file_contents.lower()
    
    for i in cln_txt:
        if i not in letter_counts:
            letter_counts[i] = 1
        else:
            letter_counts[i] += 1
    
    return letter_counts

def f_letter_freq_sort(letter_cnts):
    v_split_dict = []

    for letter, cnt in letter_cnts.items():
        v_split_dict.append({"letter": letter, "num": cnt})

    def f_sort_col(v_split_dict):
        return v_split_dict["num"]

    v_split_dict.sort(reverse=True,key=f_sort_col)

    return v_split_dict