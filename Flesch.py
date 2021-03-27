def read_file (file_name):
    """ 
    Returns the contents of a file.
    
    Parameters:
       file_name (str): the name of the file to open
           
    Returns:
       file_data_list (list of strings): the contents of the file
          returned as a list of strings.  The first
          string represents the first line of the
          file, the second string represents the 
          second line of the file, etc.
    """  

    path = '/content/gdrive/My Drive/Colab Notebooks/'
    file_to_open = path + file_name
    with open(file_to_open, 'r') as f:
        file_data_list = f.readlines()
    return file_data_list

def characters (file_name):
    """ 
    Counts the number of characters in a file.
    
    Parameters:
       file_name (str): the name of the file to open
           
    Returns:
       count_chars (int): the number of characters in a file, including letters, numerical digits, punctuation marks, whitespace and newline characters.
    
    Examples:
        count_chars ('gettysburg.txt') reutrns 1447
    """

    file_contents = read_file (file_name)
    count_chars = 0
    for line in file_contents:
        count_chars += len (line)
    return count_chars

def sentences (file_name):
    """ 
    Counts the number of sentences in a file.
    
    Parameters:
       file_name (str): the name of the file to open
           
    Returns:
       count_sentences (int): the number of sentences in a file (separated by . ? or !)
    
    Examples:
        count_sentences ('sixth-grade.txt') returns 2
    """

    file_contents = read_file (file_name)
    count_sentences = 0
    contents_string = ''
    for line in file_contents:
        contents_string += str(line)
    count_sentences = contents_string.count ('.') + contents_string.count ('?') + contents_string.count ('!') #count the number of possible ends of a sentence
    return count_sentences
    
def words (file_name):
    """ 
    Counts the number of words in a file.
    
    Parameters:
       file_name (str): the name of the file to open
           
    Returns:
       count_words (int): the number of words in a file
    
    Examples:
        count_words ('college.txt') returns 15
    """

    file_contents = read_file (file_name)
    count_words = 0
    for line in file_contents:
        line_split = line.split ()
        count_words += len (line_split)
    return count_words

def count_syllables(word):
    """
    Returns the number of syllables in the string word.
    This function uses the following heuristic for syllable counting.
        (1) Count the groups of adjacent vowels (aeiouy) in the word.
        (2) If 'e' is the last letter in a word and is preceded by a 
            non-vowel, then it does not count as a syllable (i.e., the 'e' 
            is silent).
        (3) Report that there is at least one syllable in 
            the string word.

    Parameters:
        word (str): the string that will be used by our syllable
                    counting heuristic

    Returns:
        int: the number of syllables in the string parameter word

    Examples:
        count_syllables('UniTy') returns 3
        count_syllables('me') returns 1
    """
    word_lower = word.lower () #make function non-case sensetive
    vowels = 'aeiouy'
    vowels_position = []
    i = 0
    while i < len (word_lower):
        if word_lower [i] in vowels:
            vowels_position += [i] #put each vowel posistion in a list
        i += 1
    syllables = len (vowels_position)
    k = 0
    while k < len (vowels_position) - 1:
        if vowels_position [k+1] - vowels_position [k] == 1: #vowels next to each other
            syllables -= 1 #no new syllable, substract one from previous total
        k += 1
    if word_lower [-1] == 'e' and word_lower [-2] not in vowels: # 'e' is last and preceded by non-vowel
        syllables -= 1 #no new syllable, substract one from previous total
    syllables_final = max (syllables, 1) #at least one syllable
    return (syllables_final)

def total_syllables (file_name):
    """
    Returns the number of syllables in the string word.
    This function uses the following heuristic for syllable counting.
        (1) Count the groups of adjacent vowels (aeiouy) in the word.
        (2) If 'e' is the last letter in a word and is preceded by a 
            non-vowel, then it does not count as a syllable (i.e., the 'e' 
            is silent).
        (3) Report that there is at least one syllable in 
            the string word.

    Parameters:
        file_name: the file containing the text to be analyzed

    Returns:
        int: the number of syllables in the text

    Examples:
        count_syllables('college.txt') returns 31
        count_syllables('sixth-grade.txt') returns 37
    """
    file_contents = read_file (file_name)
    number_syllables = 0
    for line in file_contents:
        line_split = line.split ()
        for word in line_split:
            word_lower = word.lower ()
            number_syllables += count_syllables (word_lower)
    return number_syllables

def flesch_grade (index):
    """
    Returns the flesch grade corresponding to the flesch index.

    Parameters:
        index (int): Flesch index calculated in the main function.

    Returns:
        str: the grade of the text based on the flesch index.

    Examples:
        grade (85) returns '6th grader'
        grade (3) returns 'College graduate'
    """
    grades = [ (100, 90), (89, 80), (79, 70), (69, 65), (64, 50), (49, 30), (30, 0)]
    grade_level = ['5th grader', '6th grader', '7th grader', '8th grader', 'High school student', \
                    'College student', 'College graduate', 'Law school graduate']
    i = 0
    if index > 100:
        return grade_level [0]
    elif index < 0:
        return grade_level [-1]
    while i < len (grades):
        if index <= grades [i] [0] and index >= grades [i] [1]:
            return grade_level [i]
        else:
            i += 1

def flesch_index_function (file_name):
    """
    Helper function to return values necessary for the assertion
    
    Parameters:
        file_name: the file containing the text to be analyzed

    Returns:
        tuple of integers: calculated values of (words per sentence, syllables per word, flesch index)

    Examples:
        flesch_index_function ('college.txt') returns (15, 2.1, 16.8)
        flesch_index_function ('sixth-grade.txt') reutrns (14.5, 1.3, 84.2)   
    """

    number_syllables = total_syllables (file_name)
    number_words = words (file_name)
    number_sentences = sentences (file_name)
    words_per_sentence = number_words/number_sentences
    syllables_per_word = number_syllables/number_words
    flesch_index = round (206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word, 1) #Flesch formula
    return words_per_sentence, syllables_per_word, flesch_index

def main ():
    file_name = input('File name: ')
    print ()

    number_syllables = total_syllables (file_name)
    print('Syllables: ', number_syllables)

    number_words = words (file_name)
    print('Words: ', number_words)

    number_sentences = sentences (file_name)
    print('Sentences: ', number_sentences)

    words_per_sentence = number_words/number_sentences
    print('Words per Sentence: ', round (words_per_sentence,1))  

    syllables_per_word = number_syllables/number_words
    print('Syllables per Word: ', round (syllables_per_word,1)) 
    print ()  

    flesch_index = flesch_index_function (file_name) [2]
    print ('Flesch Index: ', flesch_index)

    print ('Flesch Grade: ', flesch_grade (flesch_index))
    
main ()
