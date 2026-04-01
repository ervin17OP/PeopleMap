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

## 2026-04-01 08:47 - KAN-4 - Cadrage initial du produit PeopleMap

- Demande: fournir le cadrage produit, le MVP, la stack technique et les contraintes du projet.
- Actions réalisées: formalisation du positionnement de PeopleMap comme application mobile de gestion des relations humaines ; synthèse de la vision, de l'objectif, des fonctionnalités MVP, de la stack Expo + Supabase + PostgreSQL et des contraintes d'architecture ; mise à jour du `README.md` pour en faire la base de référence du projet.
- Fichiers touchés: `README.md`, `SUIVI.md`.
- Commandes/tests lancés: lecture du repo, lecture de `README.md` et `SUIVI.md`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-4` déjà créé ; cadrage aligné avec l'initialisation du projet.
- Reste à faire: découper le MVP en sous-tâches, créer une branche de travail `feature/KAN-4-initialize-project`, puis scaffold Expo et la structure initiale.
- Risques / blocages: le périmètre métier est clair, mais le modèle de données initial et les règles du moteur de recommandation restent à définir précisément.

---

## 2026-04-01 08:49 - KAN-5 - Ticket Expo initial créé

- Demande: créer un ticket Jira pour l'initialisation du projet React Native avec Expo.
- Actions réalisées: création du ticket `KAN-5` avec le périmètre Expo, TypeScript, navigation React Navigation, structure de dossiers et critères d'acceptation de démarrage simulateur + navigation fonctionnelle.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-5` créé.
- Reste à faire: lire le ticket, créer la branche `feature/KAN-5-init-projet-react-native-avec-expo`, puis démarrer le scaffold technique.
- Risques / blocages: aucun blocage identifié pour la création du ticket.

---

## 2026-04-01 08:50 - KAN-6 - Ticket setup Supabase créé

- Demande: créer un ticket Jira pour la configuration de Supabase côté auth et base de données.
- Actions réalisées: création du ticket `KAN-6` avec le périmètre création projet Supabase, configuration Auth email/password, connexion de l'app mobile à Supabase et critère d'acceptation sur l'inscription/connexion.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-6` créé.
- Reste à faire: détailler les variables d'environnement, le schéma initial et l'intégration client Supabase dans l'app Expo.
- Risques / blocages: le ticket couvre bien l'intégration de base, mais pas encore la modélisation détaillée des tables métier.

---

## 2026-04-01 08:51 - KAN-7 - Ticket fiches personne créé

- Demande: créer un ticket Jira pour la création et la gestion des fiches personne.
- Actions réalisées: création du ticket `KAN-7` avec le périmètre CRUD de base sur une personne, les champs `nom`, `type_relation`, `notes rapides` et les critères d'acceptation de création, affichage de la liste et suppression.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-7` créé.
- Reste à faire: préciser la modification dans les critères d'acceptation et préparer le modèle de données correspondant côté Supabase.
- Risques / blocages: le champ `notes rapides` devra être clarifié plus tard si on veut distinguer résumé court et notes détaillées.

---

## 2026-04-01 08:52 - KAN-8 - Ticket écran liste des personnes créé

- Demande: créer un ticket Jira pour l'écran de liste des personnes.
- Actions réalisées: création du ticket `KAN-8` avec le périmètre d'affichage de toutes les personnes sous forme de liste et les critères d'acceptation de scroll et navigation vers la fiche détail.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-8` créé.
- Reste à faire: préciser le tri/ordre d'affichage, l'état vide et la source de données.
- Risques / blocages: le ticket suppose l'existence préalable du modèle personne et d'un écran détail.

---

## 2026-04-01 08:54 - KAN-9 - Ticket UI profil psychologique créé

- Demande: créer un ticket Jira pour l'interface d'édition du profil psychologique.
- Actions réalisées: création du ticket `KAN-9` avec le périmètre d'une interface simple de sélection des traits et les critères d'acceptation sur la rapidité de l'UX et la sauvegarde instantanée.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-9` créé.
- Reste à faire: définir la liste exacte des traits, le mode de stockage et le comportement de la sauvegarde instantanée.
- Risques / blocages: sans modèle comportemental stabilisé, l'UI risque d'évoluer rapidement après le premier prototype.

---

## 2026-04-01 08:55 - KAN-10 - Ticket notes datées créé

- Demande: créer un ticket Jira pour l'ajout de notes sur une personne.
- Actions réalisées: création du ticket `KAN-10` avec le périmètre d'ajout de notes datées et les critères d'acceptation d'ajout rapide et d'affichage en liste chronologique.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-10` créé.
- Reste à faire: préciser le format de la note, l'ordre chrono exact et le lien avec l'historique d'interactions.
- Risques / blocages: attention au recouvrement fonctionnel entre notes simples et interactions structurées.

---

## 2026-04-01 09:00 - KAN-11 - Ticket historique des interactions créé

- Demande: créer un ticket Jira pour l'affichage de l'historique des interactions.
- Actions réalisées: création du ticket `KAN-11` avec le périmètre d'une timeline des interactions et les critères d'acceptation de tri par date et de lisibilité.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-11` créé.
- Reste à faire: préciser le type exact d'interactions affichées, la granularité temporelle et les actions disponibles depuis la timeline.
- Risques / blocages: possible recouvrement avec les notes datées si le modèle interaction n'est pas bien différencié.

