
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
people1 = ["Alex", "Jacob" ]
print (likes(people1))

if __name__ == "__main__":
    likes(people)
