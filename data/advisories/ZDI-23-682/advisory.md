# ZDI-23-682: Delta Electronics InfraSuite Device Master Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-682
- **ZDI-CAN:** ZDI-CAN-19406
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1142
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-682/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WebServerCallBack function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-11-30 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
