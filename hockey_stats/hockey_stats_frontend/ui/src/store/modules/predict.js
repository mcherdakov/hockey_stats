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
    fetchPredict(ctx, playerId, teamId) {
      axios.get(`${baseUrl}/predict?playerId=${playerId}&teamId=${teamId}`)
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
