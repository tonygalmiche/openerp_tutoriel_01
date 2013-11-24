InfoSaône / OpenERP Tutoriel 01 - Module minimaliste
===================

Ce module n'a aucune fonctionnalité. 

Son seul but est de montrer comment créer et installer un premier module dans OpenERP.

## Installation du module 

Après avoir installé OpenERP, il faut placer le dossier contenant ce module dans le dossier 'addons' d'OpenERP.

Par exemple, sous Debian/Ubuntu ce dossier est par défaut : 
```
/usr/lib/pymodules/python2.7/openerp/addons/
```

Ensuite, il faut mettre à jour la liste des modules dans OpenERP : 

* Menu "Configuration / Modules / Mettre à jour la liste des modules"

Pour finir, il faut installer le module : 
* Menu "Configuration / Modules installés"
* Supprimer le filtre "Installé"
* Rechercher dans la liste le nom de ce module et cliquer sur le bouton "Installer"


