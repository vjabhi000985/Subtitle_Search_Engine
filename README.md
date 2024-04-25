# Subtitle_Search_Engine
The subtitle based search engine leverages pre-trained sentence transformers (all-MiniLM-L6-v2) to understand subtitle meaning. Text preprocessing and efficient encoding enable semantic search, allowing users to find subtitles based on concepts, not just keywords. It utilizes database indexing for fast retrieval.

## The Challenge:
Finding relevant information within videos can be cumbersome. Traditional search engines often struggle to capture the nuances of spoken language.

## The Solution: 
This project delves into the world of Natural Language Processing (NLP) and Semantic Search to unlock the power of video subtitles.

## Here's the Breakdown:
- `Embracing Subtitles`: We leverage video subtitles as a rich source of textual information.
- `Taming the Text`: Text preprocessing techniques clean and prepare the subtitle data for further analysis.
- `Vectorization Magic`: We transform the subtitles into numerical representations (embeddings) that machines can understand. Here, I've specifically utilized BERT Embeddings, known for their ability to capture semantic meaning and context.
- `ChromaDB`: The Powerhouse: ChromaDB, a specialized database, stores these embeddings efficiently and allows for metadata inclusion for enhanced searchability.
- `Cosine Similarity`: Finding the Perfect Match: This mathematical technique helps us identify videos most relevant to a user's query by comparing the user's query vector to the video subtitle vectors.

## The Impact:
- `Enhanced Accuracy & Relevance`: By focusing on subtitle content, we aim to significantly improve the accuracy and relevance of video search results.
- `Improved User Experience`: This approach promises a more intuitive and user-friendly search experience for everyone.
- `Increased Accessibility`: Unlocking video information through subtitles empowers a wider audience to access the vast knowledge within video content.

## Screenshots:
1. ![Screenshot (182)](https://github.com/vjabhi000985/Subtitle_Search_Engine/assets/46738718/3c8d2732-c786-41e5-8cae-ffad43391155)
2. ![Screenshot (183)](https://github.com/vjabhi000985/Subtitle_Search_Engine/assets/46738718/5fbfed73-c1db-4894-abb3-54e62a554708)

## Demonstration url: https://youtu.be/CPh3WonOLPw?si=4wCZPlbI9TNFtWX5
