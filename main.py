import speedtest
test = speedtest.Speedtest()
print("Loading server List")
test.get_servers() # get list of servers
print("choosing best server")
best = test.get_best_server()# choose best server
print(f"Found:{best['host']} located in {best ['country']}")
print("performing downlaod test")
download_result = test.download()
print("performing upload test")
upload_result = test.upload()
ping_result = test.results.ping
print(f"Downlaod speed:{download_result / 1024 / 1024:.2f}Mbit/s")
print(f"upload speed:{upload_result / 1024 / 1024:.2f}Mbit/s")
print(f"Ping:{ping_result:.2f}ms")