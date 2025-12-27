#Xây dựng hàm giai thừa bằng đệ quy
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)