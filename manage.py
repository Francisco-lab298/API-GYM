import os
import sys

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "start"

    if command == "start":
        os.system("python src/server.py")
    elif command == "dev":
        os.system("watchmedo auto-restart --pattern='*.py' --recursive -- python src/server.py")
    else:
        print("Comando não reconhecido. Use: start | dev")
# Comando para iniciar o servidor Flask ou rodar em modo de desenvolvimento com auto-reload