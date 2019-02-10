print ("what is the number you want to divide?")
div = raw_input()
y = int(div)

listRange = list(range( 1, y+1 ))
divisorList = []

for i in listRange:
    if y % i == 0:
        divisorList.append(i)

print divisorList
