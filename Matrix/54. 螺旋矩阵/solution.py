class Solution:
    def spiralOrder(self, matrix):
        height = len(matrix)
        width = len(matrix[0])
        result = []
        if (height == 0 or width == 0):
            return result
        cur_coord = [0,0]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        direction = dirs[0]
        h_high_bound = height
        h_low_bound = 0
        w_high_bound = width
        w_low_bound = 0
        while(True):
            if w_low_bound>=w_high_bound or h_low_bound>=h_high_bound:
                break
            result.append(matrix[cur_coord[0]][cur_coord[1]])
            cur_coord[0] = cur_coord[0]+ direction[0]
            cur_coord[1] = cur_coord[1]+ direction[1]
            if cur_coord[1]>=w_high_bound:
                direction = dirs[2]
                cur_coord[1] = cur_coord[1]-1
                h_low_bound += 1
            elif cur_coord[1]<w_low_bound:
                direction = dirs[3]
                cur_coord[1] = cur_coord[1]+1
                h_high_bound -= 1
            elif cur_coord[0]>=h_high_bound:
                direction = dirs[1]
                cur_coord[0] = cur_coord[0]-1
                w_high_bound -=1
            elif cur_coord[0]<h_low_bound:
                direction = dirs[0]
                cur_coord[0] = cur_coord[0]+1
                w_low_bound += 1
            else:
                continue
            cur_coord[0] += direction[0]
            cur_coord[1] += direction[1]
        return result
if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    re = s.spiralOrder(mat)
    print(re)





