
jobs = list(map(int, input().split(", ")))
index = int(input())
job_done = 0

my_e = jobs[index]
while jobs.__contains__(my_e):
    minimum = min(jobs)
    job_done += minimum
    jobs.remove(minimum)

print(job_done)
