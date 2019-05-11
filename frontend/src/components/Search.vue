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
      loading: false,
      total: 0,
      pageNo: 1,
      pageSize: 20,
      pageCount: 0,
    }
  },
  created () {
    this.handleCurrentChange(this.pageNo)
  },
  methods: {
    handleSizeChange (val) {
      this.pageSize = val;
      this.handleCurrentChange(this.pageNo);
    },
    handleCurrentChange (val) {
      this.pageNo = val;
      this.fuzzySearch(val)
    },
    fuzzySearch (pageNo) {
      this.movies = []
      var search = this.$route.params.search
      this.loading = true
      if (search) {
        this.$http.get(`film/fuzzySearch/${search}/${pageNo}`)
          .then(response => {
            this.total = response.data.total
            this.pageCount = Math.ceil(this.total / this.pageSize)
            response.data.films.forEach(ele => {
              let half = ele.rating.average / 2
              ele.rating.halfAverage = Number(half.toFixed(1))
              ele.poster = 'https://images.weserv.nl/?url=' + ele.poster.substring(7)
              this.movies.push(ele)
            })
            this.loading = false
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
      this.fuzzySearch(this.pageNo)
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
