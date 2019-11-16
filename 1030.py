###################################
#   path에 대한 이해 
###################################

import os

filepath = 'd:/Projects/python_os/player.png'

#
print(">>> dirname : ")
print( os.path.dirname(filepath))

#
print(">>> filename : ")
print( os.path.basename(filepath))

#
print(">>> split name : ")
print( os.path.split(filepath))

# split extention(확장자 분리하기)
print(">>> split again name : ")
print( os.path.splitext(filepath))


