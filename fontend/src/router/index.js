import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Movie from '@/components/Movie'
import Type from '@/components/Type';
import Search from '@/components/Search'
Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'Main',
      component: Main,
    }, {
      path: '/detail/:id',
      name: 'Movie',
      component: Movie,
    }, {
      path: '/type/:id/:type',
      name: 'Type',
      component: Type,
    },
    {
      path: '/search/:search',
      name: 'Search',
      component: Search,
    }
  ]
})
