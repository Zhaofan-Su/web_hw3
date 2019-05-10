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
import TopSearch from './TopSearch'
import Movies from './Movies'
import Genres from './Genres'

export default {
  name: 'Type',
  components: {
    'topSearch': TopSearch,
    'movies': Movies,
    'genres': Genres
  },
  data () {
    return {
      movies: [],
      subhead: '',
    }
  },
  created () {
    this.searchGenre()
  },
  methods: {
    searchGenre () {
      var id = this.$route.params.id
      var type = this.$route.params.type
      this.movies = []
      this.subhead = ''
      this.$http.get(`film/genre/${id}`)
        .then(response => {
          response.data.forEach(ele => {
            let half = ele.rating.average / 2
            ele.rating.halfAverage = Number(half.toFixed(1))
            ele.poster = 'https://images.weserv.nl/?url=' + ele.poster.substring(7)
            this.movies.push(ele)
          })
          if (type.indexOf("电影") === -1 && type.indexOf("片") === -1) {
            this.subhead = type + "电影";
          }
          else {
            this.subhead = type;
          }
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  watch: {
    '$route' (to, from) {
      this.searchGenre()
    }
  }
}
</script>
