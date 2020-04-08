<template>
  <div>
    <button v-on:click="predict">Predict</button>
    <br>
    {{ predictInfo }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      predictInfo: '',
    };
  },
  methods: {
    predict() {
      this.predictInfo = 'Not implemented yet';
    },
  },
};
</script>
