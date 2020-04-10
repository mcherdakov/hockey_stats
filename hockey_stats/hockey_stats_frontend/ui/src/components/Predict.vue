<template>
  <div>
    <button v-on:click="predict">Predict</button>
    <br>
    {{ predictInfo }}
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      predictInfo: '',
    };
  },
  computed: {
    ...mapGetters({
      player_id: 'getPlayerId',
      team_id: 'getTeamId',
      pred: 'getPredict',
    }),
  },
  methods: {
    ...mapActions([
      'fetchPredict',
    ]),
    predict() {
      if (this.player_id === '' || this.team_id === '') {
        this.predictInfo = 'Select player and team for predict';
      } else {
        this.fetchPredict(this.player_id, this.team_id).then(() => {
          this.predictInfo = this.pred;
        });
      }
    },
  },
};
</script>

<style scoped>
  table {
    border-collapse: collapse;
    border: 1px solid grey;
    margin: auto;
  }
  th, td {
    border: 1px solid grey;
  }
</style>
