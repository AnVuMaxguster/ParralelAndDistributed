import multiprocessing

# Hàm tính tổng của một phần của dãy số
def tinh_tong(arr, result, lock):
    tong = sum(arr)
    with lock:
        result.value += tong

if __name__ == "__main__":
    # Dãy số cần tính tổng
    numbers = list(range(1, 6))  

    # Số tiến trình song song
    num_processes = 2

    # Tạo một biến chia sẻ để lưu tổng
    result = multiprocessing.Value("i", 0)

    # Tạo khóa để đồng bộ hóa truy cập vào biến kết quả
    lock = multiprocessing.Lock()

    # Chia dãy số thành các phần bằng nhau cho mỗi tiến trình
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Tạo các tiến trình
    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=tinh_tong, args=(chunk, result, lock))
        processes.append(process)

    # Khởi động các tiến trình
    for process in processes:
        process.start()

    # Chờ tất cả các tiến trình hoàn thành
    for process in processes:
        process.join()

    # In tổng kết quả
    print("Tổng của dãy số là:", result.value)
