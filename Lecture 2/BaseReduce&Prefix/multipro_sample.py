import multiprocessing 
import time

def do_something(q):
    print("Sleeping for 1 second...")
    time.sleep(1)
    q.put("Done sleeping...") # Load giá trị trả về vào hàng đợi 

def main():
    start = time.perf_counter()
    #--------------- Main work ---------------
    processes = []
    queue = multiprocessing.Queue() # Hàng đợi store các giá trị trả về từ các process

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[queue])  # Chỉ cần pass tên hàm cần thực hiện vào argument "target", ko có ().
        processes.append(p)
        p.start()   # Mới chỉ lập lịch cho process, chưa thật sự chạy ngay lập tức -> Tiếp tục thực hiện các dòng bên dưới.

    for process in processes:
        process.join()  # Đảm bảo process hoàn tất trước khi tiếp tục thực hiện các dòng bên dưới.

    results = []    #  List trích các giá trị trả về từ các process từ hàng đợi
    while not queue.empty():
        results.append(queue.get())
    
    for result in results:
        print(result)
    #--------------- Main work ---------------
    end = time.perf_counter()
    print(f"Execution time: {end-start:.2f} second(s)")

if __name__ == "__main__":
    main()


