import pandas as pd
import streamlit as st
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df=pd.read_csv('./athlete_events.csv')
region_df=pd.read_csv('./noc_regions.csv')

df=preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:image/png;base64,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')

st.sidebar.write("Created by: [Pushkar](https://github.com/PushkarWaykole)")


user_menu=st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)


if(user_menu=='Medal Tally'):
    st.sidebar.header('Medal Tally')
    years,country=helper.country_year_list(df)
    
    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country=st.sidebar.selectbox("Select Country",country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    if medal_tally.empty:
        st.title("No data Available")
    else:
        st.table(medal_tally)
        

if user_menu=='Overall Analysis':
    editions=df['Year'].unique().shape[0]
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athlets=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]
    
    
    st.title("Top Statistics")
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)
        
    col4,col5,col6=st.columns(3)
    with col4:
        st.header('Events')
        st.title(events)
    with col5:
        st.header('Nations')
        st.title(nations)
    with col6:
        st.header('Athletes')
        st.title(athlets)
        
    nations_over_time=helper.data_over_time(df,'region')
    fig=px.line(nations_over_time,x='Edition',y='region',labels={"Edition":"Edition","region":"Nations"})
    st.title("Nations participating over the years")
    st.plotly_chart(fig)
    
    events_over_time=helper.data_over_time(df,'Event')
    fig=px.line(events_over_time,x='Edition',y='Event')
    st.title("Events over the years")
    st.plotly_chart(fig)
    
    athlets_over_time=helper.data_over_time(df,'Name')
    fig=px.line(athlets_over_time,x='Edition',y='Name',labels={"Edition":"Edition","Name":"Number of Athletes"})
    st.title("Athletes over the years")
    st.plotly_chart(fig)
    
    
    st.title("Number of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)
    
    st.title("Most Successful Athletes")
    sports_list=df['Sport'].unique().tolist()
    sports_list.sort()
    sports_list.insert(0,"Overall")
    
    selected_sport=st.selectbox("Select a Sport",sports_list)
    x=helper.most_successful(df,selected_sport)
    st.table(x)
    
if user_menu=='Country-wise Analysis':
    
    st.title("Country wise Analysis")
    country_list=df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country=st.selectbox("Select a Country",country_list)

    country_df=helper.yearwise_medal_tally(df,selected_country)
    fig=px.line(country_df,x='Year',y='Medal')
    st.title(selected_country+" Medal Tally over the years")
    st.plotly_chart(fig)
    
    st.title(selected_country+" excels in the following sports")
    pt=helper.country_event_heatmap(df,selected_country)

    if(pt.empty):
        st.title("No records found")
    else:
        fig,ax = plt.subplots(figsize=(20,20))
        ax=sns.heatmap(pt,annot=True)
        st.pyplot(fig)
    
    st.title("Top 10 Athletes of "+selected_country)
    top10=helper.most_successful_countrywise(df,selected_country)
    st.table(top10)
    
if user_menu=='Athlete wise Analysis':
    
    
    
    athlet_df=df.drop_duplicates(subset=['Name','region'])

    x1=athlet_df['Age'].dropna()
    x2=athlet_df[athlet_df['Medal']=='Gold']['Age'].dropna()
    x3=athlet_df[athlet_df['Medal']=='Silver']['Age'].dropna()
    x4=athlet_df[athlet_df['Medal']=='Bronze']['Age'].dropna()

    fig=ff.create_distplot([x1,x2,x3,x4],['Overall Age','Gold Medalist','Silver Medalist','Bronze Medalist'],show_hist=False,show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)
    
    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    
    for sport in famous_sports:
        temp_df = athlet_df[athlet_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)
    
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
    

