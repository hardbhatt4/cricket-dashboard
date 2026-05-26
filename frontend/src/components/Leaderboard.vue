<script setup>
import { ref, computed, onMounted, watch } from "vue";
const props = defineProps({
    selectedTeam: String,
    selectedSeason: String,
    type: String,
});
const rows = ref([]);
const loading = ref(true);
const sortKey = ref(props.type === "batting" ? "runs" : "wickets");
const sortAsc = ref(false);

const fetchData = () => {
    const params = new URLSearchParams();
    if (props.selectedSeason) {
        params.append("season", props.selectedSeason);
    }
    if (props.selectedTeam) {
        params.append("team", props.selectedTeam);
    }
    fetch(`/api/${props.type}?${params.toString()}`)
        .then((response) => response.json())
        .then((data) => {
            rows.value = data;
            loading.value = false;
        });
};

onMounted(() => {
    fetchData();
});

watch(
    () => [props.selectedSeason, props.selectedTeam],
    () => {
        loading.value = true;
        fetchData();
    },
);

const columns = computed(() => {
    if (props.type === "batting") {
        return [
            { key: "player", label: "Player" },
            { key: "runs", label: "Runs" },
            { key: "average", label: "Average" },
            { key: "strike_rate", label: "Strike Rate" },
            { key: "sixes", label: "Sixes" },
        ];
    }
    if (props.type === "bowling") {
        return [
            { key: "player", label: "Player" },
            { key: "wickets", label: "Wickets" },
            { key: "runs_conceded", label: "Runs Conceded" },
            { key: "average", label: "Average" },
            { key: "economy", label: "Economy" },
        ];
    }
    return [];
});

const sortedRows = computed(() => {
    if (!sortKey.value) return rows.value.slice(0, 20);
    return [...rows.value]
        .sort((a, b) => {
            const aVal = a[sortKey.value] ?? -1;
            const bVal = b[sortKey.value] ?? -1;
            return sortAsc.value ? aVal - bVal : bVal - aVal;
        })
        .slice(0, 20);
});

const toggleSort = (key) => {
    if (sortKey.value === key) {
        sortAsc.value = !sortAsc.value;
    } else {
        sortKey.value = key;
        sortAsc.value = false;
    }
};
</script>

<template>
    <div class="Leaderboard">
        <h1 v-if="props.type === 'batting'">Batting Leaderboard</h1>
        <h1 v-else-if="props.type === 'bowling'">Bowling Leaderboard</h1>
        <div v-if="loading">Loading...</div>
        <table v-else>
            <thead>
                <tr>
                    <th
                        v-for="column in columns"
                        :key="column.key"
                        @click="toggleSort(column.key)"
                    >
                        {{ column.label }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in sortedRows" :key="row.player">
                    <td v-for="column in columns" :key="column.key">
                        {{ row[column.key] ?? "-" }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
