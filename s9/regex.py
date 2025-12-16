import re
""" texte="age:35,40,50"
regex="\d+"
 """"""result=re.match(regex,texte)
print(result.group())
 """
#findall
""" result=re.findall(regex,texte)
print(result)
 """
#search
""" result=re.search(regex,texte)
print(result.group()) """
#finditer
""" result=re.finditer(regex,texte)
for r in result:
    print(r.group()) """
#sub
""" result=re.sub(regex,"python",texte)
print("result",result)
print("texte",texte) """
#split
""" 
result=re.split(",",texte)
print(result) 
print(texte) """
#________________________________________________________________________________

""" texte="python est génial"
test="python"
testMAJ="Python"
test2="JAVA"
test3="est"

print(re.match(test,texte).group())

print(re.search(test,texte).group())
print(re.search(testMAJ,texte).groups())
#print(re.search(test2,texte).groups())
#print(re.search(test3,texte).group())
#print(re.match(testMAJ,texte).group())
#print(re.match(test2,texte).group())
#print(re.match(test3,texte).group())
 """
""" 
number ="Numeros :+216 ,123,456"
numscheck=re.findall(r"\d+",number)
print(numscheck) """
""" emailckech="^(\w+)@(\w+).(\w+)$"
emailtest="takwa123@gmail.com"
print(re.match(emailckech,emailtest).group()) """
""" regextestemail="^[\w.-]+@[\w]+\.\w+$"
emailtest="takwa_laffet@is-et.tn"
if re.match(regextestemail,emailtest):
    print("email correct")
else:
    print("email incorrect") """

""" texte="Bonjour, je m'appelle Takwa Laffet nous sommes en 2025"
nouveau=re.sub(r"\d+","16/12/2025",texte)
print(nouveau) """