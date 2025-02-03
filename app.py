import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image

# Header Section
st.set_page_config(page_title="Fruit and Vegetable Classifier", page_icon="🍓", layout="centered")
st.title("🍎 Fruit & Vegetable Recognition 🍅")
st.markdown("""<style>body {background-color: #f8f9fa;}</style>""", unsafe_allow_html=True)

# Load the model
try:
    model = load_model(r'C:\Users\ashwa\WhatsApp-chat-analyzer\Image_classification\Image_classification\Image_classify.keras')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Categories and Additional Info
default_image_url = "https://example.com/default.jpg"
default_info = {
    "Nutritional Content (per 100g):": "Information not available",
    "benefits": "General health benefits",
    "risks": "No significant risks known."
}

data_info = {
    'apple': {"image": "https://example.com/apple.jpg", "Nutritional Content (per 100g)": '''Calories: ~52

Carbs: ~14g

Fiber: ~2.4g

Vitamin C: ~8% RDI

Vitamin A: Trace amounts

Potassium: ~107mg''',
              "benefits": '''High in antioxidants, supports heart health.

Aids digestion due to dietary fiber.

May help regulate blood sugar levels.''',
              "risks": "Excessive consumption may cause bloating in sensitive individuals."},
    'banana': {"image": "https://example.com/banana.jpg", "Nutritional Content (per 100g)": '''Calories: ~89

Carbs: ~23g

Fiber: ~2.6g

Vitamin C: ~10% RDI

Vitamin B6: ~20% RDI

Potassium: ~358mg''',
               "benefits": '''Rich in potassium, supports heart and muscle health.

Aids digestion and promotes satiety.

Contains natural sugars for energy.''',
               "risks": "High glycemic index may affect blood sugar levels in diabetics."},
    'beetroot': {"image": "https://example.com/beetroot.jpg", "Nutritional Content (per 100g)": '''Calories: ~43

Carbs: ~10g

Fiber: ~2.8g

Vitamin C: ~4% RDI

Folate: ~20% RDI

Potassium: ~325mg''',
                 "benefits": '''Improves blood flow and lowers blood pressure.

Rich in antioxidants, supports liver health.''',
                 "risks": "May cause red urine or stool (harmless)."},
    'bell pepper': {"image": "https://example.com/bell pepper.jpg", "Nutritional Content (per 100g)":'''Calories: ~20-40

Carbs: ~6g

Fiber: ~1.7g

Vitamin C: ~213% RDI (red)

Vitamin A: High (red and yellow)

Potassium: ~210mg''' ,"benefits":'''Supports eye and skin health.

Boosts immunity and fights oxidative stress.

Low in calories, good for weight management.''' ,"risks":"Rarely causes allergies."},
    'cabbage': {"image": "https://example.com/cabbage.jpg", "Nutritional Content (per 100g)":'''Calories: ~25

Carbs: ~5.8g

Fiber: ~2.5g

Vitamin C: ~60% RDI

Vitamin K: ~85% RDI

Folate: ~10% RDI''',"benefits":'''Supports digestion and gut health.

Rich in antioxidants, may reduce inflammation.

Helps in detoxification due to sulfur compounds.''' ,"risks":"Excessive consumption may cause bloating or gas"},
    'capsicum': {"image": "https://example.com/capsicum.jpg", "Nutritional Content (per 100g)":'''Calories: ~40

Carbs: ~9g

Fiber: ~2g

Vitamin C: ~130% RDI

Vitamin B6: ~15% RDI

Vitamin A: ~10% RDI''',"benefits":'''High in vitamin C and antioxidants.

Supports skin and immune health.

May help reduce inflammation.

''' ,"risks":"Can irritate sensitive stomachs in some people."},
    'carrot': {"image": "https://example.com/carrot.jpg", "Nutritional Content (per 100g)":'''Calories: ~41

Carbs: ~10g

Fiber: ~2.8g

Vitamin A: ~334% RDI (as beta-carotene)

Vitamin C: ~9% RDI

Potassium: ~320mg''',"benefits":'''Promotes eye health and skin health.

Rich in antioxidants, supports immunity.

May help regulate blood sugar levels.''',"risks":"Excessive consumption may cause carotenemia (orange skin)."},
    'cauliflower': {"image": "https://example.com/cauliflower.jpg", "Nutritional Content (per 100g)": '''Calories: ~25

Carbs: ~5g

Fiber: ~2g

Vitamin C: ~77% RDI

Vitamin K: ~20% RDI

Folate: ~15% RDI''',"benefits":'''Supports digestion and detoxification.

Low in calories, good for weight management.

Contains compounds that may reduce cancer risk.''' ,"risks":"May cause gas or bloating in sensitive individuals."},
    'chilli pepper': {"image": "https://example.com/chilli.jpg", "Nutritional Content (per 100g)":'''Calories: ~40

Carbs: ~9g

Fiber: ~1.5g

Vitamin C: ~240% RDI

Vitamin A: ~32% RDI

Capsaicin: Bioactive compound''',"benefits":'''Boosts metabolism and reduces inflammation.

Rich in antioxidants, may improve circulation.

May act as a natural pain reliever.

''' ,"risks":'''Can cause stomach irritation and burning sensation.

Overconsumption may lead to digestive issues.'''},
    'corn': {"image": "https://example.com/corn.jpg", "Nutritional Content (per 100g)":'''Calories: ~86

Carbs: ~19g

Fiber: ~2.7g

Vitamin B6: ~13% RDI

Vitamin C: ~6% RDI

Potassium: ~270mg''',"benefits":'''Good energy source, contains antioxidants like lutein.

Supports eye health and digestion.''' ,"risks":'''May raise blood sugar levels in diabetics.

High consumption may cause weight gain.'''},
    'cucumber': {"image": "https://example.com/cucumber.jpg", "Nutritional Content (per 100g)":'''Calories: ~15

Water: ~95%

Carbs: ~3.6g

Fiber: ~0.5g

Vitamin K: ~16% RDI

Potassium: ~147mg ''',"benefits":'''Hydrating, promotes skin health.

Supports digestion and detoxification.

May help reduce swelling and puffiness.''' ,"risks":"May cause digestive discomfort in some people."},
    'eggplant': {"image": "https://example.com/eggplant.jpg", "Nutritional Content (per 100g)":'''Calories: ~25

Carbs: ~6g

Fiber: ~3g

Vitamin C: ~3% RDI

Potassium: ~230mg

Manganese: ~10% RDI''',"benefits":'''Rich in antioxidants, supports heart health.

May help regulate blood sugar levels.

Promotes weight management.''' ,"risks":"Contains solanine, which can be toxic in large amounts."},
    'garlic': {"image": "https://example.com/garlic.jpg", "Nutritional Content (per 100g)":'''Calories: ~149

Carbs: ~33g

Fiber: ~2.1g

Vitamin C: ~31% RDI

Manganese: ~23% RDI

Selenium: ~6% RDI''',"benefits":'''Boosts immunity and heart health.

Contains allicin with antibacterial properties.

May reduce cholesterol levels.''' ,"risks":'''Can cause bad breath and digestive discomfort.

High doses may thin the blood.'''},
    'ginger': {"image": "https://example.com/ginger.jpg", "Nutritional Content (per 100g)":'''Calories: ~80

Carbs: ~18g

Fiber: ~2g

Vitamin C: ~5% RDI

Gingerol: Bioactive compound''',"benefits":'''Reduces nausea and inflammation.

Supports digestion and may reduce muscle pain.

Improves circulation and boosts immunity.''' ,"risks":'''High doses may cause heartburn or upset stomach.

May interact with blood-thinning medications.'''},
    'grapes': {"image": "https://example.com/grapes.jpg", "Nutritional Content (per 100g)":'''Calories: ~69

Carbs: ~18g

Fiber: ~0.9g

Vitamin C: ~18% RDI

Vitamin K: ~22% RDI

Antioxidants: High levels (resveratrol)''',"benefits":'''High in antioxidants, supports heart health.

May improve brain function and reduce inflammation.

Supports skin and eye health.''' ,"risks":'''High sugar content may affect diabetics.

Overconsumption may lead to weight gain.'''},
    'jalepenokiwi': {"image": "https://example.com/jalepenokiwi.jpg", "Nutritional Content (per 100g)":'''Calories: ~29

Carbs: ~6.5g

Fiber: ~2.8g

Vitamin C: ~40% RDI

Vitamin A: ~10% RDI

Capsaicin: Bioactive compound''',"benefits":'''May boost metabolism and aid weight loss.

Supports immunity due to high vitamin C.

Contains antioxidants with anti-inflammatory properties.''' ,"risks":"The stomach and digestive tract can become irritated in some individuals."},
    'lemon': {"image": "https://example.com/ginger.jpg", "Nutritional Content (per 100g)":''' ''',"benefits":'''''', "risks":''''''},
    'lettuce': {"image": "https://example.com/ginger.jpg", "Nutritional Content (per 100g)":''' ''',"benefits":''' ''',"risks":''' '''},
    'mango': {"image": "https://example.com/ginger.jpg", "Nutritional Content (per 100g)":''' ''',"benefits":''' ''',"risks":''' '''},
    'onion': {"image": "https://example.com/ginger.jpg", "Nutritional Content (per 100g)":''' ''',"benefits":''' ''',"risks":''' '''},
    'orange': {"image": "https://example.com/ginger.jpg", "Nutritional Content (per 100g)":''' ''',"benefits":''' ''',''' '''},
    'paprika': {"image": "https://example.com/ginger.jpg", **default_info},
    'pear': {"image": "https://example.com/ginger.jpg", **default_info},
    'peas': {"image": "https://example.com/ginger.jpg", **default_info},
    'pineapple': {"image": default_image_url, **default_info},
    'pomegranate': {"image": default_image_url, **default_info},
    'potato': {"image": default_image_url, **default_info},
    'raddish': {"image": default_image_url, **default_info},
    'soy beans': {"image": default_image_url, **default_info},
    'spinach': {"image": default_image_url, **default_info},
    'sweetcornsweetcorn': {"image": default_image_url, **default_info},
    'sweetpotato': {"image": default_image_url, **default_info},
    'tomato': {"image": default_image_url, **default_info},
    'turnip': {"image": default_image_url, **default_info},
    'watermelon': {"image": default_image_url, **default_info}
}

