# ZDI-26-130: IceWarp collaboration Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-130
- **ZDI-CAN:** ZDI-CAN-25440
- **Date:** 2026-02-25
- **CVE:** CVE-2026-2493
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** IceWarp
- **Affected Products:** IceWarp
- **Credit:** Nicocha30
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-130/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of IceWarp. Authentication is not required to exploit this vulnerability. The specific flaw exists within handling of the ticket parameter provided to the collaboration endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Fixed in versions 14.2.0.12 ( https://support.icewarp.com/hc/en-us/community/posts/43490185733393-IceWarp-EPOS-Server-Release-Notes-Version-14-2-0-12 ) and 14.1.0.20 ( https://support.icewarp.com/hc/en-us/community/posts/43751491641233-IceWarp-EPOS-Server-Release-Notes-Version-14-1-0-20 )

## Disclosure Timeline

- 2025-12-18 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
