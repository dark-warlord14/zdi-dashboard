# ZDI-08-071: IBM Tivoli Storage Manager Express for Microsoft SQL Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-071
- **ZDI-CAN:** ZDI-CAN-321
- **Date:** 2008-10-30
- **CVE:** CVE-2008-4801
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager Express
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-071/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager Express for Microsoft SQL. Authentication is not required to exploit this vulnerability. The specific flaw resides in the Data Protection for SQL CAD service, dsmcat.exe, which listens by default on a TCP port above 1024. The process trusts a user-supplied size value, receiving the specified amount of data into a static heap buffer. By sending a specially crafted packet, an attacker can overflow that buffer leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21322623

## Disclosure Timeline

- 2008-05-12 - Vulnerability reported to vendor
- 2008-10-30 - Coordinated public release of advisory
