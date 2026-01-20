
import cv2
import numpy as np

"Glbal variables"
"Variaveis globais"
drawing = False # True if mouse is pressed 
ix, iy = -1, -1
reactangles = []

# Callback function for mouse event
# Funcao de callback para eventos do mouse
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, frame

    # Draws a rectangle on the frame based on mouse events.
    # Desenha um retangulo no frame baseado em eventos do mouse.
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y 

    elif event == cv2.EVENT_MOUSEMOVE:
        drawing = False
        reactangles.append((ix, iy, x, y))
        cv2.rectangle(frame, (ix, iy), (x, y), (255, 255, 255), -1)

# Open the video capture
# Abre a captura de video
input_video_path = "watermark_input.mp4"
cap = cv2.VideoCapture(input_video_path)

# Get video Properties 
# Obtem propriedades do video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# create a windows and set the callback function for mouse events



