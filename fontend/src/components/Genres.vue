<template>
  <div class="right" id="aside">
    <div>
      <h2 type="text" class="head_type">电影分类</h2>
      <p class="breakline"></p>
      <div class="types">
        <span v-for="(genre,index) in genres" :key="index" class="type">
          <el-button
            v-if="genre.name.length > 0"
            type="text"
            v-on:click="searchGenre(genre.id, genre.name)"
          >{{genre.name}}</el-button>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Genres',
  data () {
    return {
      genres: [],
      subhead: '',
      movies: [],
    }
  },
  created () {
    this.getGenres()
  },
  methods: {
    getGenres () {
      this.$http.get(`film/genres`)
        .then(response => {
          this.genres = response.data
          var compare = function (x, y) {
            if (x < y) {
              return -1;
            }
            else if (x > y) {
              return 1;
            }
            else {
              return 0;
            }
          };
          this.genres.sort(compare);
        })
        .catch(error => {
          console.log(error);
        });
    },
    searchGenre (id, name) {
      this.$router.push(`/type/${id}/${name}`)
    },
  }
}
</script>

<style scoped>
#aside {
  width: 24%;
  margin-right: 3%;
}
.head_type {
  color: gray;
  margin: 35px 0 17px 0;
}
.types {
  margin-bottom: 30px;
}
.types .el-button {
  font-size: 10px;
}
.type {
  display: inline-block;
  min-width: 55px;
}
</style>

