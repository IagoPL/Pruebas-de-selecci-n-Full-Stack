import unittest
from unittest.mock import patch
import requests
from api_data import get_api_data

class TestGetAPIData(unittest.TestCase):

    def test_api_test1(self):
        # Arrange
        url_1 = "https://invelonjobinterview.herokuapp.com/api/test1"
        expected_output_1 = [
            ('name', 'Raul'),
            ('email', 'test@test.com'),
            ('preferences', [1, 3, 7]),
            ('affiliate', True)
        ]
        
        # Act
        result = get_api_data(url_1)
        print("\nTest 1 - URL:", url_1)
        print("Resultado obtenido:", result)
        print("Resultado esperado:", expected_output_1)

        # Assert
        self.assertIsInstance(result, list, "El resultado debe ser una lista")
        self.assertTrue(all(isinstance(item, tuple) for item in result), "Cada elemento de la lista debe ser una tupla")
        self.assertEqual(result, expected_output_1, "El resultado de la API 1 no es el esperado")

    def test_api_test2(self):
        # Arrange
        url_2 = "https://invelonjobinterview.herokuapp.com/api/test2"
        expected_output_2 = [
            ('users', [
                {'name': 'Raul', 'email': 'test@test.com', 'preferences': [1, 3, 7], 'affiliate': True},
                {'name': 'Marino', 'email': 'test2@test.com', 'preferences': [2, 5], 'affiliate': False}
            ])
        ]
        
        # Act
        result = get_api_data(url_2)
        print("\nTest 2 - URL:", url_2)
        print("Resultado obtenido:", result)
        print("Resultado esperado:", expected_output_2)

        # Assert
        self.assertIsInstance(result, list, "El resultado debe ser una lista")
        self.assertTrue(all(isinstance(item, tuple) for item in result), "Cada elemento de la lista debe ser una tupla")
        self.assertEqual(result, expected_output_2, "El resultado de la API 2 no es el esperado")

    @patch('api_data.requests.get')
    def test_api_connection_error(self, mock_get):
        # Simular un error de conexión
        mock_get.side_effect = requests.exceptions.ConnectionError("Error de conexión")
        
        # Act
        result = get_api_data("https://invelonjobinterview.herokuapp.com/api/test1")
        
        # Assert
        self.assertEqual(result, [], "Si ocurre un error de conexión, debe retornar una lista vacía")
        print("\nTest - Error de conexión: Lista vacía")

    @patch('api_data.requests.get')
    def test_api_invalid_json(self, mock_get):
        # Simular una respuesta con JSON inválido
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.side_effect = ValueError("JSON inválido")
        
        # Act
        result = get_api_data("https://invelonjobinterview.herokuapp.com/api/test1")
        
        # Assert
        self.assertEqual(result, [], "Si el JSON es inválido, debe retornar una lista vacía")
        print("\nTest - JSON inválido: Lista vacía")
    
if __name__ == "__main__":
    unittest.main()