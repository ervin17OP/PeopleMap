import { SafeAreaView, ScrollView, StyleSheet, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';

import { FeatureCard } from '../components/FeatureCard';
import { colors } from '../theme/colors';
import { spacing } from '../theme/spacing';

export function HomeScreen() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="light" />
      <ScrollView contentContainerStyle={styles.content}>
        <View style={styles.hero}>
          <View style={styles.badge}>
            <Text style={styles.badgeText}>PeopleMap</Text>
          </View>
          <Text style={styles.title}>Mieux comprendre les personnes, sans perdre le fil.</Text>
          <Text style={styles.subtitle}>
            Une base propre pour construire ton CRM humain : profils, notes, interactions et conseils
            contextualisés.
          </Text>
        </View>

        <View style={styles.statsRow}>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>MVP</Text>
            <Text style={styles.statLabel}>Expo + TypeScript</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>KAN-5</Text>
            <Text style={styles.statLabel}>Base mobile prête</Text>
          </View>
        </View>

        <View style={styles.cards}>
          <FeatureCard
            eyebrow="Relations"
            title="Fiches personnes"
            description="Centraliser les informations utiles sur chaque relation perso ou pro."
          />
          <FeatureCard
            eyebrow="Mémoire"
            title="Notes & interactions"
            description="Retrouver rapidement le contexte, l’historique et les signaux importants."
          />
          <FeatureCard
            eyebrow="Aide"
            title="Conseils contextualisés"
            description="Préparer une interaction avec des recommandations simples basées sur des règles."
          />
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.background,
  },
  content: {
    padding: spacing.lg,
    paddingBottom: spacing.xxl,
    gap: spacing.lg,
  },
  hero: {
    marginTop: spacing.md,
    gap: spacing.md,
  },
  badge: {
    alignSelf: 'flex-start',
    backgroundColor: colors.surfaceMuted,
    borderRadius: 999,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    borderWidth: 1,
    borderColor: colors.border,
  },
  badgeText: {
    color: colors.primarySoft,
    fontWeight: '700',
    fontSize: 13,
  },
  title: {
    color: colors.text,
    fontSize: 34,
    lineHeight: 40,
    fontWeight: '800',
  },
  subtitle: {
    color: colors.textMuted,
    fontSize: 16,
    lineHeight: 24,
    maxWidth: 560,
  },
  statsRow: {
    flexDirection: 'row',
    gap: spacing.md,
  },
  statCard: {
    flex: 1,
    backgroundColor: colors.surface,
    borderRadius: 18,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: colors.border,
    gap: spacing.xs,
  },
  statValue: {
    color: colors.success,
    fontSize: 18,
    fontWeight: '800',
  },
  statLabel: {
    color: colors.textMuted,
    fontSize: 14,
  },
  cards: {
    gap: spacing.md,
  },
});
