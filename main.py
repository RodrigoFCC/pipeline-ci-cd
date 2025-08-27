from datetime import datetime

def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("output.txt", "w") as file:
        file.write(f"Última execução: {current_time}")
    
    print("Arquivo gerado com sucesso!")

if __name__ == "__main__":
    main()