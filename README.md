🎬 Movie Recommender System
<img width="1352" height="653" alt="Screenshot 2026-04-08 095016" src="https://github.com/user-attachments/assets/b1de77b2-a824-4233-a99e-891e7b581dec" />

1. 📌 Introduction

The Movie Recommender System is a machine learning-based web application that suggests movies to users based on their interests. It uses a content-based filtering approach to recommend movies similar to the one selected by the user.
The system is built using Python and deployed using Streamlit, providing an interactive and user-friendly interface.


2. 🎯 Objective

To build a recommendation system that suggests similar movies
To provide an interactive UI for users
To integrate external API for fetching movie posters
To understand and implement content-based filtering


3. 🧠 Methodology

The system uses Content-Based Filtering, which recommends items based on similarity between movie features.
Steps involved:

Data collection (movie dataset)
Data preprocessing
Feature extraction (genres, keywords, cast, crew)
Vectorization using techniques like CountVectorizer
Similarity calculation using cosine similarity
Recommendation generation


4. 🏗️ System Architecture

User Input → Streamlit UI → Recommendation Function → Similarity Matrix
         → Fetch Posters (API) → Display Results


5. 🛠️ Technologies Used

Python – Core programming
Pandas – Data manipulation
Scikit-learn – ML algorithms & similarity
Streamlit – Web app framework
Pickle – Model storage
TMDB API – Fetch movie posters


6. 📂 Project Structure

Movie-Recommender/
│
├── app.py                # Main application
├── model/
│   ├── movie_list.pkl   # Movie dataset
│   └── similarity.pkl   # Similarity matrix
│
├── requirements.txt
└── README.md


7. ⚙️ Implementation Details

🔹 Data Preprocessing
Removed null values
Combined relevant features (genres, cast, crew, keywords)
Converted text data into vectors
🔹 Model Building
Used CountVectorizer to convert text into numerical vectors
Calculated similarity using cosine similarity
🔹 Recommendation Logic
Find selected movie index
Sort similarity scores
Return top 5 similar movies


8. 🌐 API Integration

The system uses TMDB (The Movie Database) API to fetch movie posters.
Steps:
Send request using movie ID
Extract poster_path
Construct full image URL


9. 💻 User Interface

Built using Streamlit
Dropdown to select movies
Button to trigger recommendation
Displays posters and movie titles

10. 📸 Output

Displays 5 recommended movies
Shows corresponding posters
Clean and interactive layout


11. ⚠️ Challenges Faced

Handling missing or incorrect movie IDs
API timeout issues
Data preprocessing complexity
UI alignment in Streamlit


12. 🚀 Future Enhancements

Add movie ratings and reviews
Include trailer links
Implement hybrid recommendation system
Improve UI/UX design
Deploy on cloud platforms


13. ✅ Conclusion

The Movie Recommender System successfully demonstrates how machine learning can be used to provide personalized recommendations. It is efficient, scalable, and user-friendly.


14. 📚 References

TMDB API Documentation
Scikit-learn Documentation
Streamlit Documentation


15. 👤 Author

Ujala Soni
