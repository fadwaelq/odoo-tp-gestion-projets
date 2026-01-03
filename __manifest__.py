{
    "name": "TP - Gestion des Tâches Simples",
    "version": "1.0",
    "summary": "Module pédagogique pour gérer des tâches simples (TP)",
    "category": "Training",
    "author": "Fadwa El Qaqia",  # Mets ton nom ici !
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/tache_views.xml",
    ],
    "installable": True,
    "application": True,
    "icon": "/tp_gestion_taches/static/description/icon.png",
}