const NYTBaseURL = "https://api.nytimes.com/svc/topstories/v2/";
const ApiKey = "f5b344cf863b42aea00233d16ab4a86f";

function buildUrl(url) {
    return NYTBaseURL + url + ".json?api-key=" + ApiKey
}

// ./app.js
const vm = new Vue({
  el: '#app',
  data: {
    results: []
  },
  mounted() {
      this.getPosts('home');
  },
  methods:{
      getPosts(section){
          let url = buildUrl(section);
          axios.get(url).then((response) => {
              this.results = response.data.results;
          }).catch( error => { console.log(error); });
      }
  },
  computed: {
      processedPosts(){
          let posts = this.results;

          // adding image_url attribute
          posts.map(post => {
              let imgObj = post.multimedia.find(media => media.format === "superJumbo");
              post.image_url = imgObj ? imgObj.url : "http://placehold.it/300x200?text=N/A";
          });

          // put array into Chunks
          let i, j, chunkedArray = [], chunk = 4;
          for(i = 0, j = 0; i < posts.length; i += chunk, j++){
              chunkedArray[j] = posts.slice(i, i+chunk);
          }

          return chunkedArray;
      }
  }
});

// API KEY = f5b344cf863b42aea00233d16ab4a86f