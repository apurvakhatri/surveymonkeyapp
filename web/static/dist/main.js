!function(t){function n(o){if(e[o])return e[o].exports;var r=e[o]={i:o,l:!1,exports:{}};return t[o].call(r.exports,r,r.exports,n),r.l=!0,r.exports}var e={};n.m=t,n.c=e,n.i=function(t){return t},n.d=function(t,e,o){n.o(t,e)||Object.defineProperty(t,e,{configurable:!1,enumerable:!0,get:o})},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,n){return Object.prototype.hasOwnProperty.call(t,n)},n.p="/static/frontend/onboarding/dist/",n(n.s=29)}([function(t,n){t.exports=angular},function(t,n,e){"use strict";n.__esModule=!0,n.default=function(t,n){if(!(t instanceof n))throw new TypeError("Cannot call a class as a function")}},function(t,n){t.exports="ngMaterial"},function(t,n,e){"use strict";n.__esModule=!0;var o=e(32),r=function(t){return t&&t.__esModule?t:{default:t}}(o);n.default=function(){function t(t,n){for(var e=0;e<n.length;e++){var o=n[e];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),(0,r.default)(t,o.key,o)}}return function(n,e,o){return e&&t(n.prototype,e),o&&t(n,o),n}}()},function(t,n,e){t.exports=!e(9)(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},function(t,n){t.exports=function(t){return"object"==typeof t?null!==t:"function"==typeof t}},function(t,n,e){"use strict";function o(t,n,e){function o(){return t.get(a.teams())}var r={endpoint:"user/"},a={teams:function(){return r.endpoint+"getSharedTeams/"}};return{getTeams:o}}e.d(n,"a",function(){return u});var r=e(0),a=e.n(r),i=e(19),c=e(7),u=a.a.module("userApi",[i.a,c.a]).factory("UserApi",o).name;o.$inject=["ApiService","DjangoConstants","$q"]},function(t,n,e){"use strict";e.d(n,"a",function(){return a});var o=e(0),r=e.n(o),a=r.a.module("djangoConstants",[]).constant("DjangoConstants",window.djangoConstants||{}).name},function(t,n){var e=t.exports={version:"2.5.6"};"number"==typeof __e&&(__e=e)},function(t,n){t.exports=function(t){try{return!!t()}catch(t){return!0}}},function(t,n){var e=t.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=e)},function(t,n,e){var o=e(35),r=e(41),a=e(43),i=Object.defineProperty;n.f=e(4)?Object.defineProperty:function(t,n,e){if(o(t),n=a(n,!0),o(e),r)try{return i(t,n,e)}catch(t){}if("get"in e||"set"in e)throw TypeError("Accessors not supported!");return"value"in e&&(t[n]=e.value),t}},function(t,n,e){"use strict";e.d(n,"a",function(){return l});var o=e(0),r=e.n(o),a=e(2),i=e.n(a),c=e(20),u=e(24),s=e(6),l=r.a.module("appToolbar",[i.a,s.a,u.a]).component("appToolbar",c.a).name},function(t,n,e){"use strict";function o(t){var n=t.extendPalette("blue-grey",{50:"FFFFFF",800:"FFFFFF",contrastDefaultColor:"dark"});t.definePalette("white",n),t.theme("default").primaryPalette("blue-grey",{default:"800"}).accentPalette("red").backgroundPalette("white")}e.d(n,"a",function(){return u});var r=e(0),a=e.n(r),i=e(2),c=e.n(i),u=a.a.module("angularMaterialConfig",[c.a]).config(o).name;o.$inject=["$mdThemingProvider"]},function(t,n,e){"use strict";function o(t){t.defaults.xsrfCookieName="csrftoken",t.defaults.xsrfHeaderName="X-CSRFToken"}e.d(n,"a",function(){return i});var r=e(0),a=e.n(r),i=a.a.module("csrfConfig",[]).config(o).name;o.$inject=["$httpProvider"]},function(t,n,e){"use strict";e.d(n,"a",function(){return i});var o=e(0),r=e.n(o),a=e(26),i=r.a.module("github-app.fourOhFourScreen",[]).component("fourOhFourScreen",a.a).name},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(50),r=e.n(o),a=e(28),i=e(45);e.n(i);a.a.$inject=["$state"];var c={template:r.a,controller:a.a}},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(0),r=e.n(o),a=e(27),i=e(31),c=r.a.module("surveymonkey-app.accountListScreen",[a.a]).component("accountListScreen",i.a).name},function(t,n){t.exports="ui.router"},function(t,n,e){"use strict";function o(t){function n(n){return t.get(a.endpoint+n)}function e(n,e){return t.post(a.endpoint+n,e)}function o(n,e){return t.patch(a.endpoint+n,e)}function r(n){return t.delete(a.endpoint+n)}var a={endpoint:"/api/"};return{get:n,post:e,patch:o,delete:r}}e.d(n,"a",function(){return i});var r=e(0),a=e.n(r),i=a.a.module("apiService",[]).factory("ApiService",o).name;o.$inject=["$http"]},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(47),r=e.n(o),a=e(21),i=e(52);e.n(i);a.a.$inject=["$location"];var c={template:r.a,controller:a.a,bindings:{toolbarClass:"@",appName:"@",isUserLoggedIn:"<",teams:"<",goHome:"&"}}},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(1),r=e.n(o),a=e(3),i=e.n(a),c=function(){function t(n){r()(this,t),this.$location=n}return i()(t,[{key:"$onInit",value:function(){var t=this.getAppIdFromUrl(),n=this.$location.protocol(),e=this.$location.host();this.appDocUrl=n+"://"+e+"/marketplace/application/"+t}},{key:"getAppIdFromUrl",value:function(){return/applications\/(\d+)\/(.*)/g.exec(this.$location.absUrl())[1]}}]),t}()},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(48),r=e.n(o),a=e(23),i=e(53);e.n(i);a.a.$inject=["UserApi","$window","$location"];var c={template:r.a,controller:a.a,bindings:{appendUrl:"@",currentTeamDomain:"="}}},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(1),r=e.n(o),a=e(3),i=e.n(a),c=function(){function t(n,e,o){r()(this,t),this.UserApi=n,this.$window=e,this.$location=o,this.isUserLoggedIn=!1,this.currentTeam={name:"Select Team"}}return i()(t,[{key:"$onInit",value:function(){var t=this;this.UserApi.getTeams().then(function(n){t.allTeams=n.data.teams,0!=t.allTeams.length&&(t.isUserLoggedIn=!0,n.data.current&&(t.currentTeam=n.data.current,t.currentTeamDomain=t.currentTeam.domain,t.allTeams=t.allTeams.filter(function(n){return n.id!=t.currentTeam.id})))})}},{key:"changeTeam",value:function(t){var n=/(.*\.)?(.+\..+)/g,e=n.exec(this.$location.host()),o=e[e.length-1];if(null==this.appendUrl||""==this.appendUrl)var r=new RegExp(".*"+o+"(.+)"),e=r.exec(this.$location.absUrl()),a=e[1];else var a=this.appendUrl;this.$window.location=this.$location.protocol()+"://"+t.domain+"."+o+a}}]),t}()},function(t,n,e){"use strict";e.d(n,"a",function(){return s});var o=e(0),r=e.n(o),a=e(2),i=e.n(a),c=e(22),u=e(6),s=r.a.module("teamSwitcher",[i.a,u.a]).component("teamSwitcher",c.a).name},function(t,n,e){"use strict";e.d(n,"a",function(){return a});var o=e(1),r=e.n(o),a=function t(){r()(this,t)}},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(49),r=e.n(o),a=e(25),i=e(54),c=(e.n(i),{template:r.a,controller:a.a})},function(t,n,e){"use strict";function o(t,n){function e(){return t.get(c.userAccounts())}function o(n){return t.get(c.userAccounts()+n+"/")}function r(n){return t.delete(c.userAccounts()+n+"/delete/")}function a(n,e){return t.delete(c.userWebhooks(n)+e+"/")}var i=n.base_href,c={userAccounts:function(){return i+"user/"},userWebhooks:function(t){return c.userAccounts()+t+"/webhook/"}};return{getUserAccounts:e,getUserAccount:o,deleteUserAccount:r,deleteUserWebhook:a}}e.d(n,"a",function(){return c});var r=e(0),a=e.n(r),i=e(7),c=a.a.module("appApi",[i.a]).factory("AppApi",o).name;o.$inject=["$http","DjangoConstants"]},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(1),r=e.n(o),a=e(3),i=e.n(a),c=function(){function t(n){r()(this,t),this.$state=n}return i()(t,[{key:"goHome",value:function(){this.$state.go("accountList")}}]),t}()},function(t,n,e){"use strict";function o(t,n,e,o){t.html5Mode(!0),e.otherwise("/404/"),o.strictMode(!1);var r={name:"accountList",url:"/",component:"accountListScreen"},a={name:"fourOhFour",url:"/404/",component:"fourOhFourScreen"};n.state(r),n.state(a)}Object.defineProperty(n,"__esModule",{value:!0}),e.d(n,"surveymonkeyApp",function(){return h});var r=e(0),a=e.n(r),i=e(18),c=e.n(i),u=e(2),s=e.n(u),l=e(12),d=e(13),f=e(14),m=e(16),p=e(17),g=e(15),h=a.a.module("surveymonkey-app",[s.a,c.a,l.a,d.a,f.a,p.a,g.a]).config(o).component("yellowantSurveymonkeyApp",m.a).name;o.$inject=["$locationProvider","$stateProvider","$urlRouterProvider","$urlMatcherFactoryProvider"]},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(1),r=e.n(o),a=e(3),i=e.n(a),c=function(){function t(n,e,o,a,i){r()(this,t),this.AppApi=n,this.$stateParams=e,this.$mdDialog=o,this.$mdToast=a,this.$state=i}return i()(t,[{key:"$onInit",value:function(){var t=this;this.AppApi.getUserAccounts().then(function(n){t.userAccounts=n.data},function(n){t.userAccounts=null})}},{key:"stateDetails",value:function(t){var n=this;this.AppApi.getStateDetails(t).then(function(t){n.userStates=t.data},function(t){n.userStates=null})}},{key:"deleteAccount",value:function(t){var n=this;this.AppApi.deleteUserAccount(t).then(function(e){n.userAccounts=n.userAccounts.filter(function(n){return n.id!==t}),n.$mdToast.show(n.$mdToast.simple().textContent("Your integration has been successfully removed"))},function(t){console.log("Error is:"),console.log(t),n.$mdToast.show(n.$mdToast.simple().textContent("Unable to remove your account at the moment"))})}},{key:"onDeleteAccount",value:function(t){var n=this;console.log(t);var e=this.$mdDialog.prompt().title("Would you like to remove this Bitbucket integration with Yellowant?").textContent("Please type in your Bitbucket handle to confirm: "+t.user_invoke_name).placeholder("bitbucket-handle").ariaLabel("Bitbucket Handle").clickOutsideToClose(!0).ok("Delete Integration").cancel("Cancel");this.$mdDialog.show(e).then(function(e){e==t.user_invoke_name?n.deleteAccount(t.id):n.onDeleteAccount(t)},function(){})}}]),t}()},function(t,n,e){"use strict";e.d(n,"a",function(){return c});var o=e(51),r=e.n(o),a=e(30),i=e(46);e.n(i);a.a.$inject=["AppApi","$stateParams","$mdDialog","$mdToast","$state"];var c={template:r.a,controller:a.a}},function(t,n,e){t.exports={default:e(33),__esModule:!0}},function(t,n,e){e(44);var o=e(8).Object;t.exports=function(t,n,e){return o.defineProperty(t,n,e)}},function(t,n){t.exports=function(t){if("function"!=typeof t)throw TypeError(t+" is not a function!");return t}},function(t,n,e){var o=e(5);t.exports=function(t){if(!o(t))throw TypeError(t+" is not an object!");return t}},function(t,n,e){var o=e(34);t.exports=function(t,n,e){if(o(t),void 0===n)return t;switch(e){case 1:return function(e){return t.call(n,e)};case 2:return function(e,o){return t.call(n,e,o)};case 3:return function(e,o,r){return t.call(n,e,o,r)}}return function(){return t.apply(n,arguments)}}},function(t,n,e){var o=e(5),r=e(10).document,a=o(r)&&o(r.createElement);t.exports=function(t){return a?r.createElement(t):{}}},function(t,n,e){var o=e(10),r=e(8),a=e(36),i=e(40),c=e(39),u=function(t,n,e){var s,l,d,f=t&u.F,m=t&u.G,p=t&u.S,g=t&u.P,h=t&u.B,v=t&u.W,y=m?r:r[n]||(r[n]={}),b=y.prototype,w=m?o:p?o[n]:(o[n]||{}).prototype;m&&(e=n);for(s in e)(l=!f&&w&&void 0!==w[s])&&c(y,s)||(d=l?w[s]:e[s],y[s]=m&&"function"!=typeof w[s]?e[s]:h&&l?a(d,o):v&&w[s]==d?function(t){var n=function(n,e,o){if(this instanceof t){switch(arguments.length){case 0:return new t;case 1:return new t(n);case 2:return new t(n,e)}return new t(n,e,o)}return t.apply(this,arguments)};return n.prototype=t.prototype,n}(d):g&&"function"==typeof d?a(Function.call,d):d,g&&((y.virtual||(y.virtual={}))[s]=d,t&u.R&&b&&!b[s]&&i(b,s,d)))};u.F=1,u.G=2,u.S=4,u.P=8,u.B=16,u.W=32,u.U=64,u.R=128,t.exports=u},function(t,n){var e={}.hasOwnProperty;t.exports=function(t,n){return e.call(t,n)}},function(t,n,e){var o=e(11),r=e(42);t.exports=e(4)?function(t,n,e){return o.f(t,n,r(1,e))}:function(t,n,e){return t[n]=e,t}},function(t,n,e){t.exports=!e(4)&&!e(9)(function(){return 7!=Object.defineProperty(e(37)("div"),"a",{get:function(){return 7}}).a})},function(t,n){t.exports=function(t,n){return{enumerable:!(1&t),configurable:!(2&t),writable:!(4&t),value:n}}},function(t,n,e){var o=e(5);t.exports=function(t,n){if(!o(t))return t;var e,r;if(n&&"function"==typeof(e=t.toString)&&!o(r=e.call(t)))return r;if("function"==typeof(e=t.valueOf)&&!o(r=e.call(t)))return r;if(!n&&"function"==typeof(e=t.toString)&&!o(r=e.call(t)))return r;throw TypeError("Can't convert object to primitive value")}},function(t,n,e){var o=e(38);o(o.S+o.F*!e(4),"Object",{defineProperty:e(11).f})},function(t,n){},function(t,n){},function(t,n){t.exports='<md-toolbar md-colors="::{ background: \'white\', color: \'blue-grey-800\'}"> <div class=md-toolbar-tools ng-class=::$ctrl.toolbarClass> <h2 flex layout=row layout-align="start center"> <img ng-click=$ctrl.goHome() class="header-logo pointer" src=https://yellowant.s3.amazonaws.com/static/yellowanticons/logo3.png> <span class="logo-divider b">|</span> <img ng-click=$ctrl.goHome() class="header-logo pointer" src=https://cdn.smassets.net/assets/anonweb/smlib.globaltemplates/7.0.0/assets/logo/surveymonkey_logo.svg> <span ng-click=$ctrl.goHome() class="b logo-divider pointer">{{$ctrl.appName}}</span> </h2> <md-button ng-click=$ctrl.goHome()> Home </md-button> <md-button class=md-accent ng-href={{$ctrl.appDocUrl}} target=_blank> Docs </md-button> <team-switcher></team-switcher> </div> </md-toolbar> '},function(t,n){t.exports='<md-menu md-offset="0 47" ng-if=$ctrl.isUserLoggedIn> <md-button class="md-primary md-raised" ng-click=$mdMenu.open($event)>{{$ctrl.currentTeam.name}}</md-button> <md-menu-content md-colors="::{ background: \'white\', color: \'blue-grey-800\'}"> <md-menu-item ng-repeat="team in $ctrl.allTeams track by team.id"> <md-button md-colors="::{ background: \'white\', color: \'blue-grey-800\'}" ng-click=$ctrl.changeTeam(team)>{{team.name}}</md-button> </md-menu-item> <md-menu-item style=margin-top:.5rem> <md-button class="md-accent md-raised" ng-href=https://www.yellowant.com/login>Use Another Team</md-button> </md-menu-item> </md-menu-content> </md-menu> <md-button class="md-primary md-raised" ng-if=!$ctrl.isUserLoggedIn ng-href=/login> Sign In </md-button>'},function(t,n){t.exports='<div class=layout-container> <section class=mb4 layout=column layout-align="start center"> <h1 class="f1 tc">404</h1> <div> Seems like you\'ve reached a part of the universe that does not exist. </div> </section> </div>'},function(t,n){t.exports="<div layout=column layout-fill> <app-toolbar toolbar-class=layout-container go-home=$ctrl.goHome()></app-toolbar> <md-content> <ui-view></ui-view> </md-content> </div> "},function(t,n){t.exports='<div class=layout-container> <section class=mb4 layout=column layout-align="start center"> <img src=https://cdn.smassets.net/assets/anonweb/smlib.globaltemplates/7.0.0/assets/logo/surveymonkey_logo.svg height=981 width=292> <md-button target=_blank ng-if=$ctrl.userAccounts ng-href=/yellowantauthurl/yellowantauthurl class="md-accent md-raised" layout=row>Add Account </md-button> </section> <section layout=column layout-align="start center"> <md-list class="mw7 w-100" ng-if=$ctrl.userAccounts> <md-list-item ng-repeat="account in $ctrl.userAccounts track by $index"> <md-card class="w-100 has-hidden-action-buttons"> <md-content class=pa3 layout=row layout-align="space-between center" ng-if=account.app_authenticated> <a class=mb0> <div><b>YellowAnt Invoke Name:</b> {{ ::account.user_invoke_name }}</div> </a> <a ng-if=account.app_authenticated md-button class="md-primary md-raised hidden-action-buttons" ng-click=$ctrl.onDeleteAccount(account)>Delete</a> </md-content> <md-content class=pa3 layout=row layout-align="space-between center" ng-if=!account.app_authenticated> <div class=mb0> <h4 class="f3 mb2" md-colors="::{ color: \'accent\'}" style=font-size:100%>SurveyMonkey Account Not Integrated</h4> <div><b>YellowAnt Invoke Name:</b> {{ ::account.user_invoke_name }}</div> </div> <a ng-if=!account.app_authenticated md-button class="md-primary md-raised hidden-action-buttons" ng-click=$ctrl.onDeleteAccount(account)>Delete</a> <a ng-if=!account.app_authenticated md-button class="md-primary md-raised hidden-action-buttons" ng-href="/integrate_app?id={{account.id}}" target=_self>Integrate</a> </md-content> </md-card> </md-list-item> </md-list> <div ng-if=!$ctrl.userAccounts class="mw7 w-100"> <div class=mb3><i> surveymonkey is a web-based hosting service that is owned by Atlassian, used for source code and development projects that use either Mercurial or Git. </i></div> <div layout=row layout-align=center class=mb4> <img class=app-logo src=https://www.atlassian.com/dam/jcr:bd56917e-e361-4f03-b672-9f5ef5b06e80/bitbucket_rgb_slate.svg /> </div> <div> The surveymonkey integration for YellowAnt allows you to manage your account in the following ways: <ul> <li>Get user details</li> <li>Integrate repository webhooks for your YellowAnt account</li> <li>Create a repository</li> <li>Search for repositories and users</li> <li>... amongst other capabilities.</li> </ul> </div> </div> </section> </div> '},function(t,n){},function(t,n){},function(t,n){}]);