# ZDI-20-860: Advantech iView User checkForDuplicateUserName SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-860
- **ZDI-CAN:** ZDI-CAN-10700
- **Date:** 2020-07-16
- **CVE:** CVE-2020-14497
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-860/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the User class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-196-33

## Disclosure Timeline

- 2020-03-26 - Vulnerability reported to vendor
- 2020-07-16 - Coordinated public release of advisory
