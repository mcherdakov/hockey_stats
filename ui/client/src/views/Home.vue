<template>
  <div class="home">
    <h1> Hello! </h1>
    <ChooseFeatures />
  </div>
</template>

<script>
import ChooseFeatures from '@/components/ChooseFeatures.vue';

export default {
  name: 'Home',
  components: {
    ChooseFeatures,
  },
};
</script>
