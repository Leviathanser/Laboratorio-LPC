#!/bin/bash
echo "Se encriptara el mensaje encoded_msg"
base64 -d encoded_msg.b64 > decoded_msg.txt

echo "decodificar los archivos de texto como imagenens jpg"

base64 -d mystery_img1.txt > imagen1.jpg
base64 FCFM_logo.jpeg > encode_image.txt
