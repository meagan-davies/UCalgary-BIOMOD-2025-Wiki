from os import path
from pathlib import Path
from flask import Flask, render_template
from flask_frozen import Freezer
import sys

team_members = [
    {
        "name": "Durwyn Lam",
        "role": "Dry Lab Member",
        "image": "Durwyn.jpg",
        "bio": "Hello! I'm Durwyn and I am a Dry Lab member for this year's BIOMOD team. I am currently entering my third year of Biomedical Engineering at the University of Calgary. My roles involve nanomolecule modelling, contributing to project deliverables like videos, presentations, and this website. Outside BIOMOD, I am VP Communications for BMESS and Regional Marketing Lead for CUBEC. In my free time, I enjoy working out, playing piano, photography, and spending time with loved ones.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Supercut by Lorde",
            "fun_fact": "In high school, I had an Instagram account with over 60,000 followers",
            "unpopular_opinion": "Peanut butter is disgusting"
        }
    },
    {
        "name": "Jackson Qi",
        "role": "Dry Lab Member",
        "image": "Jackson.jpg",
        "bio": "I am going into my third year, majoring in Biological Sciences with a concentration in Biotechnology. My role focuses on dry lab modelling and molecular analysis, and I also contribute to experimental planning.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Wasted by Carda (feat. Emily Falvey)",
            "fun_fact": "I was on route to becoming a lifeguard before COVID",
            "unpopular_opinion": "Pineapple on pizza is fire"
        }
    },
    {
        "name": "Ryland Gujilde",
        "role": "Wet Lab Member",
        "image": "Ryland.jpg",
        "bio": "I am involved in experimental planning, protocol development, and hands-on experimentation. Fascinated by the potential of biotechnology to drive innovation in diagnostics and therapeutics.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Whenever - Gareth Donkin",
            "fun_fact": "I think pipetting is kind of therapeutic",
            "unpopular_opinion": "Kewpie mayo belongs on everything"
        }
    },
    {
        "name": "Ella Webster",
        "role": "Wet Lab Lead",
        "image": "Ella.jpg",
        "bio": "I organize and oversee all lab experiments to ensure plans and deadlines are clear. Passionate about early detection of neurological biomarkers and biomedical research.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "What Are You Listening To? - Chris Stapleton",
            "fun_fact": "I'm from a small town in New Brunswick",
            "unpopular_opinion": "Chocolate is not good"
        }
    },
    {
        "name": "Mayuri Sharma",
        "role": "Wet Lab Member",
        "image": "Mayuri.jpg",
        "bio": "Ambitious about biological and medical science, especially interdisciplinary research. Passionate about problem-solving and innovative experiments.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "",
            "fun_fact": "",
            "unpopular_opinion": ""
        }
    },
    {
        "name": "Meagan Davies",
        "role": "Team Lead",
        "image": "Meagan.jpg",
        "bio": "Passionate about interdisciplinary teamwork and research in biology, medicine, engineering, physics, and astronomy. Outside academics, I love coffee, tea, drawing, reading, and writing.",
        "linkedin": "https://www.linkedin.com/in/meagan-davies-407245214",
        "fun_facts": {
            "current_song": "Will I finish my todo list or will my todo list finish me",
            "fun_fact": "",
            "unpopular_opinion": ""
        }
    },
    {
        "name": "Ria Sinha",
        "role": "Wet Lab Member",
        "image": "Ria.jpg",
        "bio": "Excited to contribute to BIOMOD 2025. (Blurb pending)",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Calling After Me by The Wallows",
            "fun_fact": "I have a 10 year old dog!",
            "unpopular_opinion": "Pineapples taste great on pizza"
        }
    },
    {
        "name": "Zehaan Walji",
        "role": "Dry/Wet Lab Member",
        "image": "Zehaan.jpg",
        "bio": "Second-year student studying Computer Science and Biological Sciences. First year in BIOMOD assisting wet and dry lab tasks, docking, research, and SELEX.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Clutch (demo) - Melanie Faye",
            "fun_fact": "I can solve a Rubik’s cube in under 30 seconds",
            "unpopular_opinion": "Breakfast is overrated"
        }
    },
    {
        "name": "Jillian Cannon",
        "role": "Wet/Dry Lab Member",
        "image": "Jillian.jpg",
        "bio": "Passionate about molecular design and DNA nanotechnology. Helps simulate structures and plan experiments. Enjoys hiking, skiing, and playing with dogs.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Anything by the Lumineers",
            "fun_fact": "I can name all the countries in the world from memory",
            "unpopular_opinion": "Cold pizza > hot pizza"
        }
    },
    {
        "name": "Shade Odagwe",
        "role": "Wet Lab Member",
        "image": "Shade.jpg",
        "bio": "Wet Lab Member. Interested in biomedical engineering and human biology, curious and passionate about research.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Manchild - Sabrina Carpenter",
            "fun_fact": "I am currently learning Korean and how to play the guitar",
            "unpopular_opinion": ""
        }
    },
    {
        "name": "Isabel Gonzalez",
        "role": "Wet/Dry Lab Member",
        "image": "Isabel.jpg",
        "bio": "Member of both wet and dry lab. Passionate about solving real-world medical problems through engineering and biochemical research.",
        "linkedin": "",
        "fun_facts": {
            "current_song": "Otro Atardecer - Bad Bunny, The Marias",
            "fun_fact": "I speak three languages!",
            "unpopular_opinion": "Pineapple on pizza is always good"
        }
    }
]



DEBUG = True

template_folder = path.abspath('./wiki')
app = Flask(__name__, template_folder=template_folder)
app.config.from_object(__name__)

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/team.html')
def team():
    return render_template('pages/team.html', team_members=team_members)

@app.route('/<page>' + '.html')
def render_page(page):
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')

# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8080)
