import sys

disk_space, number_of_users = list(map(int, sys.stdin.readline().rstrip('\n').split()))
user_data = []
for _ in range(number_of_users):
    user_data_size = int(sys.stdin.readline().rstrip('\n'))
    if user_data_size <= disk_space:
        user_data.append(user_data_size)
user_data.sort()
user_stored_counter = 0
for udata_size in user_data:
    if disk_space - udata_size >= 0:
        user_stored_counter += 1
        disk_space -= udata_size
    else:
        break
print(user_stored_counter)