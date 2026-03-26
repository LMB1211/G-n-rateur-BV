import streamlit as st
import random

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Le Loto de la Contrainte", page_icon="🎲", layout="wide")

# --- LES DONNÉES ---

objets = [
    # 50 Objets utopiques / extrêmes
    "Un aérostat / Une montgolfière", "Un phare", "Une cité marchante", "Un sous-marin de poche", "Un monastère", "Une machine à remonter le temps", "Un pont habité", "Un vaisseau générationnel", "Une bibliothèque labyrinthique", "Un navire brise-glace", 
    "Une station spatiale", "Un observatoire astronomique", "Une arène de gladiateurs", "Un train transcontinental", "Un asile psychiatrique", "Une forteresse volante", "Un kiosque à musique", "Une usine désaffectée", "Une roulotte mécanique", "Un barrage gigantesque", 
    "Un ascenseur spatial", "Un temple oublié", "Un bunker souterrain", "Une serre botanique géante", "Une horloge monumentale", "Une plateforme pétrolière reconvertie", "Une cabane", "Un mégalithe organique", "Un mémorial", "Une taverne", 
    "Un nid géant", "Une capsule de survie", "Une station de pompage", "Un labyrinthe de verre", "Un port spatial", "Un aqueduc", "Un moulin repensé", "Un palais", "Une boîte à musique géante", "Une tente", 
    "Un reliquaire", "Un marché couvert", "Une prison de haute sécurité", "Un dirigeable de luxe", "Un théâtre anatomique", "Une tour sans fin", "Un kiosque de téléportation", "Une ruine mystique", "Une ambassade", "Une Arche",
    # 50 Objets concrets / quotidiens
    "Une station-service", "Un arrêt de bus", "Une école maternelle", "Un marché en plein air", "Une caserne de pompiers", "Un food-truck", "Une maison pavillonnaire", "Un péage", "Un gymnase", "Une tour de bureaux",
    "Un refuge", "Une gare de triage", "Un château d'eau", "Une déchetterie / centre de tri", "Une boulangerie", "Un cinéma indépendant", "Un pont suspendu", "Une capitainerie", "Un hôpital", "Une station d'épuration",
    "Un skatepark", "Un bureau de poste", "Un pigeonnier", "Un lavoir", "Une piscine en plein air", "Un silo à grains", "Un funiculaire", "Un parking à étages", "Une tiny house", "Un abri de jardin",
    "Une gare ferroviaire", "Une serre agricole", "Un hôtel de ville", "Une gare routière", "Un tribunal de grande instance", "Une capitelle (cabane en pierre sèche)", "Une éolienne", "Un belvédère", "Un centre commercial", "Une caravane Airstream",
    "Un funérarium", "Un studio d'enregistrement", "Une auberge de jeunesse", "Un atelier de menuiserie", "Une laverie automatique", "Un kiosque à journaux", "Un bateau de pêche au chalut", "Une station de métro", "Un data-center", "Un stade nautique"
]

usages = [
    # 50 Usages ouverts / épiques
    "Cacher un secret", "Surveiller les étoiles", "Célébrer un culte", "S'isoler du monde", "Produire de l'énergie", "Voyager sans but", "Fuir une menace", "Étudier l'inconnu", "Guérir une maladie", "Conserver la mémoire",
    "Rendre la justice", "S'amuser / Divertir", "Défier la gravité", "Méditer", "Négocier la paix", "Attendre la fin du monde", "Élever des créatures", "Cultiver des rêves", "Fabriquer des illusions", "Punir un crime",
    "Accueillir des exilés", "Transmettre un savoir", "Se perdre", "Dormir pour l'éternité", "Écouter le silence", "Survivre à la nuit", "Explorer les abysses", "Cartographier le vide", "Contempler l'horizon", "Réparer une machine",
    "Chercher l'inspiration", "Organiser un tournoi", "Communiquer avec l'au-delà", "Prier", "Festoyer", "Se cacher de la lumière", "Dompter les éléments", "Observer sans être vu", "Traverser une frontière", "Défendre un trésor",
    "Recycler le passé", "Capturer le vent", "Attirer l'attention", "Créer de la beauté", "Collecter des nuages", "Résoudre une énigme", "Tromper l'ennemi", "Chercher l'oubli", "Rencontrer des étrangers", "Attendre un signe",
    # 50 Usages concrets / quotidiens
    "Vendre du pain et des viennoiseries", "Attendre le bus sous la pluie", "Trier des déchets recyclables", "Apprendre à nager", "Réparer des vélos", "Stocker des archives administratives", "Cultiver des tomates en hiver", "Héberger des sans-abris", "Laver son linge", "Passer le permis de conduire",
    "Organiser un mariage", "Voter pour les élections locales", "Surveiller la baignade", "Payer l'autoroute", "Prendre un café le matin", "Garer sa voiture", "Regarder un film", "Promener son chien", "Faire de la musculation", "Accoucher",
    "Traiter les eaux usées", "Faire le plein d'essence", "Vendre des fruits et légumes", "Lire un livre au calme", "Jouer à la pétanque", "Réparer une fuite d'eau", "Attendre son tour chez le médecin", "Déposer un colis", "Acheter le journal", "Extraire du gravier",
    "Dormir une nuit en transit", "Prendre les transports pour aller au travail", "Faire grève", "Faire du skateboard", "Visiter une exposition", "Déjeuner sur le pouce", "Pêcher à la ligne", "Enregistrer un podcast", "Faire ses devoirs", "Se réunir en syndic de copropriété",
    "Apprendre la musique", "Se faire couper les cheveux", "Coudre des vêtements", "Distribuer le courrier", "Héberger des serveurs informatiques", "Observer les oiseaux migrateurs", "Saisir des données sur un ordinateur", "Changer une roue de voiture", "Fabriquer de la bière artisanale", "Regarder passer les trains"
]

