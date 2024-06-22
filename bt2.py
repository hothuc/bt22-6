print("10 test scores")
s = [input(">>") for i in range(10)]
3
print("so lon nhat, nho nhat:", max(map(int, s)) , min(map(int, s)))
print("average:", sum(map(int, s))/10)
print("second largest:", sorted(map(int, s), reverse=True)[1])
i=0
while i < 9:
    if int(s[i]) > 100 : break
    i = i + 1 
print("massage warning: the user that a value over 100 has been entered")
sorted_list = sorted(map(int, s))
print("result e :",(sum(map(int, s))-int(sorted_list[8])-int(sorted_list[9]))/8)