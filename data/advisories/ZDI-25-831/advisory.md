# ZDI-25-831: Delta Electronics DIAView Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-831
- **ZDI-CAN:** ZDI-CAN-26477
- **Date:** 2025-08-13
- **CVE:** CVE-2025-53417
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIAView
- **Credit:** hir0ot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-831/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics DIAView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 80 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-219-01

## Disclosure Timeline

- 2025-03-05 - Vulnerability reported to vendor
- 2025-08-13 - Coordinated public release of advisory
- 2025-08-13 - Advisory Updated
