from urllib import robotparser

robot_parser = robotparser.RobotFileParser()


def prepare(robots_txt_url):
    robot_parser.set_url(robots_txt_url)
    robot_parser.read()


def is_allowed(target_url, user_agent='*'):
    return robot_parser.can_fetch(user_agent, target_url)


if __name__ == '__main__':
    # todo how to deal with https
    prepare('https://www.apress.com/robots.txt')

    print(is_allowed('https://www.apress.com/category/software-development/java-software-development/', 'bookbot'))
    print(is_allowed('https://www.apress.com/category/software-development/java-software-development/', 'my-agent'))
    print(is_allowed('https://www.apress.com/category/software-development/java-software-development/', 'googlebot'))
