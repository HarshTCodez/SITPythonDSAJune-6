def tower_of_hanoi(n: int, src, dest, aux):
    if n == 0:
        return
    tower_of_hanoi(n - 1, src, aux, dest)
    print(f"Moving Disk {n} from {src} to {dest}")
    tower_of_hanoi(n - 1, aux, dest, src)


tower_of_hanoi(3, "A", "C", "B")