personnages = [
    # 50 Personnages épiques / fictifs
    "Un horloger aveugle", "Une intelligence artificielle mélancolique", "Un pirate des airs", "Un dieu oublié", "Un enfant roi", "Une botaniste extraterrestre", "Un collectionneur de souvenirs", "Un cyborg obsolète", "Un ermite centenaire", "Un inventeur incompris",
    "Une reine en exil", "Un archéologue de l'an 3000", "Un voleur de rêves", "Un architecte mégalomane", "Un mercenaire repenti", "Un diplomate intergalactique", "Une sorcière urbaine", "Un fantôme amnésique", "Un alchimiste", "Un cartographe des étoiles",
    "Un poète muet", "Une meute de loups", "Un gardien de phare", "Un explorateur des abysses", "Un juge sans pitié", "Une muse", "Un colosse de pierre", "Un marchand de sable", "Une civilisation microscopique", "Un prophète",
    "Un cuisinier nomade", "Un joueur compulsif", "Un savant fou", "Une secte secrète", "Un robot jardinier", "Un chasseur de monstres", "Un musicien ambulant", "Une princesse rebelle", "Un espion", "Un fossoyeur",
    "Un clone défectueux", "Un dragon métamorphe", "Un extraterrestre curieux", "Un esprit de la forêt", "Un maître d'arts martiaux", "Un chaman", "Un détective privé du futur", "Un pilote de mécha", "Une entité cosmique", "Le dernier humain",
    # 50 Personnages concrets / quotidiens
    "Un facteur à vélo", "Une institutrice de maternelle", "Un chauffeur de bus de nuit", "Un boulanger lève-tôt", "Une infirmière urgentiste", "Un comptable fatigué", "Un maire de petite commune", "Un étudiant en première année", "Une famille de 5 personnes en vacances", "Un retraité qui nourrit les pigeons",
    "Une agente immobilière", "Un maraîcher bio", "Un contrôleur de train", "Un agent d'entretien", "Un architecte stagiaire", "Une développeuse web en télétravail", "Un mécanicien garagiste", "Un livreur Uber Eats", "Un pêcheur breton", "Une coiffeuse",
    "Un agent de sécurité de centre commercial", "Un chauffeur de taxi", "Une bibliothécaire", "Un ouvrier du BTP", "Un kinésithérapeute", "Une avocate d'affaires", "Un groupe de touristes égarés", "Un éboueur", "Une caissière de supermarché", "Un plombier dépanneur",
    "Un adolescent en pleine crise", "Une assistante sociale", "Un garde forestier", "Un artisan menuisier", "Un pompier volontaire", "Une contrôleuse fiscale", "Un restaurateur angoissé", "Un vendeur de chaussures", "Un DJ de mariage", "Un pharmacien de garde",
    "Un chauffeur de poids lourd", "Une journaliste locale", "Un moniteur d'auto-école", "Un vendeur de kebabs", "Un huissier de justice", "Un guide de haute montagne", "Une guichetière de la Poste", "Un SDF", "Un vétérinaire de campagne", "Un inspecteur du permis de conduire"
]

