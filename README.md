# Flesch_Index
#Intro
Code computes the Flesch index and reading level for words of a text file or document

The Flesch readability index was invented by Dr. Rudolf Flesch as a tool for estimating how difficult a document is to read and comprehend. The index does not consider the meaning of words, only their lengths and the lengths of sentences, in order to assign a readability index to the document. The higher the readability index, the easier a document is to comprehend.

Flesch readability indexes are often translated into the educational level that is usually necessary to understand a document, as shown in the table below.
![image](https://user-images.githubusercontent.com/79537608/112585141-9efc1780-8dcf-11eb-92db-0f2fe048c555.png)

Flesch's formula to calculate the index  𝐹  as follows.
![image](https://user-images.githubusercontent.com/79537608/112585128-986da000-8dcf-11eb-9274-01c5bab4badd.png)

To compute  𝐹 , use the following definitions for word, sentence, and syllable.

word: Any sequence of non-whitespace characters that contain at least one letter or digit.

sentence: A period, question mark, exclamation point, colon, or semicolon defines a sentence.

syllable: Use the definition given in Problem #4 of this assignment.

Once  𝐹  is computed, the Flesch Grade Level ( 𝐺 ) is determined based on the table given earlier. For example, a Flesch index of 53.4 means that a high school student can comprehend the document.

# This code
Orignial code was created in Google Colab, path to files should be adjusted based on the files location.
Files are in txt format
