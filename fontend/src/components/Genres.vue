<template>
  <div class="right" id="aside">
    <div>
      <h2 type="text" class="head_type">电影分类</h2>
      <p class="breakline"></p>
      <div class="types">
        <span v-for="genre in genres" :key="genre" class="type">
          <el-button type="text" v-on:click="searchGenre($event)">{{genre}}</el-button>
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
      this.$http.get("static/films.json")
        .then(response => {
          response.data.forEach(element => {
            for (var i = 0; i < element.genres.length; i++) {
              this.genres.indexOf(element.genres[i]) === -1 ? this.genres.push(element.genres[i]) : 0;
            }
          })
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
    searchGenre (event) {
      this.$router.push(`/type/${event.target.innerText}`)
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

