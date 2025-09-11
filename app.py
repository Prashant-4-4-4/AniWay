from flask import Flask, render_template,request
import os 

app = Flask(__name__)

anime_data = {
    "onepunchman": {
        "title": "One Punch Man",
        "image": "saitama1.jpg",
        "bg":"saitama.jpg",
        "season": "Season 1",
        "genre": "Action, Comedy, Superhero",
        "description": "Saitama is a hero who can defeat any opponent with a single punch...",
        "episodes": {
            1: "Poo5lqoWSGw", 
            2: "Poo5lqoWSGw"
        }
    },
    "spyxfamily": {
        "title": "Spy x Family",
        "image": "spy-x-family1.jpg",
        "bg":"spy-x-family.jpg",
        "season": "Season 1",
        "genre": "Action, Comedy, Slice of Life",
        "description": "Elite spy Twilight must disguise himself as a family man...",
        "episodes": {1: "ofXigq9aIpo", 2: "ofXigq9aIpo", 3: "ofXigq9aIpo", 4: "ofXigq9aIpo"}
    },
    "tensura": {
        "title": "That Time I Got Reincarnated as a Slime",
        "image": "slime1.jpg",
        "bg":"slime.jpg",
        "season": "Season 1",
        "genre": "Isekai, Fantasy, Adventure",
        "description": "After being killed in his previous life, a man reincarnates as a slime...",
        "episodes": {1: "uOzwqb74K34", 2: "uOzwqb74K34", 3: "uOzwqb74K34", 4: "uOzwqb74K34"}
    },
    "mushokutensei": {
        "title": "Mushoku Tensei: Jobless Reincarnation",
        "image": "mushoku1.jpg",
        "bg":"mushoku.jpg",
        "season": "Season 1",
        "genre": "Isekai, Fantasy, Drama",
        "description": "A 34-year-old man with no achievements in his past life is reincarnated...",
        "episodes": {1: "M-3YqJA6UlM", 2: "M-3YqJA6UlM", 3: "M-3YqJA6UlM", 4: "M-3YqJA6UlM"}
    },
    "tokyorevengers": {
        "title": "Tokyo Revengers",
        "image": "revenger1.jpg",
        "bg":"revenger.jpg",
        "season": "Season 1",
        "genre": "Action, Drama, Time Travel",
        "description": "Takemichi Hanagaki travels back in time to change fate...",
        "episodes": {1: "Fwyc8XhXVSA", 2: "Fwyc8XhXVSA", 3: "Fwyc8XhXVSA", 4: "Fwyc8XhXVSA"}
    },
    "dandadan": {
        "title": "Dan Da Dan",
        "image": "dan-da-dan1.jpg",
        "bg":"dan-da-dan.jpg",
        "season": "Season 1",
        "genre": "Action, Supernatural, Comedy",
        "description": "A quirky mix of aliens and spirits collide when Momo meets Okarun...",
        "episodes": {1: "0XJxfbN36Uw", 2: "0XJxfbN36Uw", 3: "0XJxfbN36Uw", 4: "0XJxfbN36Uw"}
    },
    "zom100": {
        "title": "Zom 100: Bucket List of the Dead",
        "image": "zom1.jpg",
        "bg":"zom.jpg",
        "season": "Season 1",
        "genre": "Comedy, Horror, Zombie, Survival",
        "description": "Akira Tendo wakes up to a zombie apocalypse and makes a bucket list...",
        "episodes": {1: "2VvZIEXmltw", 2: "2VvZIEXmltw", 3: "2VvZIEXmltw", 4: "2VvZIEXmltw"}
    },
    "remonster": {
        "title": "Re:Monster",
        "image": "re-monster1.png",
        "bg":"remonster.jpg",
        "season": "Season 1",
        "genre": "Isekai, Fantasy, Adventure",
        "description": "Tomokui Kanata is reborn as a goblin and gains powers from what he eats...",
        "episodes": {1: "afMKriTzgIw", 2: "afMKriTzgIw", 3: "afMKriTzgIw", 4: "afMKriTzgIw"}
    },
    "iparryeverything": {
        "title": "I Parry Everything",
        "image": "parry1.jpg",
        "bg":"parry.jpg",
        "season": "Season 1",
        "genre": "Action, Adventure, Fantasy",
        "description": "Noel discovers a perfect parrying ability and begins a journey...",
        "episodes": {1: "J-ZqbLMlPdU", 2: "J-ZqbLMlPdU", 3: "J-ZqbLMlPdU", 4: "J-ZqbLMlPdU"}
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html", anime_list=anime_data)

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    results = {}
    if query:
        for key, anime in anime_data.items():
            if query in anime["title"].lower() or query in key.lower():
                results[key] = anime
    return render_template("search.html", results=results, query=query)

@app.route("/anime/<key>")
def anime_page(key):
    anime = anime_data.get(key)
    if anime:
        return render_template("anime.html", anime=anime, key=key)
    else:
        return "Anime Not Found", 404

@app.route("/watch/<series>/<int:ep>")
def watch(series, ep):
    anime = anime_data.get(series)
    if not anime:
        return "Series not found", 404

    episodes = anime.get("episodes", {})
    if ep not in episodes:
        return "Episode not found", 404

    video_id = episodes.get(ep, "")
    ep_keys = sorted(episodes.keys())
    ep_min = ep_keys[0]
    ep_max = ep_keys[-1]

    return render_template(
        "watch.html",
        series=series,
        anime=anime,
        current_ep=ep,
        video_id=video_id,
        episodes=episodes,
        ep_min=ep_min,
        ep_max=ep_max
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)