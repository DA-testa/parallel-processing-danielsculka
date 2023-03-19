# python3
# Dāniels Čulka 221RDB304

class Thread:
  def __init__(self, ix, jobTime):
    self.ix = ix
    self.jobTime = jobTime


def parallel_processing(threadCount, jobCount, jobs):
    output = []

    threads = [Thread(i, 0) for i in range(threadCount)]

    for job in jobs:
        min_thread = min(threads, key=lambda t: t.jobTime)

        output.append((min_thread.ix, min_thread.jobTime))

        min_thread.jobTime += job

    return output

def main():
    counts = list(map(int, input().split()))

    if len(counts) != 2:
        return

    threadCount = counts[0]
    jobCount = counts[1]

    data = list(map(int, input().split()))

    assert len(data) == jobCount

    result = parallel_processing(threadCount, jobCount, data)

    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
