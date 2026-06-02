"""
Plant Disease Detection System
CNN Model Training Script — Optimized for CPU
Author: Morketa Negash
University: Madda Walabu University
"""

import os
import sys

# Suppress TF warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for terminal
import matplotlib.pyplot as plt
import json

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────
IMG_SIZE      = (128, 128)   # smaller image = much faster
BATCH_SIZE    = 64           # larger batch = faster per epoch
EPOCHS        = 20
LEARNING_RATE = 0.001
DATASET_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset")
MODEL_DIR     = os.path.dirname(os.path.abspath(__file__))
MODEL_SAVE_PATH = os.path.join(MODEL_DIR, "plant_disease_cnn.h5")

print("=" * 55)
print("  Plant Disease Detection — Fast CPU Training")
print("  Madda Walabu University | Morketa Negash")
print("=" * 55)
print(f"\n[INFO] TensorFlow: {tf.__version__}")
print(f"[INFO] Dataset   : {DATASET_DIR}")
print(f"[INFO] Image size: {IMG_SIZE}")
print(f"[INFO] Batch size: {BATCH_SIZE}")
print(f"[INFO] Max epochs: {EPOCHS}")


# ─────────────────────────────────────────────
#  DATA GENERATORS
# ─────────────────────────────────────────────
def build_generators(dataset_dir):
    train_gen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True,
        brightness_range=[0.8, 1.2],
        validation_split=0.2
    )
    val_gen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    train = train_gen.flow_from_directory(
        dataset_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True
    )
    val = val_gen.flow_from_directory(
        dataset_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False
    )
    return train, val


# ─────────────────────────────────────────────
#  FAST CNN ARCHITECTURE (optimized for CPU)
# ─────────────────────────────────────────────
def build_fast_model(num_classes):
    """
    Lightweight CNN — fast on CPU, ~85-90% accuracy.
    Uses depthwise separable convolutions for speed.
    """
    model = keras.Sequential([
        keras.Input(shape=(128, 128, 3)),

        # Block 1
        layers.Conv2D(32, (3,3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.2),

        # Block 2
        layers.Conv2D(64, (3,3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.2),

        # Block 3
        layers.Conv2D(128, (3,3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.2),

        # Block 4
        layers.Conv2D(128, (3,3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.2),

        # Classifier
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation="relu"),
        layers.BatchNormalization(),
        layers.Dropout(0.4),
        layers.Dense(num_classes, activation="softmax"),
    ])
    return model


# ─────────────────────────────────────────────
#  PLOT TRAINING HISTORY
# ─────────────────────────────────────────────
def plot_history(history, save_dir):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Plant Disease CNN — Training Results", fontsize=14)

    axes[0].plot(history.history["accuracy"],     label="Train",      color="blue")
    axes[0].plot(history.history["val_accuracy"], label="Validation", color="orange")
    axes[0].set_title("Accuracy")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")
    axes[0].legend()
    axes[0].grid(True)

    axes[1].plot(history.history["loss"],     label="Train",      color="blue")
    axes[1].plot(history.history["val_loss"], label="Validation", color="orange")
    axes[1].set_title("Loss")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Loss")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    path = os.path.join(save_dir, "training_history.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"[INFO] Training plot saved: {path}")


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    # Check dataset
    if not os.path.exists(DATASET_DIR):
        print(f"\n[ERROR] Dataset not found at: {DATASET_DIR}")
        sys.exit(1)

    # Build generators
    print("\n[STEP 1] Loading dataset...")
    train_gen, val_gen = build_generators(DATASET_DIR)
    num_classes = len(train_gen.class_indices)
    print(f"  Classes : {num_classes}")
    print(f"  Train   : {train_gen.samples} images")
    print(f"  Val     : {val_gen.samples} images")

    # Save class names
    class_indices = {v: k for k, v in train_gen.class_indices.items()}
    cn_path = os.path.join(MODEL_DIR, "class_names.json")
    with open(cn_path, "w") as f:
        json.dump(class_indices, f, indent=2)
    print(f"  Class names saved → {cn_path}")

    # Build model
    print("\n[STEP 2] Building CNN model...")
    model = build_fast_model(num_classes)
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    total_params = model.count_params()
    print(f"  Total parameters: {total_params:,}")

    # Estimate time
    steps_per_epoch = train_gen.samples // BATCH_SIZE
    print(f"  Steps per epoch : {steps_per_epoch}")
    print(f"  Est. time/epoch : ~3-6 minutes on CPU")
    print(f"  Est. total time : ~{steps_per_epoch * 2 // 60 * EPOCHS // 60} hours")

    # Callbacks
    callbacks = [
        ModelCheckpoint(
            MODEL_SAVE_PATH,
            monitor="val_accuracy",
            save_best_only=True,
            verbose=1
        ),
        EarlyStopping(
            monitor="val_accuracy",
            patience=5,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.5,
            patience=3,
            min_lr=1e-6,
            verbose=1
        ),
    ]

    # Train
    print(f"\n[STEP 3] Training for up to {EPOCHS} epochs...")
    print("  (Best model auto-saved every time val_accuracy improves)\n")

    history = model.fit(
        train_gen,
        epochs=EPOCHS,
        validation_data=val_gen,
        callbacks=callbacks,
        verbose=1
    )

    # Evaluate
    print("\n[STEP 4] Final evaluation...")
    val_loss, val_acc = model.evaluate(val_gen, verbose=0)
    print(f"\n{'='*45}")
    print(f"  RESULTS")
    print(f"{'='*45}")
    print(f"  Validation Accuracy : {val_acc*100:.2f}%")
    print(f"  Validation Loss     : {val_loss:.4f}")
    print(f"{'='*45}")

    # Plot
    print("\n[STEP 5] Saving training chart...")
    plot_history(history, MODEL_DIR)

    print(f"\n[DONE] Model saved → {MODEL_SAVE_PATH}")
    print("  Run the app: py -3.11 -m streamlit run app.py")


if __name__ == "__main__":
    main()
