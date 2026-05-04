# ZDI-15-161: AlienVault Unified Security Management Plugin Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-161
- **ZDI-CAN:** ZDI-CAN-2630
- **Date:** 2015-04-29
- **CVE:** CVE-2015-3446
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** Spencer McIntyre
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-161/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Unified Security Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AlienVault framework daemon which permits remote unauthenticated changes to its .cfg file. A specially crafted plugin configuration file can specify a custom function which can contain arbitrary Python code. An attacker can exploit this condition to achieve code execution under the context of the root user.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/4415/

## Disclosure Timeline

- 2015-01-06 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
