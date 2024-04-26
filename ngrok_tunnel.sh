#!/bin/bash

# Vérifie si l'URL est passée en paramètre
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Récupère l'URL passée en paramètre
url="$1"

# Lance ngrok pour créer un tunnel HTTP vers l'URL spécifiée
ngrok http "$url"
