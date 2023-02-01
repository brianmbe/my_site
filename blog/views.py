from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "mountain-hiking",
        "image": "mountains.jpg",
        "author": "peter",
        "date": date(2023, 1, 29),
        "title": "Mountain Hiking",
        "excert": "Aipisicing elit. Dolorum busdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloribus earum quibusdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
    },
    {
        "slug": "you-only-live-once",
        "image": "woods.jpg",
        "author": "manano",
        "date": date(2023, 1, 1),
        "title": "You Only Live Once",
        "excert": "Aipisicing elit. Dolorum busdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloribus earum quibusdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
    },
    {
        "slug": "programming-is-king",
        "image": "coding.jpg",
        "author": "Nyingambe",
        "date": date(2021, 10, 9),
        "title": "Programming is King",
        "excert": "Aipisicing elit. Dolorum busdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloribus earum quibusdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
    },
    {
        "slug": "nature-at-its-best",
        "image": "woods.jpg",
        "author": "nixon",
        "date": date(2022, 1, 29),
        "title": "Nature at its best",
        "excert": "Aipisicing elit. Dolorum busdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloribus earum quibusdam, iusto consequuntur, tempore sed et autem dolores mollitia odit ipsa repellat obcaecati minima repellendus",
    }

]


def get_date(post):
    return post['date']


def start_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-post.html", {
        "all_post": all_posts
    })


def post_detail(request, slug):
    # working with list comprehension
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
