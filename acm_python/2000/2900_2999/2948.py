d = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
m = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday"]
D,M = map(int,input().split())
print(m[(d[M]+D)%7])
