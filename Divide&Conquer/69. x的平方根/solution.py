class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        sqrt_ap= (left+right)//2
        if x<=1:
            return x
        while(True):
            if (sqrt_ap<=x/sqrt_ap and (sqrt_ap+1)>x/(sqrt_ap+1)):
                break
            elif ((sqrt_ap+1)<=x/(sqrt_ap+1)):
                left = sqrt_ap+1
            else:
                right = sqrt_ap-1
            sqrt_ap = (left+right)//2

        return sqrt_ap
if __name__ == '__main__':
    s=Solution()
    print(s.mySqrt(100))