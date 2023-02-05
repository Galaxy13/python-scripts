import json
from datetime import datetime

def solve(log_cluster: list) -> str:
    log_list = []
    for log in sum(log_cluster, []):
        log_list.append(json.loads(log))
    return list(map(lambda log: '\t'.join([str(log['date']), str(log['message'])]), sorted(log_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'))))
