#for i in range(100):
    #result = "fizz" if i%3 == 0 else str(i)
    #print(result.strip(str(i)) +"buzz" if i%5 == 0 else result)
#print(["fizz" if x%3  == 0 else ("buzz" if x%5==0 else str(x)) for x in range(100)])
def fizzbuzz:
    return for i in range(101): print("fizz"*(i%3==0)+"buzz"*(i%5==0) or str(i))

def fizzbuzz_plusplus(nums, words):
  l = []
  result = 1
  for x in nums: result = result*x
  for i in range(1, result+1):
      term = i
      for j in range(len(nums)): term = str(term).strip(str(i))+words[j] if i%nums[j] == 0 else term
      l.append(term)
  return l
  
if __name__ == "__main__":
    for i in fizzbuzz_plusplus([3,5,7], ["fizz", "buzz", "jizz"]):
        print(i)