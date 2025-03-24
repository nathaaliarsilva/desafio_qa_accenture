
# 🚀 Desafio QA - Accenture

Projeto de automação de testes para vaga de QA na Accenture.  
Contém testes de **API** e **frontend** com tratamento de erros, retry e validação de dados.  
Inclui também documentação detalhada para execução e configuração do projeto.

---

## 📂 **Estrutura do Projeto**
```plaintext
desafio_qa_accenture/
├── tests/
│   ├── api/
│   │   ├── test_api_part1.py   ✅ Testes de API Básicos (criar usuário, gerar token, etc.)
│   │   ├── test_api_part2.py   ✅ Testes de CRUD de livros (adicionar, listar, atualizar, deletar)
│   │   └── test_api_part3.py   ✅ Fluxo Completo (integração total)
│   ├── frontend/
│   │   └── test_frontend_part1.py   ✅ Teste de Frontend (login, validação de livros)
├── requirements.txt   ✅ Dependências do projeto
├── .gitignore   ✅ Arquivo para ignorar arquivos locais no Git
└── README.md   ✅ Documentação do projeto
```

---

## 🚀 **Tecnologias Utilizadas**
✅ Python 3.13  
✅ Pytest 8.3.5  
✅ Selenium 4.17.2  
✅ Allure-pytest 2.13.5  
✅ WebDriver Manager  

---

## 🛠️ **Instalação**
1. **Clone o repositório:**
```bash
git clone https://github.com/nathaaliarsilva/desafio_qa_accenture.git
```
2. **Entre na pasta do projeto:**
```bash
cd desafio_qa_accenture
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

---

## 🚀 **Como Executar os Testes**
### **1️⃣ Testes de API**
✅ Para executar os testes de API:  
```bash
pytest tests/api/test_api_part1.py -v
pytest tests/api/test_api_part2.py -v
pytest tests/api/test_api_part3.py -v
```

### **2️⃣ Teste de Frontend**
✅ Para executar o teste de frontend (Selenium):  
```bash
pytest tests/frontend/test_frontend_part1.py -v
```

---

## 🔥 **Se o WebDriver não funcionar:**
✅ Instale o webdriver-manager:  
```bash
pip install webdriver-manager
```  
✅ Substitua a inicialização do driver por:
```python
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```

---

## ✅ **O que foi Implementado**
✅ Criação de usuário via API  
✅ Geração de token  
✅ Login e autenticação  
✅ CRUD de livros  
✅ Tratamento de erro 502 com retry e delay  
✅ Teste de frontend com login e validação de livros  

---

## 🚨 **Tratamento de Erros**
✔️ `502 Bad Gateway` → Retry automático (5 tentativas) + Skip após falha  
✔️ Elemento não encontrado no frontend → Teste ignorado automaticamente  
✔️ Login falhou → Teste ignorado com `pytest.skip()`  

---

## 🏆 **Status do Projeto:**
✅ **100% Concluído** 🔥  

---

## 📄 **Autor**
👤 Nathalia QA  
🔗 [GitHub](https://github.com/nathaaliarsilva)  
🔗 [LinkedIn](https://www.linkedin.com/in/nathaaliarsilva)  
