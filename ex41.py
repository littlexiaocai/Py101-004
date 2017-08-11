import random
from urllib import urlopen
import sys

WORD_URL="http://learncodethehardway.org/words.txt"

WORDS =[]

PHRASES = {
"calss %%%(%%%):":
"make a class named %%% that is-a %%%",
"calss %%%(object):\n\t def__init__(self,***)":
"class %%% has-a __init__ that takes self and *** parameters",
"class %%%(object):\n\tdef***(self,@@@)":
"class %%% has-a function named***that takes self and@@@ parameters.",
"*** = %%% ()":
"set *** to an instance of class %%%",
"***.***(@@@)":
"From *** get the *** function ,and call ti with parameters self,@@@",




}
