class Solution(object):
    def maxProfit(self,prices):
        max_profit=0
        min_price=float('inf')
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                current_profit=price-min_price
                if current_profit>max_profit:
                    max_profit=current_profit
        return max_profit
def main():
    s=Solution()
    p=[7,6,4,3,2,1]
    print(s.maxProfit(p))
main()
