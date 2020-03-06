<template>
  <div class="choose">
    <div class="playerChoose" >
      <h2> Select player </h2>
      <select>
        <option v-for="player in players" v-bind:key="player.name">{{player.name}}</option>
      </select>
    </div>
    <div class="teamChoose" >
      <h2> Select team </h2>
      <select>
        <option v-for="team in teams" v-bind:key="team.name">{{team.name}}</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChooseFeatures',
  data() {
    return {
      players: [
        { name: 'Ovechkin' },
        { name: 'Malkin' },
        { name: 'Nichushkin' },
      ],
      teams: [
        { name: 'Detroit' },
        { name: 'Monreal' },
        { name: 'CSKA' },
      ],
    };
  },
};
</script>

<style scoped>

</style>
