import time 
starttime = time.time()
time.sleep(0.2)
print("FPS:" + str( 1/(time.time() - starttime) ))