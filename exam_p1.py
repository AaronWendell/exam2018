def get_alphabet_dictionary():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    numbers = range(1,27)
    return dict(zip(alphabet, numbers))

def value_from_letters(value_dict, word):
    value = 0
    for letter in word:
        if letter in value_dict.keys():
            value += value_dict.get(letter.lower())
    return value

def import_list_from_txt(filename):
    source_data = open(filename,'r',encoding='utf8')
    line_list = source_data.readlines()
    trimmed_list = [line.strip('\n').split(' ')[0] for line in line_list]
    source_data.close()
    return trimmed_list

def get_values_for_list(source_list):
    value_dict = {}
    alphabet_dictionary = get_alphabet_dictionary()
    for item in source_list:
        value_dict.update({item : value_from_letters(alphabet_dictionary, item)})
    return value_dict

def highest_value():
    roster = import_list_from_txt('roster.txt')
    roster_with_values = get_values_for_list(roster)
    return max(roster_with_values, key=roster_with_values.get)

def words_with_same_value(word):
    word_list = import_list_from_txt('positive-words.txt')
    word_dict_with_values = get_values_for_list(word_list)
    alphabet_dictionary = get_alphabet_dictionary()
    word_value = value_from_letters(alphabet_dictionary, word)
    words = [word for word, value in word_dict_with_values.items() if value == word_value]
    return words if len(words) > 0 else None

def main():

    print("The most valuable person in the class is " + str(highest_value()))
    print("These words have the same value as the word Aaron: " + str(words_with_same_value('Aaron')))


if __name__ == '__main__':
    main()

