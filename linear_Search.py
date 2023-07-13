lst = list(map(int, input().split()))
src_Element= int(input())
def linear_Search(lst, src_Element):
      c = 0
      for ele in lst:
        if ele == src_Element:
            c += 1
      return c
print(linear_Search([1, 2, 2], 2))
print(linear_Search([1, 2, 1], 3))
print(linear_Search(lst, src_Element))
