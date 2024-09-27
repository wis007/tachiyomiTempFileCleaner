import os, colorama
colorama.init(autoreset=True)

#gestion d'un cas d'erreur (probablement de permission)
def leOnError(*args):
   pass

print(colorama.Fore.GREEN + "Début du script")

#parcour de tout les sous dossiers pour trouver les sous dossiers temporaires.
for (root,dirs,files) in os.walk('/storage/emulated/0/Tachiyomi/downloads/', topdown=True, onerror=leOnError):
   #si le chemin actuel se termine par "_tmp", c'est un dossier de fichier temporaires
   if str(root).endswith("_tmp"):
    #Pour chaque fichiers contenu là dedans je cree un fchemin d'accces absolu et je l'efface
    for fic in files:
       #chemin d'acces absolu
       cheminComplet = os.path.join(root, fic)
       #suppression du fichier
       os.remove(cheminComplet)

       print(colorama.Fore.RED + cheminComplet + " effacer avec success")
    #suppression du dossier temporaire
    os.removedirs(root)
    
    print(colorama.Fore.RED + root + " effacer avec success")
   else:
      pass

print(colorama.Fore.GREEN + "\n\nFini de supprimer les fichier temporaire de tachiyomi.\n Un petit merci et une petite etoile à wis007 sur github :)\n\n https://github.com/wis007")