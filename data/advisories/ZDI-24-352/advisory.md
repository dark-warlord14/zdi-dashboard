# ZDI-24-352: Softing edgeConnector Siemens Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-352
- **ZDI-CAN:** ZDI-CAN-21225
- **Date:** 2024-03-28
- **CVE:** CVE-2023-38126
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** edgeConnector Siemens
- **Credit:** Pan ZhenPeng (@Peterpan0927) & Li JianTao (@CurseRed) of STAR Labs SG Pte. Ltd. (@starlabs_sg)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-352/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Softing edgeConnector Siemens. Authentication is required to exploit this vulnerability. In the case of a network-adjacent attacker, the existing authentication mechanism can be bypassed. The specific flaw exists within the web console, which listens on TCP port 8099 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root within the application container.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-074-13

## Disclosure Timeline

- 2023-05-23 - Vulnerability reported to vendor
- 2024-03-28 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
