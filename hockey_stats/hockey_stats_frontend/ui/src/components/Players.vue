<template>
  <div>
    Players:
    <multiselect v-model="selectedPlayer" placeholder="Start typing..."
        :options="players" :searchable="true" label="name"
        track-by="name" :loading="isLoading" :internal-search="false"
        @search-change="asyncFind">
      <template slot="singleLabel" slot-scope="{ option }">
        {{ option.name }}
      </template>
    </multiselect>
    <div v-if="selectedPlayer !== null">
      {{storePlayerId()}}
      <br>
      <PlayersTable :info="selectedPlayer" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import PlayersTable from '@/components/PlayersTable.vue';
import Multiselect from 'vue-multiselect';

export default {
  components: {
    PlayersTable,
    Multiselect,
  },
  data() {
    return {
      selectedPlayer: null,
      isLoading: false,
      players: [],
      temp: null,
    };
  },
  computed: {
    ...mapGetters({
      storedPlayers: 'getPlayers',
      info: 'getInfo',
      temp: 'getPlayerId',
    }),
  },
  methods: {
    ...mapActions([
      'fetchPlayers',
      'fetchInfo',
    ]),
    ...mapMutations([
      'setPlayerId',
    ]),
    storePlayerId() {
      console.log(99);
      console.log(this.selectedPlayer.id);
      this.setPlayerId(this.selectedPlayer.id);
      console.log(this.temp);
    },
    asyncFind(query) {
      if (query === '') {
        return;
      }
      this.isLoading = true;
      this.fetchPlayers(query).then(() => {
        this.isLoading = false;
        this.players = this.storedPlayers;
      });
    },
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped>
.multiselect {
  width: 400px;
  margin: auto;
}
</style>
