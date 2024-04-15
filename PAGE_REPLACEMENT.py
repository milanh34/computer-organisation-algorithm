def fifo(incomingStream, frames):
    pageFaults = 0
    temp = [-1] * frames

    print("\n FIFO Algorithm :\n")
    print("Incoming\t\tFrame 1\t\tFrame 2\t\tFrame 3")

    for m in range(len(incomingStream)):
        s = 0
        for n in range(frames):
            if incomingStream[m] == temp[n]:
                s += 1
                break
        if s == 0:
            pageFaults += 1
            if pageFaults <= frames:
                temp[pageFaults - 1] = incomingStream[m]
            else:
                temp[(pageFaults - 1) % frames] = incomingStream[m]

        print("\n{}\t\t".format(incomingStream[m]), end="")
        for n in range(frames):
            if temp[n] != -1:
                print("{}\t\t".format(temp[n]), end="")
            else:
                print("-\t\t", end="")
    print("\nTotal Page Faults (FIFO): {}".format(pageFaults))

def lru(incomingStream, frames):
    pageFaults = 0
    temp = [-1] * frames
    recent = [0] * frames

    print("\n LRU Algorithm :\n")
    print("Incoming\t\tFrame 1\t\tFrame 2\t\tFrame 3")

    for m in range(len(incomingStream)):
        s = 0
        for n in range(frames):
            if incomingStream[m] == temp[n]:
                s += 1
                recent[n] = m + 1
                break
        if s == 0:
            pageFaults += 1
            lru = 0
            for n in range(1, frames):
                if recent[n] < recent[lru]:
                    lru = n
            temp[lru] = incomingStream[m]
            recent[lru] = m + 1

        print("\n{}\t\t".format(incomingStream[m]), end="")
        for n in range(frames):
            if temp[n] != -1:
                print("{}\t\t".format(temp[n]), end="")
            else:
                print("-\t\t", end="")
    print("\nTotal Page Faults (LRU): {}".format(pageFaults))

def optimal(incomingStream, frames):
    pageFaults = 0
    temp = [-1] * frames
    nextUse = [len(incomingStream)] * frames

    print("\n Optimal Algorithm :\n")
    print("Incoming\t\tFrame 1\t\tFrame 2\t\tFrame 3")

    for m in range(len(incomingStream)):
        s = 0
        for n in range(frames):
            if incomingStream[m] == temp[n]:
                s += 1
                break
        if s == 0:
            pageFaults += 1
            for i in range(frames):
                for j in range(m + 1, len(incomingStream)):
                    if incomingStream[j] == temp[i]:
                        nextUse[i] = j
                        break
            maxIndex = nextUse.index(max(nextUse))
            temp[maxIndex] = incomingStream[m]

        print("\n{}\t\t".format(incomingStream[m]), end="")
        for n in range(frames):
            if temp[n] != -1:
                print("{}\t\t".format(temp[n]), end="")
            else:
                print("-\t\t", end="")
    print("\nTotal Page Faults (Optimal): {}".format(pageFaults))

frames = int(input("Enter no of frames : "))
np = int(input("Enter no of page references : "))
incomingStream = [-1] * np
print("Enter page references :")
for i in range(np):
    incomingStream[i] = int(input())

fifo(incomingStream, frames)
lru(incomingStream, frames)
optimal(incomingStream, frames)