import axios from 'axios';

const baseUrl = 'http://localhost:5000/api';

export default {
  state: {
    teams: [],
    teamInfo: '',
  },
  mutations: {
    setTeams(state, data) {
      state.teams = data;
    },
    setTeamInfo(state, data) {
      state.teamInfo = data;
    },
  },
  actions: {
    fetchTeams(ctx, query) {
      axios.get(`${baseUrl}/search/teams/?s=${query}`)
        .then((resp) => {
          ctx.commit('setTeams', resp.data);
        });
    },
    fetchTeamInfo(ctx, id) {
      axios.get(`${baseUrl}/team?id=${id}`)
        .then((resp) => {
          ctx.commit('setTeamInfo', resp.data);
        });
    },
  },
  getters: {
    getTeams(state) {
      return state.teams;
    },
    getTeamInfo(state) {
      return state.teamInfo;
    },
  },
};
