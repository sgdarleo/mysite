# pip install streamlit
#pip install streamlit_lottie
#pip install requests
#pip install Pillow (for images display)

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image



#Set page configuration like title of page and icons
#By default, strealit layout is set as "Centre". Can set layout to "wide"
st.set_page_config(page_title="Darren Leow page", page_icon=":sparkles:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Using Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# ASSETS
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_hcwpcdew.json")
HKEX_img = Image.open("images/HKEX.webp")
SGX_img = Image.open("images/SGX.png")
iserve = Image.open("images/i-serve.png")
hocoma = Image.open("images/hocoma.png")
dih = Image.open("images/DIH.png")
hengxin = Image.open("images/hengxin.jpg")
pharmesis = Image.open("images/pharmesis.jpg")
deloitte = Image.open("images/deloitte.png")
moppetto = Image.open("images/moppetto.png")

#-----HEADER SECTION

with st.container():
# -- Wrapping contents within a container --
    st.subheader("Hi, I am Darren Leow :wave:")
# original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
    st.write("##")
    st.markdown('<div style="text-align: justify; font-size: 40px; font-weight: bold; line-height: 100%">Accountant, Strategic Planner, IPO specialist, Corporate Governance advisor, Team leader, Internal controls, Tax and Transfer Pricing</div>', unsafe_allow_html=True)
    st.write("##")
    st.markdown('<div style="text-align: justify; font-size: 18px; font-weight: normal; line-height: 1.6">I am passionate about building businesses from the ground up. I have extensive experience in working with Boards, teams and management from many countries spanning from Asia, Europe, US and South America.</div>', unsafe_allow_html=True)
    st.write("")
    st.write("[More about me >](https://www.linkedin.com/in/darleosg/)")

# ---- What I do

with st.container():
# -- Wrapping contents within a container --

    # DIVIDER
    st.write("---")
    # Creating 2 columns
    left_column, right_column = st.columns(2)

    # --Left column__
    with left_column:
        st.header("What I do")
        # Creating a space between the lines
        st.write("##")
        st.markdown('<div style="text-align: justify; font-size: 16px; font-weight: normal; line-height: 1.6">I thrive in a roll-up-your-sleeves, fast-paced growth environment where there are multitude of challenges all happening at once. Skillful in bringing to the fore the best in individuals and teams to outperform, unabating devotion to seek efficiencies in laying out long term sustainability, somewhat a perfectionist but an inclination to macro-manage. Well-versed in investor relations, fundraising and IPOs.</div>', unsafe_allow_html=True)
        st.write("##")
        # st.write("[My e-commerce platform](https://www.moppetto.com)")

    # --Right column__
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# --- PAST EXPERIENCES ---

# DIVIDER
st.write("---")
st.header("Experiences")

# Creating a space between the lines
st.write("##")

with st.container():
# -- Wrapping contents within a container --

    # Creating 2 columns
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(moppetto, width=150)

    with text_column:
        st.subheader("[Founder/Director: 2018-present](https://www.moppetto.com)")
        st.write(
            """
            - E-commerce platform for Academia and Familial-related activities
            """
        )


# Creating a space between the lines
# st.write("##")
st.write("---")
st.write("##")
with st.container():
# -- Wrapping contents within a container --

    # Creating 2 columns
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(iserve, width=50)

    with text_column:
        st.subheader("[Chief Financial Officer: 2018-2021](https://i-serve.com.my)")
        st.write(
            """
            - Payment gateway & fintech related business
            - Offline air-ticketing sales
            - IPO/Fundraising/investor relations
            """
        )

st.write("##")
st.write("---")
st.write("##")
# --- DIH ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(dih, width=150)
    with text_column:
        st.subheader("[Global CFO: 2017-2018](https://www.dih.com)")
        st.write(
            """
            Robotics Rehabilitation equipment manufacture, marketing and sale with offices in Asia, Europe, US and South America.
            """
        )


st.write("##")

# --- HOCOMA ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(hocoma, width=150)
    with text_column:
        st.subheader("[VP Finance: 2017-2018](https://www.hocoma.com)")
        st.write(
            """
            A Swiss-made brand of robotics rehabilitation equipment as part of the DIH Group
            """
        )

st.write("##")
st.write("---")
st.write("##")
# --- HKEX ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(HKEX_img, width=150)
    with text_column:
        st.subheader("[HKEX IPO: 2010](https://www.hkex.com.hk/?sc_lang=en)")
        st.write(
            """
            Led the complete process from start to end for a Dual-Primary listing in Hong Kong
            """
        )

st.write("##")

# --- HENGXIN ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(hengxin, width=150)
    with text_column:
        st.subheader("[Chief Financial Officer: 2007-2017](https://www.hengxin.com)")
        st.write(
            """
            A telecoms ancillary equipment manufacturer in China with its an secondary assembly located in Mumbai, India
            """
        )

st.write("##")
st.write("---")
st.write("##")
# --- SGX ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(SGX_img, width=150)
    with text_column:
        st.subheader("[SGX IPO: 2004](https://www.sgx.com/)")
        st.write(
            """
            Commence IPO process in April and successfully listed in October the same year.
            """
        )

st.write("##")

# --- PHARMESIS ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(pharmesis, width=150)
    with text_column:
        st.subheader("[Financial Controller: 2004-2007](https://www.pharmesis.com/)")
        st.write(
            """
            A pharmaceutical company based in China specialising in both Eastern and Western OTC and Prescribe medicines.
            """
        )

st.write("##")
st.write("---")
st.write("##")
# --- DELOITTE ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(deloitte, width=150)
    with text_column:
        st.subheader("[Deputy Manager: 1999-2004](https://www2.deloitte.com/sg/en.html)")
        st.write(
            """
            Specialised in external audit of companies across a broad spectrum of industries.
            """
        )

st.write("##")

#--- CONTACT ---
with st.container():
    st.write("---")
    st.header("Get in touch!")
    st.write("##")

    # Documentation: https://formsubmit.co/
    # --- Turn off recaptcha field at 2nd line ---
    contact_form = """
    <form action="https://formsubmit.co/darleo@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">    
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    l_column, r_column = st.columns(2)
    with l_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with r_column:
        st.empty()