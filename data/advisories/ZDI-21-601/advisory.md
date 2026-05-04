# ZDI-21-601: Ubiquiti Networks EdgeOS Improper Certificate Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-601
- **ZDI-CAN:** ZDI-CAN-11700
- **Date:** 2021-05-20
- **CVE:** CVE-2021-22909
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ubiquiti Networks
- **Affected Products:** EdgeOS
- **Credit:** awxylitol
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-601/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ubiquiti Networks EdgeOS on EdgeRouter X, EdgeRouter Pro X SFP, EdgeRouter 10X and EdgePoint 6-port routers. User interaction is required to exploit this vulnerability in that an administrator must perform a firmware update on the device. The specific flaw exists within the downloading of firmware files via HTTPS. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Ubiquiti Networks has issued an update to correct this vulnerability. More details can be found at: https://community.ui.com/releases/Security-Advisory-Bulletin-018-018/cfa1566b-4bf8-427b-8cc7-8cffba3a93a4

## Disclosure Timeline

- 2021-01-06 - Vulnerability reported to vendor
- 2021-05-20 - Coordinated public release of advisory
