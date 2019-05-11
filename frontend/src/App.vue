<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-size: 13px;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.62;
  width: 100%;
  margin: 0 auto;
}
#article {
  min-height: 420px;
  margin: 0 2%;
}

.left {
  float: left;
  padding-right: 24px;
  width: 60%;
  margin-left: 8%;
}

.right {
  float: right;
}

.head {
  margin: 40px 0 12px 0;
  color: gray;
}
.clearfix:after {
  content: ".";
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}

.breakline {
  border-bottom: 1px dashed #8fb2c9;
  clear: both;
}

a {
  vertical-align: top;
  text-decoration: none;
}
a:visited {
  text-decoration: none;
  color: #000;
}
a:hover {
  text-decoration: none;
  color: gray;
  cursor: pointer;
}
.el-progress-bar__innerText {
  color: #333;
}
</style>
