<script setup>
import { ref, onMounted } from "vue";
import AppHeader from "./components/AppHeader.vue";
import KpiCards from "./components/KpiCards.vue";
import Leaderboard from "./components/Leaderboard.vue";
const selectedSeason = ref("");
const selectedTeam = ref("");
const seasons = ref([]);
const teams = ref([]);
onMounted(() => {
    fetch("/api/meta")
        .then((res) => res.json())
        .then((data) => {
            seasons.value = data.seasons;
            teams.value = data.teams;
        });
});
</script>

<template>
    <AppHeader
        :selected-season="selectedSeason"
        :selected-team="selectedTeam"
        :seasons="seasons"
        :teams="teams"
        @update:season="selectedSeason = $event"
        @update:team="selectedTeam = $event"
    />
    <main>
        <KpiCards
            :selected-season="selectedSeason"
            :selected-team="selectedTeam"
        />
        <div class="leaderboard-container">
            <Leaderboard
                :selected-season="selectedSeason"
                :selected-team="selectedTeam"
                type="batting"
            />
            <Leaderboard
                :selected-season="selectedSeason"
                :selected-team="selectedTeam"
                type="bowling"
            />
        </div>
    </main>
</template>
