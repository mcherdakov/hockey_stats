import axios from 'axios';

const baseUrl = 'http://localhost:5000/api';

export default {
  state: {
    teams: [],
    teamInfo: '',
    teamId: '',
  },
  mutations: {
    setTeams(state, data) {
      state.teams = data;
    },
    setTeamId(state, data) {
      state.teamId = data;
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
    getTeamId(state) {
      return state.teamId;
    },
    getTeamInfo(state) {
      return state.teamInfo;
    },
  },
};
