<template>
  <div>
    <topSearch></topSearch>
    <div id="article">
      <movies :_movies="movies" :_subhead="subhead"></movies>
      <genres></genres>
    </div>
  </div>
</template>

<script>
import TopSearch from './TopSearch';
import Movies from "./Movies";
import Genres from './Genres';
export default {
  name: 'Search',
  components: {
    'movies': Movies,
    'topSearch': TopSearch,
    'genres': Genres,
  },
  data () {
    return {
      subhead: '',
      movies: [],
    }
  },
  created () {
    this.fuzzySearch
  },
  methods: {
    fuzzySearch () {
      this.movies = [];
      var search = this.$route.params.search
      if (search) {
        this.$http.get("static/films.json")
          .then(response => {
            response.data.forEach(ele => {
              if (ele.title.indexOf(search) !== -1) {
                this.movies.push(this.$functions.getMovie(ele));
              }
              // 查找电影别名
              ele.aka.filter((value) => {
                if (value.includes(search)) {
                  this.movies.push(this.$functions.getMovie(ele));
                }
              });
              // 查找导演
              ele.directors.filter((value) => {
                if (value.name.includes(search)) {
                  this.movies.push(this.$functions.getMovie(ele));
                }
              });
            });

          })
          .catch(error => {
            console.log(error);
          })
      }
      this.subhead = "搜索结果";
    }
  },
  watch: {
    '$route' (to, from) {
      this.fuzzySearch()
    }
  }
}
</script>
