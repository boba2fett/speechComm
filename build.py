from custom_commands import commands
from inspect import getmembers, isfunction

functions_list = [o[0] for o in getmembers(commands) if isfunction(o[1])]
print("Keyword:",commands.keyword)
print("Functions found:")
print(functions_list)
functions_list+=[commands.keyword]

words=list()
for function in functions_list:
    if "_" in function:
        words += function.split("_")
    else:
        words+=[function]

speechwords=open("lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict","w")

allspeechwords=open("lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict.backup","r")

print(words)


while l:=allspeechwords.readline():
    if l.split(" ")[0] in words or l.split(" ")[0].split("(")[0] in words:
        speechwords.write(l)
speechwords.close()
