import pytest 
from main import min_coins
def test_min_coins(coins, target_amount):
    dp = [float('inf')] * (target_amount+ 1)
    dp[0] = 0
    for i in range(len(coins) - 1, -1, -1):
        for j in range (1,target_amount+1):
            dp[i][j]= float('inf')
            take = float('inf')
            noTake = float('inf')
            
            #if we take coins[i]coin
            if j - coins[i]>=0:
                take = dp[i][j - coins[i]]
                if take !=float('inf'):
                    take +=1
            if i + 1 <len(coins):
                noTake =dp[i+1][j] 
                
                dp[i][j]=min(take,noTake)
                
            if dp[0][target_amount]!=float('inf'):
                return dp[0][target_amount]
            return-1
if __name__ == "__main__":
    coins =[1,4,6,9,14]
    target_amount = 26
    print(test_min_coins(coins,target_amount))
    

         
