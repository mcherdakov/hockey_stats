<template>
  <div>
    <button v-on:click="predict">Predict</button>
    <br>
    <br>
    <div v-if="predictInfo !== null &  typeof (predictInfo) === 'object'" >
      <PredictTable :info="predictInfo" />
    </div>
    <div v-if="predictInfo !== null & typeof (predictInfo) === 'string'">
      {{predictInfo}}
    </div>
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';
import PredictTable from '@/components/PredictTable.vue';

export default {
  components: {
    PredictTable,
  },
  data() {
    return {
      predictInfo: null,
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
        this.fetchPredict({ teamId: this.team_id, playerId: this.player_id }).then(() => {
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
