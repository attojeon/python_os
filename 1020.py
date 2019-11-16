###################################
#   현재 작업 중인 디렉토리에 있는 모든 파일과 디렉토리 목록을 한줄씩 출력하기
###################################

import os

# get_current_working_directory(현재 작업 디렉토리 구하기)
cur_dir = os.getcwd()
all = os.walk(cur_dir).__next__()

# 다음의 출력을 보고 all이 포함하는 것을 잘 이해해야 합니다. 
print(all)

# 현재 디렉토리 출력
print(">>> current path : {}".format(all[0]))

# 디렉토리 출력
for d in all[1]:
    print("{}/ ".format(d))

# 파일 출력
for f in all[2]:
    print("{}".format(f))


