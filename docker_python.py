from rich import print

def main():
    data = [
        {
        f"key{i}": f"value{i}"
        } for i in range(20)
    ]
    print(data)


if __name__ == "__main__":
    main()