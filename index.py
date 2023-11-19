def main():
    all_actived = 0
    ranged = 0
    for i in range(1):
        n = 2
        actived = 0
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                for z in range(1, n + 1):
                    if x**2 + y**2 == z**2:
                        actived += 1
                        print(f"{x},{y},{z}")
        all_actived += actived
        ranged += 1
    sub_actived = all_actived/ranged
    print(f"1부터 {n}까지의 모든 수에 대응하는 피타고라스의 수 배열 개수 : {sub_actived}개")
def index():
    b = 200
    n = 0
    for i in range(b):
        all_actived = 0
        ranged = 0
        n += 1
        for i in range(1):
            actived = 0
            for x in range(1, n + 1):
                for y in range(1, n + 1):
                    for z in range(1, n + 1):
                        if x**2 + y**2 == z**2:
                            actived += 1
        all_actived += actived
        ranged += 1
        sub_actived = all_actived/ranged
        if n<sub_actived:
            print(f"{n}, {sub_actived}")
        else:
            print(f"{n}, {sub_actived}")
if __name__ == '__main__':
    index()