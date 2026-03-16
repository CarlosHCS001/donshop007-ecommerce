import pytest
from unittest.mock import patch, MagicMock
from routes.orders import calcular_frete

def test_calcular_frete_sudeste():
    """testa frete para SP sem chamar API real"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'uf': 'SP',
        'logradouro': 'Avenida Paulista',
        'bairro': 'Bela Vista',
        'localidade': 'São Paulo'
    }

    with patch('routes.orders.requests.get', return_value=mock_response):
        frete, dados = calcular_frete('00000000')

    assert frete == 15.00
    assert dados['uf'] == 'SP'
