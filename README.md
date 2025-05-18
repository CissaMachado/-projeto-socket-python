# 🎓 Projeto Socket Cliente/Servidor em Python

Projeto foi desenvolvido como atividade prática da disciplina de **Redes I**, com o objetivo de aplicar os conceitos de comunicação entre processos usando o **protocolo TCP** e a biblioteca `socket` do Python.

---

## 🧠 Objetivos

- Implementar um sistema básico de comunicação TCP.
- Estudar a estrutura de sockets em Python.
- Compreender o fluxo de envio e recebimento de dados entre cliente e servidor.

---

## ⚙️ Tecnologias utilizadas

- 🐍 Python 3.x  
- 🧱 Biblioteca padrão `socket`  
- 💻 Ambiente: Windows 10  

---

## 📊 Diagrama de Comunicação

```plaintext
 CLIENTE                          SERVIDOR
    |                                 |
    | -------- Conexão TCP -------->  |
    |                                 |
    | ---- Envia nome digitado ---->  |
    |                                 |
    | <---- Envia nome do servidor -- |
    |                                 |
    | -------- Fecha conexão -------- |
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/CissaMachado/-projeto-socket-python.git
cd -projeto-socket-python
```

### 2. Execute o servidor

Em um terminal, rode:

```bash
python servidor.py
```


### 3. Execute o cliente

Em outro terminal, rode:

```bash
python cliente.py
```


---

## 🧾 O que cada arquivo faz

### 🔹 `servidor.py`

- Cria um socket com protocolo TCP.  
- Define IP e porta para escutar conexões.  
- Aguarda conexão de um cliente.  
- Ao se conectar:
  - Recebe uma mensagem (nome) do cliente.
  - Exibe essa mensagem no terminal.
  - Solicita ao usuário (no terminal do servidor) que digite o nome do servidor.
  - Envia o nome de volta ao cliente.
  - Fecha a conexão.

### 🔹 `cliente.py`

- Cria um socket TCP.  
- Conecta-se ao servidor.  
- Solicita ao usuário que digite seu nome.  
- Envia o nome ao servidor.  
- Aguarda resposta (nome do servidor).  
- Exibe a resposta.  
- Fecha a conexão.

---

## 📌 Observações

- O IP usado é `127.0.0.1` (localhost), ideal para testes locais.
- A porta utilizada é `5000`, mas pode ser alterada nos dois arquivos, desde que mantenha a mesma nos dois lados.
- A comunicação é bidirecional: cliente → servidor e depois servidor → cliente.

---

## 📸📸📸

1. Cliente digitando nome  
2. Servidor exibindo nome recebido  
3. Diálogo completo mostrado em ambos os terminais


```markdown
![Cliente terminal](![image](https://github.com/user-attachments/assets/6dff50fa-55ae-4712-a7b9-4aaee66afb4c)
)
![Servidor terminal](![image](https://github.com/user-attachments/assets/eca5ef9a-3df5-436a-8b04-f8399bf48f10)
)
```

---

## 👩‍💻 Autora

Feito por **Cecília Machado**  e **Davi Antônio**  
📘 Projeto acadêmico para a disciplina de Redes I  
📅 Ano: 2025
