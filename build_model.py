import os, json, shutil
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Save to temp location first (avoids OneDrive sync issues)
TEMP_PATH = r"C:\Temp\plant_disease_cnn.keras"
FINAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "plant_disease_cnn.keras")

os.makedirs(r"C:\Temp", exist_ok=True)

CLASS_NAMES = {
    0:"Apple___Apple_scab", 1:"Apple___Black_rot", 2:"Apple___Cedar_apple_rust",
    3:"Apple___healthy", 4:"Corn___Cercospora_leaf_spot", 5:"Corn___Common_rust",
    6:"Corn___Northern_Leaf_Blight", 7:"Corn___healthy", 8:"Potato___Early_blight",
    9:"Potato___Late_blight", 10:"Potato___healthy", 11:"Tomato___Bacterial_spot",
    12:"Tomato___Early_blight", 13:"Tomato___Late_blight", 14:"Tomato___Leaf_Mold",
    15:"Tomato___Septoria_leaf_spot", 16:"Tomato___Spider_mites", 17:"Tomato___Target_Spot",
    18:"Tomato___Tomato_Yellow_Leaf_Curl_Virus", 19:"Tomato___Tomato_mosaic_virus",
    20:"Tomato___healthy"
}

print("[INFO] Building lightweight CNN model...")

model = keras.Sequential([
    layers.Input(shape=(224, 224, 3)),
    layers.Conv2D(16, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(32, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(21, activation="softmax"),
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Save to temp first
print(f"[INFO] Saving to temp: {TEMP_PATH}")
model.save(TEMP_PATH)

if os.path.exists(TEMP_PATH):
    size_mb = os.path.getsize(TEMP_PATH) / (1024 * 1024)
    print(f"[OK] Temp save successful: {size_mb:.2f} MB")
    # Copy to final location
    shutil.copy2(TEMP_PATH, FINAL_PATH)
    print(f"[OK] Copied to: {FINAL_PATH}")
    final_size = os.path.getsize(FINAL_PATH) / (1024 * 1024)
    print(f"[OK] Final size: {final_size:.2f} MB")
else:
    print("[ERROR] Temp save failed!")

print("\n[DONE]")
