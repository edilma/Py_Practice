
def likes(names):
    count = len(names)
    if count>3:
        others = count-2
    match count:
        case 0:
            return f"no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            return f"{names[0]}, {names[1]} and {others} others like this"


people = ["Alex", "Jacob", "Mark", "Max" ]
# people1 = ["Alex", "Jacob" ]
# print (likes(people1))

arr = [3,2,1,5]

for i in arr:
    m= True if i==2 else False
    #print (m)

n=6
for i in range (6):
    if i not in arr:
        arr.append(i)

print(arr)
    
    

if __name__ == "__main__":
    likes(people)
