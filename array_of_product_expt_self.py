class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=[1] * len(nums)

        new_products= nums[0]

        for i in range (len(nums)-2, -1, -1):
            products[i]= products[i+1] * nums[i+1]

        for j in range(1, len(nums)):
            print(nums[j])
            products[j] = new_products * products[j]
            new_products *= nums[j]
        
        return products


