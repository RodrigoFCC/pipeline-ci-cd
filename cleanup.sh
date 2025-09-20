#!/bin/bash

IMAGE_NAME=$1
if [ -z "$IMAGE_NAME" ]; then
    echo "Uso: $0 <nome-da-imagem>"
    exit 1
fi

TAGS=$(docker images --format "{{.Tag}}" $IMAGE_NAME | sort -r)

KEEP_TAG=$(echo "$TAGS" | head -n 1)
echo "Mantendo tag: $KEEP_TAG"

echo "$TAGS" | tail -n +2 | while read TAG; do
    echo "Removendo tag: $TAG"
    docker rmi $IMAGE_NAME:$TAG 2>/dev/null || true
done

echo "Limpeza concluída"