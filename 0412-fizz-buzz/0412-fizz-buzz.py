class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        for i in range(1,n+1):
            if i% 15==0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i% 5==0:
                answer.append("Buzz")
            elif i% 5==0 or i% 3 ==0:
                answer.append("FizzBuzz")
            
            else:
                answer.append(str(i))
        return answer



        