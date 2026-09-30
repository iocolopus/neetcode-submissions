class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        heights = [0] + heights + [0]

        s_dic = [] # Stack monotonico ascendente estricto
        s_inv = [] # Stack monotonico ascendete estricto

        nb_d = [0] * len(heights)
        nb_i = [0] * len(heights)

        sol = []

        for i in range(len(heights)):

            while s_dic and heights[s_dic[-1]] > heights[i]: # No se cumple la condicion desdendente
                p = s_dic.pop() # heights[i] es siguiente mas grande por la derecha de p
                nb_d[p] = (i - p) - 1
            s_dic.append(i)

            while s_inv and heights[-(s_inv[-1] + 1)] > heights[-(i + 1)]:
                p = s_inv.pop() # heights[i] es iguiente mas grande por la derecha de
                nb_i[-(p + 1)] = (i - p) - 1
            s_inv.append(i)

        for i, (n_d, n_i) in enumerate(zip(nb_d, nb_i)):
            sol.append((n_d + n_i + 1) * heights[i])

        return max(sol)