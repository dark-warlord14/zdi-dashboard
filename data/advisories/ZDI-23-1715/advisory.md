# ZDI-23-1715: ManageEngine Applications Manager SingleSignOn Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1715
- **ZDI-CAN:** ZDI-CAN-21226
- **Date:** 2023-11-15
- **CVE:** CVE-2023-38333
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** Applications Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1715/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ManageEngine Applications Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SingleSignOn page. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/applications_manager/security-updates/security-updates-cve-2023-38333.html

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
