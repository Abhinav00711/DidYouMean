def DidYouMean(test_str,word_list):
  similar_word=""
  similar_word_length=0
  minimum_change=100
  for word in word_list:
    word_minimum_change=0
    temp_list=[]
    for char_test_str in test_str:
      if char_test_str not in word:
        word_minimum_change+=1
      elif test_str.count(char_test_str)!=word.count(char_test_str) and char_test_str not in temp_list:
        temp_list.append(char_test_str)
        word_minimum_change+=1
    for char_word in word:
      if char_word not in test_str:
        word_minimum_change+=1
      elif test_str.count(char_word)!=word.count(char_word) and char_word not in temp_list:
        temp_list.append(char_word)
        word_minimum_change+=1
    if word_minimum_change<minimum_change:
      minimum_change=word_minimum_change
      similar_word_length=len(word)
      similar_word=word
    elif word_minimum_change==minimum_change:
      if similar_word_length>len(word):
        similar_word_length=len(word)
        print(word)
        similar_word=word
  return similar_word

print(DidYouMean('strawrdry', ['cherry', 'pineapple', 'melon','orange','strawberry','rasberry']))