<template>
  <div>
    <topSearch></topSearch>
    <div id="article">
      <div class="left" v-loading.fullscreen,lock="loading">
        <movies :_movies="movies" :_subhead="subhead"></movies>
        <!-- 分页器 -->
        <el-pagination
          :page-size="pageSize"
          :current-page="pageNo"
          :page-count="pageCount"
          layout="total, prev, pager, next, jumper"
          :total="total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          class="pagination"
        ></el-pagination>
      </div>

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
      loading: false,
      total: 0,
      pageNo: 1,
      pageSize: 20,
      pageCount: 0,
    }
  },
  created () {
    this.searchGenre(this.pageNo)
  },
  methods: {
    handleSizeChange (val) {
      this.pageSize = val;
      this.handleCurrentChange(this.pageNo);
    },
    handleCurrentChange (val) {
      this.pageNo = val;
      this.searchGenre(val)
    },
    searchGenre (pageNo) {
      var id = this.$route.params.id
      var type = this.$route.params.type
      this.movies = []
      this.subhead = ''
      this.loading = true
      this.$http.get(`film/genre/${id}/${pageNo}`)
        .then(response => {
          this.total = response.data.total
          this.pageCount = Math.ceil(this.total / this.pageSize)
          response.data.films.forEach(ele => {
            let half = ele.rating.average / 2
            ele.rating.halfAverage = Number(half.toFixed(1))
            ele.poster = 'https://images.weserv.nl/?url=' + ele.poster.substring(7)
            this.movies.push(ele)
          })
          if (type === "脱口秀" || type === "舞台艺术" || type === "News" || type === "Adult" || type === "戏曲") {
            this.subhead = type
          }
          else if (type.indexOf("电影") === -1 && type.indexOf("片") === -1) {
            this.subhead = type + "电影";
          }
          else {
            this.subhead = type;
          }
          this.loading = false
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  watch: {
    '$route' (to, from) {
      this.searchGenre(this.pageNo)
    }
  }
}
</script>

<style scoped>
.pagination {
  text-align: center;
  padding-top: 5%;
  padding-bottom: 8%;
  clear: both;
}
</style>
