<script setup>
import { ref, watch, onMounted } from "vue";
const props = defineProps({
  selectedSeason: String,
  selectedTeam: String,
});

const kpi = ref(null);
const loading = ref(true);
const fetchKpi = () => {
  const params = new URLSearchParams();
  if (props.selectedSeason) {
    params.append("season", props.selectedSeason);
  }
  if (props.selectedTeam) {
    params.append("team", props.selectedTeam);
  }
  fetch(`/api/kpi?${params.toString()}`)
    .then((response) => response.json())
    .then((data) => {
      kpi.value = data;
      loading.value = false;
    });
};

onMounted(() => {
  fetchKpi();
});

watch(
  () => [props.selectedSeason, props.selectedTeam],
  () => {
    loading.value = true;
    fetchKpi();
  },
);
</script>

<template>
  <div v-if="loading">Loading KPIs</div>
  <div v-else>
    <div class="kpi-card">
      <h3>Total Matches</h3>
      <p>{{ kpi.matches_played.toLocaleString() }}</p>
    </div>
    <div class="kpi-card">
      <h3>Runs Scored</h3>
      <p>{{ kpi.runs_scored.toLocaleString() }}</p>
    </div>
    <div class="kpi-card">
      <h3>Total Sixes</h3>
      <p>{{ kpi.total_sixes.toLocaleString() }}</p>
    </div>
    <div class="kpi-card">
      <h3>Total Wickets</h3>
      <p>{{ kpi.total_wickets.toLocaleString() }}</p>
    </div>
  </div>
</template>
