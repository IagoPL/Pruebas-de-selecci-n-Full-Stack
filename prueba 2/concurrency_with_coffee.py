import threading

def print_phrase(phrase):
    """Función que imprime una frase sin salto de línea"""
    print(phrase, end='')

def concurrency_with_coffee():
    """
    Crea 5 threads que imprimen frases en orden sin saltos de línea,
    luego imprime una frase final al terminar.
    """
    print("- I'm tired, Bob!", end=' ')
    
    # Definir las frases que cada thread va a imprimir
    phrases = [
        "Do you know ",
        "that our bodies ",
        "are made of coffee? ",
        "-Try drinking ",
        "it! "
    ]
    
    # Crear los threads
    threads = []
    for phrase in phrases:
        thread = threading.Thread(target=print_phrase, args=(phrase,))
        threads.append(thread)
    
    # Iniciar los threads en el orden correcto
    for thread in threads:
        thread.start()

    # Esperar a que todos los threads terminen
    for thread in threads:
        thread.join()

    # Imprimir la frase final
    print("- You're right!")

if __name__ == "__main__":
    concurrency_with_coffee()
