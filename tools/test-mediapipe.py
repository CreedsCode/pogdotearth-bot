from tkinter import E
import cv2
import mediapipe as mp#
import os
import pandas as pd

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
def do(images, mediapipe_options):
  with mp_hands.Hands(
     static_image_mode=True,
      max_num_hands=8,
      min_tracking_confidence= mediapipe_options["min_tracking_confidence"],
      min_detection_confidence= mediapipe_options["min_detection_confidence"]) as hands:
    for idx, file in enumerate(images):
      # Read an image, flip it around y-axis for correct handedness output (see
      # above).
      filename = os.path.basename(file)

      image = cv2.flip(cv2.imread(file), 1)
      # Convert the BGR image to RGB before processing.
      results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

      # Print handedness and draw hand landmarks on the image.
      # print('Handedness:', results.multi_handedness)
      if not results.multi_hand_landmarks:
        cv2.imwrite('images/tests/mediapipe/0_' + filename, cv2.flip(image, 1))
        continue
      image_height, image_width, _ = image.shape
      annotated_image = image.copy()
      for hand_landmarks in results.multi_hand_landmarks:
        # print('hand_landmarks:', hand_landmarks)
        # print(
        #     f'Index finger tip coordinates: (',
        #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
        #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
        # )
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      
      cv2.imwrite('images/tests/mediapipe/1_' + filename, cv2.flip(annotated_image, 1))

if __name__ == "__main__":
  
  df = pd.read_excel("mediapipe.xlsx", "tests")

  # for row in pandas (one test)   = 1293
  for index, row in df.iterrows():
    print("Starting batch, ", index)
    if(str(row["samples_got_right"]) != "nan"):
      print("Progress found, move ahead")
      print(index)
      continue
    folder_directory = r"images/tests/everything"
    images = os.listdir(folder_directory)
    mediapipe_options = {
      "max_num_hands": 8,
      "min_tracking_confidence": row["min_tracking_confidence"],
      "min_detection_confidence": row["min_detection_confidence"]
    }
    
    do([f"{folder_directory}/{image}" for image in images], mediapipe_options)
    right_result_count = 0
    wrong_result_count = 0

    for root, dir, files in os.walk("images/tests/mediapipe"):
      for file in files:
        deconstructed_file = file.split("_")
        mediapipe_result = "nohands" if deconstructed_file[0] == "0" else "hands"
        correct_result = deconstructed_file[1]

        if mediapipe_result == correct_result:
          right_result_count += 1
        else:
          wrong_result_count += 1
        
        os.remove("images/tests/mediapipe/" + file)
    
    df.at[index, 'samples_got_right'] = right_result_count
    df.at[index, 'sample_got_wrong'] = wrong_result_count
    print(right_result_count, wrong_result_count, 100 * float(right_result_count)/float(right_result_count + wrong_result_count) )
    df.to_excel("part_mediapipe_results.xlsx")

  df.to_excel("mediapipe_results.xlsx")