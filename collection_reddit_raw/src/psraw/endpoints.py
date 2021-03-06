import praw


def sort_type(value):
    """Ensures values passed in are one of the valid set"""
    directions = {'asc', 'desc'}

    if value in directions:
        return value
    else:
        raise ValueError('Value must be one of: {}'.format(directions))


LIMIT_DEFAULT = 500
BASE_ADDRESS = 'https://apiv2.pushshift.io/reddit'
ENDPOINTS = {
    'comment_search': {
        'params': {
            'after': int,
            'before': int,
            'limit': int,
            'q': str,
            'sort': sort_type,
            'subreddit': str,
            'author': str,
            'link_id': str
        },
        'limit': LIMIT_DEFAULT,
        'return_type': praw.models.Comment,
        'url': '/search/comment/'
    },
    'submission_search': {
        'params': {
            'after': int,
            'before': int,
            'limit': int,
            'q': str,
            'author': str,
            'sort': sort_type,
            'subreddit': str
        },
        'limit': LIMIT_DEFAULT,
        'return_type': praw.models.Submission,
        'url': '/search/submission/'
    }
}
