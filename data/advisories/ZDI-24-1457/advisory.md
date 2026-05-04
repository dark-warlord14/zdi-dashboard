# ZDI-24-1457: Delta Electronics InfraSuite Device Master _gExtraInfo Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1457
- **ZDI-CAN:** ZDI-CAN-24594
- **Date:** 2024-11-06
- **CVE:** CVE-2024-10456
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Simon Humbert of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1457/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the _gExtraInfo attribute. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-303-03

## Disclosure Timeline

- 2024-06-26 - Vulnerability reported to vendor
- 2024-11-06 - Coordinated public release of advisory
- 2024-11-06 - Advisory Updated
