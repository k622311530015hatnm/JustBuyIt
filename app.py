
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Just Buy It",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# SAMPLE ALTERNATIVE PRODUCTS
# -----------------------------
PRODUCTS = {
    "Smartphone": [
        ("Xiaomi Redmi Note", 5000000),
        ("Samsung Galaxy A56", 9000000),
        ("Google Pixel A Series", 12000000),
        ("Samsung Galaxy S FE", 15000000),
    ],
    "Laptop": [
        ("Acer Aspire", 11000000),
        ("Lenovo IdeaPad", 12000000),
        ("ASUS Vivobook", 15000000),
        ("HP Pavilion", 16000000),
    ],
    "Headphones": [
        ("Sony WH-CH520", 1200000),
        ("Soundcore Q30", 1800000),
        ("JBL Tune 770NC", 2200000),
        ("Sony WH-1000XM4", 5500000),
    ],
    "Sneakers": [
        ("Nike Revolution", 1500000),
        ("Adidas Duramo", 1800000),
        ("Converse Chuck Taylor", 1600000),
        ("New Balance 530", 2800000),
    ],
    "Fashion": [
        ("Basic T-shirt", 250000),
        ("Casual Shirt", 500000),
        ("Basic Jeans", 700000),
        ("Hoodie", 900000),
    ],
    "Other": []
}

# -----------------------------
# DESIGN
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Baloo 2', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 8% 8%, rgba(255, 190, 218, .42), transparent 24%),
        radial-gradient(circle at 95% 12%, rgba(171, 225, 255, .55), transparent 25%),
        radial-gradient(circle at 75% 90%, rgba(205, 192, 255, .42), transparent 28%),
        #f8f8ff;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 48px 55px 42px 55px;
    border-radius: 34px;
    background: linear-gradient(120deg, #dff7ff 0%, #e9e1ff 52%, #ffe6f3 100%);
    border: 1px solid rgba(255,255,255,.9);
    box-shadow: 0 18px 50px rgba(105, 118, 180, .15);
    margin-bottom: 28px;
}

.hero:before, .hero:after {
    content: "";
    position: absolute;
    border-radius: 50%;
    opacity: .35;
}

.hero:before {
    width: 180px;
    height: 180px;
    background: #fff;
    right: -50px;
    top: -60px;
}

.hero:after {
    width: 130px;
    height: 130px;
    background: #b9eaff;
    left: -45px;
    bottom: -60px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    background: rgba(255,255,255,.65);
    color: #489dbd;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 2px;
}

.hero-title {
    color: #25345c;
    font-size: 54px;
    line-height: 1.05;
    font-weight: 800;
    margin: 20px 0 12px 0;
}

.hero-title span {
    color: #55a9c7;
}

.hero-description {
    color: #60718b;
    font-size: 19px;
    max-width: 650px;
    line-height: 1.5;
}

.hero-icons {
    position: absolute;
    right: 55px;
    bottom: 35px;
    font-size: 85px;
    transform: rotate(-8deg);
}

.panel {
    background: rgba(255,255,255,.83);
    border: 1px solid rgba(210,220,244,.9);
    border-radius: 28px;
    padding: 28px 32px;
    box-shadow: 0 12px 35px rgba(100, 113, 170, .08);
    margin-bottom: 24px;
}

.section-title {
    color: #27375e;
    font-size: 27px;
    font-weight: 800;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #8290a8;
    font-size: 15px;
    margin-bottom: 20px;
}

