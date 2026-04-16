# 🎵 Scrobbler

A music analytics dashboard built with Django and the Last.fm API. Search for any artist and get a detailed overview of their stats, top tracks, similar artists, and more.

🌐 **Live:** [scrobbler.irenemendoza.dev](https://scrobbler.irenemendoza.dev)

---

## ✨ Features

- 🔍 Search for any artist by name
- 📊 View listener counts and total scrobbles
- 🎵 Browse top tracks
- 💿 Explore top albums with cover art
- 🏷️ Discover tags and genres
- 👥 Find similar artists

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12, Django
- **API:** [Last.fm API](https://www.last.fm/api)
- **Styling:** Tailwind CSS v4, Syne font
- **Libraries:** `requests`, `python-dotenv`, `whitenoise`, `gunicorn`
- **Deployment:** DigitalOcean (Ubuntu 24.04, CloudPanel, Nginx, Gunicorn)

---

## 🚀 Run it locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/scrobbler.git
cd scrobbler
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root of the project:

```
LASTFM_API_KEY=your_api_key_here
LASTFM_BASE_URL=your_base_url_here
```

You can get a free API key at [last.fm/api](https://www.last.fm/api).

### 5. Run the development server

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000` in your browser.

---

## 🗺️ Roadmap

- [ ] 🔄 Migrate frontend from Django Templates to **React**
- [ ] 📈 Add charts for listening trends
- [ ] 🌍 Display artist biography and origin

---

## 👩‍💻 Author

Made by [Irene Mendoza](https://irenemendoza.dev)