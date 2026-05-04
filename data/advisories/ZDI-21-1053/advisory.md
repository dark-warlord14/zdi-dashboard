# ZDI-21-1053: Microsoft Windows Lock Screen Improper Access Control Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1053
- **ZDI-CAN:** ZDI-CAN-13692
- **Date:** 2021-09-02
- **CVE:** CVE-2021-26431
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1053/
## Vulnerability Details

This vulnerability allows physically present attackers to bypass authentication on affected installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the lock screen. The issue results from the lack of proper access control prior to authentication. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26431

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-09-02 - Coordinated public release of advisory
