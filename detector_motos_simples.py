
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Carrega modelo YOLOv8
model = YOLO("yolov8n.pt")

# Inicia webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

print("Detecção de motos em tempo real (pressione 'e' para sair)")

coordenadas_detectadas = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inferência
    results = model(frame)[0]

    for det in results.boxes:
        cls_id = int(det.cls[0])
        label = model.names[cls_id]
        conf = float(det.conf[0])

        if label in ["motorbike", "motorcycle"] and conf > 0.5:
            x1, y1, x2, y2 = map(int, det.xyxy[0])
            coordenadas_detectadas.append((x1, y1))
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 255), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 255), 2)

    cv2.imshow("Detecção de Motos", frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()

# Gera mapeamento simples
plt.figure(figsize=(8, 5))
plt.title("Pontos de Detecção de Motos")
plt.xlabel("Largura")
plt.ylabel("Altura")
plt.gca().invert_yaxis()

for x, y in coordenadas_detectadas:
    plt.plot(x, y, 'ro', markersize=4)

plt.grid(True)
plt.tight_layout()
plt.show()
