import { StatusBar } from "expo-status-bar";
import { SafeAreaView, StyleSheet, Text, View } from "react-native";

export default function App() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="dark" />
      <View style={styles.container}>
        <Text style={styles.eyebrow}>PeopleMap</Text>
        <Text style={styles.title}>Mieux comprendre les personnes qui comptent</Text>
        <Text style={styles.body}>
          Une base propre Expo est en place. La suite servira a ajouter les ecrans,
          les profils comportementaux et les recommandations d'interaction.
        </Text>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Prochaine etape</Text>
          <Text style={styles.cardBody}>
            Connecter le flux produit aux tickets Jira et construire le premier vrai
            parcours utilisateur.
          </Text>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#f6f1e8",
  },
  container: {
    flex: 1,
    justifyContent: "center",
    paddingHorizontal: 24,
    gap: 16,
  },
  eyebrow: {
    color: "#8a5a44",
    fontSize: 16,
    fontWeight: "700",
    textTransform: "uppercase",
    letterSpacing: 1.2,
  },
  title: {
    color: "#1f2a2a",
    fontSize: 36,
    fontWeight: "800",
    lineHeight: 42,
  },
  body: {
    color: "#415050",
    fontSize: 17,
    lineHeight: 26,
  },
  card: {
    marginTop: 12,
    borderRadius: 20,
    backgroundColor: "#ffffff",
    padding: 20,
    shadowColor: "#000000",
    shadowOpacity: 0.08,
    shadowRadius: 18,
    shadowOffset: { width: 0, height: 8 },
    elevation: 3,
  },
  cardTitle: {
    color: "#1f2a2a",
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 8,
  },
  cardBody: {
    color: "#546565",
    fontSize: 15,
    lineHeight: 22,
  },
});