[data-testid="stWidgetLabel"] p {
    color: #405174 !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

[data-baseweb="input"],
[data-baseweb="select"],
[data-baseweb="textarea"] {
    background: white !important;
    border-radius: 13px !important;
    border: 1px solid #dbe3f4 !important;
}

[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    color: #263657 !important;
}

.stButton > button {
    width: 100%;
    border: 0;
    border-radius: 18px;
    min-height: 58px;
    color: white !important;
    background: linear-gradient(100deg, #62b6d5, #8f83e9);
    font-size: 18px;
    font-weight: 800;
    box-shadow: 0 9px 22px rgba(115, 139, 221, .28);
}

.stButton > button:hover {
    border: 0;
    color: white !important;
    background: linear-gradient(100deg, #4ca5c6, #796de0);
}

.result-box {
    text-align: center;
    padding: 32px;
    border-radius: 25px;
    background: linear-gradient(135deg, #e2f8f0, #e5f3ff);
    border: 1px solid #c9ebdf;
}

.result-label {
    color: #73918c;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
}

.result-word {
    color: #329d83;
    font-size: 54px;
    font-weight: 800;
    margin: 8px 0;
}

.result-product {
    color: #526c82;
    font-size: 19px;
}

.result-message {
    color: #5c7185;
    font-size: 16px;
    margin-top: 12px;
}

.metric-card {
    background: white;
    border-radius: 22px;
    padding: 22px;
    border: 1px solid #e1e7f5;
    min-height: 130px;
    box-shadow: 0 8px 24px rgba(100, 113, 170, .07);
}

.metric-icon {
    font-size: 28px;
}

.metric-label {
    color: #8793aa;
    font-size: 14px;
    font-weight: 700;
    margin-top: 5px;
}

.metric-value {
    color: #29385d;
    font-size: 28px;
    font-weight: 800;
    line-height: 1.2;
    margin-top: 7px;
}

.metric-note {
    color: #91a0b6;
    font-size: 12px;
}

.score-card {
    background: linear-gradient(135deg, #fff1fa, #f1edff);
    border: 1px solid #eadcf5;
    border-radius: 25px;
    padding: 25px;
    text-align: center;
}

.score-number {
    color: #8c76d9;
    font-size: 50px;
    font-weight: 800;
}

.alt-card {
    background: white;
    border: 1px solid #e0e6f4;
    border-radius: 22px;
    padding: 22px;
    min-height: 175px;
    box-shadow: 0 8px 24px rgba(100, 113, 170, .06);
}

.alt-name {
    color: #304064;
    font-size: 19px;
    font-weight: 800;
}

.alt-price {
    color: #5b9fc4;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

.alt-saving {
    color: #5fa68d;
    font-size: 14px;
    font-weight: 700;
    margin-top: 8px;
}

.footer {
    text-align: center;
    color: #9ba7bb;
    font-size: 13px;
    padding: 25px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e1e7f5;
    padding: 16px;
    border-radius: 18px;
}

div[data-testid="stMetricLabel"] {
    color: #8290a8 !important;
}

div[data-testid="stMetricValue"] {
    color: #29385d !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ PERSONAL FINANCE · MINDFUL SPENDING</div>
    <div class="hero-title">Think twice.<br><span>Buy wisely.</span></div>
    <div class="hero-description">
        Just Buy It helps you understand your spending habits,
        reflect on your next purchase and discover more affordable options.
    </div>
    <div class="hero-icons">🛍️ ✨</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INPUT FORM
# -----------------------------
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🛍️ Tell us about your purchase</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Fill in a few simple details to get your personal purchase insight.</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input(
        "🛒 What do you want to buy?",
        placeholder="e.g. iPhone 18, sneakers, headphones..."
    )
    category = st.selectbox("🏷️ Product category", list(PRODUCTS.keys()))
    price = st.number_input(
        "💰 Product price (VND)",
        min_value=0,
        value=0,
        step=100000,
        format="%d"
    )
    income = st.number_input(
        "💵 Monthly income (VND)",
        min_value=0,
        value=15000000,
        step=100000,
        format="%d"
    )

with col2:
    savings = st.number_input(
        "🏦 Available savings (VND)",
        min_value=0,
        value=30000000,
        step=100000,
        format="%d"
    )
    usage = st.number_input(
        "📦 Expected usage per month",
        min_value=0,
        max_value=1000,
        value=10,
        step=1
    )
    need = st.slider("💗 How necessary is it?", 1, 5, 3)
    want = st.slider("🔥 How much do you want it?", 1, 5, 3)
    days_wanted = st.number_input(
        "⏳ How many days have you wanted it?",
        min_value=0,
        value=7,
        step=1
    )

st.markdown('</div>', unsafe_allow_html=True)

if st.button("✨ ANALYZE MY PURCHASE", use_container_width=True):
    if not product_name.strip():
        st.error("Please enter a product name.")
    elif price <= 0:
        st.error("Please enter a valid product price.")
    elif income <= 0:
        st.error("Please enter a valid monthly income.")
    else:
        # -----------------------------
        # CALCULATIONS
        # -----------------------------
        price_income = price / income * 100
        work_hours = price / (income / 176)
        cash_burden = price / savings * 100 if savings > 0 else 100
        cost_per_use = price / usage if usage > 0 else price

        financial_score = min(price_income / 100 * 30, 30)
        necessity_score = (5 - need) / 4 * 20
        desire_score = want / 5 * 15
        urgency_score = max(0, (7 - days_wanted) / 7 * 20)
        low_usage_score = max(0, (20 - usage) / 20 * 15)

        impulse_score = round(min(
            financial_score + necessity_score + desire_score +
            urgency_score + low_usage_score, 100
        ), 1)

        if impulse_score >= 70:
            recommendation = "DON'T BUY"
            result_color = "#d76b91"
            message = "This purchase may be strongly influenced by emotion. Consider waiting and reviewing your priorities."
        elif impulse_score >= 45:
            recommendation = "WAIT"
            result_color = "#b58a43"
            message = "You may want to give yourself more time before making the final decision."
        else:
            recommendation = "BUY"
            result_color = "#329d83"
            message = "The calculated impulse score is relatively low. Still, make sure this purchase fits your budget."

        # -----------------------------
        # RESULT
        # -----------------------------
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">✨ Your purchase insight</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">YOUR RECOMMENDATION</div>
            <div class="result-word" style="color:{result_color};">{recommendation}</div>
            <div class="result-product">🛍️ {product_name} · {price:,.0f} VND</div>
            <div class="result-message">{message}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📌 Your key indicators")

        m1, m2, m3, m4 = st.columns(4)

        metrics = [
            ("💰", "Price / Income", f"{price_income:,.1f}%", "Share of monthly income"),
            ("⏱️", "Work Hours", f"{work_hours:,.1f}", "Estimated working hours"),
            ("🏦", "Cash Burden", f"{cash_burden:,.1f}%", "Share of available savings"),
            ("🔥", "Impulse Score", f"{impulse_score}/100", "Reflection score"),
        ]

        for column, (icon, label, value, note) in zip([m1, m2, m3, m4], metrics):
            with column:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # -----------------------------
        # DASHBOARD
        # -----------------------------
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📊 Your personal dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">A visual summary of your financial situation and buying behavior.</div>', unsafe_allow_html=True)

        d1, d2 = st.columns([1, 1])

        with d1:
            st.markdown('<div class="score-card">', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">🔥 EMOTIONAL PURCHASE TENDENCY</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="score-number">{impulse_score}<span style="font-size:22px;">/100</span></div>', unsafe_allow_html=True)
            st.progress(int(impulse_score))
            st.markdown(f'<div class="metric-label">Level: {"High" if impulse_score >= 70 else "Moderate" if impulse_score >= 45 else "Low"}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with d2:
            st.markdown("#### 💸 Money snapshot")
            money_df = pd.DataFrame({
                "Item": ["Product price", "Monthly income", "Available savings"],
                "Amount (VND)": [price, income, savings]
            })
            st.dataframe(money_df, hide_index=True, use_container_width=True)

        st.markdown("#### 🧩 What affects your score?")

        score_df = pd.DataFrame({
            "Factor": [
                "Financial burden",
                "Low necessity",
                "Desire level",
                "Purchase urgency",
                "Low usage"
            ],
            "Score": [
                round(financial_score, 1),
                round(necessity_score, 1),
                round(desire_score, 1),
                round(urgency_score, 1),
                round(low_usage_score, 1)
            ]
        })

        chart_col, table_col = st.columns([1.25, 1])

        with chart_col:
            st.bar_chart(score_df.set_index("Factor"), height=300)

        with table_col:
            st.dataframe(score_df, hide_index=True, use_container_width=True)
            st.metric("Cost per use", f"{cost_per_use:,.0f} VND")

        st.markdown("#### 💗 Your self-assessment")

        behavior_df = pd.DataFrame({
            "Factor": ["Necessity", "Desire"],
            "Score": [need, want]
        })
        st.bar_chart(behavior_df.set_index("Factor"), height=220)

        st.caption("This is an illustrative scoring model for a student project, not a psychological diagnosis.")

        st.markdown('</div>', unsafe_allow_html=True)

        # -----------------------------
        # ALTERNATIVES
        # -----------------------------
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">💡 More affordable alternatives</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Explore sample options that cost less than your selected product.</div>', unsafe_allow_html=True)

        alternatives = [
            {"name": name, "price": item_price}
            for name, item_price in PRODUCTS[category]
            if 0 < item_price < price
        ][:3]

        if alternatives:
            st.success(f"💰 Choosing a cheaper option could save you up to {price - alternatives[0]['price']:,.0f} VND.")

            alt_cols = st.columns(len(alternatives))
            for column, item in zip(alt_cols, alternatives):
                saving = price - item["price"]
                with column:
                    st.markdown(f"""
                    <div class="alt-card">
                        <div class="alt-name">🛍️ {item["name"]}</div>
                        <div class="alt-price">{item["price"]:,.0f} VND</div>
                        <div class="alt-saving">💰 Save {saving:,.0f} VND</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("No cheaper sample products were found in this category.")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="footer">
            Just Buy It · An experimental tool for mindful spending.<br>
            Sample prices are illustrative only.
        </div>
        """, unsafe_allow_html=True)
