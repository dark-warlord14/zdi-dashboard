# ZDI-23-1756: Delta Electronics InfraSuite Device Master PlayWaveFile Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1756
- **ZDI-CAN:** ZDI-CAN-22013
- **Date:** 2023-11-30
- **CVE:** CVE-2023-47279
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1756/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PlayWaveFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-331-01

## Disclosure Timeline

- 2023-08-29 - Vulnerability reported to vendor
- 2023-11-30 - Coordinated public release of advisory
