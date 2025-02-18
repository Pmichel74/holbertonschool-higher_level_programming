Je vais vous faire un résumé détaillé de l'utilisation de curl pour consommer des données d'API.

## 1. Installation et Vérification de curl

### Vérification de l'installation
```bash
curl --version
```
Sortie attendue :
```
curl 7.88.1 (x86_64-pc-linux-gnu) libcurl/7.88.1 OpenSSL/3.0.8
Protocols: http https ftp ftps ...
Features: SSL IPv6 libz UnixSockets ...
```

## 2. Opérations de Base avec curl

### 1. Requête GET simple
```bash
# Récupérer tous les posts
curl https://jsonplaceholder.typicode.com/posts
```
Sortie : Liste de posts au format JSON

### 2. Afficher uniquement les en-têtes
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```
Sortie :
```
HTTP/2 200
date: Tue, 18 Feb 2025 12:42:00 GMT
content-type: application/json
cache-control: max-age=43200
...
```

## 3. Opérations CRUD Avancées

### 1. Créer (POST)
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Mon titre","body":"Contenu","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

### 2. Lire (GET) avec paramètres
```bash
# Récupérer un post spécifique
curl https://jsonplaceholder.typicode.com/posts/1

# Filtrer les posts
curl https://jsonplaceholder.typicode.com/posts?userId=1
```

### 3. Mettre à jour (PUT)
```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"Titre modifié","body":"Nouveau contenu","userId":1}' \
  https://jsonplaceholder.typicode.com/posts/1
```

### 4. Supprimer (DELETE)
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

## 4. Options Utiles de curl

### 1. Format et Présentation
```bash
# Formater la sortie JSON
curl https://jsonplaceholder.typicode.com/posts | json_pp

# Sauvegarder dans un fichier
curl -o posts.json https://jsonplaceholder.typicode.com/posts
```

### 2. En-têtes Personnalisés
```bash
curl -H "Authorization: Bearer token123" \
     -H "Content-Type: application/json" \
     https://api.exemple.com/data
```

### 3. Verbosité et Débogage
```bash
# Mode verbeux
curl -v https://jsonplaceholder.typicode.com/posts

# Afficher le temps de réponse
curl -w "\nTemps total: %{time_total}s\n" \
     https://jsonplaceholder.typicode.com/posts
```

## 5. Gestion des Erreurs Courantes

### 1. Certificats SSL
```bash
# Ignorer la vérification SSL (déconseillé en production)
curl -k https://site-avec-cert-invalide.com

# Spécifier un certificat
curl --cacert mon-cert.pem https://api.exemple.com
```

### 2. Redirection
```bash
# Suivre les redirections
curl -L http://site-qui-redirige.com
```

## 6. Bonnes Pratiques

1. **Sécurité**
   - Toujours utiliser HTTPS en production
   - Ne pas désactiver la vérification SSL sans raison valable
   - Protéger les informations sensibles dans les en-têtes

2. **Performance**
   - Utiliser la compression quand possible
   - Mettre en cache les réponses quand approprié
   - Limiter la verbosité en production

3. **Débogage**
   - Utiliser -v pour le débogage
   - Sauvegarder les réponses importantes
   - Vérifier les codes de statut HTTP

## 7. Exemples de Réponses Typiques

### Succès (200 OK)
```json
{
  "id": 1,
  "title": "Mon Post",
  "body": "Contenu",
  "userId": 1
}
```

### Erreur (404 Not Found)
```json
{
  "error": "Resource not found"
}
```

### Création Réussie (201 Created)
```json
{
  "id": 101,
  "title": "Nouveau Post",
  "body": "Contenu",
  "userId": 1
}
```

Cette structure couvre les aspects essentiels de l'utilisation de curl pour interagir avec des APIs RESTful, de l'installation aux opérations avancées en passant par les bonnes pratiques.