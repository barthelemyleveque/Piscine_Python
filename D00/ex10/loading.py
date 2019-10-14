import time

def ft_progress(liste):
    length = len(liste)
    start_time = time.time()
    for i in liste:
        print("ETA : %.2fs [%3d%%] [% -21s] %4d/%4d | elapsed time %.2fs" % (10 -(time.time() - start_time), i/length*100, str(int( 20 * i/length) * "=" + ">"), i, length, (time.time() - start_time)), end="\r")
        yield i

liste = range(1000)
for elem in ft_progress(liste):
    time.sleep(0.01)