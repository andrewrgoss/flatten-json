# Flatten JSON

Sample JSON data that is not flat:

```json
{
    "name": "Cap'n Chuck",
    "aliases": ["Chuck Force 1", "Whistlepig"],
    "physical": {
        "height_in": 27,
        "weight_lb": 19
    },
    "wood_chucked_lbs": 2219
}
```

How do you load JSON like this into a regular database table so you can
query it with SQL? One possible way is to flatten the data to make this possible.

For example, Cap'n Chuck's record would be flattened as follows:

```json
{
    "name": "Cap'n Chuck",
    "aliases.0": "Chuck Force 1",
    "aliases.1": "Whistlepig",
    "physical.height_in": 27,
    "physical.weight_lb": 19,
    "wood_chucked_lbs": 2219
}
```

## Potential Issues With This Approach

This approach will required a fixed table schema in order to insert the flattened values into a columnar database.
The problem is, the woodchuck JSON data being ingested in going to be flattened to varying column
widths. For example, a woodchuck record being loaded in could end up having 5 different
aliases instead of just 2. While RDBMSs operate with a relational model defined by schema,
NoSQL databases offer a non-relational and schema-less data model. With a document store
data model offered through NoSQL, the woodchuck JSON data could be directly imported without
being flattened first. The woodchuck data could be queried by properties in a similar fashion
as a relational database but wouldn't be required to adhere to the strict structure of
a database table.