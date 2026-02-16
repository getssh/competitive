class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_val = float("inf")
        res = []

        for el in list1:
            if el in list2:
                if list1.index(el) + list2.index(el) < min_val:
                    min_val = list1.index(el) + list2.index(el)
                    res = []
                    res.append(el)
                elif list1.index(el) + list2.index(el) == min_val:
                    res.append(el)

        return res