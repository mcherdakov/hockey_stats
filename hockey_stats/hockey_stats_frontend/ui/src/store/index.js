import Vue from 'vue';
import Vuex from 'vuex';
import players from './modules/players';
import teams from './modules/teams';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    players,
    teams,
  },
});
