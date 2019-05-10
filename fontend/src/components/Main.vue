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
  name: 'Main',
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
    this.initial();
  },
  methods: {
    initial () {
      this.subhead = "";
      this.$http.get(`film/all`)
        .then(response => {
          response.data.forEach(ele => {
            let half = parseFloat(ele.rating.average) / 2
            ele.rating.halfAverage = Number(half.toFixed(1))
            ele.poster = 'https://images.weserv.nl/?url=' + ele.poster.substring(7)
            this.movies.push(ele)
          })
        })
        .catch(error => {
          console.log(error);
        });
      this.subhead = ''
    },
  }
}
</script>

<style scoped>
/* 顶部搜索框样式 */
#search {
  height: 10%;
  background-color: #eef7f2;
  width: 100%;
  margin: 0;
  text-align: center;
}
#search .el-input {
  margin: 3% auto;
  width: 50%;
  position: relative;
}

/* 电影部分样式*/
.left .el-button {
  font-size: 13px;
  border: none;
  padding: 0;
  display: inline;
}
.left .el-button--text {
  margin-block-end: 0.83em;
  margin-block-start: 0.83em;
  margin: 40px 0 12px 0;
  padding-bottom: 0;
  padding-top: 0;
  font-size: 1.5em;
  font-weight: bold;
  color: gray;
}

.left .el-button--text:hover {
  color: #000;
}

.subhead {
  font-size: 1.2em;
  color: #00a65f;
}
#wrapper {
  width: 100%;
  margin: 0 auto;
}

#article {
  min-height: 420px;
  margin: 0 2%;
}

/* 以下为右侧样式设置 */

.pagination {
  text-align: center;
  margin-top: 2%;
  margin-bottom: 5%;
  clear: both;
}
</style>


