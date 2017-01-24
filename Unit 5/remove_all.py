original = [1,2,1,3,5,1]
target = 1
def remove_all(original, target):
    while target in original:
        original.remove(target)
print(original)
remove_all(original,target)
print(original)