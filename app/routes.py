from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def home():
    cards = [
        {
            "title": "App Educativa",
            "description": "Accede a tu app educativa principal",
            "link": "https://app.losmundosedufis.com",
            "icon": "fas fa-school"
        },
        {
            "title": "Ko-fi / Donaciones",
            "description": "Apoya el proyecto con una aportación",
            "link": "https://donar.losmundosedufis.com",
            "icon": "fas fa-hand-holding-heart"
        },
        {
            "title": "Opositores",
            "description": "Accede a la app de opositores",
            "link": "https://opos.losmundosedufis.com",
            "icon": "fas fa-graduation-cap"
        },
        {
            "title": "Polos Creativos (Beta)",
            "description": "Versión de pruebas para gestionar el polo creativo",
            "link": "https://polos.losmundosedufis.com",
            "icon": "fas fa-cogs"
        },
        {
            "title": "Web Oficial",
            "description": "Visita la web principal de Los Mundos Edufis",
            "link": "https://losmundosedufis.com",
            "icon": "fas fa-globe"
        },
        {
            "title": "Creador de Ligas Deportivas",
            "description": "Herramienta para crear y gestionar ligas deportivas escolares.",
            "link": "link_a_creador_ligas",
            "icon": "fas fa-sportsball"
        },
        {
            "title": "Recursos Educativos",
            "description": "Accede a material y recursos útiles para tus clases.",
            "link": "link_a_recursos",
            "icon": "fas fa-book"
        },
        {
            "title": "Mundo Emocional",
            "description": "Explora el desarrollo emocional en el proceso educativo.",
            "link": "link_a_mundo_emocional",
            "icon": "fas fa-brain"
        },
        {
            "title": "Mundo Social",
            "description": "Fomenta la interacción social y la colaboración en el aprendizaje.",
            "link": "link_a_mundo_social",
            "icon": "fas fa-users"
        },
        {
            "title": "Mundo Físico",
            "description": "Promueve la actividad física y el bienestar en la educación.",
            "link": "link_a_mundo_fisico",
            "icon": "fas fa-dumbbell"
        },
        {
            "title": "Mundo Interior",
            "description": "Fomenta la introspección y el autoconocimiento.",
            "link": "link_a_mundo_interior",
            "icon": "fas fa-heart"
        },
        {
            "title": "Mundo Mental",
            "description": "Desarrolla la inteligencia cognitiva y las habilidades mentales.",
            "link": "link_a_mundo_mental",
            "icon": "fas fa-head-side-brain"
        }
    ]
    return render_template("index.html", cards=cards)
