<template>
  <b-container class="mt-3" fluid>
    <b-form @submit.stop.prevent="onSubmit">
      <div class="d-flex mb-3">
        <b-form-file
          v-model="image"
          placeholder=""
          class="w-auto flex-grow-1"
        ></b-form-file>
      </div>

      <b-img
        v-if="hasImage"
        :src="imageSrc"
        class="mb-3"
        width="200"
        height="200"
        center
        fluid
        block
        rounded
      ></b-img>

      <b-button :disabled="!hasImage" variant="primary" type="submit"
      >Upload image</b-button>
      <b-button
        v-if="hasImage"
        variant="danger"
        class="ml-3"
        @click="clearImage"
      >Clear image</b-button>
      <div v-if="response" > {{response}} </div>
    </b-form>
  </b-container>
</template>

<script>
const base64Encode = (data) =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(data);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });

export default {
  data() {
    return {
      image: null,
      imageSrc: null,
      response:null,
    };
  },
  computed: {
    hasImage() {
      return !!this.image;
    },
  },
  watch: {
    image(newValue, oldValue) {
      if (newValue !== oldValue) {
        if (newValue) {
          base64Encode(newValue)
            .then((value) => {
              this.imageSrc = value;
            })
            .catch(() => {
              this.imageSrc = null;
            });
        } else {
          this.imageSrc = null;
        }
      }
    },
  },
  methods: {
    clearImage() {
      this.image = null;
    },

    onSubmit() {
      if (!this.image) {
        alert("Please select an image.");
        return;
      }
      const baseURI = "http://localhost:5000/";
      const config = {
        headers: { 'Content-Type': 'multipart/form-data' }
      }
      const formData = new FormData();

      formData.append('file', this.image);
      this.$http
        .post(baseURI, formData, config)
        .then((result) => {
          this.response = result;
        }).catch(function (error) {
          if (error.response) {
            // Request made and server responded
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
          } else if (error.request) {
            // The request was made but no response was received
            console.log(error.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log('Error', error.message);
          }
        });
    },
  },
};
</script>
