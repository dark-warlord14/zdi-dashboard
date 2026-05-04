# ZDI-22-1483: Delta Industrial Automation InfraSuite Device Master CheckLoadingStartupConfig Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1483
- **ZDI-CAN:** ZDI-CAN-17549
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41772
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1483/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CheckLoadingStartupConfig function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-07 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
