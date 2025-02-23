def get_num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_char(text):
    char_count = {}
    text_to_lower = text.lower()
    for char in text_to_lower:
        if char in char_count:
            char_count[char] += 1
            
        else:
            char_count[char] = 1
           
    return char_count

def sort_on(dict):
    return list(dict.values())[0]


def sort_list(dictio):
    char_list = []
    
    for dic in dictio:
        
        dic_value = dictio[dic]
        new_dir = {dic:dic_value}
        if dic.isalpha():
            
            
            char_list.append(new_dir)
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list    
