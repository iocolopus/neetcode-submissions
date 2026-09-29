class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m_stack = []
        sol = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while m_stack and temperatures[m_stack[-1]] < t:
                p = m_stack.pop()
                sol[p] = i - p
            m_stack.append(i)

        return sol