"""
Treatment recommendations and disease information database.
Updated to match actual dataset classes (15 classes).
"""

DISEASE_INFO = {

    # ── NOT A LEAF ──────────────────────────────────────────────────
    "Not_A_Leaf": {
        "display_name": "Not a Leaf",
        "crop": "Unknown",
        "severity": "None",
        "description": "The uploaded image does not appear to be a plant leaf. Please upload a clear photo of a leaf for accurate disease detection.",
        "symptoms": [],
        "treatment": ["Upload a clear, close-up photo of a plant leaf."],
        "prevention": "Ensure the leaf fills most of the frame with good lighting.",
    },

    # ── PEPPER ──────────────────────────────────────────────────────
    "Pepper__bell___Bacterial_spot": {
        "display_name": "Pepper Bacterial Spot",
        "crop": "Pepper (Bell)",
        "severity": "High",
        "description": (
            "Bacterial spot is caused by Xanthomonas campestris. "
            "It is one of the most serious diseases of pepper, causing "
            "defoliation, fruit spots, and significant yield loss."
        ),
        "symptoms": [
            "Small, water-soaked spots on leaves that turn brown",
            "Yellow halo surrounding lesions",
            "Raised, scab-like spots on fruit",
            "Premature defoliation in severe cases",
        ],
        "treatment": [
            "Apply copper-based bactericides at first sign of disease",
            "Remove and destroy infected plant material",
            "Avoid overhead irrigation to reduce leaf wetness",
            "Use disease-free certified transplants",
        ],
        "prevention": "Use resistant varieties and practice 2-year crop rotation with non-host crops.",
    },
    "Pepper__bell___healthy": {
        "display_name": "Healthy Pepper",
        "crop": "Pepper (Bell)",
        "severity": "None",
        "description": "The pepper plant appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": ["Continue regular monitoring and good agricultural practices."],
        "prevention": "Maintain proper irrigation, fertilization, and spacing.",
    },

    # ── POTATO ──────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "display_name": "Potato Early Blight",
        "crop": "Potato",
        "severity": "Moderate",
        "description": (
            "Early blight is caused by Alternaria solani. It typically affects "
            "older leaves first and can cause significant defoliation and yield loss."
        ),
        "symptoms": [
            "Dark brown spots with concentric rings (target-board pattern)",
            "Yellow halo surrounding the lesions",
            "Lesions start on older, lower leaves",
            "Premature defoliation",
        ],
        "treatment": [
            "Apply fungicides containing chlorothalonil or mancozeb",
            "Remove and destroy infected plant debris",
            "Ensure adequate plant nutrition (especially nitrogen)",
            "Avoid overhead irrigation",
        ],
        "prevention": "Use certified disease-free seed potatoes and practice crop rotation.",
    },
    "Potato___Late_blight": {
        "display_name": "Potato Late Blight",
        "crop": "Potato",
        "severity": "Critical",
        "description": (
            "Late blight, caused by Phytophthora infestans, is the most destructive "
            "potato disease. It was responsible for the Irish Potato Famine of the 1840s."
        ),
        "symptoms": [
            "Water-soaked, pale green lesions on leaves",
            "White, fuzzy mold on underside of leaves in humid conditions",
            "Lesions turn brown/black rapidly",
            "Brown rot in tubers",
        ],
        "treatment": [
            "Apply systemic fungicides (metalaxyl, cymoxanil) immediately",
            "Destroy infected plants to prevent spread",
            "Avoid working in fields when plants are wet",
            "Harvest tubers promptly if disease is severe",
        ],
        "prevention": "Use resistant varieties and apply preventive fungicide sprays during cool, wet weather.",
    },
    "Potato___healthy": {
        "display_name": "Healthy Potato",
        "crop": "Potato",
        "severity": "None",
        "description": "The potato plant appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": ["Continue regular monitoring and good agricultural practices."],
        "prevention": "Use certified seed potatoes and practice 3-year crop rotation.",
    },

    # ── TOMATO ──────────────────────────────────────────────────────
    "Tomato_Bacterial_spot": {
        "display_name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "severity": "High",
        "description": (
            "Bacterial spot is caused by Xanthomonas species. It affects leaves, "
            "stems, and fruit, causing significant yield and quality losses."
        ),
        "symptoms": [
            "Small, water-soaked spots on leaves",
            "Spots turn brown with yellow halos",
            "Raised, scab-like spots on fruit",
            "Defoliation in severe cases",
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove and destroy infected plant material",
            "Avoid overhead irrigation",
            "Use disease-free transplants",
        ],
        "prevention": "Use resistant varieties and copper sprays as a preventive measure.",
    },
    "Tomato_Early_blight": {
        "display_name": "Tomato Early Blight",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Caused by Alternaria solani, early blight is a common fungal disease "
            "that affects tomato plants, especially under warm, humid conditions."
        ),
        "symptoms": [
            "Dark brown spots with concentric rings on older leaves",
            "Yellow tissue surrounding the lesions",
            "Stem lesions (collar rot) near the soil line",
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, mancozeb, or copper)",
            "Remove infected lower leaves",
            "Mulch around plants to prevent soil splash",
            "Ensure proper plant spacing for air circulation",
        ],
        "prevention": "Rotate crops and use resistant tomato varieties.",
    },
    "Tomato_Late_blight": {
        "display_name": "Tomato Late Blight",
        "crop": "Tomato",
        "severity": "Critical",
        "description": (
            "Caused by Phytophthora infestans, late blight can destroy an entire "
            "tomato crop within days under favorable conditions."
        ),
        "symptoms": [
            "Large, irregular, water-soaked lesions on leaves",
            "White mold on the underside of leaves",
            "Brown, greasy-looking lesions on stems",
            "Firm, brown rot on fruit",
        ],
        "treatment": [
            "Apply systemic fungicides (metalaxyl + mancozeb) immediately",
            "Remove and bag infected plants — do not compost",
            "Avoid wetting foliage when irrigating",
        ],
        "prevention": "Monitor weather forecasts and apply preventive sprays during cool, wet periods.",
    },
    "Tomato_Leaf_Mold": {
        "display_name": "Tomato Leaf Mold",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Leaf mold is caused by Passalora fulva. "
            "It is most common in greenhouse tomatoes under high humidity."
        ),
        "symptoms": [
            "Pale green or yellow spots on upper leaf surface",
            "Olive-green to grayish-purple mold on the underside",
            "Leaves curl and wither in severe cases",
        ],
        "treatment": [
            "Reduce humidity by improving ventilation",
            "Apply fungicides (chlorothalonil or copper)",
            "Remove and destroy infected leaves",
        ],
        "prevention": "Maintain relative humidity below 85% and ensure good air circulation.",
    },
    "Tomato_Septoria_leaf_spot": {
        "display_name": "Tomato Septoria Leaf Spot",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Septoria leaf spot, caused by Septoria lycopersici, is one of the most "
            "destructive diseases of tomato foliage."
        ),
        "symptoms": [
            "Numerous small, circular spots with dark borders and gray centers",
            "Tiny black dots (pycnidia) visible in center of spots",
            "Yellowing and dropping of infected leaves",
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, mancozeb, or copper) at first sign",
            "Remove infected leaves immediately",
            "Avoid overhead watering",
            "Mulch to prevent soil splash",
        ],
        "prevention": "Practice crop rotation and use disease-free transplants.",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "display_name": "Tomato Spider Mites (Two-spotted)",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids "
            "that feed on plant cells, causing stippling and bronzing of leaves."
        ),
        "symptoms": [
            "Fine stippling (tiny yellow/white dots) on upper leaf surface",
            "Bronze or silvery discoloration of leaves",
            "Fine webbing on the underside of leaves",
            "Leaf drop in severe infestations",
        ],
        "treatment": [
            "Apply miticides (abamectin, bifenazate) or insecticidal soap",
            "Spray the underside of leaves thoroughly",
            "Introduce predatory mites for biological control",
            "Increase humidity — mites thrive in dry conditions",
        ],
        "prevention": "Avoid water stress and dusty conditions that favor mite outbreaks.",
    },
    "Tomato__Target_Spot": {
        "display_name": "Tomato Target Spot",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Target spot is caused by Corynespora cassiicola. It affects leaves, "
            "stems, and fruit, and is favored by warm, humid conditions."
        ),
        "symptoms": [
            "Brown lesions with concentric rings (target pattern)",
            "Yellow halo around lesions",
            "Lesions on fruit appear as dark, sunken spots",
        ],
        "treatment": [
            "Apply fungicides (azoxystrobin, chlorothalonil)",
            "Improve air circulation through pruning",
            "Avoid overhead irrigation",
        ],
        "prevention": "Use resistant varieties and practice crop rotation.",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "display_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "crop": "Tomato",
        "severity": "Critical",
        "description": (
            "TYLCV is a devastating viral disease transmitted by the silverleaf "
            "whitefly (Bemisia tabaci). It can cause up to 100% yield loss."
        ),
        "symptoms": [
            "Upward curling and yellowing of young leaves",
            "Stunted plant growth",
            "Flower drop and poor fruit set",
            "Small, crumpled leaves",
        ],
        "treatment": [
            "No cure — remove and destroy infected plants immediately",
            "Control whitefly populations with insecticides (imidacloprid)",
            "Use yellow sticky traps to monitor whitefly populations",
            "Apply reflective mulches to repel whiteflies",
        ],
        "prevention": "Plant TYLCV-resistant varieties and use insect-proof nets in nurseries.",
    },
    "Tomato__Tomato_mosaic_virus": {
        "display_name": "Tomato Mosaic Virus (ToMV)",
        "crop": "Tomato",
        "severity": "High",
        "description": (
            "Tomato mosaic virus is a highly contagious virus spread by contact "
            "with infected plant material, tools, and hands."
        ),
        "symptoms": [
            "Mosaic pattern of light and dark green on leaves",
            "Leaf distortion and curling",
            "Stunted growth",
            "Mottled or streaked fruit",
        ],
        "treatment": [
            "No chemical cure — remove and destroy infected plants",
            "Disinfect tools with 10% bleach solution between plants",
            "Wash hands thoroughly before handling plants",
        ],
        "prevention": "Use virus-free certified seeds and resistant varieties.",
    },
}


def get_disease_info(class_name: str) -> dict:
    """Returns disease information for a given class name."""
    return DISEASE_INFO.get(
        class_name,
        {
            "display_name": class_name.replace("_", " "),
            "crop": "Unknown",
            "severity": "Unknown",
            "description": "No detailed information available for this class.",
            "symptoms": [],
            "treatment": ["Consult a local agricultural expert for advice."],
            "prevention": "Practice general good agricultural practices.",
        },
    )


SEVERITY_COLORS = {
    "None":     "#28a745",   # green
    "Moderate": "#ffc107",   # yellow
    "High":     "#fd7e14",   # orange
    "Critical": "#dc3545",   # red
    "Unknown":  "#6c757d",   # gray
}