contextes_chrono = [
    # 50 Époques extrêmes / historiques
    "Pendant la Révolution Industrielle", "À la fin de l'Univers", "Dans les années 1920 (Années Folles)", "Époque victorienne (Steampunk)", "Antiquité mythologique", "Futur cyberpunk (2077)", "Juste avant l'impact d'un météore", "Au temps des dinosaures", "Moyen-Âge uchronique (Fantasy)", "Rétrofuturisme des années 50",
    "Pendant une ère glaciaire", "La première minute de la Création", "Époque des Grandes Découvertes", "En l'an 3000", "La veille d'une grande guerre", "Le jour de l'apocalypse", "Pendant une éclipse solaire totale", "L'Âge d'or de la piraterie", "À l'aube de l'humanité", "Renaissance magique",
    "Le temps des croisades", "Après la disparition de l'humanité", "Dans un futur utopique (Solarpunk)", "En pleine période de prohibition", "L'Âge d'or de la science-fiction", "Un mardi pluvieux", "Pendant la construction des pyramides", "Le crépuscule des dieux", "Période Edo au Japon", "Années 80 (Néons et Synthwave)",
    "Fin du 19ème siècle", "Pendant un bug informatique mondial", "Une époque figée dans le temps", "La nuit des temps", "Époque des samouraïs", "Pendant la Guerre Froide", "L'ère de la colonisation spatiale", "Le siècle des Lumières", "Dans un futur dictatorial", "À l'époque de la ruée vers l'or",
    "Juste après la découverte du feu", "Pendant une pandémie zombie", "Un futur où la technologie a disparu", "Le dernier jour de l'été", "La nuit d'Halloween", "Un hiver nucléaire", "L'ère des machines intelligentes", "Au temps des mythes grecs", "Pendant un festival millénaire", "Une minute de silence",
    # 50 Moments concrets / quotidiens
    "Aujourd'hui, vers 15h", "Pendant la canicule de l'été 2003", "Les Trente Glorieuses (Années 60)", "Le matin de Noël", "Pendant le confinement de 2020", "Un dimanche après-midi en automne", "La semaine prochaine", "L'hiver rude de 1954", "La nuit du passage à l'an 2000", "Pendant la mi-temps d'un match de foot",
    "Au lever du soleil en plein mois d'août", "Pendant les grèves de Mai 68", "Un vendredi soir de chassé-croisé sur l'autoroute", "Les années 90 (Grunge et premiers portables)", "L'heure de pointe (18h-19h)", "Lors de la rentrée des classes", "Pendant une panne de courant de quartier", "Un jour de marché (mercredi matin)", "Pendant la Révolution Française (1789)", "Les années 70 (Pattes d'éph et chocs pétroliers)",
    "La nuit de la Saint-Sylvestre", "Pendant les congés payés de 1936", "Un lundi matin gris et pluvieux", "Lors d'une alerte météo orange pour orages", "Pendant les Jeux Olympiques", "Au moment de la fermeture des bars (2h du matin)", "Le jour de la Fête de la Musique", "L'après-guerre (1945-1950)", "Pendant un épisode de pollution aux particules fines", "Le premier jour des soldes",
    "Au crépuscule (l'heure bleue)", "Pendant les élections présidentielles", "Époque gallo-romaine", "Un jour férié désert en ville", "Pendant une vague de froid polaire (-10°C)", "Le jour de la récolte des vendanges", "À l'heure du déjeuner (12h30)", "La Belle Époque (1900-1914)", "Pendant un mariage à la mairie", "Un soir de pleine lune dégagée",
    "Les années 2000 (Y2K)", "Le jour du baccalauréat", "Pendant le passage du Tour de France", "Un samedi après-midi", "La nuit la plus courte de l'année (solstice d'été)", "Pendant une brocante/vide-grenier", "Le premier jour de la neige", "Un jour de grève des transports", "Au beau milieu de la nuit (3h45 du matin)", "Il y a exactement 10 ans"
]

