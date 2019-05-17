import time
from BinarySearchTree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
namebst1 = None
namebst2 = None

for name_1 in names_1:
    if not namebst1:
        namebst1 = BinarySearchTree(name_1)
    else:
        namebst1.insert(name_1)

for name_2 in names_2:
    if not namebst2:
        namebst2 = BinarySearchTree(name_2)
    else:
        namebst2.insert(name_2)

counter = []
def checkdupes(subject, checker):
    if subject.contains(checker.value):
        duplicates.append(checker.value)
    if checker.left:
        checkdupes(subject, checker.left)
    if checker.right:
        checkdupes(subject, checker.right)


checkdupes(namebst2, namebst1)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

