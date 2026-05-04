# ZDI-24-1606: 7-Zip Qcow Handler Infinite Loop Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1606
- **ZDI-CAN:** ZDI-CAN-24307
- **Date:** 2024-11-21
- **CVE:** CVE-2024-11612
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H
- **Affected Vendors:** 7-Zip
- **Affected Products:** 7-Zip
- **Credit:** 2ourc3
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1606/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of 7-Zip. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the processing of streams. The issue results from a logic error that can lead to an infinite loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in 7-Zip 24.08

## Disclosure Timeline

- 2024-06-26 - Vulnerability reported to vendor
- 2024-11-21 - Coordinated public release of advisory
- 2024-11-26 - Advisory Updated
