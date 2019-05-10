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
    this.fuzzySearch()
  },
  methods: {
    fuzzySearch () {
      this.movies = []
      var search = this.$route.params.search
      if (search) {
        this.$http.get(`film/fuzzySearch/${search}`)
          .then(response => {
            response.data.forEach(ele => {
              let half = ele.rating.average / 2
              ele.rating.halfAverage = Number(half.toFixed(1))
              ele.poster = 'https://images.weserv.nl/?url=' + ele.poster.substring(7)
              this.movies.push(ele)
            })

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
