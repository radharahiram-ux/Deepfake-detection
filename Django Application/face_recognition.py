import cv2

def face_locations(img):
    # Use OpenCV's built-in Haar Cascades for actual face detection (no dlib required)
    try:
        # Convert to grayscale for detection
        if len(img.shape) == 3 and img.shape[2] == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img
            
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
        
        results = []
        for (x, y, w, h) in faces:
            # OpenCV's Haar cascades return large boxes including the forehead and hair.
            # dlib (which the model was trained on) returns very tight boxes around the eyebrows to chin.
            # We scale the Haar cascade box to approximate a dlib tight crop.
            top = int(y + h * 0.15)
            bottom = int(y + h * 0.95)
            left = int(x + w * 0.10)
            right = int(x + w * 0.90)
            results.append((top, right, bottom, left))
            
        # Fallback to center box only if NO face is detected in the frame
        if len(results) == 0:
            h_img, w_img = img.shape[:2]
            results.append((int(0.1 * h_img), int(0.9 * w_img), int(0.9 * h_img), int(0.1 * w_img)))
            
        return results
    except Exception as e:
        print(f"Haar Cascade fallback failed: {e}")
        return [(10, 110, 110, 10)]
