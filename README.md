# TP - Gestion des Tâches Simples

**Auteur** : Fadwa ELQAQIA  
**Module Odoo** : tp_gestion_taches  
**Version** : 1.0  
**LAB 2** : Création d’un module Odoo personnalisé

## Objectif
Créer un module Odoo qui permet de :
- Ajouter un menu "Tâches TP"
- Gérer des tâches simples (Nom de la tâche, Responsable, Date d’échéance, Priorité, Statut : À faire / En cours / Terminée, Description, Jours restants)
- Afficher en liste, formulaire et vue Kanban avec couleurs et drag & drop

## Améliorations ajoutées
- Champ Priorité avec tri automatique
- Calcul des jours restants
- Coloration des lignes selon statut
- Vue Kanban complète
- Icône personnalisée

## Structure
- models/tache.py
- views/tache_views.xml
- security/ir.model.access.csv
- static/description/icon.png
- __manifest__.py
