# ZDI-18-583: npm mosca Regular Expression Parsing Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-583
- **ZDI-CAN:** ZDI-CAN-6306
- **Date:** 2018-06-13
- **CVE:** CVE-2018-11615
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:N/I:N/A:C
- **Affected Vendors:** npm
- **Affected Products:** mosca
- **Credit:** Federico "phretor" Maggi of Trend Micro Security Research and Davide "_ocean" Quarta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-583/
## Vulnerability Details

This vulnerability allows remote attackers to deny service on vulnerable installations of npm mosca. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of topics. A crafted regular expression can cause the broker to crash. An attacker can leverage this vulnerability to deny access to the target system.

## Additional Details

Fixed in version 2.8.2

## Disclosure Timeline

- 2018-06-01 - Vulnerability reported to vendor
- 2018-06-13 - Coordinated public release of advisory
- 2018-06-13 - Advisory Updated
