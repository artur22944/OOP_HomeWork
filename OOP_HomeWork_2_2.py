import os


def sorted_files():
    files = ["1.txt", "2.txt", "3.txt"]
    sort_file = "sorted.txt"

    files_data = []
    for file in files:
        with open(os.path.join("sorted", file), "r", encoding="utf-8") as f:
            data = f.readlines()
            files_data.append((file, len(data), data))

    files_data = sorted(files_data, key=lambda x: x[1])

    with open(os.path.join("sorted", sort_file), "w", encoding="utf-8") as f:
        for file, data_len, data in files_data:
            f.write(f"{file}\n")
            f.write(f"{data_len}\n")
            f.writelines(data)
            f.write("\n")


sorted_files()
