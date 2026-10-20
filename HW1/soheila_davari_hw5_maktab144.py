#5
def report(name , *scores ,title="student"):
    if scores:
        average=sum(scores)/len(scores)
        score_list=",".join(str(score) for csore in scores)
    else:
        average=0
        score_list="no score"
    
    print(f"{title} {name} -scores:{sore_list}- average :{average}")
report("soheila")