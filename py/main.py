"""
COMP20008 Elements of Data Processing
2026 Semester 1
Assignment 1

Solution: main file

DO NOT CHANGE THIS FILE!
"""

import os
import sys


def verify_task1():
    try:
        from task1 import task1
    except ImportError as e:
        print("Task 1's function not found.")
        print("Error Text:")
        print(e)
        
        return

    print("=" * 80)
    print("Executing Task 1...\n")
    task1()

    # print("Checking Task 1.1's output...\n")
    print("Checking Task 1's output...\n")

    for expected_file in ["task1_squirrel.csv"]:
        if os.path.isfile(expected_file):
            print(f"\tTask 1's {expected_file} output found.\n")
            if os.path.getsize(expected_file) == 0:
                print(f"\t❗ Task 1's {expected_file} output has size zero - please verify it uploaded correctly.\n")
        else:
            print(f"\t❗ Task 1's {expected_file} output NOT found. Please check your code.\n")

    print("Finished Task 1")
    print("=" * 80)


def verify_task2():

    try:
        from task2 import task2
    except ImportError as e:
        print("Task 2's function not found.")
        print("Error Text:")
        print(e)
        return

    print("=" * 80)
    print("Executing Task 2...\n")
    task2()

    print("Checking Task 2's output...\n")

    for expected_file in ["task2_shift.png", "task2_eating.png"]:
        if os.path.isfile(expected_file):
            print(f"\tTask 2's {expected_file} output found.\n")
            if os.path.getsize(expected_file) == 0:
                print(f"\t❗ Task 2's {expected_file} output has size zero - please verify it uploaded correctly.\n")
        else:
            print(f"\t❗ Task 2's {expected_file} output NOT found. Please check your code.\n")

    print("Finished Task 2")
    print("=" * 80)

def verify_task3():

    try:
        from task3 import task3
    except ImportError as e:
        print("Task 3's function not found.")
        print("Error Text:")
        print(e)
        return

    print("=" * 80)
    print("Executing Task 3...\n")
    task3()

    print("Checking Task 3's output...\n")

    for expected_file in ["task3_days.png", "task3_wordpies.png", "task3_shifts.png"]:
        if os.path.isfile(expected_file):
            print(f"\tTask 3's {expected_file} output found.\n")
            if os.path.getsize(expected_file) == 0:
                print(f"\t❗ Task 3's {expected_file} output has size zero - please verify it uploaded correctly.\n")
        else:
            print(f"\t❗ Task 3's {expected_file} output NOT found. Please check your code.\n")

    print("Finished Task 3")
    print("=" * 80)

def verify_task4():

    try:
        from task4 import task4
    except ImportError as e:
        print("Task 4's function not found.")
        print("Error Text:")
        print(e)
        return

    print("=" * 80)
    print("Executing Task 4...\n")
    task4()

    print("Checking Task 4's output...\n")

    for expected_file in ["task4_elbow.png", "task4_elbow.png", "task4_scatter.png", "task4_density.png", "task4_cluster0.csv"]:
        if os.path.isfile(expected_file):
            print(f"\tTask 4's {expected_file} output found.\n")
            if os.path.getsize(expected_file) == 0:
                print(f"\t❗ Task 4's {expected_file} output has size zero - please verify it uploaded correctly.\n")
        else:
            print(f"\t❗ Task 4's {expected_file} output NOT found. Please check your code.\n")

    files_in_directory = [f for f in os.listdir("/home/") if "task4_cluster" in f and f[-4:] == ".csv"]
    print(f"Found {len(files_in_directory)} files that contained task4_clusterX.csv - {files_in_directory}")

    print("Finished Task 4")
    print("=" * 80)

def verify_task5():
    print("=" * 80)

    for expected_file in ["discussion_template.pdf"]:
        if os.path.isfile(expected_file):
            print(f"\tTask 5's {expected_file} output found.\n")
            if os.path.getsize(expected_file) == 0:
                print(f"\t❗ Task 5's {expected_file} output has size zero - please verify it uploaded correctly.\n")
        else:
            print(f"\t❗ Task 5's {expected_file} output NOT found. Please check you have uploaded the file and that it has the correct file type.\n")

    print("Finished Task 5")
    print("=" * 80)

def main():
    args = sys.argv
    assert len(args) >= 2, "Please provide a task."
    task = args[1]
    valid_tasks = ["all"] + ["task" + str(i) for i in range(1, 6)]
    assert task in valid_tasks, \
        f"Invalid task \"{task}\", options are: {valid_tasks}."
    if task == "task1":
        verify_task1()
    elif task == "task2":
        verify_task2()
    elif task == "task3":
        verify_task3()
    elif task == "task4":
        verify_task4()
    elif task == "task5":
        verify_task5()
    elif task == "all":
        verify_task1()
        verify_task2()
        verify_task3()
        verify_task4()
        verify_task5()

if __name__ == "__main__":
    main()

