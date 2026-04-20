
total_money=1000
spent=748
calculate=total_money-spent
print("change returned:", calculate)
note=[500,200,100,50,20,10,5,2,1]
for i in note:
    if calculate>=i:
        print(i,":",calculate//i)
        calculate=calculate%i