# ZDI-25-926: Delta Electronics DIALink Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-926
- **ZDI-CAN:** ZDI-CAN-26827
- **Date:** 2025-10-01
- **CVE:** CVE-2025-58321
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIALink
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-926/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics DIALink. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DataCenter service, which listens on TCP port 7631 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-259-07

## Disclosure Timeline

- 2025-05-08 - Vulnerability reported to vendor
- 2025-10-01 - Coordinated public release of advisory
- 2025-10-01 - Advisory Updated
