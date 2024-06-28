import mediapipe as mp
import cv2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Load data
df = pd.read_csv('coords.csv')

# Split features and target
X = df.drop('class', axis=1)
y = df['class']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# Define classification pipeline
pipeline = make_pipeline(StandardScaler(), LogisticRegression())

# Train the model
model = pipeline.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Classification report
report = classification_report(y_test, y_pred)

# Print accuracy
print("Accuracy:", accuracy)

# Print classification report
print("Classification Report:")
print(report)

# Save the model
with open('body_language.pkl', 'wb') as f:
    pickle.dump(model, f)
