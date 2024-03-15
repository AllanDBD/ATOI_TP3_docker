import redis

def count_words(filename):
    # Initialisation de Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Ouvrir le fichier texte
    with open(filename, 'r') as file:
        # Parcourir chaque ligne du fichier
        for line in file:
            # Diviser la ligne en mots
            words = line.split()
            # Compter les occurrences de chaque mot
            for word in words:
                # Incrémenter le compteur de chaque mot dans Redis
                r.hincrby('word_count', word, 1)

    # Récupérer les mots et leurs comptes finaux
    word_counts = r.hgetall('word_count')
    
    # Afficher les mots et leurs comptes finaux
    for word in r.hkeys('word_count'):
        count = r.hget('word_count', word).decode('utf-8')
        print(f"{word.decode('utf-8')}: {count}")

if __name__ == "__main__":
    filename = '/home/allandbd/ATOI_24_TP/TP3_docker/ex6/gp.txt'  # Nom de votre fichier texte
    count_words(filename)
