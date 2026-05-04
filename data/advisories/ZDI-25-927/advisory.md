# ZDI-25-927: Delta Electronics DIALink Directory Traversal Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-927
- **ZDI-CAN:** ZDI-CAN-26843
- **Date:** 2025-10-01
- **CVE:** CVE-2025-58320
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIALink
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-927/
## Vulnerability Details

This vulnerability allows remote attackers to overwrite configuration files on affected installations of Delta Electronics DIALink. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 7631 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-259-07

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-10-01 - Coordinated public release of advisory
- 2025-10-01 - Advisory Updated
