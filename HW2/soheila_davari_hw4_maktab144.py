#4
students = [
 {"name": "Sara", "score": 92, "attendance": 0.95},
 {"name": "Ali", "score": 67, "attendance": 0.60},
 {"name": "Omid", "score": 85, "attendance": 0.88},
 {"name": "Neda", "score": 74, "attendance": 0.99},
 {"name": "Reza", "score": 55, "attendance": 0.70},
]
def filterred_student(stu_list):
    return list(filter(
        lambda x:x["score"]>70 and x["attendance"]>0.8, stu_list))


# print(filterred_student(students))

def name_score(stu_list):
    result=[(x["name"],x["score"]) for x in filterred_student(stu_list)]
    return sorted(result , key=lambda x:x[1]  , reverse=True)    
print(name_score(students))

stu_dic={x[0]:x[1] for x in name_score(students)}
print(stu_dic)

# print(list(map(
#     lambda x:(x[0],x[1]+5) , stu_dic.items()
# )))
after_prize=({name:score+5 if score<=95 else 100 for name, score in stu_dic.items()})
print(after_prize)
from functools import reduce
print(f"total score ={reduce(lambda x,y:x+y , after_prize.values())}")
def gen(stu_list):
    for x , y in stu_list.items():
        yield f"name:{x} , score:{y:.2f}"


for item in gen(after_prize):
    print(item)

