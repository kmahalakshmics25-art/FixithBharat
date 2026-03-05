import numpy as np

classes = [
    "pothole",
    "garbage",
    "broken_streetlight",
    "water_leak"
]

def predict_image(image):

    # Dummy prediction for now
    index = np.random.randint(0, len(classes))

    return {
        "issue": classes[index],
        "confidence": 0.87
    }
