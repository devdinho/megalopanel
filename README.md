# Megalopanel

Megalopanel é um painel de monitoramento do sistema que coleta informações em tempo real sobre o uso da CPU, memória, disco e rede de uma máquina. Ele usa Flask e Flask-SocketIO para transmitir essas informações para os clientes conectados via WebSocket. O painel é projetado para exibir esses dados de forma interativa em tempo real.

## Funcionalidades

- **Monitoramento em tempo real**: Coleta informações sobre a utilização da CPU, memória, disco e rede.
- **WebSocket**: Usa Flask-SocketIO para emitir informações em tempo real para todos os clientes conectados.
- **Execução em segundo plano**: Emite as informações periodicamente (a cada 5 segundos).

## Requisitos

- Python 3.6 ou superior
- Flask
- Flask-SocketIO
- psutil

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/devdinho/megalopanel.git
   cd megalopanel
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. Execute o aplicativo Flask:

   ```bash
   python main.py
   ```

2. O servidor estará rodando em `http://127.0.0.1:5000`.

3. Conecte-se ao painel usando um navegador. As informações do sistema serão atualizadas em tempo real.

## Arquitetura

- **Flask**: Framework web para o servidor.
- **Flask-SocketIO**: Usado para comunicação em tempo real via WebSocket.
- **psutil**: Biblioteca para coletar informações sobre o sistema.
- **JSON**: Formato utilizado para a troca de dados entre o servidor e os clientes.

## Exemplo de Evento

O servidor envia periodicamente informações como o uso de CPU, memória e disco, conforme mostrado abaixo:

```json
{
    "cpu_usage_percent": 45.3,
    "memory_total": 8589934592,
    "memory_available": 4294967296,
    "memory_percent": 50.1,
    "disk_total": 250000000000,
    "disk_used": 150000000000,
    "disk_percent": 60.1,
    "network_sent": 1048576,
    "network_recv": 2097152
}
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções de bugs. Para contribuir:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça as alterações desejadas.
4. Envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).