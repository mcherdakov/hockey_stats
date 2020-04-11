import axios from 'axios';

const baseUrl = 'http://localhost:5000/api';

export default {
  state: {
    predict: '',
  },
  mutations: {
    setPredict(state, data) {
      state.predict = data;
    },
  },
  actions: {
    fetchPredict(ctx, payload) {
      axios.get(`${baseUrl}/predict?player_id=${payload.playerId}&team_id=${payload.teamId}`)
        .then((resp) => {
          ctx.commit('setPredict', resp.data);
        });
    },
  },
  getters: {
    getPredict(state) {
      return state.predict;
    },
  },
};
