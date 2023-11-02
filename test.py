with open("refreshToken", "r") as file:
    token = file.readline()
    print(token, type(token))