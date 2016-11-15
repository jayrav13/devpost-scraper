# devpost-scraper

A team of four hackers built [PostDev](https://github.com/otmichael/Idea), (our [submission](https://devpost.com/software/postdev-k286c0)), a project that generates project ideas for hackers based on every project that's ever been submitted to [DevPost](https://devpost.com). To enable this, we wrote a web scraper that pulls every project on DevPost (at the time, 57,000+). This this repository contains that data and the scripts that pulled it. 

## Getting Started

### Clean Up

To pull fresh data, you can start by clearing current data by doing the following:

```sh
rm -rf data/*
rm -rf content/*
```

The two above folders store all of the data files associated with DevPost's content. What do these files look like:

### Data Structure

NOTE - currently, neither the `data/` folder or the `content/` folder described below are available in this repo because of their sheer size. To get started with scraping, execute:

```sh
mkdir data content
```

... to create the two folders that will serve as destinations for the below scripts.

We first look at the `data/` folder, which contains high level information of all projects. When executing the following request:

```sh
curl -i -X GET "https://devpost.com/software/search?query=&page=1"
```

...DevPost scans the client's User Agent and recognizes that this request is NOT coming from a browser, thus returning a JSON object of all of the projects on that given page, where `page=1` is the most recent. We can iterate through this until the array size returned is 0.

An example:

```sh
{
  "software": [
    {
      "class_name": "Software",
      "name": "PostDev",
      "tagline": "Analyze DevPost - by hackers for hackers",
      "slug": "postdev-k286c0",
      "url": "https://devpost.com/software/postdev-k286c0",
      "members": [
        "jayrav13",
        "nsamarin",
        "otmichael",
        "snowiswhite"
      ],
      "tags": [
        "python",
        "flask",
        "react",
        "redux",
        "mdl",
        "markovify",
        "machine-learning",
        "ibm-watson",
        "amazon-ec2"
      ],
      "winner": false,
      "photo": null,
      "has_video": false,
      "like_count": 2,
      "comment_count": 0
    }
  ],
  "total_count": 1
}
```

Note that while this result is just an example and had a specific search query, leaving that field blank per the above example will return all projects on that page as objects in the array with key "software". Executing `data.py` from the root of the project will return all of these for you.

While this provides an incredible amount of information, a key component our project looked for was the detailed project description drafted by the submitting team. Thus, we move to the second and critical folder: `content/`. The content folder houses one file for every project on DevPost, approximately 57,000. The structure is as follows:

```sh
{
  "url": "https://devpost.com/software/trip-py-planner",
  "content": "..."
}
```

Here, the "content" key's value is the HTML page representing this project at the time of the request. I did this mainly to keep the script to make 57,000 requests as fast as possible, but also to preserve additional details past just the description in the event that they are useful.

The biggest challenge: making the 57,000 requests in an acceptable amount of time. My solution came from [this StackOverflow response](http://stackoverflow.com/questions/2632520/what-is-the-fastest-way-to-send-100-000-http-requests-in-python) that provided direction on how to make a mass number of requests in Python.

#### NOTE:

Because of how much data the `content/` folder houses, we are currently not including it in this repository. Above instructions will enable you to grab everything you need, and it should take around 2 hours to complete.

### TODO
- Write the final script that combines high level results and specific details into one, manageable JSON file that represents all projects on DevPost.
- Create an "update" script that only pulls the most recent projects, stopping when it encounters the first project that already exists in the current data set.

### Helper shell commands

List number of files:

```sh
ls -al | wc -l
```

List directory size:

```sh
du -h -c . -l
```

...where `.` is the directory you're looking to calculate size for.

### Team

[Jay Ravaliya](https://github.com/jayrav13)
[Mikey Oz](https://github.com/otmichael)
[Nikita Samarin](https://github.com/nsamarin)
[Jaeick Bae](https://github.com/jibae2)

