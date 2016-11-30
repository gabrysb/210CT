"""INPUT string
strList <- list(string)

VOWEL (list, vwl)
	FOR i = 0 to len(list)
		IF list[i] = “vwl”
		remove element from list
	RETURN list

CALL vowel(strList, a)
CALL vowel(strList, e)
CALL vowel(strList, i)
CALL vowel(strList, o)
CALL vowel(strList, u)

OUTPUT strList
 Write a recursive function (pseudocode and code) that removes all vowels from a given string s. Input: "beautiful" Output: "btfl". This code takes the vowel and has a function that can remove any letter passed to it from a list made from the string input."""

l = input("put in word")
strlist = list(l)

def vowel(lst, vwl):
 	print(lst, vwl)
 	for i in lst:
   		if i == vwl:
     			lst.remove(i)
 	return(lst)
     
lst1 = vowel(strlist, "a")
lst2 = vowel(lst1, "e")
lst3 = vowel(lst2, "i")
lst4 = vowel(lst3, "o")
lst5 = vowel(lst4, "u")

print(lst5)
