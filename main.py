import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
import time,ppp


class page_0(tk.Frame):
    """C'est la page o ou de bienvenue"""
    def __init__(self,master):
        super().__init__(master)
        # Mots de bienvenue au participant
        self.bienvenue()
    def show(self):
        #Placer le widget lui même
        self.pack(fill = 'both',expand = True)
        
    def bienvenue(self):
        """C'est la fonction qui va vous souhaitez la bienvenue au joueur"""
        self['bg'] = 'blue'
        #self.grab_set()
        label = tk.Label(self, text = 'Bienvenue Dans Le Jeux De \n Pierre Papier Ciseaux \n😁❤️🙂\n Créaction de N.Canisius',font=('Comic Sans MS',30,'bold'),fg = 'blue',relief = 'ridge' )
        self.agree = tk.Button(self,text = 'OK',font=('Verdana',15,'bold'),fg='red',bg = 'ivory',cursor = 'hand2')
        self.agree.place(relx = 0.5,rely = 0.85)
        label.place(relx=0,rely = 0,relheight=0.5,relwidth=1)
   
    
class page_1(tk.Frame):
    """C'est la page d'accueil"""
    def __init__(self,master,chemin,icone):
        super().__init__(master)
        self.chemin = chemin
        self.longueur = self.master.winfo_height()
        self.largeur = self.master.winfo_width()
        self.configure(height=self.longueur,width = self.largeur)
        #Ici, on parle de l'icone
        self.icone = icone
        # Ici, on affiche les widgets
        self.widgets()
            
        
        #configuration de la fonction resize 
        Thread(target=self.master.bind,args=('<Configure>',self.resize),daemon = True).start()
        #Ici, je vais le placer sur la fenêtre principale
        #self.pack(fill = 'both',expand=True), on va plutot le packer au niveau du bouton de la page de bienvenue
    def quitter(self):
        """Cette fonction va nous permettre de quiter la fenêtre"""
        self.fenetre = tk.Toplevel(self)
        self.fenetre.title('Pierre Papier Ciseaux')
        self.fenetre.iconbitmap(self.icone)
        #self.fen['bg'] = 'cyan'
        #self.fen.overrideredirect(True)
        self.fenetre.grab_set()
        self.fenetre.resizable(0,0)
        self.fenetre.geometry('360x170+250+250')
        self.info = tk.Label(self.fenetre,text = 'Voulez-vous fermer \n la fenêtre ?',font=('Comic Sans MS',20,'bold'),fg = 'blue',relief = 'ridge')
        self.oki = tk.Button(self.fenetre,text = 'Oui',font=('Verdana',15,'bold'),fg='blue',command = self.master.destroy,cursor = 'hand2')
        self.aide = tk.Button(self.fenetre,text = 'Non',font=('Verdana' ,15,'bold'),fg='green',command = self.fenetre.destroy,cursor = 'hand2')
        self.info.place(x = 25,y = 0)
        self.oki.place(x = 60,y = 110)
        self.aide.place(x = 250,y = 110)
    #Configuration de la page d'ouverture des célébrations
    
    def widgets(self):
        """ Ici, on place les widgets sur la frame """
        # Ici, on affiche le canvas qui va porter le fond d'écran
        self.canva = tk.Canvas(self,height=self.longueur,width = self.largeur)
        self.photo = ImageTk.PhotoImage(Image.open(self.chemin))
        self.canva.create_image(0,0,image = self.photo,anchor = 'nw')
        #On place le widgets
        self.canva.place(x = 0,y = 0)

        # Ici, on va afficher les boutons qui vont nous permettre de quitter la page d'accueil
        self.bouton_1 = tk.Button(self,text = 'Lancer le jeu',font = 'Times 20',bd = 2,fg='white',bg = "#7FC9E6",activeforeground="grey",activebackground="#7FC9E6",relief='ridge',width = 15,cursor = 'hand2')
        self.bouton_2 = tk.Button(self,text = 'Quitter',font = 'Times 20',bd = 2,fg='red',bg = "ivory",activeforeground="white",activebackground="red",relief='ridge',command = lambda :self.quitter(),width = 15,cursor= 'hand2')
        self.bouton_1.place(relx=0.38,rely=0.55)
        self.bouton_2.place(relx=0.38,rely=0.90)
    
   
    def resize(self,event):
        """Ici, définition de la fonction de la fontion resize"""
        try:
            self.longueur = self.master.winfo_height()
            self.largeur = self.master.winfo_width()
            self.configure(height=self.longueur,width = self.largeur)
            self.canva.configure(height=self.longueur,width = self.largeur)
            self.new_photo = Image.open(self.chemin)
            self.redimensionner = self.new_photo.resize((self.largeur,self.longueur))
            self.photo = ImageTk.PhotoImage(self.redimensionner)
            self.canva.create_image(0,0,image = self.photo, anchor = 'nw')
        except:
            pass
    



