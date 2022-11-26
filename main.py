import scrapy
from scrapy.crawler import CrawlerProcess
import UrlProccessor
from ConcordiaScraper import ConcordiaSpider
import Scikit
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # process = CrawlerProcess()
    # # Ask the page count limit
    # totalLimit = int(input("Enter the page count limit: "))
    # ConcordiaSpider.totalLimit = totalLimit
    # process.crawl(ConcordiaSpider)
    # process.start()
    # print("Crawler finished")

    urlProc = UrlProccessor.UrlProcessor()
    print(sorted(urlProc.sentientScores.items(), key=lambda x:x[1]))

    Scikit = Scikit.Scikit()
    dataset = Scikit.createModelData()
    Scikit.vectorize(dataset)

    Scikit.createKMeansClustering(6)
    # centroids = Scikit.kmeans.cluster_centers_

    colors = ["g.", "r."]




    # for i in range(len(dataset)):
    #     print("coordinate:",dataset[i],"label:",labels[i])
    #     plt.plot(dataset[i][0],dataset[i][1],colors[labels[i]], markersize=10)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
