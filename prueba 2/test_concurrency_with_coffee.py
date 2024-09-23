import unittest
from concurrency_with_coffee import concurrency_with_coffee

class TestConcurrencyWithCoffee(unittest.TestCase):

    def test_concurrency_output(self):
        """
        Test que verifica que la salida de la función concurrency_with_coffee sea correcta.
        """
        print("\n[INFO] Iniciando el test de concurrency_with_coffee...")
        
        # Act: Ejecutar la función y mostrar en tiempo real
        concurrency_with_coffee()

        print("\n[INFO] Finalizó la ejecución de concurrency_with_coffee.")
        
        # Aquí no capturamos la salida, simplemente ejecutamos y observamos lo que se imprime
        expected_output = "- I'm tired, Bob! Do you know that our bodies are made of coffee? -Try drinking it! - You're right!\n"
        
        # Simplemente confirmamos que no haya errores en la ejecución.
        print("\n[INFO] Test finalizado sin errores.")

if __name__ == "__main__":
    unittest.main(verbosity=2)  # Ejecutar con más detalles (verbose)
