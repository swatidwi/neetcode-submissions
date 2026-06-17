class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product_list = [0] * len(nums)
        postfix_product_list = [0] * len(nums)
        result = []

        prefix_product_list[0] = 1
        postfix_product_list[-1] = 1
        
        i = 1
        while (i<len(nums)):
            prefix_product_list[i] = prefix_product_list[i-1]*nums[i-1]
            i+=1

        print(prefix_product_list)

        j = len(nums)-2
        while j>=0:
            postfix_product_list[j] = nums[j+1] * postfix_product_list[j+1]
            j = j-1

        print(postfix_product_list)

        for i in range(len(nums)):
            result.append(prefix_product_list[i]*postfix_product_list[i])
        return result


        
