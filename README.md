# Rootkit Educacional - Prova de Conceito

<p align="center">
  <a href="https://github.com/cesarneves-security/rootkit.git"><img src="/img/1.png" alt="ROOTKIT"></a>
  <a href="https://github.com/cesarneves-security/rootkit.git"><img src="/img/2.png" alt="ROOTKIT"></a>
  <a href="https://github.com/cesarneves-security/rootkit.git"><img src="/img/3.png" alt="ROOTKIT"></a>
</p>

Este projeto é um **rootkit educacional** desenvolvido com o objetivo de explorar e estudar técnicas de ocultação de processos, arquivos, conexões, drivers e manipulação de logs. **Não deve ser utilizado para fins maliciosos** e é destinado apenas para **fins éticos e educacionais**.

## Funcionalidades

- **Ocultação de Processos**: Permite ocultar processos específicos do sistema.
- **Ocultação de Arquivos**: Renomeia arquivos utilizando uma técnica de obfuscação, tornando-os invisíveis.
- **Ocultação de Conexões**: Esconde conexões de rede com base no IP e porta.
- **Ocultação de Drivers**: Permite ocultar drivers específicos.
- **Manipulação de Logs**: Remove seletivamente entradas de log que contenham informações sobre o rootkit.
- **Interceptação de Syscalls**: Monitora processos ativos e simula a interceptação de chamadas de sistema (syscalls).
- **Detecção de Anti-rootkits**: Identifica a presença de ferramentas anti-rootkit e encerra a execução para evitar detecção.
- **Verificação de Itens Ocultos**: Lista todos os processos, arquivos, conexões e drivers ocultados para fins de verificação.

## Como usar

### Requisitos

- **Python 3**
- **Biblioteca psutil** (`pip install psutil`)

### Instalação

1. Clone o repositório:
```bash
https://github.com/cesarneves-security/rootkit.git
```
2. Navegue até o diretório do projeto:
```bash
cd rootkit
```
3. Instalação da ferramenta:
```bash
python3 rootkit.py
```

### Comandos disponíveis:

- **Ocultar Processo**:
  ```bash
  hide_process <nome_do_processo>
    - hide_process firefox
  ```

- **Ocultar Arquivo**:
  ```bash
  hide_file <caminho_do_arquivo>
    - hide_file /home/user/documento.txt
  ```

- **Ocultar Conexão**:
  ```bash
  hide_connection <ip:porta>
    - hide_connection 192.168.0.10:8080
  ```

- **Ocultar Driver**:
  ```bash
  hide_driver <nome_do_driver>
    - hide_driver usb_storage
  ```
- **Mostrar Itens Ocultos**:
  ```bash
  show_hidden
  ```

- **Manipular Logs**:
  ```bash
  manipulate_logs
  ```

- **Interceptar Syscalls**:
  ```bash
  intercept_syscalls
  ```

- **Verificar Itens Ocultos**:
  ```bash
  verify
  ```

- **Detectar Anti-rootkits**:
  ```bash
  detect_anti_rootkit
  ```

- **sair**:
  ```bash
  exit
  ```
### Contribuição
Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request
