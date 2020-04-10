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
    <div v-if="selectedPlayer !== null" >
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
    };
  },
  computed: {
    ...mapGetters({
      storedPlayers: 'getPlayers',
      info: 'getInfo',
    }),
  },
  watch: {
    selectedPlayer(newPlayer) {
      this.setPlayerId(newPlayer.id);
    },
  },
  methods: {
    ...mapActions([
      'fetchPlayers',
      'fetchInfo',
    ]),
    ...mapMutations([
      'setPlayerId',
    ]),
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
