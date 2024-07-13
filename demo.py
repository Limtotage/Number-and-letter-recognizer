import cv2
cap =cv2.VideoCapture(0+CAP_DSHOW)
WIDTH =cap.get(cv2.CAP_PROP_FRAME_WIDTH)
HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
while cap.isOpened():
    ch, frame = cap.read()
    frame=cv2.rotate(frame,cv2.ROTATE_180)
    frame_copy=frame.copy()
    bbox_size=(60,60)
    bbox=[(
        int(WIDTH//2-bbox_size[0]//2),
        int(HEIGHT//2-bbox_size[1]//2),
        int(WIDTH//2+bbox_size[0]//2),
        int(HEIGHT//2+bbox_size[1]//2))]
    img_crop = frame[bbox[0][1]:bbox[1][1],
                     bbox[0][0]:bbox[1][0]]
    img_gray=cv2.cvtColor(img_crop,cv2.COLOR_BGR2GRAY)
    img_gray=cv2.resize(img_gray,(200,200))
    cv2.imshow("kirpik",img_gray)
    cv2.imshow("Oku",frame_copy)
    if cv2.waitKey(1) and 0xFF==27:
        break
cv2.destroyAllWindows()
