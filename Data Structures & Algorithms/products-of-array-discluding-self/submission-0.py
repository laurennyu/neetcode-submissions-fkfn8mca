class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_indices = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(zero_indices) < 2:
                    zero_indices.append(i)
            else:
                total_product *= nums[i]
        
        if len(zero_indices) == 0:
            products = [total_product] * len(nums)
            for i in range(len(products)):
                products[i] = int(products[i]/nums[i])
            return products
        elif len(zero_indices) > 1:
            return [0] * len(nums)
        else:
            products = [0] * len(nums)
            products[zero_indices[0]] = total_product
            return products