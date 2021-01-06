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
      const baseURI = "https//localhost:5000/endpoint";
      this.$http
        .post(baseURI, { image: this.imageSrc })
        .then((result) => {
          console.log(result);
        });
    },
  },
};
</script>
