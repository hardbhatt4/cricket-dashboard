<script setup>
const props = defineProps({
    selectedSeason: String,
    selectedTeam: String,
    seasons: Array,
    teams: Array,
});

const emit = defineEmits(["update:season", "update:team"]);
</script>

<template>
    <header>
        <h1>Cricket Stats Dashboard</h1>
        <div class="filters">
            <select
                v-on:change="emit('update:season', $event.target.value)"
                :value="selectedSeason"
            >
                <option value="">All Seasons</option>
                <option v-for="season in seasons" :key="season" :value="season">
                    {{ season }}
                </option>
            </select>

            <select
                v-on:change="emit('update:team', $event.target.value)"
                :value="selectedTeam"
            >
                <option value="">All Teams</option>
                <option v-for="team in teams" :key="team" :value="team">
                    {{ team }}
                </option>
            </select>
        </div>
    </header>
</template>
