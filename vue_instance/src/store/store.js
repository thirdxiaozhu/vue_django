import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        userid: Cookie.get("userid"),
        username: Cookie.get("userid"),
        usertype: Cookie.get("usertype"),
        token: Cookie.get("token"),
    },
    mutations:{
        saveToken: function(state , userToken){
            state.userid = userToken.userid;
            state.username = userToken.username;
            state.usertype = userToken.usertype;
            state.token = userToken.token;
            Cookie.set("userid", userToken.userid, "7d");
            Cookie.set("username", userToken.username, "7d");
            Cookie.set("usertype", userToken.usertype, "7d");
            Cookie.set("token", userToken.token, "7d");
        },
        clearToken: function(state){
            state.userid = null;
            state.username = null;
            state.usertype = null;
            state.token = null;
            Cookie.remove('userid');
            Cookie.remove('username');
            Cookie.remove('usertype');
            Cookie.remove('token');
        }
    }
})