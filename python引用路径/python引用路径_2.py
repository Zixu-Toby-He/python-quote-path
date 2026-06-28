import os
import sys
import numpy
def pause():
	print("")
	os.system("pause")

路径={}
python目录 = sys.exec_prefix
r"""
sys.exec_prefix = r"C:\ProgramData\Anaconda3"
"""
路径["python include路径"]=os.path.join(python目录,"include")
路径["python      库目录"]=os.path.join(python目录,"libs")
路径["numpy include路径"]=numpy.get_include()
print("")
for i in 路径:
	print(f"\t{i}\t\t\t{路径[i]}\n")

pause()

