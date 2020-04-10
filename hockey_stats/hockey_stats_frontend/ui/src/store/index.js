import Vue from 'vue';
import Vuex from 'vuex';
import players from './modules/players';
import teams from './modules/teams';
import predict from './modules/predict';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    predict,
    players,
    teams,
  },
});
