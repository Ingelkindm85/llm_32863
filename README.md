# LLM Repositorio de Pruebas
Repositorio de trabajo con modelos de lenguaje largo usando ollama

## 1. Instalación de Ollama

Para instalar ollama accedemos a la página de {ollama} (https://ollama.com/download/linux), en una terminal se ejecuta el siguiente comando 

````bash
$ curl -fsSL https://ollama.com/install.sh | sh
````

## 2. Ejecutar el servidor

Una vez instalado se ejecuta el servidor ollama con el siguiente comando

````bash
$ ollama serve
````

## 3. Descargar algun modelo

En la página {modelos} (https://ollama.com/library) de ollama se busca el modelo deseado y se descarga con el siguiente comando:

````bash
$ ollama pull tinyllama
````

## 4. Prueba de request a la API REST

Para realizar una petición básica a la API de ollama se sigue la siguiente estructura

````bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
````

### 4.1 Consulta a la API REST sin stream

````bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
  "stream": false
}' 






