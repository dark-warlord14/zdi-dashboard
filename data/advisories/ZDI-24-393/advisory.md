# ZDI-24-393: Ivanti Avalanche WLAvalancheService Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-393
- **ZDI-CAN:** ZDI-CAN-22989
- **Date:** 2024-04-23
- **CVE:** CVE-2024-27977
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-393/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the WLAvalancheService, which listens on TCP port 1777 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-3-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2024-01-09 - Vulnerability reported to vendor
- 2024-04-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
