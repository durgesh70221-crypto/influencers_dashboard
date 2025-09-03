import streamlit as st
import pandas as pd
import altair as alt

data = """
Name / Handle,Platform,"Followers / Subscribers Count",Category / Niche,Contact Information
Priyanka Mishra,Instagram,156.9K,"Online trainers",N/A
Sumit Varyani,Instagram,N/A,"Photography, Travel & Food",N/A
Nuzhat Parween,Instagram,124.7K,Cricket,N/A
Shriya Gullah,Instagram,143.4K,"Makeup / Beauty",N/A
Khushhali Sharma,Instagram,141.7K,N/A,N/A
Mehak Smoker,Instagram,157.4K,VJs & RJs,N/A
Anushka Bajpayee,Instagram,N/A,"Fashion, Lifestyle, Model",anushkabajpayee@gmail.com
Annie Jain,Instagram,489.7K,Appliance Reviewers,N/A
Naini Jain,Instagram,250.1K,"Family, Kids & Pets",N/A
ARISH GOUR,Instagram,205.2K,"Pets & Animals",N/A
Renuka Pahade,Instagram,198.5K,Fitness,N/A
Shiway,Instagram,196.1K,Freestylers,N/A
Bhopali Points,Instagram,206.9K,Vloggers,N/A
Arpita,Instagram,46.9K,Food,N/A
Shatakshi Rai,Instagram,30.8K,"Food, Fashion",N/A
Mayuriii,Instagram,25.8K,Fashion,N/A
Rohan Pathak,Instagram,25.2K,N/A,N/A
Kamal Batham,Instagram,24K,"Arts, Doodling & Painting",N/A
Akash Pandey,Instagram,23.6K,N/A,N/A
Vikash Malviya,Instagram,21.7K,Fashion,N/A
Divyani Ghosh,Instagram,24.2K,N/A,N/A
Sudeep Shah,Instagram,19.2K,N/A,N/A
Anurag Dhakad,Instagram,18.9K,N/A,N/A
Anshu Samraat MandLekar,Instagram,18.5K,"Family, Kids & Pets",N/A
Divyanshi_Das,Instagram,18.1K,N/A,N/A
Shalinni,Instagram,18.4K,N/A,N/A
Kartik Swamy,Instagram,16.6K,"Travel & Places",N/A
Pratibha Sahu,"Instagram, YouTube",N/A,"Dancer, Fashion Designer",N/A
Harshita Rajak,YouTube,23.7K,"Beauty, Fashion, Lifestyle",N/A
Yogesh Sharma,YouTube,244K,"Travel, Vlogs",Yogeshsharmadance@gmail.com
Wanderlust Shashank,YouTube,N/A,"Travel, Vlogs",N/A
IFRAH,Instagram,19.9K,"Crafts & DIY Arts",N/A
Shefali Alvares Rashid,Instagram,57K,Musicians,N/A
Nir Addie,Instagram,53.6K,N/A,N/A
Mamta,Instagram,49.3K,"Family, Kids & Pets",N/A
Arish,Instagram,46.8K,"Pets & Animals",N/A
Laaraib Siddique,Instagram,41.1K,Musicians,N/A
Syed Mehboob Ali,Instagram,40.6K,N/A,N/A
Shryansh Bisen,Instagram,36.3K,VJs & RJs,N/A
deepbellus makeup,Instagram,34.3K,Makeup,N/A
saloni chouksey,Instagram,33K,"Family, Kids & Pets",N/A
THE BHOPAL,Instagram,33.6K,"City-focused, Travel & Places",N/A
SUBHAN UDDIN,Instagram,30.3K,N/A,N/A
"""

def parse_followers(follower_str):
    if pd.isna(follower_str) or not isinstance(follower_str, str):
        return 0
    lower_str = follower_str.lower()
    if 'k' in lower_str:
        return float(lower_str.replace('k', '')) * 1000
    if 'm' in lower_str:
        return float(lower_str.replace('m', '')) * 1000000
    try:
        return int(follower_str)
    except (ValueError, TypeError):
        return 0

df = pd.read_csv(pd.io.common.StringIO(data.strip()))
df.columns = df.columns.str.strip()
df['Followers / Subscribers Count'] = df['Followers / Subscribers Count'].apply(parse_followers)
df = df.dropna(subset=['Name / Handle', 'Followers / Subscribers Count'])
df = df[df['Followers / Subscribers Count'] > 0]

def get_tier(followers):
    if 100000 <= followers <= 500000:
        return 'Mid-tier'
    if 15000 <= followers < 100000:
        return 'Micro'
    if 5000 <= followers < 15000:
        return 'Nano'
    return 'Other'

df['Tier'] = df['Followers / Subscribers Count'].apply(get_tier)
df['Category / Niche'] = df['Category / Niche'].fillna('General').str.strip()
df['Contact Available'] = df['Contact Information'].apply(lambda x: 1 if pd.notna(x) and x != 'N/A' else 0)

st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
        }
        .metric-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .metric-title {
            font-size: 1.125rem;
            color: #8a7a6a;
            font-weight: 500;
        }
        .metric-value {
            font-size: 2.5rem;
            color: #6d5d4d;
            font-weight: 700;
        }
        .card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align: center; color: #6D5D4D; font-size: 3rem; font-weight: 700;">Bhopal Influencer Hub</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #8A7A6A; font-size: 1.25rem;">An interactive dashboard to explore content creators in Bhopal</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<p style="text-align: center; color: #6D5D4D; font-size: 1rem; margin-top: 1rem;">This dashboard provides a comprehensive overview of the influencer landscape in Bhopal, based on the provided report data. Use the filters below to dynamically explore creators by their platform, niche, and follower size. The charts and influencer list will update in real-time to help you identify the perfect match for your campaigns.</p>', unsafe_allow_html=True)
    
    st.markdown("---")

