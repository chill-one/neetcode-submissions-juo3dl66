class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        [1,0,1,2,1,1,7,5]
        [0,1,0,1,0,1,0,1]
           1  
        """
        total = 0
        for customer, is_grumpy in zip(customers, grumpy):
            if not is_grumpy:
                total += customer

        left = 0
        best_customers = 0
        curr_customer = 0
        for right in range(len(customers)):
            curr_customer += customers[right] if grumpy[right] else 0
            if right - left + 1 < minutes:
                continue
            print(curr_customer)
            best_customers = max(curr_customer, best_customers)
            curr_customer -= customers[left] if grumpy[left] else 0
            left += 1

        return total + best_customers
