
#The biggest number will be a long int.  
# sum the digits of the digits of the string
def Add_BigNumber(numa, numb):
   import math
   total = numa + numb
   print (total)


#if the string is odd put _ at the end
def split_string(str):
   result = []
   if (len(str)%2 !=0):
      str = str + "_"
   i = 0
   for i in range(len(str)):
       result.append(str[i])
       i = i + 2
   return result

def split_string2(str):
    if len(str)%2 != 0:
      #append _ at the end of the list
        str[-1] += "_"
    even_pos_chars = [char for i, char in enumerate(str) if i%2 !=0 ]
    return even_pos_chars



      

my_sentence = "Hello, this is me"
numa = 123_0000_456_789
numb = 987654322
#Add_BigNumber(numa, numb)

#print(split_string2(my_sentence))

      

   





if __name__ == "__main__":
   #split_string(str)
   #Add_BigNumber(numa, numb )
   #split_string2(str)
   split_string_to_list(str)
   