import streamlit as st
import requests
import io
from PIL import Image

st.title("YOLO Object Detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Convert the image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    if st.button("Upload and Predict"):
        try:
            # Send the image to the storage service
            upload_response = requests.post("http://127.0.0.1:8001/upload", files={"file": ("image.jpg", img_bytes)})
            
            if upload_response.status_code == 200:
                st.success("Image uploaded successfully.")
                upload_data = upload_response.json()
                filepath = upload_data['filepath']
                
                # Send the image to the prediction service
                predict_response = requests.post("http://127.0.0.1:8000/predict", files={"file": ("image.jpg", img_bytes)})
                
                # Display the prediction results
                if predict_response.status_code == 200:
                    st.image(predict_response.content, caption='Predicted Image.', use_column_width=True)
                else:
                    st.error(f"Error: Could not get prediction. Status code: {predict_response.status_code}")
                    st.error(f"Response content: {predict_response.text}")
            else:
                st.error(f"Error: Could not upload image. Status code: {upload_response.status_code}")
                st.error(f"Response content: {upload_response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to services: {e}")
