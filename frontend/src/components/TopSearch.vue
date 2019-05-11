<template>
  <div id="search">
    <el-tooltip content="点击返回主页" placement="left" effect="light">
      <el-button type="text" id="head" v-on:click="initial">电影乐园</el-button>
    </el-tooltip>
    <el-input placeholder="请输入电影名、导演" v-model="search">
      <el-button slot="append" icon="el-icon-search" v-on:click="fuzzySearch"></el-button>
    </el-input>
  </div>
</template>

<script>
export default {
  name: 'TopSearch',
  data () {
    return {
      search: ''
    }
  },
  methods: {
    fuzzySearch () {
      this.$router.push(`/search/${this.search}`)
    },
    initial () {
      this.$router.push(`/`)
    }
  }
}
</script>

<style scoped>
/* 顶部搜索框样式 */
#search {
  height: 8%;
  background-color: #eef7f2;
  width: 100%;
  margin: 0 auto;
  text-align: center;
}
#search .el-input {
  margin: 3% auto;
  width: 50%;
  position: relative;
}
#head {
  font-weight: bold;
  display: inline-block;
  font-size: 36px;
  text-align: left;
  margin-right: 6%;
  font-family: FZShuTi;
  color: #7a7374;
}
#head:hover {
  color: #000;
}
</style>