class page_2(tk.Frame):
    def __init__(self,master,image_1,image_2,image_3):
        super().__init__(master)
        #Ici, nous allons implémenter le chronomètre comme référentiel
        self.debut = time.time()
        self.liste = ['Pierre ✊','Papier 📜',' Ciseau ✂️',' Ciseau ✂️',' ']#En fait, l'ajout de ciseaux deux fois est fait par soucis d'animation
        # Etablissement de la  base de donnée des points
        self.base_point = {'ordinateur':0,'utilisateur':0}
        #Les couleurs utilisés
        self.couleur = ["green","blue",'red']
        #Ici, c'est une valeur qui va nous permettre de mettre un frein à la fonction bind notamment sur le clavier
        self.status = False
        #Configuration des images
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3
        #Placement des widgets
        self.widgets()
        #Configuration des boutons
        self.configuration_boutons()
        
        
    def info_general(self):
        """Cette fonction va nous permettre d'afficher les informations sur le jeu""" 
        self.fen.geometry('560x360+300+300')
        self.agree = tk.Button(self.fen,text = 'OK',font=('Verdana',15,'bold'),fg='red',bg = 'ivory',command = self.fen.destroy,cursor= 'hand2')
        self.agree.place(relx = 0.45,rely = 0.85)
        self.ok.place_forget()
        self.aide.place_forget()
        self.info.configure(text = "Pour jouer le jeu , \nvous allez appuyer sur un bouton en bas \n représentant un élément de \n pierre papier ciseaux \n \
Vous avez tout votre temps \n pour taper un élément \n L'ordinateur est toujours \n prêt 😁😂")
        

    def begining(self,icone):
        """Cette fonction sert à demander à l'utilisateur s'il veut commencer"""
        self.icone = icone
        self.fen = tk.Toplevel(self)
        self.fen.title('Pierre Papier Ciseaux')
        self.fen.iconbitmap(self.icone)
        #self.fen['bg'] = 'cyan'
        #self.fen.overrideredirect(True)
        self.fen.grab_set()
        self.fen.resizable(0,0)
        self.fen.geometry('360x170+250+250')
        self.info = tk.Label(self.fen,text = 'Voulez-vous commencer \n la partie',font=('Comic Sans MS',20,'bold'),fg = 'blue',relief = 'ridge')
        self.ok = tk.Button(self.fen,text = 'oui',font=('Verdana',15,'bold'),fg='blue',command = self.fen.destroy,cursor= 'hand2')
        self.aide = tk.Button(self.fen,text = 'aide',font=('Verdana' ,15,'bold'),fg='green',command = self.info_general,cursor= 'hand2')
        self.info.place(x = 10,y = 0)
        self.ok.place(x = 60,y = 110)
        self.aide.place(x = 250,y = 110)
    def widgets(self):
        """On va pouvoir définir les widgets de cette fenêtre"""
        #Configurations des images
        self.Image_1 = ImageTk.PhotoImage(Image.open(self.image_1),(50,50)) 
        self.Image_2 = ImageTk.PhotoImage(Image.open(self.image_2),(50,50))
        self.Image_3 = ImageTk.PhotoImage(Image.open(self.image_3),(50,50)) 
        #Configuration des boutons
        self.bouton_1 = tk.Button(self,relief='solid',image=self.Image_1,text = '0',cursor= 'hand2')
        self.bouton_2 = tk.Button(self,relief='solid',image=self.Image_2,text = '1',cursor= 'hand2')
        self.bouton_3 = tk.Button(self,relief='solid',image=self.Image_3,text = '2',cursor= 'hand2')
        self.bouton_4 = tk.Button(self,relief='flat',text = "Retour",font = 'Verdana 20',bd = 2,fg='red',bg = "ivory",activeforeground="white",activebackground="red",cursor= 'hand2')
        self.bouton_5 = tk.Button(self,relief='flat',text = "Reintialiser",font = 'Verdana 20',bd = 2,fg='blue',bg = "white",activeforeground="white",activebackground="red",cursor= 'hand2')        
        

        #Configuration des labels
        self.label_1 = tk.Label(self,relief='ridge',bd = 1,image = self.Image_3)
        self.label_2 = tk.Label(self,relief='ridge',bd = 1,image = self.Image_2)
        self.label_3 = tk.Label(self,relief='ridge',bd = 1,image = self.Image_1)
        self.label_5 =tk.Label(self,font=('Comic Sans MS',15,'bold'),fg = 'blue',relief='ridge',bd = 1)
        self.label_6 =tk.Label(self,font=('Comic Sans MS',14,'bold'),text = 'Faîtes un \n choix',fg = 'blue',anchor='center')
        self.label_7 =tk.Label(self,font=('Comic Sans MS',15,'bold'),fg = 'blue',relief='ridge',bd = 1)
        self.label_8 =tk.Label(self,font=('Comic Sans MS',28,'bold'),text = 'On \n commence',fg = 'blue',relief='ridge',bd = 1)
        self.label_9 =tk.Label(self,font=('Comic Sans MS',20,'bold'),text = 'Ton score :',fg = 'blue',relief='ridge',bd = 1)
        self.label_4 =tk.Label(self,font=('Comic Sans MS',20,'bold'),text = "Score de \n l'ordinateur",fg = 'blue',relief='ridge',bd = 1)
        #Placement des labels et boutons
        self.bouton_1.place(relx=0,rely = (2/3),relheight=(1/3),relwidth=0.25)
        self.bouton_2.place(relx=0.25,rely = (2/3),relheight=(1/3),relwidth=0.25)
        self.bouton_3.place(relx=0.5,rely = (2/3),relheight=(1/3),relwidth=0.25)
        self.bouton_4.place(relx=0.75,rely = (11/12),relheight=(1/12),relwidth=0.25)
        self.bouton_5.place(relx=0.75,rely = 0,relheight=(1/12),relwidth=0.25)

        self.label_1.place(relx=0,rely = 0,relheight=(1/3),relwidth=0.25)
        self.label_2.place(relx=0.25,rely = 0,relheight=(1/3),relwidth=0.25)
        self.label_3.place(relx=0.5,rely = 0,relheight=(1/3),relwidth=0.25)
        self.label_4.place(relx=0.75,rely = (1/12),relheight=(1/4),relwidth=0.25)
        self.label_5.place(relx=0,rely = (1/3),relheight=(1/6),relwidth=0.25)
        self.label_6.place(relx=0.25,rely = (1/3),relheight=(1/3),relwidth=0.25)
        self.label_7.place(relx=0.5,rely = (1/2),relheight=(1/6),relwidth=0.25)
        self.label_8.place(relx=0.75,rely = (1/3),relheight=(1/3),relwidth=0.25)
        self.label_9.place(relx=0.75,rely = (2/3),relheight=(1/4),relwidth=0.25)
    #Configuration des commandes des boutons
    def configuration_boutons(self):
        """Cette fonction va nous permettre de faire la configuration des boutons,l'objectifs"""
        self.bouton_1.configure(state = 'normal',command = lambda: Thread(target = self.bouton_fonction,args = (self.bouton_1,),daemon = True).start())
        self.bouton_2.configure(state = 'normal',command = lambda: Thread(target = self.bouton_fonction,args = (self.bouton_2,),daemon = True).start() )
        self.bouton_3.configure(state = 'normal',command = lambda: Thread(target = self.bouton_fonction,args = (self.bouton_3,),daemon=True).start() )
        self.bouton_5.configure(command = self.reintialiser)
    def tour_a_tour(self):
        """Cette fonction va permettre de tourner en boucle pierre, papier ciseaux sur un label"""

        self.temps = time.time() - self.debut
        self.compteur = int(int(self.temps*1.4 )% 5) #La, on aura uniquement les nombres 0,1,2
        self.label_8.configure(text=f"{self.liste[self.compteur]}")
        self.after(100,self.tour_a_tour)
    
    def evenements(self):
        """Ca a rapport aux évenements qui seront enclenchés lorsque la personne va vouloir démarrer le jeu"""
        Thread(target=self.after,args=(100,self.tour_a_tour),daemon = True).start()
        

    def selection_du_label_ordi(self,voila):
        """Cette fonction permet à l'ordinateur de selectionné un label"""
        self.voila = voila
        
        if self.choix_ordi == 0:
            self.label_3.config(bg = self.voila)
        if self.choix_ordi == 1:
            self.label_2.config(bg = self.voila)
        if self.choix_ordi == 2:
            self.label_1.config(bg = self.voila)
    
    def coloration_de_label(self,vainqueur):
        """Ici, c'est concernant la coloration et le marquage du choix fait par l'ordinateur"""
        self.vainqueur = vainqueur
        if self.vainqueur == 'ordinateur':
            return 'green'
        if self.vainqueur == 'nul':
            return 'blue'
        if self.vainqueur == 'utilisateur':
            return 'red'


    def coloration_du_bouton(self):
        """Cette fonction va permettre de colorier les autres boutons"""

        if self.gagnant == 'ordinateur':
            return self.couleur[2]
        if self.gagnant == 'nul':
            return self.couleur[1]
        if self.gagnant == 'utilisateur':
            return self.couleur[0]

    def bouton_fonction(self,element):
        """Cette fonction va nous permettre de gérer la logique des boutons"""

        self.element = element
        #Ici, on met la valeur de status sur true pour la suite
        self.status = True
        # Ici, le choix de l'ordi
        self.choix_ordi = ppp.choix_ordi()
        # Ici, la configuration du bouton sélectionnée
        self.choix_person = int(self.element.cget('text'))
        self.label_7.configure(text = self.liste[self.choix_person])
        self.label_5.configure(text = self.liste[self.choix_ordi])
        #Ici, on connait le gagnant 
        self.gagnant = ppp.reussir(self.choix_person,self.choix_ordi)
        #Configuration de la couleur du widget sélectionné
        self.element.configure(bg = self.coloration_du_bouton())
        #Coloration du label de l'ordinateur
        self.teinte = str(self.coloration_de_label(self.gagnant)) #Configuration de la couleur du label
        
        self.selection_du_label_ordi(self.teinte)
        #Maintenant on va bloquer tous les boutons 
        for button in (self.bouton_1,self.bouton_2,self.bouton_3):
            button.configure(state='disabled')
        #Cette fonction va permettre à l'utilisateur de connaitre celui qui a gagné
        self.annonce()
        # Attribution des points
        self.point = ppp.point(self.gagnant)
        self.base_point['ordinateur'] += self.point[1]
        self.base_point['utilisateur'] += self.point[0]
        self.label_4.configure(text = f"Score de \n l'ordinateur : \n {self.base_point['ordinateur']}")
        self.label_9.configure(text = f"Ton score  : \n {self.base_point['utilisateur']}")

        # Maintenant on va recommencer la partie
        Thread(target = self.master.bind,args = ('<Key>',self.recommencer),daemon = True).start()
        Thread(target = self.master.bind,args = ('<Button-1>',self.recommencer),daemon = True).start()

    def reintialiser(self):
        """Cette fonction va nous permettre de réintialiser le score """
        # Attribution des points
        self.base_point['ordinateur'] = 0
        self.base_point['utilisateur'] = 0
        self.label_4.configure(text = f"Score de \n l'ordinateur : \n {self.base_point['ordinateur']}")
        self.label_9.configure(text = f"Ton score  : \n {self.base_point['utilisateur']}")
        #Maintenant on va débloquer tous les boutons 
        for button in (self.bouton_1,self.bouton_2,self.bouton_3):
            button.configure(state='normal')
        #Maintenat on va restaurer tous les couleurs
        for button in (self.bouton_1,self.bouton_2,self.bouton_3):
            button.configure(bg='white')
        #De même pour tous les autres labels
        for label in (self.label_1,self.label_2,self.label_3):
            label.configure(bg='white')    
        self.status = False
        self.label_6.configure(text = 'Faîtes un \n choix',fg = 'blue')
        self.label_5.configure(text = '...',fg = 'blue')
        self.label_7.configure(text = '...',fg = 'blue')


    def recommencer(self,event):
        """Cette fonction va nous permettre de réintialiser la fenêtre"""
        if self.status == True:
            #Maintenant on va débloquer tous les boutons 
            for button in (self.bouton_1,self.bouton_2,self.bouton_3):
                button.configure(state='normal')
            #Maintenat on va restaurer tous les couleurs
            for button in (self.bouton_1,self.bouton_2,self.bouton_3):
                button.configure(bg='white')
            #De même pour tous les autres labels
            for label in (self.label_1,self.label_2,self.label_3):
                label.configure(bg='white')    
            self.status = False
            #cette ligne nous permet de nous débarrasser de cet élément encombrant
            self.master.after_cancel(self.deranger)
            self.label_6.configure(text = 'Faîtes un \n choix',fg = 'blue')
            self.label_5.configure(text = '...',fg = 'blue')
            self.label_7.configure(text = '...',fg = 'blue')
        else:
            pass
    def annonce(self):
        """Cette fonction nous permet d'annoncer le nom de celui qui a gagné"""
        if self.gagnant == 'ordinateur':
            self.label_6.configure(text = "Ce n'est pas ta\n chance \n maintenant; tu as \n perdu 😣😫",fg = 'purple')
        if self.gagnant == 'nul':
            self.label_6.configure(text = "Zut, c'est \n un nul 😑")
        if self.gagnant == 'utilisateur':
            self.label_6.configure(text = "Super, tu  \nas gagné 😎, \n Félicitations \n 🫡😍",fg = 'orange')
        #On va afficher un texte sur l'écran pour la personne au cas il veut réessayer
        self.deranger = self.master.after(6000,lambda : self.label_6.config(text = "Cliquer sur \n n'importe \n quelle touche du \n clavier ou de la \n souris pour continuer",fg = 'blue'))
        


