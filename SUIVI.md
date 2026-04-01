# SUIVI

Journal de suivi opérationnel du projet `PeopleMap`.

But:

- garder une trace courte et utile de ce qu'OpenClaw ou Codex a fait
- permettre une reprise rapide par une simple relecture
- centraliser les actions importantes liées à Jira, GitHub et au code

Mode d'emploi:

- ajouter une entrée après chaque tâche significative
- ne pas effacer l'historique
- rester concret et court
- inclure la clé Jira si elle existe

Modèle d'entrée:

## YYYY-MM-DD HH:MM - KAN-XXX - Titre court

- Demande: ...
- Actions réalisées: ...
- Fichiers touchés: ...
- Commandes/tests lancés: ...
- Git: branche ..., commit ...
- Jira: ticket lu/créé/commenté ...
- Reste à faire: ...
- Risques / blocages: ...

---

## 2026-04-01 08:45 - Setup - Workflow Jira/GitHub/OpenClaw

- Demande: préparer un environnement stable pour travailler avec OpenClaw, GitHub, Jira et Telegram.
- Actions réalisées: création du repo PeopleMap, connexion GitHub, mise en place du helper Jira local, configuration du workspace OpenClaw, connexion Telegram, documentation des conventions de travail.
- Fichiers touchés: `README.md`, `AGENTS.md`, `TOOLS.md`, `USER.md`, `IDENTITY.md`, `SOUL.md`, `scripts/jira`, `scripts/jira.py`, `docs/jira-workflow.md`.
- Commandes/tests lancés: vérification GitHub push, appels API Jira (`me`, `search`, `get`), tests OpenClaw gateway et Telegram.
- Git: branche `main`, derniers commits de setup déjà poussés sur GitHub.
- Jira: accès au projet `KAN` confirmé, création de ticket depuis Telegram testée avec succès.
- Reste à faire: démarrer le développement réel de PeopleMap à partir d'un ticket Jira.
- Risques / blocages: stabilité imparfaite du lancement automatique OpenClaw au boot Windows; lancement manuel stable préféré pour l'instant.

---

## 2026-04-01 13:30 - KAN-6 - Base Expo reconstruite pour partage

- Demande: remettre le repo dans un etat recuperable sur un autre PC puis tout pousser sur GitHub.
- Actions realisees: reconstruction d'une base Expo versionnable dans mobile/, ajout d'un App.tsx minimal, d'une configuration Expo/TypeScript propre, et d'un .gitignore local pour exclure .expo, dist et 
ode_modules.
- Fichiers touches: mobile/.gitignore, mobile/package.json, mobile/app.json, mobile/babel.config.js, mobile/tsconfig.json, mobile/index.ts, mobile/App.tsx, SUIVI.md.
- Commandes/tests lances: nettoyage de 
ode_modules, 
pm install, lancement Expo web local.
- Git: branche eature/KAN-6-setup-supabase, commit a creer puis push.
- Jira: travail transverse pour rendre le chantier mobile partageable.
- Reste a faire: reconnecter le vrai travail fonctionnel OpenClaw aux tickets actifs et stabiliser l'apercu mobile Expo Go.
- Risques / blocages: la pile actuelle demande une version Node un peu plus recente pour certains paquets React Native, meme si le preview web fonctionne deja.

