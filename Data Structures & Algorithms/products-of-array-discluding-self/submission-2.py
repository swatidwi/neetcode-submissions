class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,4,6]

        # [1,1,2,8]

        # [,6,1]

        product_left = [1]
        for k in range(1,len(nums)):
            product_left.append(product_left[k-1] * nums[k-1])

        product_right = [1]
        # 3 to 0
        for k in range((len(nums)-2), -1, -1):
            product_right = [(product_right[0] * nums[k+1])] + product_right

        result = []
        for i in range(len(nums)):
            result.append(product_left[i]*product_right[i])

        return result

