def toh(n: int, src: str, dest: str, aux: str):
    if n == 0:
        return
    toh(n - 1, src, aux, dest)
    print(f"Moving disk {n} from {src} to {dest}")
    toh(n - 1, aux, dest, src)


toh(4, "A", "C", "B")
