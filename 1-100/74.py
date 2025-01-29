class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rr = 0, len(matrix) - 1
        cl, cr = 0, (len(matrix[0]) * len(matrix)) - 1
        rsize = len(matrix[0])

        while cl <= cr:
            midc = (cl + cr) // 2
            midr = midc // rsize

            if matrix[midr][midc % rsize] == target:
                return True
            elif matrix[midr][midc % rsize] < target:
                cl = midc + 1
                rl = cl // rsize
            else:
                cr = midc - 1
                rr = cr // rsize
        return False