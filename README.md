# Citrusgroup


### Prerequisites

Install docker and docker-compose on your computer
* [Docker](https://docs.docker.com/install/) - The web framework used

### Run project

Run ``` docker-compose up --build ``` from the root directory.
You should now have a postgres database on port 6432 and a django web application on port 8000


### Population tool

In the terminal, Run ``` docker-compose exec web python manage.py shell ```from the terminal after
running ``` docker-compose up --build ```.
Then in the terminal run the following:
```
from propertymatching import population_tool
population_tool.main()
```

if you want to run the individual functions within population_tool, add the extension, e.g. the following:

``` population_tool.insert_function_name() ```
