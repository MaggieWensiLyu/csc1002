nums = []

def promptNumber():
    idx=1
    prompt = "enter" + str(idx) + "number:"
    while True:
        n = input(prompt)
        if n == "x":
            break
        try:
          n=eval(n)
          if type(n) in (int, float) :
              n= int(n)
              nums.append(n)
              idx+=1      
        except:
            continue

def compute(nlist,c):
    ans = nlist [0]
    for val in nlist [1:]:
        ans=c(ans,val)
        print(ans)

promptNumber()
# promptNumber("second")
# promptNumber("third")
# promptNumber("forth")
# promptNumber("fifth")

compute(nums)