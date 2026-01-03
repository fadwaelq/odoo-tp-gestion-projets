from odoo import models, fields


class TpTache(models.Model):
    _name = "tp.tache"
    _description = "Tâche TP"
    _order = "date_echeance asc, priorite desc, name"  # Tri intelligent : échéance → priorité → nom

    # Champs obligatoires / principaux
    name = fields.Char(
        string="Nom de la tâche",
        required=True,
        help="Titre ou description courte de la tâche"
    )

    responsable = fields.Many2one(
        'res.users',
        string="Responsable",
        default=lambda self: self.env.user,
        help="Personne en charge de la tâche"
    )

    date_echeance = fields.Date(
        string="Date d'échéance",
        help="Date limite pour terminer la tâche"
    )

    # Champ Priorité ajouté
    priorite = fields.Selection([
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    ],
        string="Priorité",
        default='moyenne',
        help="Niveau d'urgence de la tâche"
    )

    # Statut de la tâche
    statut = fields.Selection([
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
    ],
        string="Statut",
        default='a_faire',
        help="État actuel de la tâche"
    )

    description = fields.Text(
        string="Description",
        help="Détails supplémentaires sur la tâche"
    )