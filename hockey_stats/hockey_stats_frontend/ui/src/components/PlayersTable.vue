<template>
  <div class="home">
    <div v-if="info !== ''">
      <table>
        <tr>
          <td>id</td><td>{{ info.id }}</td>
        </tr>
        <tr>
          <td>name</td><td>{{ info.name }} </td>
        </tr>
        <tr>
          <td>nationality</td><td> {{ info.nationality }} </td>
        </tr>
        <tr>
          <td>youth team</td><td> {{ info.youth_team }} </td>
        </tr>
        <tr>
          <td>position</td><td> {{ info.position }} </td>
        </tr>
        <tr>
          <td>shoots</td><td> {{ info.shoots }} </td>
        </tr>
        <tr>
          <td>height</td><td> {{ info.height }} </td>
        </tr>
        <tr>
          <td>weight</td><td> {{ info.weight }} </td>
        </tr>
        <tr>
          <td>age</td><td> {{ info.age }} </td>
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
