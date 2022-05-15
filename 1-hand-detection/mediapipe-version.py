import cv2
import mediapipe as mp#
import os

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
def do(images):
  with mp_hands.Hands(
      static_image_mode=True,
      max_num_hands=8,
      min_tracking_confidence=0.2,
      min_detection_confidence=0.3) as hands:
    for idx, file in enumerate(images):
      # Read an image, flip it around y-axis for correct handedness output (see
      # above).
      image = cv2.flip(cv2.imread(file), 1)
      # Convert the BGR image to RGB before processing.
      results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

      # Print handedness and draw hand landmarks on the image.
      print('Handedness:', results.multi_handedness)
      if not results.multi_hand_landmarks:
        continue
      image_height, image_width, _ = image.shape
      annotated_image = image.copy()
      for hand_landmarks in results.multi_hand_landmarks:
        print('hand_landmarks:', hand_landmarks)
        print(
            f'Index finger tip coordinates: (',
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
        )
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      
      cv2.imwrite('images/tests/mediapipe/penis' + str(idx) + '.png', cv2.flip(annotated_image, 1))

if __name__ == "__main__":
  
  folder_directory = "images/everything"
  images = os.listdir(folder_directory)
  do([f"{folder_directory}/{image}" for image in images])
  
  cv2.waitKey(50000)
  cv2.destroyAllWindows()