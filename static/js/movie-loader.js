
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

