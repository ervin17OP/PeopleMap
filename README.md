# PeopleMap

Application mobile de gestion des relations humaines.

## Vision

PeopleMap agit comme un « CRM humain » personnel : un outil pour analyser, comprendre et améliorer ses interactions sociales, en combinant mémoire relationnelle, profils comportementaux et aide à la préparation des échanges.

## Objectif

Permettre à un utilisateur de :

- gérer ses relations personnelles et professionnelles
- structurer ses observations sur les personnes
- mieux comprendre les profils comportementaux
- adapter ses interactions grâce à des conseils contextualisés

> Contrainte MVP : pas d'IA dans un premier temps ; les recommandations reposent sur des règles explicites.

## MVP

- création de fiches `Personne`
- ajout de notes et d'un historique d'interactions
- définition manuelle d'un profil comportemental
- moteur de recommandations basé sur des règles
- module `Préparer une interaction`

### Règle métier clé du MVP

Chaque personne possède un **profil comportemental**.

Le système génère ensuite des **conseils** à partir d'une **combinaison de traits**.

Exemple :

```ts
const profile = {
  communication: 'émotionnel',
  conflit: 'évite',
};
```

Conseils possibles associés :

- utiliser un ton doux
- éviter la confrontation directe
- poser des questions ouvertes

Implication produit : le moteur de recommandation doit rester explicable, déterministe et fondé sur des règles lisibles, sans IA pour le MVP.

## Stack technique

- **Mobile** : React Native avec Expo
- **Backend** : Supabase
- **Base de données** : PostgreSQL
- **Auth** : Supabase Auth

## Modèle métier initial

### Personne

Une fiche `Personne` contient au minimum :

- identité de base (`nom`)
- type de relation (`ami`, `collègue`, `famille`, `autre`)
- notes rapides
- notes datées / interactions
- profil comportemental

### Profil comportemental

Le profil comportemental est saisi manuellement à partir de traits structurés.

Premiers axes envisagés pour le MVP :

- `communication`
- `conflit`

Ce profil alimente directement :

- l'affichage de recommandations sur la fiche personne
- le module `Préparer une interaction`

## Contraintes produit et techniques

- UX simple et rapide
- pas d'IA pour le MVP
- architecture scalable pour permettre l'ajout d'IA plus tard

## Status

- projet créé
- dépôt Git initialisé
- workspace OpenClaw configuré
- GitHub connecté
- helper Jira connecté pour le projet `KAN`
- Telegram disponible comme canal de commande
- cadrage produit initial défini
- première application Expo initialisée dans `mobile/`

## Lancer l'application mobile

```bash
cd /mnt/c/Users/ervin/PeopleMap/mobile
npm install
npm start
```

Raccourcis utiles :

```bash
cd /mnt/c/Users/ervin/PeopleMap/mobile
npm run web
```

## Structure actuelle

```text
mobile/
  src/
    components/
    navigation/
    screens/
    services/
    store/
    theme/
```

## Prochaine étape recommandée

Construire le prochain incrément produit sur cette base Expo : auth, données Supabase et premiers écrans métier du MVP.

## Workflow opérationnel

- Jira est la source de vérité pour le suivi
- GitHub héberge le code et les branches
- OpenClaw peut être piloté depuis Telegram ou le Control UI
- Codex et OpenClaw partagent le même workspace local

## Développement piloté par tickets

- lire ou créer un ticket Jira d'abord
- créer une branche avec la clé Jira
- implémenter le travail
- commit avec la clé Jira
- push vers GitHub
- commenter le ticket Jira avec le statut
