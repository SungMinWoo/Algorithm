from collections import defaultdict, Counter

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = []
report_count = []
report = set(report)
report_list = [reports.split() for reports in report]

report_dict = defaultdict(list)
for id in id_list:
    for reports in report_list:
        if id == reports[0]:
            report_dict[reports[0]].append(reports[1]) # 이름별로 모으기
    report_count += report_dict[id]

report_id_list = [key for key, value in Counter(report_count).items() if value >= k] # 신고당한 유저

for key, value in report_dict.items():
    answer.append(len(set(value) & set(report_id_list)))

print(answer)


