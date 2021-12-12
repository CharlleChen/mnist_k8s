import time, requests, threading
import os

NUM_THREADS = int(os.getenv('NUM_THREADS'))
NUM_REQUESTS = int(os.getenv('NUM_REQUESTS'))

INTERNAL_IP = True

if INTERNAL_IP: 
    url = 'http://' + os.environ['INFER_MNIST_END_SERVICE_PORT'] + ':' + os.environ['INFER_MNIST_END_SERVICE_PORT'] + '/inference'
else: 
    # print('No external ip set')
    # exit(1)
    url = 'http://35.238.215.58:5000/inference'
    NUM_THREADS = 100
    NUM_REQUESTS = 10


threads_lst = []


def html_post(thread_time):
    thread_time.start = time.time()
    files = {'image': open('test.png', 'rb')}
    for i in range(NUM_REQUESTS):
        res = requests.post(url, files=files)
        # ********* For Debug purpose only ********* # 
        # print(f"res->{res}")
        # res_test = requests.get(url)
        # print(f"res_test->{res_test}")
        # ********* For Debug purpose only ********* # 
    thread_time.end = time.time()
    thread_time.total = thread_time.end - thread_time.start
    target_string = f"{thread_time.total} seconds from thread {threading.current_thread().ident}.\n"
    print(target_string)


thread_time = threading.local()

for i in range(NUM_THREADS):
    t = threading.Thread(target=html_post, args=(thread_time,))
    t.start()
    threads_lst.append(t)

for t_ind in threads_lst:
    t_ind.join()



