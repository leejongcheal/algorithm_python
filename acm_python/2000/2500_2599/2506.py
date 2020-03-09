N = int(input())
print(sum((q*(q+1))//2 for q in map(len,input()[::2].split('0'))))