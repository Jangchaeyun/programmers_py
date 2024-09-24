def solution(n, t, m, timetable):
    answer = 0
    crewTime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    busTime = [9*60 + t*i for i in range(n)]

    i = 0
    for tm in busTime:
      cnt = 0
      while cnt < m and i < len(crewTime) and crewTime[i] <= tm:
        i += 1
        cnt += 1
      if cnt < m: answer = tm
      else: answer = crewTime[i - 1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)