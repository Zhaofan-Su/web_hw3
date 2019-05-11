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
      loading: false,
      total: 0,
      pageNo: 1,
      pageSize: 20,
      pageCount: 0,
    }
  },
  created () {
    this.initial();
    this.handleCurrentChange(this.pageNo)
  },
  methods: {
    initial () {
      this.subhead = ''
    },
    handleSizeChange (val) {
      this.pageSize = val;
      this.handleCurrentChange(this.pageNo);
    },
    handleCurrentChange (val) {
      this.pageNo = val;
      this.getData(val)
    },
    getData (pageNo) {
      this.movies = []
      this.total = 0
      this.loading = true
      this.$http.get(`film/main/${pageNo}`)
        .then(response => {
          this.total = response.data.total
          this.pageCount = Math.ceil(this.total / this.pageSize)
          response.data.films.forEach(ele => {
            let half = parseFloat(ele.rating.average) / 2
            ele.rating.halfAverage = Number(half.toFixed(1))
            ele.poster = 'https://images.weserv.nl/?url=' + ele.poster.substring(7)
            this.movies.push(ele)
          })
          this.loading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
  watch: {
    '$route' (to, from) {
      this.getData(this.pageNo)
    }
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

.pagination {
  text-align: center;
  padding-top: 5%;
  padding-bottom: 8%;
  clear: both;
}
</style>


