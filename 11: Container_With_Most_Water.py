class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=-1
        left=0
        right=len(height)-1
        while right>left:
            minimum=min(height[left],height[right])
            current_area= (right-left) * minimum
            if current_area>area:
                area=current_area
            if height[left]==minimum:
                left+=1
            else:
                right-=1
        return area

#runtime: O(n)
