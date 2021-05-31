import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        userid: Cookie.get("userid"),
        token: Cookie.get("token"),
    },
    mutations:{
        saveToken: function(state , userToken){
            state.userid = userToken.userid;
            state.token = userToken.token;
            Cookie.set("userid", userToken.userid, "20min");
            Cookie.set("token", userToken.token, "20min");
        },
    }
})