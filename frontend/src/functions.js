var functions = {}

functions.getTitle = function (title, aka) {

  var result = "";
  result = title.replace(" ", " / ");

  if (aka[0] !== "") {
    aka.forEach(ele => {
      result += " / " + ele;
    });
  }
  return result;
}

functions.getDirectors = function (directors) {
  var result = "";
  for (var i = 0; i < directors.length; i++) {
    result += directors[i].name;
    result += " / ";
  }
  return result.substring(0, result.length - 2);
}

functions.getCasts = function (casts) {
  var result = "";
  for (var i = 0; i < casts.length; i++) {
    result += casts[i].name;
    result += " / ";
  }
  result += "...";
  return result;
}

functions.getStars = function (score) {
  var result = "";
  var score = parseFloat(score);
  return score;
}

functions.getHalfAverage = function (score) {
  var half = parseFloat(score) / 2;
  return Number(half.toFixed(1))
}
functions.getPoster = function (url) {
  if (url !== undefined) {
    var _url = url.substring(7);
    return 'https://images.weserv.nl/?url=' + _url;
  }
}

functions.getMovie = function (element) {
  // 整理放到电影对象中的数据
  var movie = {
    id: element._id,
    title: this.getTitle(element.title, element.aka),
    directors: this.getDirectors(element.directors),
    rating: element.rating,
    casts: this.getCasts(element.casts),
    poster: this.getPoster(element.poster),
    score: this.getStars(element.rating.average),
    genres: element.genres,
    halfAverage: this.getHalfAverage(element.rating.average)
  };
  return movie;
}

functions.install = function (Vue, options) {
  Vue.prototype.$functions = functions
  Vue.functions = functions
}



export default functions