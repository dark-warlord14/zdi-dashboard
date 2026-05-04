# ZDI-23-378: Microsoft Windows IKEEXT Service Vendor ID Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-378
- **ZDI-CAN:** ZDI-CAN-18935
- **Date:** 2023-03-31
- **CVE:** CVE-2023-21758
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** insu of 78ResearchLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-378/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IKEEXT service, which listens on UDP ports 500 and 4500. A crafted Vendor ID payload can cause a null pointer dereference. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21758

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
