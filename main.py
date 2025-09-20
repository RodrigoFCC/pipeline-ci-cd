from datetime import datetime

def generate_output():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_content = f"Última execução: {current_time}"
    
    with open("output.txt", "w") as file:
        file.write(output_content)
    
    return output_content

def main():
    result = generate_output()
    print("Arquivo gerado com sucesso!")
    print(f"Conteúdo: {result}")
    return result

if __name__ == "__main__":
    main()