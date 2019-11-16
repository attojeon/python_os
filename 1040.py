###################################
#   현재 디렉토리에 있는 이미지 파일 한 개를 복사하여 새로운 이름으로 저장하시오.
#   player.png => player_new.png
###################################

import os
import shutil # shell util

# 
cur_dir = os.getcwd()

filename = os.path.join(cur_dir, 'player.png')
b = os.path.exists(filename)

# 아래에 적절한 코드를 작성해서 새로운 파일이름으로 저장될 있게 하시오.
# 'player' + '_new' + '.png'와 같은 문자들을 합칠 수 있도록 코드와 함수를 작성해야 합니다.
# 직접 player_new.png와 같이 작성해서는 안됩니다.
# 코드 라인 수는 제한이 없습니다. 
new_filename = ''

if b == True:
    shutil.copy( filename, new_filename)