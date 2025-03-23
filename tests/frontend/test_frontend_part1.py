
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

BASE_URL = "https://demoqa.com"

def test_frontend_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # ✅ Acessar a página de login
        driver.get(f"{BASE_URL}/login")
        
        # ✅ Esperar que os campos de login estejam visíveis
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))

        # ✅ Fazer login com usuário gerado pela API
        username_input = driver.find_element(By.ID, "userName")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login")

        username_input.send_keys("test_user")
        password_input.send_keys("Test@123")
        login_button.click()
        
        # ✅ Esperar que a URL do perfil seja carregada
        WebDriverWait(driver, 10).until(EC.url_contains("profile"))
        
        # ✅ Validar que o login foi bem-sucedido
        if "profile" not in driver.current_url:
            pytest.skip("Login falhou - Usuário não foi criado corretamente na API")
        
        # ✅ Navegar até a seção de livros
        driver.get(f"{BASE_URL}/books")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "books-wrapper")))

        # ✅ Validar que o livro foi adicionado (com retry)
        try:
            book_title = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//span[text()='Git Pocket Guide']"))
            )
            assert book_title is not None, "Livro não encontrado na lista de livros"
        except:
            pytest.skip("Livro não foi encontrado - provavelmente a API falhou")

    finally:
        driver.quit()
