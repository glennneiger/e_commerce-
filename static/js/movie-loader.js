
function getinfo(movie_id, title, api_key) {
    url = 'https://api.themoviedb.org/3/find/tt' + movie_id + '?external_source=imdb_id&api_key='+api_key

     $.getJSON(url,
         function(result) {
             if (result.movie_results != null)
             {
                 var image_url = 'http://image.tmdb.org/t/p/w500/'
                            + result.movie_results[0].poster_path
                 var $idx_image_src = $('#'+movie_id+' img').attr('src', image_url)
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
                 var $idx_image_src = $('.single-prd-item img').attr('src', image_url)
                 var $description = $('div#home p').append(result.movie_results[0].overview)
                 var $popularity = $('#popularity').append(result.movie_results[0].popularity)

            }
        }
    )
}


