{% extends "layout.html" %}
{% block content %}
    <h1 class="mb-3">Posts by {{ user.username }} ({{ posts.total }})</h1>
    {% for post in posts.items %}
        <article class="media content-section">
          <img class="rounded-circle article-img" src="{{ url_for('static', filename='profile_pics/' + post.author.image_file) }}">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="{{ url_for('users.user_posts', username=post.author.username) }}">{{ post.author.username }}</a>
              <small class="text-muted">{{ post.date_posted.strftime('%Y-%m-%d') }}</small>
            </div>
            <h2><a class="article-title" href="{{ url_for('posts.post', post_id=post.id) }}">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}
    {% for page_num in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
      {% if page_num %}
        {% if posts.page == page_num %}
          <a class="btn btn-info mb-4" href="{{ url_for('users.user_posts', username=user.username, page=page_num) }}">{{ page_num }}</a>
        {% else %}
          <a class="btn btn-outline-info mb-4" href="{{ url_for('users.user_posts', username=user.username, page=page_num) }}">{{ page_num }}</a>
        {% endif %}
      {% else %}
        ...
      {% endif %}
    {% endfor %}
{% endblock content %}