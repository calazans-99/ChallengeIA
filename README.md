
# 🛵 MotoTrack360 - Detecção de Motos com YOLOv8 (Versão Simples)

Este projeto é uma versão **minimalista e funcional** de um sistema de **detecção de motos em tempo real** utilizando **YOLOv8** e **OpenCV**, voltado para demonstrações rápidas, testes e projetos acadêmicos. É parte da proposta do Challenge 2025 da FIAP com foco em Visão Computacional aplicada ao rastreio de veículos nos pátios da Mottu.

---

## 🎯 Objetivo

Detectar **motocicletas** através da webcam do computador, identificar a posição onde ocorrem as detecções e exibir essas posições graficamente ao final da execução.

---

## 🚀 Funcionalidades

- ✅ Detecção ao vivo com webcam
- 🧠 Uso de modelo pré-treinado YOLOv8 (Ultralytics)
- 🖼️ Caixa delimitadora e confiança exibidas na tela
- 🗺️ Mapeamento gráfico das regiões onde as motos foram detectadas
- ❌ Sem gravação de vídeo ou arquivos intermediários

---

## 🧰 Requisitos

Certifique-se de ter o Python instalado (>= 3.8) e execute o seguinte comando para instalar as dependências:

```bash
pip install ultralytics opencv-python matplotlib
```

---

## 📂 Arquivos do Projeto

```
📦 mototrack360/
├── detector_motos_simples.py     # Script principal
├── yolov8n.pt                    # (opcional) Modelo YOLOv8 leve, baixado automaticamente
```

---

## ▶️ Como Executar

1. Certifique-se de que uma webcam está conectada ao seu computador.
2. Execute o script no terminal:

```bash
python detector_motos_simples.py
```

3. Uma janela será aberta com a detecção ao vivo. Pressione **`e`** para sair.
4. Após encerrar, será exibido um **gráfico com os pontos de detecção**.

---

## 📊 Exemplo de saída gráfica

O gráfico exibido ao final mostra os pontos onde motos foram detectadas no campo de visão da câmera, ajudando a visualizar o "pátio virtual" monitorado.

---

## 🧠 Sobre o YOLOv8

Este projeto utiliza o modelo `yolov8n.pt`, uma versão leve do YOLOv8 (You Only Look Once), treinado no dataset COCO que contém a classe `motorcycle`. O modelo é baixado automaticamente pela biblioteca **Ultralytics** na primeira execução.

---

## 💡 Aplicações Possíveis

- Prova de conceito para rastreamento de frotas em pátios
- Sistemas de vigilância inteligente
- Projetos acadêmicos com foco em IA e Visão Computacional
- Base para expansão com IoT, APIs REST e dashboards

---

## 📌 Observações

- O script não salva vídeo, não exige banco de dados e pode ser executado em qualquer computador com Python e webcam.
- Pode ser expandido para detecção de outros objetos como carros, pessoas, etc.

---

Desenvolvido por alunos da FIAP como parte do **Challenge 2025 - Mottu** 🚀
