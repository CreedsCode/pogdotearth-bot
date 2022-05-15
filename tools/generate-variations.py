import itertools
from numpy import append
import pandas as pd

df = pd.read_excel("mediapipe.xlsx","combinations")

iterables = [ df["tracking_values"].tolist(), df["detection_values"].tolist() ]
tracking_confidence = []
detection_confidence = []

for min_tracking_confidence, min_detection_confidence in itertools.product(*iterables):
    tracking_confidence.append(min_tracking_confidence)
    detection_confidence.append(min_detection_confidence) 

df = pd.DataFrame()
df["min_tracking_confidence"] = tracking_confidence
df["min_detection_confidence"] =  detection_confidence
df.to_excel("mediapipe_generated_combination.xlsx", index=False)