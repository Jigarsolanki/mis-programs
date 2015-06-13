def cords_generator(row, col, length_of_the_word, direction):
    for index in range(length_of_the_word):
        yield {
            'NORTH': lambda: [ row - index, col],
            'NORTH_EAST': lambda: [ row - index, col + index ],
            'EAST': lambda: [ row, col + index ],
            'SOUTH_EAST': lambda: [ row + index, col + index ],
            'SOUTH': lambda: [ row + index, col ],
            'SOUTH_WEST': lambda: [ row + index, col - index ],
            'WEST': lambda: [ row, col - index ],
            'NORTH_WEST': lambda: [ row - index, col - index ]
        }[ direction ]()


def get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, direction):
    matched_cords = []
    word_mached = False

    for index, cords in enumerate(cords_generator(root_row_index, root_column_index, len(word), direction)):
        is_out_of_bound = not (0 <= cords[0] < len(word_table) and
                            0 <= cords[1] < len(word_table[root_row_index]))
        if is_out_of_bound or word[index] != word_table[cords[0]][cords[1]]:
            word_mached = False
            break
        else:
            if (index + 1) == len(word):
               word_mached = True
            matched_cords.append([ cords[0], cords[1] ])

    if word_mached:
        return matched_cords
    else:
        return None


def check_north(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'NORTH')


def check_north_east(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'NORTH_EAST')


def check_east(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'EAST')


def check_south_east(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'SOUTH_EAST')


def check_south(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'SOUTH')


def check_south_west(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'SOUTH_WEST')


def check_west(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'WEST')


def check_north_west(word_table, root_row_index, root_column_index, word):
    return get_matched_cords_by_dir(word_table, root_row_index, root_column_index, word, 'NORTH_WEST')


def find_word(word_table, word):
    match_cords = []
    for row_index in range(len(word_table)):
        current_row = word_table[row_index]
        for column_index in range(len(current_row)):
            cords = (check_south(word_table, row_index, column_index, word) or
                        check_north(word_table, row_index, column_index, word) or
                        check_east(word_table, row_index, column_index, word) or
                        check_west(word_table, row_index, column_index, word) or
                        check_south_west(word_table, row_index, column_index, word) or
                        check_south_east(word_table, row_index, column_index, word) or
                        check_north_west(word_table, row_index, column_index, word) or
                        check_north_east(word_table, row_index, column_index, word))

            if cords is not None:
                match_cords = match_cords + cords

    return match_cords

def highlight_all(word_table, words_locations):
    map_string = ''
    for row_index in range(len(word_table)):
        current_row = word_table[row_index]
        row_string = ''
        for column_index in range(len(current_row)):
            letter = word_table[row_index][column_index]
            if [ row_index, column_index ] in words_locations:
                row_string += '\033[1;31m' + letter + '\033[1;m' + ' '
            else:
                row_string += letter + ' '

        map_string += row_string + '\n'
    print map_string

if __name__ == "__main__":
    word_table = [
      [ 'A','F','B','J','A','E','R','G','O','S','D','B','A','N','F','B','Z','S'],
      [ 'J','B','T','D','S','N','O','A','R','S','G','D','S','C','D','B','V','M'],
      [ 'E','B','J','Q','W','E','F','O','D','B','E','J','T','B','N','S','D','B'],
      [ 'B','M','T','N','S','O','W','E','F','A','B','M','Y','K','N','S','T','O'],
      [ 'U','Y','O','A','V','N','X','Z','N','V','N','W','U','R','U','I','H','O'],
      [ 'B','N','A','W','J','E','I','E','R','G','S','O','M','B','D','S','I','O'],
      [ 'Q','J','W','R','E','U','D','N','B','V','N','M','T','O','O','E','S','T'],
      [ 'I','Y','G','I','B','N','S','D','F','K','G','U','J','H','Y','I','V','N'],
      [ 'S','E','J','B','O','T','Y','R','O','W','E','R','J','H','E','F','B','M'],
      [ 'E','R','A','W','J','E','I','E','W','E','E','R','J','H','D','R','A','V']
    ]

    highlight_all(word_table, [])
    word_to_search = raw_input('Enter a word to highlight: ')
    if word_to_search is not '':
        words_locations = find_word(word_table, word_to_search)
        highlight_all(word_table, words_locations)
