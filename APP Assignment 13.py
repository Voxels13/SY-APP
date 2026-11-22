import threading
import time

def count_numbers():
    for i in range(1, 6):
        print("Count:", i)
        time.sleep(1)

def calculate_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i**2)
        time.sleep(1)

def calculate_cubes():
    for i in range(1, 6):
        print("Cube of", i, "=", i**3)
        time.sleep(1)

if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=count_numbers)
    t2 = threading.Thread(target=calculate_squares)
    t3 = threading.Thread(target=calculate_cubes)

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()

    print("All threads finished")