---

## 2026-04-01 09:02 - KAN-12 - Ticket moteur de règles créé

- Demande: créer un ticket Jira pour l'implémentation du moteur de recommandations basé sur des traits.
- Actions réalisées: création du ticket `KAN-12` avec le périmètre d'un système de recommandations à base de règles, un exemple de combinaison de traits et le critère d'acceptation d'une fonction pure retournant des conseils.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-12` créé.
- Reste à faire: définir le format des traits, le moteur de matching des règles et la structure de sortie des conseils.
- Risques / blocages: le modèle de règles doit rester simple au MVP pour éviter une complexité prématurée.

---

## 2026-04-01 09:06 - KAN-13 - Ticket affichage recommandations créé

- Demande: créer un ticket Jira pour l'affichage des recommandations sur la fiche personne.
- Actions réalisées: création du ticket `KAN-13` avec le périmètre d'affichage des conseils sur la fiche personne et les critères d'acceptation de lisibilité et d'adaptation au profil.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-13` créé.
- Reste à faire: préciser le format visuel des conseils, le moment de recalcul et le lien exact avec le moteur de règles.
- Risques / blocages: dépendance directe au modèle de profil psychologique et au moteur de recommandations.

---

## 2026-04-01 09:10 - KAN-14 - Ticket préparation d'interaction créé

- Demande: créer un ticket Jira pour le module de préparation d'une interaction.
- Actions réalisées: création du ticket `KAN-14` avec le périmètre d'un formulaire simple (`objectif`, `contexte`), un retour structuré en `DO` / `DON'T` et un critère d'acceptation basé sur une génération pilotée par des règles.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-14` créé.
- Reste à faire: définir les entrées exactes du formulaire, le format de sortie et la connexion avec le moteur de recommandations.
- Risques / blocages: dépend fortement de la qualité initiale du modèle de règles et de la structure des profils.

---

## 2026-04-01 09:13 - KAN-15 - Ticket UI cohérente créé

- Demande: créer un ticket Jira pour la mise en place d'une UI cohérente.
- Actions réalisées: création du ticket `KAN-15` avec le périmètre couleurs, composants UI (`cards`, `buttons`) et spacing, ainsi que le critère d'acceptation d'une interface propre et cohérente.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-15` créé.
- Reste à faire: définir un mini design system MVP (palette, typographie, tokens d'espacement, variantes de composants).
- Risques / blocages: sans direction visuelle minimale formalisée, le ticket peut rester trop large.

---

## 2026-04-01 09:14 - KAN-16 - Ticket authentification créé

- Demande: créer un ticket Jira pour l'authentification utilisateur.
- Actions réalisées: création du ticket `KAN-16` avec le périmètre `login / register` et le critère d'acceptation de session persistante.
- Fichiers touchés: `SUIVI.md`.
- Commandes/tests lancés: `./scripts/jira create --summary ... --description ...`.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: ticket `KAN-16` créé.
- Reste à faire: préciser les écrans, le flux exact, les validations de formulaire et le mécanisme de persistance de session dans Expo.
- Risques / blocages: fort lien avec la configuration Supabase Auth du ticket `KAN-6`.

---

## 2026-04-01 09:16 - KAN-12/KAN-13/KAN-14 - Précision métier sur le profil comportemental

- Demande: préciser la logique métier entre profil comportemental et conseils générés.
- Actions réalisées: formalisation dans le `README.md` du principe suivant : chaque personne possède un profil comportemental, et le système génère des conseils à partir d'une combinaison de traits ; ajout d'un exemple `communication: émotionnel` + `conflit: évite` menant à des conseils concrets.
- Fichiers touchés: `README.md`, `SUIVI.md`.
- Commandes/tests lancés: aucune.
- Git: branche `main`, aucun commit créé à ce stade.
- Jira: précision transverse utile pour `KAN-12`, `KAN-13` et `KAN-14`.
- Reste à faire: transformer cette logique en structure de données de traits puis en format de règles exécutable.
- Risques / blocages: il faudra éviter une explosion du nombre de combinaisons si trop de traits sont introduits trop tôt.

---

## 2026-04-01 10:15 - KAN-5 - Workflow Git push WSL documenté

- Demande: fiabiliser le push Git depuis WSL/OpenClaw et conserver les changements de workflow en attente.
- Actions réalisées: ajout de l'instruction de contournement via wrapper Windows dans `AGENTS.md`, ajout des scripts `scripts/git-push.cmd` et `scripts/git-push.ps1`, conservation du cadrage produit dans `README.md`, mise à jour du journal de suivi.
- Fichiers touchés: `AGENTS.md`, `README.md`, `SUIVI.md`, `scripts/git-push.cmd`, `scripts/git-push.ps1`.
- Commandes/tests lancés: `git status`, `git diff`, lecture des scripts de push.
- Git: branche `feature/KAN-5-init-projet-react-native-avec-expo`, commit en préparation.
- Jira: travail de support autour de `KAN-5`.
- Reste à faire: pousser la branche et reprendre l'implémentation Expo.
- Risques / blocages: l'auth Git depuis cette session WSL peut encore bloquer le push normal.

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
