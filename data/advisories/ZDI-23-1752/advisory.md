# ZDI-23-1752: Delta Electronics InfraSuite Device Master UploadMedia Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1752
- **ZDI-CAN:** ZDI-CAN-21707
- **Date:** 2023-11-30
- **CVE:** CVE-2023-46690
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1752/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics InfraSuite Device Master. Authentication is required to exploit this vulnerability. The specific flaw exists within the UploadMedia function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-331-01

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2023-11-30 - Coordinated public release of advisory
