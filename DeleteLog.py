import shutil
import R8_lib
res = R8_lib.InitLib()
shutil.rmtree('logs', ignore_errors=True)