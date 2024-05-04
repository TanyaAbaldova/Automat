print ("Введите сумму", end=" ")
X = int(input())
print ("Введите срок", end=" ")
Y = int(input())

def bank(X,Y):
    for y in (1,Y+1):
        X=X+(X*0.1)
        sum=X
        #for sum in (Y+1):
        print(sum)
bank(X,Y)