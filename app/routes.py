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
        }
    ]
    return render_template("index.html", cards=cards)
