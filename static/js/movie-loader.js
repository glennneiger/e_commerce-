
function getinfo(movie_id, title, api_key) {
    url = 'https://api.themoviedb.org/3/find/tt' + movie_id + '?external_source=imdb_id&api_key='+api_key

     $.getJSON(url,
         function(result) {
             if (result.movie_results != null)
             {
                 var image_url = 'http://image.tmdb.org/t/p/w500/'
                            + result.movie_results[0].poster_path
                            console.log(image_url,  $idx_image_src, $('#'+movie_id+' img'))
                 var $idx_image_src = $('#'+movie_id+' img').attr('src', image_url)
                 console.log(image_url,  $idx_image_src, $('#'+movie_id+' img'))
            }
        }
    )
}

function get_movie_data(movie_id, title, api_key) {
    url = 'https://api.themoviedb.org/3/find/tt' + movie_id + '?external_source=imdb_id&api_key='+api_key

     $.getJSON(url,
         function(result) {
             if (result.movie_results != null)
             {
                 var image_url = 'http://image.tmdb.org/t/p/w500/'
                            + result.movie_results[0].poster_path
                 console.log(result.movie_results)
                 // result.movie_results[0].overview
                 var $idx_image_src = $('.single-prd-item img').attr('src', image_url)
                 var $description = $('div#home p').append(result.movie_results[0].overview)
                 var $popularity = $('#popularity').append(result.movie_results[0].popularity)
                 console.log($description)
            }
        }
    )
}

function add_impression(user_id, event_type, content_id, session_id, csrf_token) {
            $.ajax({
                 type: 'POST',
                 url: '/collect/log/',
                 data: {
                        "csrfmiddlewaretoken": csrf_token,
                        "event_type": event_type,
                        "user_id": user_id,
                        "content_id": content_id,
                        "session_id": session_id
                        },
                 fail: function(){
                     console.log('log failed(' + event_type + ')')
                    }
})};
