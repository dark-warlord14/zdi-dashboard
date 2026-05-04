# ZDI-22-410: (Pwn2Own) Cisco RV340 upload.cgi sessionid Improper Input Validation Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-410
- **ZDI-CAN:** ZDI-CAN-15882
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20705
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Bien Pham (@bienpnn) from Team Orca of Sea Security (security.sea.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-410/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Cisco RV340 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the sessionid parameter provided to the upload.cgi endpoint. The issue results from the lack of proper validation of the user-supplied sessionid cookie. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
