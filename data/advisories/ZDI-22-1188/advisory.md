# ZDI-22-1188: (Pwn2Own) Tesla ice_updater Time-Of-Check Time-Of-Use Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1188
- **ZDI-CAN:** ZDI-CAN-17463
- **Date:** 2022-09-08
- **CVE:** CVE-2022-3093
- **CVSS:** 7.6
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model 3
- **Credit:** @Jedar_LZ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1188/
## Vulnerability Details

This vulnerability allows physical attackers to execute arbitrary code on affected Tesla vehicles. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ice_updater update mechanism. The issue results from the lack of proper validation of user-supplied firmware. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Issue was fixed starting in Tesla’s 2022.16.0.3 release.

## Disclosure Timeline

- 2022-06-22 - Vulnerability reported to vendor
- 2022-09-08 - Coordinated public release of advisory
