import sys
import random

if len(sys.argv) !=3:
    print("Argumens 2개 확인   [원본파일] [변환파일]")
    sys.exit()

orgFile = sys.argv[1]
rndFile = sys.argv[2]

print (orgFile)
print (rndFile)
# , encoding='UTF8' , encoding='CP949'
fid = open(orgFile,'r', encoding='UTF8')
li = fid.readlines()
fid.close()

print(li)
random.shuffle(li)
print(li)

# , encoding='UTF8' , encoding='CP949'
fid = open(rndFile,'w', encoding='UTF8')
fid.writelines(li)
fid.close()

outStr = f'파일 내용을 Random 으로 섞음 [ {orgFile} -> {rndFile} ]'

print(outStr)
