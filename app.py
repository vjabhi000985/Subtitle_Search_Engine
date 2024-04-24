import streamlit as st
import chromadb
import time

# load the dataset
path = "db"

client = chromadb.PersistentClient(path=path)
client.heartbeat()
collection = client.get_collection(name="subtitle_sem")
# print(client.heartbeat())

def similar_title(query_text):
    
    result = collection.query(
        query_texts=query_text,
        include=["metadatas", "distances"],
        n_results=5
    )
    ids = result['ids'][0]
    distances = result['distances'][0]
    metadatas = result['metadatas'][0]
    zipped_data = zip(metadatas, ids, distances)
    sorted_data = sorted(zipped_data, key=lambda x: x[1], reverse=True)
    return sorted_data

st.title('🔍 Beyond Keywords: Subtitle Search Revolution')
st.subheader('Tired of video trailer roulette? 😫')
st.subheader('Subtitle search: Your shortcut to the good stuff.🥁')

query_text = st.text_input('Enter your search query:')
search = st.button("Search")
if search:
    result = collection.query(
        query_texts = query_text,
        include=["metadatas", 'distances'],
        n_results=10
    )
    
    with st.spinner('Wait for it...'):
        time.sleep(5)
    
    st.success('Here are the most relevant subtitle names:')
    ids = result['ids'][0]
    distances = result['distances'][0]
    metadatas = result['metadatas'][0]
    zipped_data = zip(ids, distances, metadatas)
    sorted_data = sorted(zipped_data, key=lambda x: x[1], reverse=True)

    for metadata, ids, distance in sorted_data:
        subtitle_name = metadata['subtitle_name']
        subtitle_id = metadata['subtitle_id']
        subtitle_link = f"https://www.opensubtitles.org/en/subtitles/{subtitle_id}"
        st.markdown(f"[{subtitle_name}]({subtitle_link})")