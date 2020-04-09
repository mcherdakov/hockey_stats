<template>
  <div class="home">
    <div v-if="info !== ''">
      <table>
        <tr>
          <td>id</td><td>{{ info.id }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    'info',
  ],
};
</script>

<style scoped>
  table {
    border-collapse: collapse;
    border: 1px solid grey;
    margin: auto;
  }
  th, td {
    border: 1px solid grey;
  }
</style>
