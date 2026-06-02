import os
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "plant_disease_cnn.h5")
print("Looking for:", model_path)
print("Exists:", os.path.exists(model_path))
if os.path.exists(model_path):
    print("Size:", round(os.path.getsize(model_path)/1024/1024, 2), "MB")

# List all files in model dir
model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model")
print("\nFiles in model dir:")
for f in os.listdir(model_dir):
    fp = os.path.join(model_dir, f)
    size = os.path.getsize(fp) if os.path.isfile(fp) else 0
    print(f"  {f} ({round(size/1024,1)} KB)")
