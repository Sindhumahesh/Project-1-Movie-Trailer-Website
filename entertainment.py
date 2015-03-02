import media
import fresh_tomatoes

#media and fresh_tomatoes are the names of the python file
#Movie is the name of the class defined in media file

#creating instances of the class Movie
walk_story = media.Movie("A Walk to Remember",
                         "A story of two North Carolina teens, Landon Carter and Jamie Sullivan, who are thrown together after Landon gets into trouble and is made to do community service.",
                         "http://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                         "https://www.youtube.com/watch?v=k3B2XBcp7vA","English")
godfather_story = media.Movie("The Godfather",
                              "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                              "http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                              "https://www.youtube.com/watch?v=sY1S34973zA","English")
good_story = media.Movie("The Good, the Bad and the Ugly",
                         "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
                         "http://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                         "https://www.youtube.com/watch?v=WCN5JJY_wiA","English")
gone_girl = media.Movie("Gone Girl",
                        "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.",
                        "http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=esGn-xKFZdU","English")
dark_knight = media.Movie("The Dark Knight",
                          "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                          "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY","English")
inception_story = media.Movie("Inception",
			      "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
			      "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
			      "https://www.youtube.com/watch?v=8hP9D6kZseM",
			      "English")
three_idiots = media.Movie("3 Idiots",
                          "Two friends are searching for their long lost companion.They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them idiots",
                          "http://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                          "https://www.youtube.com/watch?v=xvszmNXdM4w","Hindi")
ohmygod_story = media.Movie("Oh My God",
                            "A shopkeeper who takes God to court when his shop is destroyed by an earthquake.",
                            "http://upload.wikimedia.org/wikipedia/en/e/e0/OMG_Poster.png",
                            "https://www.youtube.com/watch?v=S3b7F4rGre0","Hindi")
titanic_story = media.Movie("Titanic",
			    "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
			    "http://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
			    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
			    "English")
movies = [walk_story,godfather_story,good_story,gone_girl,dark_knight,inception_story,three_idiots,ohmygod_story,titanic_story]
fresh_tomatoes.open_movies_page(movies)


