import nmap
import json
from datetime import datetime

def generar_evidencia():
    nm = nmap.PortScanner()
    target = '127.0.0.1'
    print(f"[*] Escaneando objetivos en {target}...")
    
    # Escaneamos el puerto 3000 que ya tienes activo
    nm.scan(target, '3000')
    
    evidencia = {
        "proyecto": "Sentinel Lab",
        "fase": "Reconocimiento Inicial",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "host": target,
        "estado": nm[target].state(),
        "puertos_abiertos": list(nm[target]['tcp'].keys())
    }

    with open('evidencia_recon.json', 'w') as f:
        json.dump(evidencia, f, indent=4)
    print("[+] Archivo 'evidencia_recon.json' generado con éxito.")

if __name__ == "__main__":
    generar_evidencia()
