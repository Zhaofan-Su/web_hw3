<template>
  <div>
    <topSearch></topSearch>
    <div id="article">
      <detail></detail>
      <genres></genres>
    </div>
  </div>
</template>

<script>
import TopSearch from './TopSearch'
import Detail from './Detail'
import Genres from './Genres'
export default {
  name: 'Movie',
  components: {
    'topSearch': TopSearch,
    'detail': Detail,
    'genres': Genres
  }
}
</script>
