# 🧑‍🤝‍🧑 Django Social Media App

A simple yet functional social media platform built using Django. Users can sign up, log in, create posts with captions and images, follow/unfollow other users, and interact via likes and comments.

---

## 🚀 Features

- ✅ User Signup/Login with session authentication
- ✅ User Profile page with profile info and user posts
- ✅ Create and delete posts (with image and caption)
- ✅ View feed showing posts from followed users
- ✅ Like and Unlike posts
- ✅ Comment on posts
- ✅ Follow and unfollow other users
- ✅ Media upload support
- ✅ Clean and responsive UI (Bootstrap integrated)

---

## 📦 Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Backend      | Python, Django       |
| Frontend     | HTML, CSS, Bootstrap |
| Database     | SQLite (default)     |
| Template     | Django Templates     |

---

## 🛠️ Getting Started

Follow these steps to run the project locally on your system:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/social-media-app.git
cd social-media-app
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate          # On Windows
source venv/bin/activate       # On Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (for admin login)
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

Now open your browser and go to:  
👉 `http://127.0.0.1:8000/`

---

## 🖼️ Screenshots

> Add real screenshots under a `/screenshots` folder and reference them here:

- **User Feed:**  
  ![Feed](screenshots/feed.png)

- **Create Post:**  
  ![Create Post](screenshots/create_post.png)

- **Like/Comment on Posts:**  
  ![Like Comment](screenshots/interaction.png)

- **User Profile:**  
  ![Profile](screenshots/profile.png)

---

## 🗂️ Folder Structure

```
social-media-app/
├── core/                    # Main Django app (posts, users)
├── media/                   # User uploaded content
├── static/                  # Static files (CSS/JS)
├── templates/               # HTML templates
├── social_media_project/    # Django settings and URLs
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## 🌐 Optional Deployment

You can host this app for free on:
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Replit](https://replit.com/)

---

## 📧 Contact

**Developer:** Khushi Maurya  
**Role:** Python Developer Intern  
**Organization:** CodeAlpha  

---

## 🤝 Acknowledgements

Thanks to my mentors and team at **CodeAlpha** for their support and guidance during this internship project.
