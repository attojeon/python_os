###################################
#   1. 현재 작업 중인 디렉토리의 전체 path 출력하기
#   2. 현재 디렉토리에 있는 모든 파일(디렉토리 포함) 출력하기
###################################

import os


# 아래 두 출력을 비교해서 그 차이를 정확히 이해하고 설명해 보시오.
cwd = os.getcwd()
all = os.listdir( cwd )

for f in all:
    fullpath = os.path.join(cwd, f)
    if os.path.isfile(fullpath):
        print("{} {}".format(fullpath, os.path.getsize(fullpath)))
    elif os.path.isdir(fullpath):
        print("{}/".format(fullpath))

