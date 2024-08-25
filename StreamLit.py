import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as com
com.iframe("https://lottie.host/embed/da10ef94-760b-4df4-b250-501989b789b7/XFuDbCwnGu.json")
# CSS để ẩn "Made with Streamlit"
# st.markdown("""
# <style>
# .st-emotion-cache-yfhhig.ef3psqc5 {
#     visibility: hidden;            
# }
# </style>
# """, unsafe_allow_html=True)
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://images.pexels.com/photos/2086917/pexels-photo-2086917.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
  background-size: cover;
}

h2 {
    font-family: 'Arial', sans-serif;
    color: #FFFFFF;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    text-shadow: 2px 2px 5px #000000;
    margin-bottom: 20px;
}

input[type="text"], textarea {
    background-color: rgba(0,0,0,1);
}

.stTextArea [data-baseweb=base-input] {
    background-image: linear-gradient(140deg, rgb(0, 0, 0) 0%, rgb(0,0,0) 50%, rgb(0,0,0) 75%);
}

div.stButton > button {
    background-color: green;
    color: white;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Tạo menu bên trái
menu = st.sidebar.radio(
    "Thông tin về các buổi Seminar",
    ("Buổi 1", "Buổi 2", "Buổi 3", "Buổi 4", "Buổi 5", "Buổi 6")
)

# Hiển thị nội dung theo lựa chọn của người dùng
if menu == "Buổi 1":
    st.markdown("<h2>Thông tin Seminar From Math to AI Buổi 1</h2>", unsafe_allow_html=True)
    st.write("""
    **Friday, 19/7/2024:**

    - 8.30-9.00 am: Registration and Ceremony

    - 9.00-9.30 am: **Hoàng Phi Dũng** (PTIT): Math and AI, the picture

    - 9.30-10.00 am: **Bùi Quang Đạt** (D22 Computer Science-PTIT): Matrix analysis, gradient of vector-valued function.

    - 10.00-10.45 am: **Nguyễn Hồng Đức** (Master at Tokyo Univ.): Applied Math + AI and problems of self-driving cars.

    **Abstract:** Some problems: Ground segmentation (phân tách mặt phẳng), Simultaneous Localization and Mapping (định vị và lập bản đồ đồng thời), Object detection and tracking (phát hiện và theo dấu vật thể).

    - 10.45 am: Discussion.
    """)

elif menu == "Buổi 2":
    st.markdown("<h2>Thông tin Seminar From Math to AI Buổi 2</h2>", unsafe_allow_html=True)
    st.write("""
    **Thursday, 25/7/2024**

    - 8.30-8.50 am: **Nguyen Manh Cong** (D23 Security-PTIT), Some probability distributions.

    - 9.00-9.45 am: **Tran Van Khanh** (D23 Information Technology-PTIT): Linear Algebra and Linear regression.

    - 9.55 am: Discussion.
    """)

elif menu == "Buổi 3":
    st.markdown("<h2>Thông tin Seminar From Math to AI Buổi 3</h2>", unsafe_allow_html=True)
    st.write("""
    **Thursday, 01/8/2024**

    - 8.30-8.50 am: **Nguyen Manh Cong** (D23 Security-PTIT), Some probability distributions 2.

    - 9.00-9.30 am: **Dao Binh Minh** (D23 Computer Science-PTIT): On the Maximum likelihood.

    - 9.30 am: Discussion.
    """)

elif menu == "Buổi 4":
    st.markdown("<h2>Thông tin Seminar From Math to AI Buổi 4</h2>", unsafe_allow_html=True)
    st.write("""
    **Thursday, 15/08/2024 - 9.00 am at 206-A2, PTIT**

    - 9.00-9.30 am: **Le Khanh Chi** (College of Science and Engineering, University of Minnesota, US): Retrieval-Augmented Generation.

    **Abstract:** In this talk, we will discuss about RAG (Retrieval-Augmented Generation). RAG is an AI framework that combines the strengths of traditional information retrieval systems (such as databases) with the capabilities of generative large language models (LLMs).

    - 10.00-10.20 am: **Nguyen Manh Hung** (D20 Information Technology-PTIT): 3D View Synthesis: Exploring NeRF and Applications in Real-Time Interactive Virtual Portraits.

    - 10.30 am: Discussion.
    """)

elif menu == "Buổi 5":
    st.markdown("<h2>Thông tin Seminar From Math to AI Buổi 5</h2>", unsafe_allow_html=True)
    st.write("""
    **Thursday, 22/08/2024 - 9.00 am at 206-A2, PTIT**

    - 9.00-9.20 am: **Nguyen Thi Hien** (D22 IT - PTIT): Logistic regression.

    Abstract: In this talk, we will discuss about logistic regression, a fundamental statistical method widely used for binary classification problems.

    - 9.30-10.30 am: **Bui Quang Dat** (D22 Computer Science - PTIT): Anomaly Detection.

    Abstract: Explore anomaly detection techniques to identify unusual data patterns and enhance system reliability.  
    """)

elif menu == "Buổi 6":
    st.markdown("<h2>Đăng Ký Seminar From Math to AI Buổi 6</h2>", unsafe_allow_html=True)
    
    # Form để thu thập thông tin cho Buổi 6
    with st.form(key='registration_form'):
        name = st.text_input('Họ và tên:', help='Nhập họ và tên của bạn', placeholder='Nhập họ và tên của bạn')
        student_id = st.text_input('Mã sinh viên:', help='Nhập mã sinh viên của bạn', placeholder='Nhập mã sinh viên của bạn')
        class_name = st.text_input('Lớp:', help='Nhập lớp của bạn', placeholder='Nhập lớp của bạn')
        title = st.text_input('Title:', help='Nhập tiêu đề bài thuyết trình', placeholder='Nhập tiêu đề bài thuyết trình')
        abstract = st.text_area('Abstract:', help='Nhập tóm tắt nội dung', placeholder='Nhập tóm tắt nội dung')
        time = st.text_input('Thời gian chia sẻ:', help='Nhập thời gian chia sẻ', placeholder='Nhập thời gian chia sẻ')
        
        # Nút submit
        submit_button = st.form_submit_button(label='Submit')

    # Khi người dùng nhấn Submit
    if submit_button:
        # Tạo một DataFrame từ thông tin người dùng nhập vào
        data = {
            'Họ và tên': [name],
            'Mã sinh viên': [student_id],
            'Lớp': [class_name],
            'Title': [title],
            'Abstract': [abstract],
            'Thời gian chia sẻ': [time]
        }
        df = pd.DataFrame(data)

        # Lưu thông tin vào file Excel
        file_name = 'AI_Buoi6.xlsx'
        
        # Kiểm tra xem file có tồn tại hay không, nếu có thì ghi thêm vào file
        if os.path.exists(file_name):
            df_existing = pd.read_excel(file_name)
            df = pd.concat([df_existing, df], ignore_index=True)
        
        df.to_excel(file_name, index=False)

        # Thông báo rằng dữ liệu đã được lưu
        st.success('Thông tin của bạn đã được lưu thành công!')
