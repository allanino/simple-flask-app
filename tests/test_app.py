from nose.tools import assert_equals


class TestApp(object):

    def setUp(self):
        # Set app to test running app
        import app as app_module
        app = app_module.app

        # Assign test_client() to app
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_ping(self):
        # Try access without authentication
        res = self.app.get('/ping')
        assert_equals(res.status_code, 200)
        assert_equals(res.data, 'OK')
