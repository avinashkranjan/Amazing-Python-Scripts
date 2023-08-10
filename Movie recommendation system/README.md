# Movie Recommender System Project
A content based movie recommender system using cosine similarity based on tmdb dataset from kaggle

kaggel link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

This project aims to recommend the different movies based on given input by using machine learning techniques, specifically the cosine_similarity. The model is trained on a dataset containing various features of movie tmdb dataset, such as 'movie_id','title','overview','genres','keywords','cast','crew' and other relevant factors.

## Dataset

The dataset used for this project consists of a collection of all the hollywood movie, each with associated features and the corresponding cast and crew. The dataset is preprocessed to handle missing values, categorical variables, and feature scaling, ensuring the data is suitable for training the recommendation model.  

Dataset link: In the dataset folder(movies.csv) and (credits.csv)
## Algorithm

Based on Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback....

Cosine Similarity: It calculates the Cosine Similarity between the two non-zero vectors. A vector is a single dimesingle-dimensional signal NumPy array. Cosine similarity is a measure of similarity, often used to measure document similarity in text analysis.

ast: It is Abstract Syntax Tree. It contains ast.literal_eval() function. It is used to evaluate trees of the Python abstract syntax grammar. Abstract syntax changes with each python release. Custom parsers are one use case of ast.literal_eval() function.

PorterStemmer: It is used to determine domain vocabularies in domain analysis. Stemming is desirable as it may reduce redundancy as most of the time the word stem and their inflected/derived words mean the same.

## Dependencies

The following dependencies are required to run the project:

-streamlit==1.24.1
-scikit-learn==1.2.1
-pandas==1.5.3
-numpy==1.25.1
-requests==2.31.0


To install the required dependencies, you can use the following command:

```shell
pip install xgboost numpy pandas scikit-learn streamlit
```

## Usage
Clone the repository:
```shell
git clone https://github.com/your-username/Movie-Recommender-System.git
```
Navigate to the project directory:
```shell
cd Movie-Recommender-System
```
Install the dependencies:
```shell
pip install -r requirements.txt
```
Run the Streamlit app:
```shell
streamlit run app.py
```

Open your browser and go to http://localhost:8501/ to access the movie recommendation system app.

Or you can use the deployed project using the link: https://movie-recommender-system-ml-ca6n1lthfcd-kanishka.streamlit.app/

## Disclaimer
The movie recommendation system provided by this project are based on a ml model and may not always accurately reflect the real movies secenerios. The predictions should be used for reference purposes only, and dataset of tmdb from kaggle can vary due to various factors.

## Author

https://github.com/kanishkasah20