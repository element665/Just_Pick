# Just Pick 🎬🎰

**Just Pick** is a Flask-based web app that takes the agony out of choosing a movie. Using a slot machine interface, it randomly surfaces films from your personal media library across three slots. Lock in a title you're interested in and keep spinning the others — narrowing your entire library down to just three contenders.

---

## Features

- Slot machine UI with 3 independent movie slots
- Lock individual slots while continuing to spin the others
- Fetches movie details and poster art via the OMDB API
- Designed to work with your own personal media library
- Deployable via Docker with a simple volume mount for your movie list

---

## Prerequisites

- A free OMDB API key — register at [omdbapi.com](https://www.omdbapi.com/apikey.aspx)
- [Docker](https://docs.docker.com/get-docker/) installed on your machine
- A plain text file containing your movie list (one title per line)

---

## Generating Your Movie List

Just Pick reads from a plain `.txt` file with one movie title per line. If your media library is stored in a local folder, you can generate this file easily from the terminal.

**Mac / Linux:**
```bash
ls /path/to/your/movies > movie_list.txt
```

**Windows (Command Prompt):**
```cmd
dir /b "C:\path\to\your\movies" > movie_list.txt
```

**Windows (PowerShell):**
```powershell
Get-ChildItem "C:\path\to\your\movies" -Name > movie_list.txt
```

You may want to clean up the file afterward to remove file extensions or anything that isn't a movie title. Any plain text editor works fine for this.

---

## Environment Variables

Just Pick requires a `.env` file to pass your OMDB API key to the container. Create a file named `.env` in the same directory you plan to run the container from, with the following content:

```
OMDB_API_KEY=your_api_key_here
```

No quotes around the value, no spaces around the `=`.

---

## Installation & Setup

### Pull the Docker image

```bash
docker pull element665/justpick:latest
```

The image is published as a multi-architecture build and supports both **amd64** (standard desktops, laptops, and cloud servers) and **arm64** (Apple Silicon, Raspberry Pi). Docker will automatically pull the correct version for your machine.

### Create your docker-compose.yml

Create a `docker-compose.yml` file in your working directory:

```yaml
services:
  justpick:
    image: element665/justpick:latest
    container_name: justpick
    ports:
      - 3344:5000
    volumes:
      - /path/to/your/movie_list.txt:/movie-slot/movie_list.txt:ro
    env_file:
      - .env
```

Replace `/path/to/your/movie_list.txt` with the actual path to your movie list file on your host machine.

### Start the app

```bash
docker compose up -d
```

Then open your browser and navigate to:

```
http://localhost:3344
```

### Stop the app

```bash
docker compose down
```

---

## Usage

1. Open the app in your browser
2. Click **Spin** to randomly populate all three slots with movies from your library
3. If a movie in a slot catches your eye, click the **Lock** button on that slot to hold it in place
4. Keep spinning the remaining unlocked slots until you've narrowed down to your pick
5. Click a movie title or poster to view more details pulled from OMDB

---

## Project Structure

```
Just_Pick/
├── flask_app.py          # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
├── movie_list.txt        # Sample movie list (replace with your own)
├── Dockerfile
└── docker-compose.yml
```

---

## Notes

- The included `movie_list.txt` is a sample placeholder. For the best experience, supply your own list via the Docker volume mount as shown above.
- The OMDB free tier allows up to 1,000 requests per day. For typical personal use this is more than sufficient.
- The app binds to port `5000` inside the container. The compose file above maps this to port `3344` on your host — feel free to change the host port to whatever suits your setup.

---

## License

This project is open source. Feel free to fork, modify, and make it your own.
