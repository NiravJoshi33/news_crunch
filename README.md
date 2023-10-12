
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[news_crunch](https://github.com/NiravJoshi33/news_crunch)">
    <img src="https://github.com/NiravJoshi33/news_crunch/blob/main/nc_long_logo.png" alt="Logo" width="500" height="80">
  </a>

<h3 align="center">News Crunch</h3>

  <p align="center">
    An app to scrape data from news websites and display the articles in web GUI. 
    <br />
    <a href="https://github.com/NiravJoshi33/news_crunch"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NiravJoshi33/news_crunch">View Demo</a>
    ·
    <a href="https://github.com/NiravJoshi33/news_crunch/issues">Report Bug</a>
    ·
    <a href="https://github.com/NiravJoshi33/news_crunch/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot](https://github.com/NiravJoshi33/news_crunch/blob/main/app_screenshot.png)

This is an app that scrapes news article details such as title, date, auther etc. from different news websites, processes the data and shows on a single page. 

This app is inspired by [inshorts](https://m.inshorts.com/en/read)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites & Installation

Before starting, please make sure that following dependencies are installed on your machine
* [Python](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)

After the above dependecies are installed, follow below instructions:
* Clone the repo
  Clone the repo
   ```sh
   git clone https://github.com/NiravJoshi33/news_crunch.git
   ```
* Navigate to the project folder using CLI
* Install other dependecies with following command
  ````
  pip install -r requirements.txt
  ````
  Wait for the packages to be installed.


<!-- USAGE EXAMPLES -->
## How to Use

Follow the below instructions to run the project

* Navigate to the path `news_scrapper/spiders` and run following scrips one by one. (Ideally all these should be run by a single script but due to inherrent behavior of the scrapy's twisted engine, one it is started for one process, it stops another process from starting. I am working on it to resolve this.)
  ```
  news_spider1.py
  ```
  ```
  news_spider2.py
  ```
    ```
  news_spider3.py
  ```
    ```
  news_spider4.py
  ```
    ```
  news_spider5.py
  ```
    ```
  news_spider6.py
  ```
  **Known Issue:** Don't worry if `news_spider3.py` gives an error. The website sometimes blocks spider from running. The app can run without this script working.
* Navigate to project folder and run the main script
  ```
  main.py
  ```
* After the script has run, browser should open and display a GUI. In case, this browser doesn't open, open it manually and open following url
  ```
  http://localhost:8501
  ```
* By default, a side bar will load with the page. From there, you can deselect any website you don't want to see news from and use the slider to select the number of articles to show.

<!-- ROADMAP -->
## To Do

- [ ] Resolve Major Bugs with the current Basic Version
  - [ ] Run the app with the single script
  - [ ] OpenSSL Error occuring sometimes
  - [ ] Clean Data before showing in GUI
    - [ ] Dates from all websites in same format
  - [ ] Inconsistent card size due to different size of thumbs and excerpts

See the [open issues](https://github.com/NiravJoshi33/news_crunch/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - Nirav Joshi \
Email - niravjoshi3000@gmail.com \
Project Link: [https://github.com/NiravJoshi33/news_crunch](https://github.com/NiravJoshi33/news_crunch)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Scrapy Course - Python Web Scraping for Beginners](https://www.youtube.com/watch?v=mBoX_JCKZTE&pp=ygUNc2NyYXB5IGNvdXJzZQ%3D%3D) by freecodecamp.org
* [Python Streamlit Full Course](https://www.youtube.com/watch?v=RjiqbTLW9_E&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) by [Othneil Drew](https://github.com/othneildrew)
* Awesome community on [stackoverflow](https://stackoverflow.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NiravJoshi33/news_crunch.svg?style=for-the-badge
[contributors-url]: https://github.com/NiravJoshi33/news_crunch/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/NiravJoshi33/news_crunch.svg?style=for-the-badge
[forks-url]: https://github.com/NiravJoshi33/news_crunch/network/members
[stars-shield]: https://img.shields.io/github/stars/NiravJoshi33/news_crunch.svg?style=for-the-badge
[stars-url]: https://github.com/NiravJoshi33/news_crunch/stargazers
[issues-shield]: https://img.shields.io/github/issues/NiravJoshi33/news_crunch.svg?style=for-the-badge
[issues-url]: https://github.com/NiravJoshi33/news_crunch/issues
[license-shield]: https://img.shields.io/github/license/NiravJoshi33/news_crunch.svg?style=for-the-badge
[license-url]: https://github.com/NiravJoshi33/news_crunch/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
