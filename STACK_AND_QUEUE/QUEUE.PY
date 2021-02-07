if __name__ == '__main__':
    from collections import deque
    queue=deque()
    # TO INSERT ELEMENT IN QUEUE
    for i in range(1,6):
        queue.append(i)
    # FOR DELETE ELEMENT IN QUEUE   
    queue.popleft()

    for i in queue:
        print(i)