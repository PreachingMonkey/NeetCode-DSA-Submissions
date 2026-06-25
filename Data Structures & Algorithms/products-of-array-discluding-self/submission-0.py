class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        new_List  = [0]*len(nums)
        prod = 1
        for i in range (len(nums)):
            if nums[i]==0:
                zeros+=1
            else:
                prod*=nums[i]

        if zeros>1:
            return new_List
        
        for i in range(0,len(nums)):
            if zeros==1:

                if nums[i]==0:
                    new_List[i]=prod
                elif nums[i]!=0:
                    new_List[i]=0 
            
            else:
                new_List[i] = prod//nums[i]
        return new_List
        