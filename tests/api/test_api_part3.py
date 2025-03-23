
import requests
import time
import pytest

BASE_URL = "https://demoqa.com"

# ✅ Nome de usuário dinâmico para cada execução
USER_PAYLOAD = {
    "userName": f"test_user_{int(time.time())}",
    "password": "Test@123"
}

BOOK_PAYLOAD = {
    "userId": "",
    "collectionOfIsbns": [{"isbn": "9781449325862"}]
}

def create_user():
    response = requests.post(f"{BASE_URL}/Account/v1/User", json=USER_PAYLOAD)
    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 201, f"Erro ao criar usuário: {response.text}"
    user_id = response.json().get("userID")
    BOOK_PAYLOAD["userId"] = user_id
    assert user_id is not None
    return user_id

def generate_token():
    response = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=USER_PAYLOAD)
    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 200, f"Erro ao gerar token: {response.text}"
    token = response.json().get("token")
    assert token is not None
    return token

def authorize_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=USER_PAYLOAD, headers=headers)
    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 200, f"Erro ao autorizar usuário: {response.text}"

def add_book(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=BOOK_PAYLOAD, headers=headers)
    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 201, f"Erro ao adicionar livro: {response.text}"

def get_books(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/BookStore/v1/Books", headers=headers)
    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 200, f"Erro ao obter livros: {response.text}"
    books = response.json().get("books", [])
    assert len(books) > 0, "Nenhum livro encontrado"
    return books

def update_book(token):
    headers = {"Authorization": f"Bearer {token}"}
    new_isbn = "9781491904244"
    payload = {
        "userId": BOOK_PAYLOAD["userId"],
        "isbn": new_isbn
    }
    response = requests.put(f"{BASE_URL}/BookStore/v1/Books/9781449325862", json=payload, headers=headers)
    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 200, f"Erro ao atualizar livro: {response.text}"

# ✅ Retry maior e tratamento de erro 502
def delete_book(token, retries=5):
    headers = {"Authorization": f"Bearer {token}"}
    isbn = "9781449325862"
    
    for attempt in range(retries):
        response = requests.delete(f"{BASE_URL}/BookStore/v1/Book?UserId={BOOK_PAYLOAD['userId']}&ISBN={isbn}", headers=headers)
        if response.status_code == 204:
            break
        if response.status_code == 502:
            print(f"Tentativa {attempt + 1}/5: Erro 502 - Aguardando 5 segundos para tentar novamente...")
            time.sleep(5)
        else:
            break

    if response.status_code == 502:
        pytest.skip("Servidor retornou 502 Bad Gateway")
    assert response.status_code == 204, f"Erro ao deletar livro: {response.text}"

# ✅ Teste de fluxo completo
def test_full_flow():
    user_id = create_user()
    time.sleep(1)
    token = generate_token()
    time.sleep(1)
    authorize_user(token)
    time.sleep(1)
    add_book(token)
    time.sleep(1)
    books = get_books(token)
    assert any(book["isbn"] == "9781449325862" for book in books), "Livro não encontrado após adição"
    time.sleep(1)
    update_book(token)
    time.sleep(1)
    delete_book(token)
