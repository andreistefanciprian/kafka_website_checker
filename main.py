from website_checker import WebsiteChecker

if __name__ == '__main__':

    # define variables
    url = 'https://api.github.com'

    # check website
    check = WebsiteChecker(url)
    check.website_checker()
    print(check.response_time)
    print(check.status_code)