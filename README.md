# TestProject

To RUN UI tests:

py.test --html=report.html gui_tests/tests/ --browser firefox/chrome

Currently supports MacOS drivers, but feel free to add drivers for your OS into gui_tests/drivers

To RUN API tests:

py.test --html=report.html api_tests/tests/
