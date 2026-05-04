# ZDI-22-1044: ICONICS GENESIS64 GenBroker64 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1044
- **ZDI-CAN:** ZDI-CAN-17389
- **Date:** 2022-08-03
- **CVE:** CVE-2022-33319
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Axel '0vercl0k' Souchet from https://doar-e.github.io/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1044/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ICONICS GENESIS64 GenBroker64. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GenBroker64 service, which listens on TCP port 38080 by default. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose information in the context of the current process or to create a denial-of-service condition on the system.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-202-04

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-08-03 - Coordinated public release of advisory
