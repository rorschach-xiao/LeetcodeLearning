class Solution:
    def getLeastNumbers(self, arr, k):
        start, end = 0, len(arr) - 1
        for i in range(len(arr)):
            pos = self.partition(arr, start, end)
            if pos < k - 1:
                start = pos + 1
            elif pos > k - 1:
                end = pos - 1
            else:
                break
        return arr[:k]

    def partition(self, arr, start, end):
        pivot = arr[start]
        left_ptr = start
        right_ptr = end
        while (left_ptr < right_ptr):
            while (left_ptr < right_ptr and arr[right_ptr] > pivot):
                right_ptr -= 1
            while (left_ptr < right_ptr and arr[left_ptr] <= pivot):
                left_ptr += 1
            if left_ptr < right_ptr:
                self.swap(arr, left_ptr, right_ptr)
        self.swap(arr, start, left_ptr)
        return left_ptr

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

if __name__ == '__main__':
    s = Solution()
    l = [1,4,2,3,7,834,134,525,123,78,12,65,27,12,8]
    k = 8
    print(s.getLeastNumbers(l,k))



