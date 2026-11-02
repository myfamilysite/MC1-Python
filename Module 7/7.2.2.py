try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print("File not found.")
    
finally:
    if 'file' in locals():
        file.close()
        print("File closed.")




