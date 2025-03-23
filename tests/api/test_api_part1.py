
import requests
import time

BASE_URL = "https://demoqa.com"

# ✅ Nome de usuário dinâmico para cada execução
USER_PAYLOAD = {
    "userName": f"test_user_{int(time.time())}",
    "password": "Test@123"
}

def test_create_user():
    response = requests.post(f"{BASE_URL}/Account/v1/User", json=USER_PAYLOAD)
    assert response.status_code == 201, f"Erro ao criar usuário: {response.text}"
    user_id = response.json().get("userID")
    assert user_id is not None

def test_generate_token():
    response = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=USER_PAYLOAD)
    assert response.status_code == 200, f"Erro ao gerar token: {response.text}"
    token = response.json().get("token")
    assert token is not None
    return token

def test_authorize_user():
    token = test_generate_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=USER_PAYLOAD, headers=headers)
    assert response.status_code == 200, f"Erro ao autorizar usuário: {response.text}"

def test_list_books():
    response = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert response.status_code == 200, f"Erro ao listar livros: {response.text}"
    books = response.json().get("books", [])
    assert len(books) > 0, "Nenhum livro disponível"

# ✅ Nome de usuário gerado dinamicamente para evitar conflito
def test_main():
    global USER_PAYLOAD
    USER_PAYLOAD = {
        "userName": f"test_user_{int(time.time())}",
        "password": "Test@123"
    }

    response = requests.post(f"{BASE_URL}/Account/v1/User", json=USER_PAYLOAD)
    assert response.status_code == 201, f"Erro ao criar usuário: {response.text}"
    
    token_response = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=USER_PAYLOAD)
    assert token_response.status_code == 200, f"Erro ao gerar token: {token_response.text}"
    token = token_response.json().get("token")
    
    headers = {"Authorization": f"Bearer {token}"}
    auth_response = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=USER_PAYLOAD, headers=headers)
    assert auth_response.status_code == 200, f"Erro ao autorizar usuário: {auth_response.text}"
    
    books_response = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert books_response.status_code == 200, f"Erro ao listar livros: {books_response.text}"
    books = books_response.json().get("books", [])
    assert len(books) > 0, "Nenhum livro disponível"
