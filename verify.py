import hashlib
import requests
import os

# URL cru do seu main.py no GitHub
GITHUB_RAW_URL = 'https://raw.githubusercontent.com/fdvictorlima/controle_recepcao/refs/heads/main/main.py'
LOCAL_FILE = 'main.py'

def get_file_hash(content: bytes) -> str:
    """Retorna o hash SHA256 do conteúdo do arquivo."""
    return hashlib.sha256(content).hexdigest()

def download_remote_file(url: str) -> bytes:
    """Faz o download do arquivo remoto."""
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def read_local_file(path: str) -> bytes:
    """Lê o conteúdo do arquivo local."""
    if not os.path.exists(path):
        return b''
    with open(path, 'rb') as f:
        return f.read()

def main():
    try:
        remote_content = download_remote_file(GITHUB_RAW_URL)
        local_content = read_local_file(LOCAL_FILE)

        remote_hash = get_file_hash(remote_content)
        local_hash = get_file_hash(local_content)

        if remote_hash != local_hash:
            print("Versão remota é mais atual. Atualizando...")
            with open(LOCAL_FILE, 'wb') as f:
                f.write(remote_content)
            print("Atualização concluída.")
        else:
            print("main.py já está atualizado.")
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")

if __name__ == "__main__":
    main()
