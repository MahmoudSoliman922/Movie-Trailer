import media
import fresh_tomatoes
# Creating Instences
v_for_vendetta = media.Movie("V for Vendetta",
                         "In a future British tyranny a "
                         "shadowy freedom fighter"
                         "known only by the alias of V plots to overthrow it"
                         "with the help of a young woman.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYzllMjJkODAtYjMwMi00YmNhLWFhYzAtZjZjODg5YzEwOGUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,679,999_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=IHVzzxrPt1c")
avatar = media.Movie("Avatar",
                      "Story about blue creatures",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # NOQA
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
the_god_father = media.Movie("The God Father",
                             "The aging patriarch of an organized crime"
                             "dynasty transfers control of his clandestine"
                             "empire to his reluctant son.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=sY1S34973zA")
sherlouk_houlms = media.Movie("Sherlouk Houlms",
                             "Genius Guy solves difficult cases",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_SY1000_CR0,0,669,1000_AL_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=Egcx63-FfTE")
karate_kid = media.Movie("Karate Kid",
                        "Kid learns Karate",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSN0nj8gbK0fo4UO9qK0gaRxfCNgdGygDZgSMqbZ88d97W_8622",  # NOQA
                        "https://www.youtube.com/watch?v=n7JhKCQnEqQ")
star_wars = media.Movie("Star Wars",
                       "SCI-FI movie",
                       "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1200px-Star_Wars_Logo.svg.png",  # NOQA
                       "https://www.youtube.com/watch?v=Q0CbN8sfihY")
# creating list of instances
movs = [v_for_vendetta,
        avatar, the_god_father,
        sherlouk_houlms,
        karate_kid, star_wars]
# passing the list of instances to open_movies_page() method
fresh_tomatoes.open_movies_page(movs)
