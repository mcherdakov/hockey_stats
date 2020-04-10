import axios from 'axios';

const baseUrl = 'http://localhost:5000/api';

export default {
  state: {
    players: [],
    info: '',
    playerId: '',
  },
  mutations: {
    setPlayers(state, data) {
      state.players = data;
    },
    setPlayerId(state, data) {
      state.playerId = data;
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
    savePlayerId(ctx, playerId) {
      ctx.commit('setPlayerId', playerId);
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
    getPlayerId(state) {
      return state.playerId;
    },
    getInfo(state) {
      return state.info;
    },
  },
};
