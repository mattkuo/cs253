#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
# from apps.unit3.blog import BlogHandler
# from apps.unit3.submitpost import SubmitPostHandler
# from apps.unit3.newpost import NewPostHandler
# from apps.unit4.signup import SignupHandler
# from apps.unit4.welcome import WelcomeHandler
# from apps.unit4.login import LoginHandler
# from apps.unit4.logout import LogoutHandler
# from apps.unit5.blog import BlogHandler
# from apps.unit5.submitpost import SubmitPostHandler
# from apps.unit5.newpost import NewPostHandler
# from apps.unit5.signup import SignupHandler
# from apps.unit5.welcome import WelcomeHandler
# from apps.unit5.login import LoginHandler
# from apps.unit5.logout import LogoutHandler
# from apps.unit5.feed import JsonFeedHandler
from apps.unit6.blog import BlogHandler
from apps.unit6.submitpost import SubmitPostHandler
from apps.unit6.newpost import NewPostHandler
from apps.unit6.signup import SignupHandler
from apps.unit6.welcome import WelcomeHandler
from apps.unit6.login import LoginHandler
from apps.unit6.logout import LogoutHandler
from apps.unit6.feed import JsonFeedHandler
from apps.unit6.flush import FlushHandler

app = webapp2.WSGIApplication([
    # ('/unit3/blog', BlogHandler), # 10 most recent entries
    # ('/unit3/blog/newpost', SubmitPostHandler), # Submit post
    # ('/unit3/blog/([0-9]+)', NewPostHandler), # New post
    # ('/unit4/signup', SignupHandler),
    # ('/unit4/welcome', WelcomeHandler),
    # ('/unit4/login', LoginHandler),
    # ('/unit4/logout', LogoutHandler),
    # ('/unit5/blog', BlogHandler), # 10 most recent entries
    # ('/unit5/blog/newpost', SubmitPostHandler), # Submit post
    # ('/unit5/blog/([0-9]+)', NewPostHandler), # New post
    # ('/unit5/blog/signup', SignupHandler),
    # ('/unit5/blog/welcome', WelcomeHandler),
    # ('/unit5/blog/login', LoginHandler),
    # ('/unit5/blog/logout', LogoutHandler),
    # ('/unit5/blog/([a-zA-Z0-9]*)\.json', JsonFeedHandler),
    ('/unit6/blog', BlogHandler), # 10 most recent entries
    ('/unit6/blog/newpost', SubmitPostHandler), # Submit post
    ('/unit6/blog/([0-9]+)', NewPostHandler), # New post
    ('/unit6/blog/signup', SignupHandler),
    ('/unit6/blog/welcome', WelcomeHandler),
    ('/unit6/blog/login', LoginHandler),
    ('/unit6/blog/logout', LogoutHandler),
    ('/unit6/blog/([a-zA-Z0-9]*)\.json', JsonFeedHandler),
    ('/unit6/blog/flush', FlushHandler),
], debug=True)
