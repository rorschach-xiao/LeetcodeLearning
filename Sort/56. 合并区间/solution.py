class Solution:
    def merge(self, intervals):
        intervals.sort()
        merged_inter = []
        for inter in intervals:
            if merged_inter == []:
                merged_inter.append(inter)
            else:
                if merged_inter[len(merged_inter) - 1][1] >= inter[0]:
                    merged_inter[len(merged_inter) - 1][1] = max(
                        merged_inter[len(merged_inter) - 1][1], inter[1])
                else:
                    merged_inter.append(inter)
        return merged_inter

if __name__ =='__main__':
    intervals = [[1,6],[4,7],[20,49],[25,60]]
    s = Solution()
    merged_intervals = s.merge(intervals)
    print(merged_intervals)
