<template>
  <div>
    <div class="left" id="detail">
      <h1>
        {{movie.title}}
        <span>({{movie.year}})</span>
      </h1>
      <div class="subjectwrapper clearfix">
        <div class="subject clearfix">
          <div id="mainpic">
            <img :src="imgSrc" alt="图片加载出错" :onerror="defaultSrc">
          </div>
          <div id="info">
            <p>
              编剧：
              <span class="writer" v-for="(writer,index) in movie.writers" :key="index">
                {{writer.name}}
                <span
                  v-if="movie.writers.length!=1&& index!= movie.writers.length-1"
                >&nbsp;/&nbsp;</span>
              </span>
            </p>
            <p>
              类型：
              <span class="genre" v-for="(genre,index) in movie.genres" :key="index">
                <el-button type="text" v-on:click="searchGenre($event)">{{genre.name}}</el-button>
                <span v-if="movie.genres.length!=1&&index!=movie.genres.length-1">&nbsp;/&nbsp;</span>
              </span>
            </p>
            <p>
              语言：
              <span class="lang" v-for="(lang,index) in movie.languages" :key="index">
                {{lang}}
                <span
                  v-if="movie.languages.length!=1&&index!=movie.languages.length-1"
                >&nbsp;/&nbsp;</span>
              </span>
            </p>
            <p v-if="movie.aka!=null&&movie.aka[0]!==''">
              别名：
              <span class="aka" v-for="(name,index) in movie.aka" :key="index">
                {{name}}
                <span v-if="movie.aka.length!=1&& index!=movie.aka.length-1">&nbsp;/&nbsp;</span>
              </span>
            </p>
            <p v-if="movie.imdb!=''">
              IMDB：
              <span class="imdb">{{movie.imdb}}</span>
            </p>
            <p>
              时长：
              <span class="duration">{{movie.duration}}分钟</span>
            </p>
            <p>
              制片国家/地区：
              <span
                class="countries"
                v-for="(country, index) in movie.countries"
                :key="index"
              >
                <span>
                  {{country}}
                  <span
                    v-if="movie.countries.length!=1&&index!=movie.countries.length-1"
                  >&nbsp;/&nbsp;</span>
                </span>
              </span>
            </p>
          </div>
          <div class="interest">
            <div class="interestwrap clearbox">
              <div class="scoring">
                豆瓣评分
                <span class="score" v-if="movie.rating">&nbsp;&nbsp;{{movie.rating.average}}</span>
              </div>
              <div class="clearfix rating" v-if="movie.rating">
                <div class="clearfix">
                  <el-rate
                    v-model="movie.rating.halfAverage"
                    disabled
                    text-color="#ff9900"
                    score-template="{value}"
                    class="rate"
                  ></el-rate>
                  <div>{{movie.rating.rating_people}}人评价</div>
                </div>
              </div>
              <div class="item" v-if="movie.rating">
                <div v-for="(star, index) in stars" :key="index">
                  {{5-index}}星：
                  <el-progress
                    :text-inside="true"
                    :stroke-width="12"
                    :percentage="parseFloat(stars[index])"
                    class="progress"
                  ></el-progress>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="description" v-if="movie.title">
        <div class="head">
          {{movie.title.split(" ")[0]}}
          <span>的剧情简介</span>
        </div>
        <p class="breakline"></p>
        <p class="desInfo">{{movie.summary}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Detail',
  data () {
    return {
      movie: {},
      imgSrc: '',
      stars: [],
      defaultSrc: 'this.src="' + require('../assets/default.jpg') + '"'
    }
  },
  created () {
    this.search()
  },
  methods: {
    search () {
      this.$http.get(`film/detail/${this.$route.params.id}`)
        .then(response => {
          this.movie = response.data
          this.imgSrc = 'https://images.weserv.nl/?url=' + response.data.poster.substring(7)
          let half = response.data.rating.average / 2
          this.movie.rating.halfAverage = Number(half.toFixed(1))
          this.movie.languages = response.data.languages.split(',')
          this.movie.aka = response.data.aka.split(',')
          this.movie.countries = response.data.countries.split(',')
          this.stars.push(response.data.rating.five)
          this.stars.push(response.data.rating.four)
          this.stars.push(response.data.rating.three)
          this.stars.push(response.data.rating.two)
          this.stars.push(response.data.rating.one)
        })
        .catch(err => {
          console.log(err)
        })

    },
    searchGenre (event) {
      this.$router.push(`/type/${event.target.innerText}`)
    }
  }

}
</script>

<style scoped>
#detail {
  width: 65%;
  margin: 15px 1% 40px 4%;
}

h1 {
  font-size: 26px;
  word-wrap: break-word;
  font-weight: 600;
}
h1 span {
  color: gray;
}
#info p {
  font-weight: bold;
}
p span {
  font-weight: normal;
}
span .el-button {
  display: inline-block;
  margin: 0;
  text-align: left;
  padding: 0;
}
.subjectwrapper {
  float: none;
  display: block;
  position: relative;
  margin-bottom: 15px;
}

#mainpic {
  margin-right: 15px;
  float: left;
  overflow: hidden;
  text-align: middle;
}
#info {
  float: left;
  width: auto;
  word-wrap: break-word;
}
img {
  margin-bottom: 10px;
  width: 135px;
  height: 100%;
  border-width: 0;
}
.imdb {
  color: #3377aa;
}
.writer,
.genre {
  color: #00a65f;
}
.interest {
  float: right;
  width: 20%;
  margin-right: 1%;
  padding: 0 0 0 15px;
  border-left: 1px solid #8fb2c9;
  color: gray;
}
.interestwrap {
  padding-bottom: 15px;
  font-size: 12px;
  line-height: 16px;
}
.clearbox {
  clear: both;
  width: 100%;
}
.scoring {
  margin-bottom: 12px;
}
.score {
  font-size: 20px;
  font-weight: bold;
  vertical-align: bottom;
  color: #000;
  line-height: 16px;
}
.people {
  vertical-align: bottom;
}
.rate {
  font-size: 12px;
  vertical-align: bottom;
  display: inline-block;
}
.rating {
  margin-bottom: 8px;
}
.item .el-progress {
  display: inline;
}
.head {
  margin: 30px 0 10px 0;
  font-size: 16px;
  font-weight: bold;
  color: #00a65f;
}
.head span {
  color: #000;
}
.desInfo {
  text-indent: 2em;
  color: #22202e;
}
.progress >>> .el-progress-bar__innerText {
  color: #333;
}
</style>




