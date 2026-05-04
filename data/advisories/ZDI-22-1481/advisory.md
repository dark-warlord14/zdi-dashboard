# ZDI-22-1481: Delta Industrial Automation InfraSuite Device Master Device-Gateway CtrlLayerNWCmd_FileOperation Opcode 512 Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1481
- **ZDI-CAN:** ZDI-CAN-17547
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41657
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1481/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within CtrlLayerNWCmd_FileOperation, opcode 512. When parsing the fileName element, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
