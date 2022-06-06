import re
def translate(word_or_phrase):
  words_list = re.findall(r"[\w']+|[.,!?; ]",word_or_phrase)
  pig_list = []
 
  for word in words_list:
    match= re.search("^[AEIOUaeiou]",word)
    cap = False
    
    
    if word[0].isupper():
      cap=True
      word = word.lower()
      

    if match != None:
      word = word + "ay"
    else:
      if re.search("qu",word) == None:
        for letter in word:
          if re.search("[AEIOUaeiou]",letter)!= None:
            ending= word[word.index(letter):]
            beggining = word[:word.index(letter)]
            word= ending+beggining+"ay"
            break
      else:
        for letter in word:
          if re.search("[AEIOaeio]",letter)!=None:
            ending= word[word.index(letter):]
            beggining = word[:word.index(letter)]
            word = ending+beggining+"ay"
            break

    if cap == True:
      word = word.replace(word[0],word[0].upper())
    
    pig_list.append(word)  
  
  output_str = "".join(pig_list)
  
  return output_str         