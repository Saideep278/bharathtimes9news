const nav_pol = document.getElementById('nav_pol');
const nav_spo = document.getElementById('nav_spo');
const nav_bus = document.getElementById('nav_bus');
const nav_ent = document.getElementById('nav_ent');
const nav_cri = document.getElementById('nav_cri');
const nav_int = document.getElementById('nav_int');


const ssportsBtn = document.getElementById('sports_btn');
const politicsBtn = document.getElementById('politics_btn');
const businessBtn = document.getElementById('business_btn');

const loadBtn = document.getElementById('btn');
const spinner = document.getElementById('spinner');
const total = JSON.parse(document.getElementById('json-total').textContent);
const alert = document.getElementById('alert');

function loadmorePost() {
  var _current_item = $('.single_content').length
  const content_container = document.getElementById('content')
  $.ajax({
    url: '{% url "load" %}',
    type: 'GET',
    data: {
      'total_item': _current_item
    },
    beforeSend: function () {
      loadBtn.classList.add('not-visible');
      spinner.classList.remove('not-visible');
    },
    success: function (response) {
      const data = response.posts
      spinner.classList.add('not-visible');

      data.map(i => {
        var temp = "abcd/"
        temp = temp + i.media
        console.log(i.media);

        content_container.innerHTML += `<div class="single_content border border-light mt-2 pl-2">
                                              <h2> ${i.title} </h2>
                                              <a href="${i.id}"> <img class="img" src=" ${temp} "></a>
                                              <p class="desc">  ${i.tagline}  </p>
                                              </div>`
      });
      if (_current_item == total) {
        alert.classList.remove('not-visible');
      } else {
        loadBtn.classList.remove('not-visible');
      }


    },
    error: function (err) {
      console.log(err);
    }
  })
}

function loadCategory(param) {
  const content_container = document.getElementById('content')
  $.ajax({
    url: param,
    type: 'GET',
    success: function (response) {
      const data = response.news
      content_container.innerHTML = `<div class="single_content border border-light mt-2 pl-2">
                                              
                                              </div>`
      data.map(i => {
        var temp = "abcd/"
        temp = temp + i.media
        

        content_container.innerHTML += `<div class="single_content border border-light mt-2 pl-2">
                                              <h2> ${i.title} </h2>
                                              <a href="${i.id}"> <img class="img" src=" ${temp} "></a>
                                              <p class="desc">  ${i.tagline}  </p>
                                              </div>`
      });
    },
    error: function (err) { console.log("HII"); }
  })
};

loadBtn.addEventListener('click', () => {
  loadmorePost();
});

ssportsBtn.addEventListener('click', () => {
  loadCategory("sports");
});

politicsBtn.addEventListener('click', () => {
  loadCategory("politics");
});

businessBtn.addEventListener('click', () => {
  loadCategory("business");
});



nav_pol.addEventListener('click', () => {
  loadCategory("politics");
});
nav_spo.addEventListener('click', () => {
  loadCategory("sports");
});
nav_bus.addEventListener('click', () => {
  loadCategory("business");
});
nav_ent.addEventListener('click', () => {
  loadCategory("entertainment");
});
nav_cri.addEventListener('click', () => {
  loadCategory("crime");
});
nav_int.addEventListener('click', () => {
  loadCategory("international");
});
