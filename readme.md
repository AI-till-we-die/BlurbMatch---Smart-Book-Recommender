# BlurbMatch - Smart Book Recommender

![Screenshot 2025-01-06 195345](https://github.com/user-attachments/assets/a50aa93a-54bf-4552-9751-8a9a305d0ee3)

![Screenshot 2025-01-05 153140](https://github.com/user-attachments/assets/79ed5bec-f440-453b-958c-0e0b9dfabd1c)


## Project Description

BlurbMatch is a web-based book recommender system that leverages Natural Language Processing (NLP) techniques to provide users with relevant book suggestions. Instead of relying on full, often lengthy, book descriptions, BlurbMatch focuses on analyzing the concise book blurbs found on the back cover. By extracting key features like character details and the main conflict from these blurbs, our system efficiently identifies books that share similar themes and narrative elements, offering a fast and relevant recommendation experience.

This project utilizes Django for the backend and a combination of HTML, CSS, and JavaScript for the frontend. It employs libraries such as NLTK, scikit-learn, and pandas in the backend for text processing and machine learning tasks, and a transformer model for computing similarity. This approach allows for an increase in performance without much of a compromise to relevancy while also being scalable and maintainable.

## Key Features

*   **NLP-Powered Recommendations:** Uses advanced NLP techniques to analyze book blurbs, including preprocessing, tokenization, stop word removal, and lemmatization.
*   **Efficient TF-IDF Model:** Implements a TF-IDF vectorizer to create numerical representations of book blurbs and calculate the cosine similarities.
*  **Transformer Similarity Computation:** Leverages the `all-mpnet-base-v2` Sentence Transformer model for enhanced similarity detection in case you need it.
*   **Dynamic Book Recommendations:** Provides a dynamic list of the recommended books based on user input.
*   **User-Friendly Web Interface:** A simple, responsive web interface where users can enter a book blurb and receive similar book recommendations.
*   **Dynamic Styling:** Styles the output dynamically by making sure the title of the book is in purple using javascript.

## Interface

The user interface of BlurbMatch is designed to be straightforward and intuitive. The main page includes the following elements:

1.  **Input Area**: A text area for users to paste a book blurb.
2.  **Submit Button**: Initiates the search for similar books based on the provided blurb. It also has a loading spinner, which appears while the system is processing the request.
3.  **Results Section**: Displays the list of recommended books and their descriptions using a clear, themed format. The book titles are displayed in purple for better visibility.

## Technology Used

*   **Frontend:** HTML, CSS, JavaScript.
*   **Backend:** Django, Python.
*   **NLP Libraries:** NLTK for text processing, scikit-learn for TF-IDF vectorization and cosine similarity, pandas for data handling, and `sentence-transformers` for transformer-based embedding generation.
*    **Transformer Model**: `all-mpnet-base-v2` Sentence Transformer model.
*   **Data:** `translated_dataset.csv` that is a CSV file containing book titles, pre-processed descriptions and original book titles.

## Project Structure
```
blurbmatch/
├── manage.py
├── myproject/
│ ├── settings.py
│ └── urls.py
├── myapp/
│ ├── views.py
│ └── urls.py
├── preprocessing/
│ ├── model_integration.py
│ └── preprocessing.ipynb
├── templates/
│ └── main.html
├── static/
│ ├── style.css
│ └── js/
│ └── main.js
└── translated_dataset.csv
```

*   `manage.py`: Django's command-line utility for administrative tasks.
*   `myproject/`: The main Django project directory.
    *   `settings.py`: Contains the project settings.
    *   `urls.py`: Contains the project-level URL configurations.
*   `myapp/`: The Django app directory.
    *   `views.py`: Handles the application's logic and views.
    *   `urls.py`: Contains the app-level URL configurations.
*   `preprocessing/`: Directory containing the machine learning modules.
    *   `model_integration.py`: Contains the logic to load the dataset, build the tf-idf model and recommend the books.
*  `templates/`: Directory for the HTML template.
    *   `main.html`: The main HTML template.
*   `static/`: Directory for static assets (CSS, JavaScript, images).
    *  `style.css`: Contains the CSS style of the website.
    *    `js/main.js`: Contains the main javaScript code.
*   `translated_dataset.csv`: The dataset containing the translated book blurbs used to create the model.

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/blurbmatch.git
    cd blurbmatch
    ```
2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv env
    source env/bin/activate   # On Linux/macOS
    env\Scripts\activate  # On Windows
    ```
3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```
5.  **Access the application in your web browser** at `http://127.0.0.1:8000/`.

## Dataset

The project uses `translated_dataset.csv`, which should be located in the project root. This CSV file contains columns for the original book title, the translated book description, and the preprocessed description. Ensure you replace the placeholder with the actual dataset filename in `views.py`.

## Team Members

| Name             | GitHub Profile                       |
| ---------------- | ------------------------------------ |
| Youssef Husseiny | [https://github.com/yuseiff](https://github.com/yuseiff)     |
| Mohamed Desoky   | [https://github.com/MohamedDesoky22](https://github.com/MohamedDesoky22)   |
| Samaa Khaled    | [https://github.com/Samaa-khaled411](https://github.com/Samaa-khaled411)   |
| Habiba Ahmed     |                                      |

