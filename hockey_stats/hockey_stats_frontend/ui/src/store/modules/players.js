import axios from 'axios';

const baseUrl = 'http://localhost:5000/api';

export default {
  state: {
    players: [],
    info: '',
  },
  mutations: {
    setPlayers(state, data) {
      state.players = data;
    },
    setInfo(state, data) {
      state.info = data;
    },
  },
  actions: {
    fetchPlayers(ctx, query) {
      axios.get(`${baseUrl}/search/players/?s=${query}`)
        .then((resp) => {
          ctx.commit('setPlayers', resp.data);
        });
    },
    fetchInfo(ctx, id) {
      axios.get(`${baseUrl}/player?id=${id}`)
        .then((resp) => {
          ctx.commit('setInfo', resp.data);
        });
    },
  },
  getters: {
    getPlayers(state) {
      return state.players;
    },
    getInfo(state) {
      return state.info;
    },
  },
};
