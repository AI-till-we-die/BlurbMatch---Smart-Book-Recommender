import sys
import os
from django.shortcuts import render
from django.http import JsonResponse

# Add the preprocessing directory to Python's module path
sys.path.append(os.path.join(os.path.dirname(__file__), '../preprocessing'))

from model_integration import load_translated_dataset, create_tfidf_matrix, recommend_books_by_blurb

# Load dataset and TF-IDF model on startup
dataset_path = "translated_dataset.csv"
dataset = load_translated_dataset(dataset_path)
tfidf_vectorizer, tfidf_matrix = create_tfidf_matrix(dataset)

def home(request):
    return render(request, "main.html")

def recommend_books(request):
    if request.method == "POST":
        user_blurb = request.POST.get("blurb", "")
        recommendations = recommend_books_by_blurb(user_blurb, tfidf_vectorizer, tfidf_matrix, dataset)
        return JsonResponse(recommendations, safe=False)
    return JsonResponse({"error": "Invalid request method"}, status=400)
