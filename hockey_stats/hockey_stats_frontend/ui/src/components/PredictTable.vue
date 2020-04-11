<template>
  <div class="home">
    <div v-if="info !== ''">
      <table>
        <tr>
          <td>goals</td>
          <td>assists</td>
          <td>points</td>
          <td>+/-</td>
        </tr>
        <tr>
          <td>{{ info.goals }}</td>
          <td>{{ info.assists }} </td>
          <td> {{ info.goals + info.assists }} </td>
          <td> {{ info.p_m }} </td>
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
