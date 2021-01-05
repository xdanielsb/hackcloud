<template>
  <div>
    <!-- Plain mode -->
    <b-form-file v-model="file" class="mt-3" plain></b-form-file>
    <div class="mt-3">Selected file: {{ file ? file.name : 'no file' }}</div>
    <button v-on:click="sendFileName(file.name)">Send file</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        file: null
      }
    },
    methods: {
    sendFileName: function (fileName) {
      const baseURI = 'https//localhost:5000/endpoint'
      console.log(fileName)
      this.$http.post(baseURI,{'name': fileName})
      .then((result) => {
        console.log(result)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
