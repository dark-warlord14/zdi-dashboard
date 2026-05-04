# ZDI-22-413: (Pwn2Own) Cisco RV340 Firmware Update Improper Certificate Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-413
- **ZDI-CAN:** ZDI-CAN-15810
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20703 , CVE-2022-20704
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Gaurav Baruah
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-413/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. User interaction is required to exploit this vulnerability in that an administrator must perform a firmware update on the device. The specific flaw exists within the downloading of firmware files via HTTPS. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