categories = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper',
    'corn',
    'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepenokiwi', 'lemon', 'lettuce', 'mango', 'onion',
    'orange',
    'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach',
    'sweetcornsweetcorn',
    'sweetpotato', 'tomato', 'turnip', 'watermelon'
]

# Sidebar Input
st.sidebar.header("Input Options")

# Image Upload
uploaded_file = st.sidebar.file_uploader("Upload a fruit or vegetable image", type=["jpg", "jpeg", "png"])

# Text Input
text_input = st.sidebar.text_input("Or, enter the name of a fruit or vegetable:")

if uploaded_file:
    try:
        # Display uploaded image
        st.sidebar.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image
        img_height, img_width = 180, 180
        image = Image.open(uploaded_file).convert('RGB')
        image_resized = image.resize((img_height, img_width))
        img_array = tf.keras.utils.img_to_array(image_resized)
        img_batch = tf.expand_dims(img_array, 0)

        # Prediction
        predictions = model.predict(img_batch)
        scores = tf.nn.softmax(predictions[0])
        category = categories[np.argmax(scores)]
        confidence = np.max(scores) * 100

        # Display results
        st.subheader("Prediction Results")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image, caption=f"Identified: {category.title()}", use_column_width=True)
        with col2:
            st.write(f"### Predicted Category: `{category.title()}`")
            st.write(f"### Confidence: `{confidence:.2f}%`")

        # Additional Information
        info = data_info.get(category, {"image": default_image_url, **default_info})
        st.image(info["image"], caption=f"Example of {category.title()}", use_column_width=True)
        st.markdown(f"### Nutritional Content (per 100g):\n{info['Nutritional Content (per 100g)']}")
        st.markdown(f"### Benefits:\n{info['benefits']}")
        st.markdown(f"### Risks:\n{info['risks']}")

    except Exception as e:
        st.error(f"Error processing image: {e}")

elif text_input:
    text_input_lower = text_input.strip().lower()
    if text_input_lower in categories:
        st.subheader("Text Input Results")
        info = data_info.get(text_input_lower, {"image": default_image_url, **default_info})
        st.image(info["image"], caption=f"Example of {text_input.title()}", use_column_width=True)
        st.markdown(f"### Identified Category: `{text_input.title()}`")
        st.markdown(f"### Nutritional Content (per 100g):\n{info['Nutritional Content (per 100g)']}")
        st.markdown(f"### Benefits:\n{info['benefits']}")
        st.markdown(f"### Risks:\n{info['risks']}")
    else:
        st.error("The entered name does not match any known category. Please check the spelling or try another name.")

else:
    st.warning("Please upload an image or enter a name to get started.")

# Footer
st.markdown("""
---
Developed with ❤️ by Ashwani Baghel using TensorFlow and Streamlit.

""", unsafe_allow_html=True)
