str1 = "earth"
str2 = 'heare'

def get_same(str1:str,str2:str)->bool:
    if len(str1) != len(str2):
        return False
    
    for i in  str1:
        if i in str2:
            str2 = str2.replace(i,"",1)
        else:
            return False
        
    return len(str2)==0

result = get_same(str1,str2)
print(result)



