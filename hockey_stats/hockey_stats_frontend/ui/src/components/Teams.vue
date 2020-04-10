<template>
  <div>
    Teams:
    <multiselect v-model="selectedTeam" placeholder="Start typing..."
                 :options="teams" :searchable="true" label="name"
                 track-by="name" :loading="isLoading" :internal-search="false"
                 @search-change="asyncFind">
      <template slot="singleLabel" slot-scope="{ option }">
        {{ option.name }}
      </template>
    </multiselect>
    <div v-if="selectedTeam !== null">
      <br>
      <TeamsTable :info="selectedTeam" />
    </div>
  </div>
</template>

<script>


import { mapActions, mapGetters, mapMutations } from 'vuex';
import TeamsTable from '@/components/TeamsTable.vue';
import Multiselect from 'vue-multiselect';

export default {
  components: {
    TeamsTable,
    Multiselect,
  },
  data() {
    return {
      selectedTeam: null,
      isLoading: false,
      teams: [],
    };
  },
  computed: {
    ...mapGetters({
      storedTeams: 'getTeams',
      info: 'getTeamInfo',
    }),
  },
  watch: {
    selectedTeam(newTeam) {
      this.setTeamId(newTeam.id);
    },
  },
  methods: {
    ...mapActions([
      'fetchTeams',
      'fetchTeamInfo',
    ]),
    ...mapMutations([
      'setTeamId',
    ]),
    asyncFind(query) {
      if (query === '') {
        return;
      }
      this.isLoading = true;
      this.fetchTeamInfo(query).then(() => {
        this.isLoading = false;
        this.teams = this.storedTeams;
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
