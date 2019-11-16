###################################
#   1. 현재 작업 중인 디렉토리의 전체 path 출력하기
#   2. 현재 디렉토리 아래의 mnist 디렉토리에 있는 모든 파일(디렉토리 포함) 출력하기
###################################

import os
import sys

dataset_path = os.path.join(os.getcwd(), 'dataset')
print(dataset_path)

# 아래 두 출력을 비교해서 그 차이를 정확히 이해하고 설명해 보시오.
print(os.walk(dataset_path))
print(os.walk(dataset_path).__next__()[1])

classes = os.walk(dataset_path).__next__()[1]

for c in classes:
    c_dir = os.path.join(dataset_path, c)
    images = os.walk(c_dir).__next__()[2]
    print(c)
    print(images)
