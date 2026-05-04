# ZDI-24-1158: Rockwell Automation ThinManager ThinServer Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1158
- **ZDI-CAN:** ZDI-CAN-24040
- **Date:** 2024-08-22
- **CVE:** CVE-2024-7988
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** ThinManager
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation ThinManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ThinServer service. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.rockwellautomation.com/en-ca/trust-center/security-advisories/advisory.SD1692.html

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
