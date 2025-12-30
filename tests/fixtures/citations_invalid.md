# Invalid Citations Fixture

This file contains INTENTIONALLY INVALID citations that should FAIL verification.
Used for testing that the verification script catches errors.

## Citation 1: Missing Required Fields

```yaml
id: Missing-Title
type: book
authors:
  - Smith, John
year: 2020
publisher: Academic Press
url: https://www.example.com/book
verified: true
```

## Citation 2: Invalid ISBN (bad checksum)

```yaml
id: Bad-ISBN-Checksum
type: book
authors:
  - Doe, Jane
title: "Book with Bad ISBN"
year: 2020
publisher: Academic Press
isbn: 978-0-13-468599-0
url: https://www.example.com/book
verified: true
verification_url: https://www.example.com/book
notes: "ISBN checksum is wrong (last digit should be 1, not 0)"
```

## Citation 3: Invalid ISBN (wrong length)

```yaml
id: Bad-ISBN-Length
type: book
authors:
  - Doe, Jane
title: "Book with Wrong ISBN Length"
year: 2020
publisher: Academic Press
isbn: 978-0-13-46859
url: https://www.example.com/book
verified: true
verification_url: https://www.example.com/book
notes: "ISBN is only 12 digits, should be 10 or 13"
```

## Citation 4: Invalid DOI Format

```yaml
id: Bad-DOI
type: article
authors:
  - Johnson, Alice
title: "Article with Bad DOI"
journal: "Test Journal"
year: 2023
doi: "not-a-valid-doi"
url: https://www.example.com/article
verified: true
verification_url: https://www.example.com/article
notes: "DOI doesn't match format 10.xxxx/..."
```

## Citation 5: Invalid URL Format

```yaml
id: Bad-URL
type: article
authors:
  - Williams, Bob
title: "Article with Bad URL"
journal: "Test Journal"
year: 2023
doi: "10.1234/test.2023.001"
url: not-a-valid-url
verified: true
verification_url: https://www.example.com/article
notes: "URL doesn't start with http:// or https://"
```

## Citation 6: Invalid Year (too old)

```yaml
id: Bad-Year-Old
type: book
authors:
  - Ancient, Author
title: "Book from the Past"
year: 1850
publisher: Old Press
url: https://www.example.com/old-book
verified: true
verification_url: https://www.example.com/old-book
notes: "Year 1850 is before the valid range (1900-2030)"
```

## Citation 7: Invalid Year (future)

```yaml
id: Bad-Year-Future
type: book
authors:
  - Future, Author
title: "Book from the Future"
year: 2099
publisher: Future Press
url: https://www.example.com/future-book
verified: true
verification_url: https://www.example.com/future-book
notes: "Year 2099 is after the valid range (1900-2030)"
```

## Citation 8: Missing Year

```yaml
id: Missing-Year
type: book
authors:
  - Timeless, Author
title: "Book Without Year"
publisher: Eternal Press
url: https://www.example.com/timeless
verified: true
verification_url: https://www.example.com/timeless
notes: "Missing required year field"
```

## Citation 9: Invalid Verification URL

```yaml
id: Bad-Verification-URL
type: article
authors:
  - Tester, Test
title: "Article with Bad Verification URL"
journal: "Test Journal"
year: 2023
doi: "10.1234/test.2023.002"
url: https://www.example.com/article
verified: true
verification_url: ftp://not-http.example.com/file
notes: "Verification URL uses ftp:// instead of http(s)://"
```