search_term = st.text_input("Search by name...", key='search')

col1, col2, col3 = st.columns(3)
with col1:
    platform_filter = st.selectbox("Platform", ["All Platforms"] + sorted(df['Platform'].unique().tolist()), key='platform')
with col2:
    niche_filter = st.selectbox("Niche", ["All Niches"] + sorted(df['Category / Niche'].unique().tolist()), key='niche')
with col3:
    tier_filter = st.selectbox("Tier", ["All Tiers", "Nano", "Micro", "Mid-tier", "Other"], key='tier')

filtered_df = df.copy()

if search_term:
    filtered_df = filtered_df[filtered_df['Name / Handle'].str.contains(search_term, case=False)]
if platform_filter != "All Platforms":
    filtered_df = filtered_df[filtered_df['Platform'] == platform_filter]
if niche_filter != "All Niches":
    filtered_df = filtered_df[filtered_df['Category / Niche'] == niche_filter]
if tier_filter != "All Tiers":
    filtered_df = filtered_df[filtered_df['Tier'] == tier_filter]

st.markdown("---")

col1_metrics, col2_metrics, col3_metrics = st.columns(3)
with col1_metrics:
    st.markdown(f'<div class="metric-card"><div class="metric-title">Total Influencers</div><div class="metric-value">{len(filtered_df)}</div></div>', unsafe_allow_html=True)
with col2_metrics:
    avg_followers = filtered_df['Followers / Subscribers Count'].mean() if not filtered_df.empty else 0
    st.markdown(f'<div class="metric-card"><div class="metric-title">Avg. Followers</div><div class="metric-value">{(avg_followers/1000):.1f}K</div></div>', unsafe_allow_html=True)
with col3_metrics:
    contact_count = filtered_df['Contact Available'].sum()
    st.markdown(f'<div class="metric-card"><div class="metric-title">Contact Info Available</div><div class="metric-value">{contact_count}</div></div>', unsafe_allow_html=True)

st.markdown("---")

chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.markdown('<h3 style="text-align: center; color: #6D5D4D; font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Influencers by Niche</h3>', unsafe_allow_html=True)
    niche_counts = filtered_df['Category / Niche'].value_counts().head(10).reset_index()
    niche_counts.columns = ['Niche', 'Count']
    chart = alt.Chart(niche_counts).mark_bar().encode(
        y=alt.Y('Niche', sort='-x', title=None),
        x=alt.X('Count', title='Number of Influencers'),
        tooltip=['Niche', 'Count'],
        color=alt.value('#D1C7B9')
    ).properties(
        width='container'
    )
    st.altair_chart(chart, use_container_width=True)

with chart_col2:
    st.markdown('<h3 style="text-align: center; color: #6D5D4D; font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Platform Distribution</h3>', unsafe_allow_html=True)
    platform_counts = filtered_df['Platform'].value_counts().reset_index()
    platform_counts.columns = ['Platform', 'Count']
    chart = alt.Chart(platform_counts).mark_arc(outerRadius=120).encode(
        theta=alt.Theta('Count', stack=True),
        color=alt.Color('Platform', scale=alt.Scale(range=['#E8C3B9', '#B9AD9E'])),
        tooltip=['Platform', 'Count']
    ).properties(
        width='container'
    )
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.markdown('<h3 style="color: #6D5D4D; font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Influencer Profiles</h3>', unsafe_allow_html=True)

if filtered_df.empty:
    st.info("No influencers found matching your filters.")
else:
    cols_per_row = 4
    num_rows = (len(filtered_df) + cols_per_row - 1) // cols_per_row
    
    for i in range(num_rows):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            idx = i * cols_per_row + j
            if idx < len(filtered_df):
                influencer = filtered_df.iloc[idx]
                with cols[j]:
                    st.markdown(f'<div class="card">', unsafe_allow_html=True)
                    st.markdown(f'<h4 style="font-size: 1.25rem; font-weight: 600; color: #6D5D4D; margin-bottom: 0.5rem; line-height: 1.5;">{influencer["Name / Handle"]}</h4>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 0.875rem; color: #8a7a6a; margin-bottom: 0.25rem;"><strong>Platform:</strong> {influencer["Platform"]}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 0.875rem; color: #8a7a6a; margin-bottom: 0.25rem;"><strong>Followers:</strong> {influencer["Followers / Subscribers Count"] / 1000:.1f}K</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 0.875rem; color: #8a7a6a; margin-bottom: 0.25rem;"><strong>Niche:</strong> {influencer["Category / Niche"]}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 0.875rem; color: #8a7a6a; margin-bottom: 0.25rem;"><strong>Tier:</strong> {influencer["Tier"]}</p>', unsafe_allow_html=True)
                    
                    if pd.notna(influencer['Profile URL']) and influencer['Profile URL'].strip():
                        st.markdown(f'<a href="{influencer["Profile URL"]}" target="_blank" style="display: block; width: 100%; text-align: center; background-color: #B9AD9E; color: white; padding: 0.5rem; border-radius: 0.5rem; margin-top: 1rem; text-decoration: none;">View Profile</a>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="background-color: #e0e0e0; color: #a0a0a0; text-align: center; padding: 0.5rem; border-radius: 0.5rem; margin-top: 1rem;">No Profile</div>', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
