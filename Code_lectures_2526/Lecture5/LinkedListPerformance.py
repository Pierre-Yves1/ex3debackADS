from LinkedList import LinkedList
import time
# om verschillen in performance tss gewone en gelinkte lijst te tonen
startTime = time.time()
list = LinkedList()
for i in range(100000): ## insert vooraan in een gelinkte list
    list.insert(0, "Chicago")
elapsedTime = time.time() - startTime
print("Time for LinkedList is", elapsedTime, "seconds")

startTime = time.time()
list = []  ##inset voorraan in een gewone lijst
for i in range(100000):
    list.insert(0, "Chicago")
elapsedTime = time.time() - startTime
print("Time for list is", elapsedTime, "seconds")
