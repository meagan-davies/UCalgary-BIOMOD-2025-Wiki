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
        "bio": "Hi! My name is Jackson and I am going into my third year of study, majoring in biological sciences with a concentration in biotechnology. I love volunteering, listening to music and pursuing hobbies in my spare time, such as chess, for example. My role here at BIOMOD is primarily focused upon dry lab modelling and the in-depth analysis of molecular structures. However, I have contributed to the experimental planning and design aspect as well.",
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
        "bio": "As a Wet Lab Member on the BIOMOD team, I am involved in experimental planning, protocol development, and hands-on experimentation. I’m especially fascinated by the potential of biotechnology to drive innovation in diagnostics and therapeutics. This project has deepened my interest in studying and engineering biomolecules to develop smarter, more responsive systems that can transform research and patient care. Being part of a team that combines creativity with molecular precision has been both challenging and inspiring!",
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
        "bio": "I am the Wet Lab Lead for the 2025 BIOMOD Team. In this role I organize and oversee all of the experiments we will be conducting in the lab to ensure there is a clear plan and everything is completed for the team set deadlines. I have a passion for finding the why for neurological diseases and learning about how we can detect them as early as possible. Studying these biomarkers and what causes them to be present is something I want to continue learning about in the lab.",
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
        "bio": "I’m very ambitious about biological and medical science, particularly the interdisciplinary research that drives progress in these fields. My passion for research is driven by problem-solving, refining methodologies, and exploring innovative experiments. It’s this combination of intellectual challenge and hands-on discovery that motivated me to join the BIOMOD 2025 team as a wet lab member.",
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
            "current_song": "Je te laisserai des mots - Patrick Watson",
            "fun_fact": "I helped build a satellite.",
            "unpopular_opinion": "Preffered work hours are 11pm to 2am."
        }
    },
    {
        "name": "Ria Sinha",
        "role": "Wet Lab Member",
        "image": "Ria.jpg",
        "bio": "As a member of the Wet Lab team, I am very interested in exploring how biomolecules can be manipulated to create tools that can improve healthcare outcomes. I am also excited to explore the field of biotechnology through this project. My roles include designing the protocols, and helping perform in-lab experiments. In my free time, I enjoy hiking, playing piano, and listening to podcasts.",
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
        "bio": "My name is Zehaan Walji, and I am entering my second year at the University of Calgary, where I am studying Computer Science and Biological Sciences. I chose this degree because I have always been fascinated by the intersection between technology and biology. Outside of academics, I love solving Rubik’s cubes and playing chess. This is my first year participating in BIOMOD, where I am being mentored in both the wet lab and dry lab teams, assisting with docking, research, and the in silico SELEX process.",
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
        "bio": "I have a passion for molecular design, DNA nanotechnology, and using science to improve lives. In BIOMOD, I’m part of both the wet and dry lab teams, where I help simulate our structures and plan experiments. Outside the lab, I love hiking, skiing, and playing with my dogs!",
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
        "bio": "My name is Shade Odagwe. I am a Wet Lab Member of the BIOMOD Team. My interest in research developed from a place of curiosity. Bioloy has alway been a point of interest for me, and I was curious about how our understanding of the human body could deepen the knowledge and means of how we take care of ourselves. This curiosity fueled mmy passion for reaserch and for studying Biomedical Engineering.",
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
        "bio": "Hi! My name is Isabel and I am both a member of the wet and dry lab for UCalgary’s BIOMOD team! I am passionate about solving real world medical problems through applying engineering principles and design. BIOMOD has let me collaborate on a project at the intersection of engineering and biochemistry, while performing innovative and exciting research.",
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
    sorted_members = sorted(team_members, key=lambda m: m["name"].split()[-1].lower())
    return render_template('pages/team.html', team_members=sorted_members)

@app.route('/<page>' + '.html')
def render_page(page):
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')

# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8080)
