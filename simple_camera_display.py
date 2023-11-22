import cv2

class CameraDisplay:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def display_camera(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error reading frame")
                break

            cv2.imshow('Camera Frame', frame)

            # Press 'q' to exit the loop and close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_display = CameraDisplay()
    camera_display.display_camera()
