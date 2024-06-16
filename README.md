Write a function for parsing a text file (parse_file), which takes the path to the file as its only argument and returns a set of dictionaries containing the data. The function is intended to be used only in the following way:
```python
def parse_file(path):
    ...


def load_data(path):
    parsed_data = parse_file(path)

    for document in parsed_data:
        ...
        # load document to database (or do something else)
```

The file is a collection of key-value data, with the key and value separated by a colon.
Extra spaces must be removed from the values, and multiline values must be combined into one line, maintaining hyphens (but not indentations).
Data with duplicate keys is considered multi-line, i.e. in the source file the following two entries are identical:
```
foo: bar
     baz

foo: bar
foo: baz
```

Each document in the file is separated by at least one blank line; lines beginning with the `#` character are comments and should be ignored.

An example of the source data is in the file `example.txt`.

An example of one of the resulting dictionaries after processing:

```python
{'as-block': 'AS30720 - AS30979',
 'type': 'REGULAR',
 'descr': 'RIPE NCC ASN block',
 'remarks': 'These AS Numbers are further assigned to network\n' \
            'operators in the RIPE NCC service region. AS\n' \
            'assignment policy is documented in:\n' \
            '<http://www.ripe.net/ripe/docs/asn-assignment.html>\n' \
            'RIPE NCC members can request AS Numbers using the\n' \
            'form located at:\n' \
            '<http://lirportal.ripe.net/lirportal/liruser/resource_request/draw.html?name=as-number>\n' \
            'data has been transferred from RIPE Whois Database 20050221',
 'org': 'ORG-AFNC1-AFRINIC',
 'admin-c': 'TEAM-AFRINIC',
 'tech-c': 'TEAM-AFRINIC',
 'mnt-by': 'AFRINIC-HM-MNT',
 'mnt-lower': 'AFRINIC-HM-MNT',
 'changed': '***@ripe.net 20031001\n' \
            '***@ripe.net 20040421\n' \
            '***@ripe.net 20050202\n' \
            '***@afrinic.net 20050205',
 'source': 'AFRINIC'}
```

Restrictions:

* Python 3.7+;
* standard library only.

What will the bonuses be for:

* if the file opens and closes correctly even in the event of an execution;
* if the code is structured (short and clear functions, good naming, comments where necessary);
* if it will be possible to parse large files (larger than the RAM size);
* if type annotations are specified;
* if the code is formatted using pep8;
* if it will be possible to parse data from a gzip archive without unpacking.
--- 

*The solution can be posted on Github in an open repository, and can also be freely shown as examples of your code =)*
