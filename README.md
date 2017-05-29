# Python/Flask REST API Example

## Invoking the API

```
export BASE_URL=http://localhost:5000
export AUTH=miguel:python

# list
curl -i -u $AUTH $BASE_URL/v1/tasks

# get
curl -i -u $AUTH $BASE_URL/v1/tasks/1

# create
curl -i -u $AUTH -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' $BASE_URL/v1/tasks

# update
curl -i -u $AUTH -H "Content-Type: application/json" -X PUT -d '{"done":true}' $BASE_URL/v1/tasks/2

# delete
curl -i -u $AUTH -X DELETE $BASE_URL/v1/tasks/2
```

## Resources

* [Flask REST example](https://gist.github.com/miguelgrinberg/5614326)
