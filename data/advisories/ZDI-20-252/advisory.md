# ZDI-20-252: ELOG Electronic Logbook drop-count Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-252
- **ZDI-CAN:** ZDI-CAN-10115
- **Date:** 2020-02-12
- **CVE:** CVE-2020-8859
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** ELOG
- **Affected Products:** Electronic Logbook
- **Credit:** Asif Akbar of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-252/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of ELOG Electronic Logbook. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of HTTP parameters. A crafted request can trigger the dereference of a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition.

## Additional Details

Fixed in version 3.1.4-033e292

## Disclosure Timeline

- 2020-01-31 - Vulnerability reported to vendor
- 2020-02-12 - Coordinated public release of advisory
