<template>
  <div class="home">
    <div v-if="info !== ''">
      <table>
        <tr>
          <td>id</td><td>{{ info.id }}</td>
        </tr>
        <tr>
          <td>league_name</td><td>{{ info.league_name }} </td>
        </tr>
        <tr>
          <td>team_name</td><td> {{ info.team_name }} </td>
        </tr>
        <tr>
          <td>year_founded</td><td> {{ info.year_founded }} </td>
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
