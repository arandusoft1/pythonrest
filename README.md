# Python/Flask REST API Example

## Invoking the API

```
# list
curl -i -u miguel:python http://localhost:5000/v1/tasks

# get
curl -i -u miguel:python http://localhost:5000/v1/tasks/1

# create
curl -i -u miguel:python -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/v1/tasks

# update
curl -i -u miguel:python -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/v1/tasks/2

# delete
curl -i -u miguel:python -X DELETE http://localhost:5000/v1/tasks/2
```

## Resources

* [Flask REST example](https://gist.github.com/miguelgrinberg/5614326)
