# ZDI-23-009: Microsoft Windows IKEEXT Service Vendor ID Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-009
- **ZDI-CAN:** ZDI-CAN-18647
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21547
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** insu of 78ResearchLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-009/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IKEEXT service, which listens on UDP ports 500 and 4500. A crafted Vendor ID payload can cause a null pointer dereference. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21547

## Disclosure Timeline

- 2022-10-13 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
