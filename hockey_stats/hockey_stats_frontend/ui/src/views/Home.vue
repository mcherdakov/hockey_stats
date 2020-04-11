<template>
  <div>
    <Players />
    <br>
    <Teams />
    <br>
    <Predict />
  </div>
</template>

<script>

import Players from '@/components/Players.vue';
import Teams from '@/components/Teams.vue';
import Predict from '@/components/Predict.vue';

export default {
  components: {
    Players,
    Teams,
    Predict,
  },
};
</script>