# Définition des chemins d'accès des photos
path = ppp.resource_path('image.jpg')
ico = ppp.resource_path('icone.ico')
pierre_im = ppp.resource_path('pierre.png')
papier_im = ppp.resource_path('papier.png')
ciseaux_im = ppp.resource_path('ciseau.png')

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600+100+100')
        self.title('Pierre Papier Ciseaux')
        self.iconbitmap(ico)
        #Définition de la page 0
        self.page0 = page_0(self)
        
        #Placer la fenetre 0
        self.page0.show()
        
        #Définition de la page d'accueil en une instance
        self.accueil = page_1(self,path,ico)
        # Définition de la page de jeu en une seconde instance
        self.fenetre_1 = page_2(self,pierre_im,papier_im,ciseaux_im)
        
       
        #Configuration du bouton de la page0
        self.page0.agree.configure(command = lambda :Thread(target = self.fonction_du_bouton_agree,daemon = True).start())
        
        # Ici, c'est la fonction correspondant au bouton de quitter de la fenêtre, on accède à l'attribut simplement et de l'evenement 
        self.accueil.bouton_1.configure(command=lambda : Thread(target = self.fonction_du_bouton_1,daemon = True).start())
        # Ici, c'est la fonction correspondant au bouton de la page d'accueil
        self.fenetre_1.bouton_4.configure(command=lambda:Thread(target = self.fonction_du_bouton_quatre,daemon = True).start())
        #configuration de l'evenement fermeture  de la fenetre principale
        self.protocol('WM_DELETE_WINDOW',lambda :self.accueil.quitter())
        # Ceci sera affiché en dernier position
        self.mainloop()
    def fonction_du_bouton_agree(self):
        """Cette fonction va nous permettre de configurer la fonction du bouton agree"""
        self.page0.destroy()
        self.accueil.pack(fill = 'both',expand = True)
    def fonction_du_bouton_1(self):
        """Cette fonction va nous permettre d'exécuter les fonctions du bouton 1"""
        self.accueil.pack_forget()
        self.fenetre_1.pack(fill = 'both',expand=True)
        self.fenetre_1.begining(ico)
        self.fenetre_1.evenements()
    def fonction_du_bouton_quatre(self):
        """Cette fonction va nous permettre de configurer la fonction du bouton quatre"""
        self.fenetre_1.pack_forget()
        self.accueil.pack(fill = 'both',expand=True)
        self.fenetre_1.reintialiser()
app()