contextes_geo = [
    # 50 Biomes / Territoires extrêmes ou fictifs
    "Le cratère d'un volcan en éruption", "Une fosse océanique abyssale", "La surface d'un astéroïde", "Une forêt bioluminescente", "L'orbite d'un trou noir", "Un désert de sel infini", "La calotte glaciaire d'une exoplanète", "Les anneaux d'une géante gazeuse", "Un vaste réseau de grottes de cristal", "La chaîne de montagnes de l'Himalaya martien",
    "Un océan de magma", "La stratosphère", "Une toundra gelée post-apocalyptique", "L'épicentre d'un ouragan perpétuel", "Le cœur d'une nébuleuse", "Un continent englouti", "Une plaine ravagée par les radiations", "Un système de canyons extraterrestres", "La surface de la Lune", "Les nuages d'acide de Vénus",
    "Une jungle d'algues géantes sous-marines", "Un champ d'astéroïdes dense", "Un univers de poche en expansion", "L'œil d'un cyclone de la taille de Jupiter", "Un biome fongique géant", "Une savane de cristal", "Le manteau terrestre", "Un lac d'ammoniac liquide", "Une plaine de cendres volcaniques", "Un archipel céleste (îles flottantes)",
    "La ceinture de Kuiper", "Un continent de plastique à la dérive", "Un désert de sable rouge balayé par les vents", "Une forêt pétrifiée millénaire", "Le lit asséché d'un océan antique", "Une vallée encaissée sans lumière solaire", "Une banquise en dislocation", "Une étendue de toundra permafrostée", "Un maelström océanique", "Les confins de la Voie Lactée",
    "Un marais acide brumeux", "Le sommet d'une montagne qui perce l'atmosphère", "Une zone de singularité temporelle", "Un delta fluvial toxique", "Un cratère d'impact météorique géant", "Une steppe aride balayée par des tempêtes magnétiques", "Le point Nemo (le pôle d'inaccessibilité océanique)", "L'intérieur d'un glacier millénaire", "Une plaine de geysers en éruption", "La face cachée d'une lune rocheuse",
    # 50 Biomes / Territoires réels et concrets
    "Le désert de l'Arizona", "La forêt amazonienne", "La toundra sibérienne", "La cordillère des Andes", "Le delta du Gange", "Le Sahara", "Les fjords de Norvège", "La Grande Barrière de Corail", "Les plaines de la pampa argentine", "La vallée de la Mort (Death Valley)",
    "Les hauts plateaux du Tibet", "La savane du Serengeti", "La forêt noire en Allemagne", "Le littoral breton balayé par les vents", "La taïga canadienne", "L'outback australien", "Le bassin du Congo", "Le golfe du Bengale", "La steppe mongole", "Le grand canyon du Colorado",
    "Les Everglades en Floride", "Le désert de Gobi", "Les îles Galápagos", "La péninsule antarctique", "La vallée du Rift en Afrique de l'Est", "Les Alpes suisses", "Le marais poitevin", "La mer Morte", "Le delta de l'Okavango", "La plaine de la Beauce",
    "Les calanques de Marseille", "Le désert d'Atacama", "La baie d'Halong", "Les landes d'Écosse", "Le littoral de la Patagonie", "La mer de Glace", "Les plaines du Midwest américain", "La lagune de Venise", "Le Kilimandjaro", "Le désert de Mojave",
    "La forêt de séquoias géants", "La Camargue", "L'archipel d'Hawaï", "La région des chutes du Niagara", "La vallée du Nil", "La mer d'Aral (asséchée)", "Le cercle polaire arctique", "Les îles Féroé", "Les Cévennes", "Le golfe du Morbihan"
]

delais = ["1 semaine", "2 semaines", "3 semaines", "4 semaines (1 mois)"]

# --- INTERFACE UTILISATEUR ---
st.title("🎲 Le Loto de la Contrainte")
st.write("Bienvenue dans le générateur de défis ! Appuyez sur le bouton pour obtenir votre prochain brief créatif et sa deadline.")

st.divider()

# --- LE BOUTON ET LE TIRAGE ---
if st.button("🚀 Générer un nouveau défi !", use_container_width=True):
    
    # Sélection aléatoire
    choix_objet = random.choice(objets)
    choix_usage = random.choice(usages)
    choix_perso = random.choice(personnages)
    choix_chrono = random.choice(contextes_chrono)
    choix_geo = random.choice(contextes_geo)
    choix_delai = random.choice(delais)
    
    st.success(f"🎉 Voici votre nouveau défi créatif ! Vous avez **{choix_delai}** pour le réaliser.")
    
    # Affichage visuel sur 3 colonnes pour une meilleure lisibilité
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"**📦 Objet :**\n\n{choix_objet}")
        st.info(f"**🌍 Lieu (Site) :**\n\n{choix_geo}")
        
    with col2:
        st.info(f"**🛠️ Usage :**\n\n{choix_usage}")
        st.info(f"**⏳ Époque :**\n\n{choix_chrono}")

    with col3:
        st.info(f"**👤 Personnage :**\n\n{choix_perso}")
        st.error(f"**⏱️ Deadline :**\n\n{choix_delai}")

st.divider()
st.caption("À vos crayons/souris, et que le meilleur gagne !")
