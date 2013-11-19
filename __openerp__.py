# -*- coding: utf-8 -*-

# Doc : https://doc.openerp.com/trunk/server/03_module_dev_01/
#       https://doc.openerp.com/trunk/server/03_module_dev_01/#manifest-file-openerp-py

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 01",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 01 
===================================================
Ce module n'a aucune fonctionnalité. 
Son seul but est de montrer comment créer et installer un premier module dans OpenERP

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',

  "depends" : [],       # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],      # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],      # Liste des fichiers XML à installer pour charger les données de démonstration
  "update_xml" : [],    # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)
  "installable": True,  # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False       # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}





