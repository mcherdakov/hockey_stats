<template>
  <div>
    <button v-on:click="predict">Predict</button>
    <br>
    {{ predictInfo }}
  </div>
</template>

<script>

import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      predictInfo: '',
      player_id: null,
    };
  },
  computed: {
    ...mapGetters({
      player_id: 'getPlayerId',
    }),
  },
  methods: {
    predict() {
      console.log(5);
      console.log(this.player_id);
      if (this.player_id === null || this.player_id === '') {
        this.predictInfo = 'Select player and team for predict';
      } else {
        this.predictInfo = this.player_id;
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
