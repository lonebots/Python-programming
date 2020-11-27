n=list(map(int, input().split()))
m=max(n)
n.sort()
for i in range(1,m):
  if i != n[i-1]:
    print(i,end="")
    break
    
    
   #this has problems with the internal test cases!the correct solution for the problem is given below as comment


# getMissingNo takes list as argument 
def getMissingNo(A): 
    n = len(A) 
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A 
  
# Driver program to test above function 
li=[]
li= list(map(int, input ().split ())) 
miss = getMissingNo(li) 
print(int(miss)) 
