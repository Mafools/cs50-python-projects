def main():
    B = input()
    print(convert(B))

def convert(B):
    B = B.replace(":)", "🙂").replace(":(", "🙁")
    return B

main()
