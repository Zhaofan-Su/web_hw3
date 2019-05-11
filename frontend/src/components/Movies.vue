<template>
  <div>
    <div id="movies">
      <div style="margin:0">
        <el-button type="text" v-on:click="initial" class="head">全部影片&nbsp;</el-button>
        <span v-if="subhead.length!=0" class="el-icon-d-arrow-right subhead">&nbsp;{{subhead}}</span>
      </div>

      <div id="contents" v-if="movies.length!=0">
        <ul>
          <li v-for="movie in movies" :key="movie.title">
            <p class="breakline"></p>
            <table>
              <tbody>
                <tr class="movie">
                  <td class="image">
                    <a @click="goDetail(movie._id)">
                      <img :src="movie.poster" alt="加载图片出错" :onerror="defaultSrc">
                    </a>
                  </td>
                  <td>
                    <div class="intro">
                      <a @click="goDetail(movie.id)" class="title">{{movie.title}}</a>
                      <div class="clearfix">
                        <div class="directors">
                          导演：
                          <span
                            v-for="(director, index) in movie.directors"
                            :key="index"
                          >{{director.name}}&nbsp;&nbsp;</span>
                        </div>
                        <div class="genres">
                          <span
                            v-for="(genre, index) in movie.genres"
                            :key="index"
                            class="genre"
                          >{{genre.name}}</span>
                        </div>
                      </div>

                      <p>
                        演员：
                        <span v-for="(cast,index) in movie.casts" :key="index">
                          <span v-if="index != movie.casts.length-1">{{cast.name}}&nbsp;/&nbsp;</span>
                          <span v-else>{{cast.name}}...</span>
                        </span>
                      </p>
                      <div class="clearfix star">
                        <el-rate
                          v-model="movie.rating.halfAverage"
                          disabled
                          text-color="#ff9900"
                          score-template="{value}"
                          class="score"
                        ></el-rate>
                        <span class="score">&nbsp;{{movie.rating.average}}&nbsp;</span>
                        <span class="rate_people">&nbsp;&nbsp;[{{movie.rating.rating_people}}人评价]</span>
                      </div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </li>
        </ul>
      </div>
      <div id="no-contents" v-else>没有你查找的影片呢，再试试其他的吧。</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Movies',
  props: {
    _movies: {
      type: Array,
      required: true,
      default: () => []
    },
    _subhead: {
      type: String,
      required: true
    },
  },
  data () {
    return {
      movies: [],
      subhead: this._subhead,
      defaultSrc: 'this.src="' + require('../assets/default.jpg') + '"',
    }
  },
  watch: {
    _movies (val) {
      this.movies = val
      this.subhead = this._subhead
    }
  },
  mounted () {
    this.movies = this._movies
    this.total = this.movies.length;
    this.subhead = this._subhead;
  },
  methods: {
    goDetail (id) {
      this.$router.push(`/detail/${id}`)
    },
    handleSizeChange (val) {
      this.pageSize = val;
      this.handleCurrentChange(this.pageNo);
    },
    handleCurrentChange (val) {
      this.pageNo = val;
      this.getData(val)
    },
    initial () {
      this.$router.push(`/`);
    },
  }
}

</script>

<style scoped>
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
.directors,
.genre {
  color: #00a65f;
}

.directors {
  float: left;
}
.genre {
  float: right;
}
#contents {
  word-break: break-all;
}

#contents table {
  border-collapse: collapse;
  width: 100%;
}

#contents table tbody {
  vertical-align: middle;
}
td {
  vertical-align: top;
  text-decoration: none;
}

.directors,
.genre {
  vertical-align: bottom;
  margin-top: 5px;
}

.genre {
  display: inline-block;
  margin-left: 8px;
}

.title {
  color: #8076a3;
  font-size: 15px;
}

.image {
  width: 100px;
}

.image img {
  width: 75px;
  max-width: 100%;
  vertical-align: middle;
}

.score {
  display: inline-block;
  vertical-align: bottom;
  color: rgb(255, 153, 0);
}

li {
  list-style: none;
  padding: 0;
}
ul {
  margin: 0;
  padding: 0;
}
</style>