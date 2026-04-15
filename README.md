# Sentinel-Lab---Fase-de-Reconocimiento
Simular ataques OWASP Top 10 y Escalada de Privilegios para validar reglas en el SIEM.

STATUS: ACTIVE

    🛡️ Infraestructura desplegada con Docker (Juice Shop activo).

    🔍 Reconocimiento automatizado con Framework Python (Nmap).

    📂 Reporte generado: evidencia_recon.json.

 
    Lograda la integración de agentes locales con un cluster de Wazuh en Docker, 
    permitiendo la detección de escaneos de red (Nmap) ejecutados mediante scripts personalizados en Python".

🚀 Guía de Instalación y Despliegue

Sigue estos pasos para replicar el entorno de Sentinel Lab en tu máquina local.
1. Requisitos Previos

    Docker & Docker Compose instalados.

    Python 3.10+ y Nmap instalados en el sistema.

    Git para clonar el repositorio.

2. Configuración del SIEM (Wazuh) 🛡️

Este módulo despliega la infraestructura de monitoreo mediante contenedores.

    Navega a la carpeta del SIEM:
    Bash

   - cd Sentinel-Lab---Fase-de-Reconocimiento/SIEM/screentshots/wazuh-docker/single-node

    Generar certificados (Paso Crítico):
    Bash

    -sudo docker-compose -f generate-indexer-certs.yml run --rm generator

    Levantar la infraestructura:
    Bash

   - sudo docker-compose up -d

    Acceder al Dashboard: * URL: https://localhost

        Credenciales: User: admin / Pass: SecretPassword.

3. Configuración del Agente de Monitoreo 👁️

Para que el SIEM detecte los ataques realizados desde tu PC, debes vincularla como agente:

    En el Dashboard de Wazuh, selecciona "Add agent".

    Selecciona el SO Linux (DEB amd64).

    En "Server address", ingresa la IP: 127.0.0.1.

   - Ejecuta el comando de instalación generado en tu terminal.

    Inicia el servicio:
    Bash

   - sudo systemctl start wazuh-agent

4. Ejecución de la Fase Ofensiva (Python) 🐍

Simulación de escaneo de vulnerabilidades para validar las reglas de detección:

    Navega a la carpeta de reconocimiento:
    Bash

    cd ../../../recon/sentinel\ lab

    Activa el entorno virtual:
    Bash

    source venv/bin/activate

    Ejecuta el escaneo:
    Bash

    python3 ataque_recon.py
        
🛠️ Guía de Resolución de Problemas (Troubleshooting)

Durante el despliegue de este laboratorio, se identificaron y resolvieron los siguientes retos técnicos críticos:
1. Conflicto de Montaje en Docker (Error: "Not a directory")

    Problema: Al intentar levantar el servicio wazuh.indexer, Docker reportaba un error de montaje indicando que el archivo de certificado admin-key.pem era tratado como un directorio.

    Causa: Intentar ejecutar docker-compose up antes de generar los certificados SSL provocaba que Docker creara carpetas vacías con los nombres de los archivos esperados.

    Solución: 1. Detener servicios y limpiar volúmenes: sudo docker-compose down -v.
    2. Eliminar carpetas de configuración corruptas: sudo rm -rf config/wazuh_indexer_ssl_certs.
    3. Generar certificados legítimos: sudo docker-compose -f generate-indexer-certs.yml run --rm generator.
    4. Reiniciar el despliegue: sudo docker-compose up -d.

2. Entorno de Python Protegido (PEP 668)

    Problema: Error externally-managed-environment al intentar instalar python-nmap mediante pip.

    Causa: Restricciones de seguridad en versiones modernas de Linux para proteger las librerías del sistema.

    Solución: Uso de entornos virtuales para aislar las dependencias del script de ataque:

        Activar el entorno: source venv/bin/activate.

        Instalar dependencias dentro del entorno: pip install python-nmap.

3. Visibilidad de Agentes en el SIEM

    Problema: El Dashboard de Wazuh mostraba "0 agentes", imposibilitando la detección de los ataques de reconocimiento.

    Causa: El Manager de Wazuh estaba operativo, pero no tenía agentes instalados en los endpoints para recolectar telemetría.

    Solución: Despliegue manual del agente de Wazuh en el host local configurando la dirección 127.0.0.1 y verificando el estado del servicio con sudo systemctl status wazuh-agent.


   🎯 Conclusión Técnica y Resultados

El Sentinel Lab ha demostrado con éxito la integración de capacidades ofensivas y defensivas en un entorno controlado. Los resultados clave incluyen:

    Detección Efectiva: Se logró una visibilidad del 100% sobre los escaneos de reconocimiento realizados con el script personalizado de Python, categorizando las alertas bajo el framework de MITRE ATT&CK.

    Orquestación Robusta: El uso de Docker para el despliegue del stack de Wazuh garantiza una infraestructura escalable, persistente y fácil de replicar en entornos de producción.

    Gestión de Agentes: La implementación exitosa del agente local permitió la correlación de eventos del sistema operativo con el análisis de tráfico de red, cerrando la brecha entre el ataque y la respuesta.

    Preparación para Respuesta a Incidentes: Este laboratorio sienta las bases para automatizar respuestas ante incidentes, como el bloqueo automático de IPs tras la detección de escaneos persistentes.
