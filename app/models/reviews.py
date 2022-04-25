

class Reviews:

    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        # save_review method that appends the review object to a class variable all_reviews that is an empty list.
        Reviews.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        # clears all the Items from the list.
        Reviews.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):

        response = []

        for review in cls.all_reviews: # loops through all the reviews in the all_reviews list
            if review.movie_id == id: # checks for reviews that have the same movie ID as the id passed.
                response.append(review) # append those reviews to a new response list

        return response