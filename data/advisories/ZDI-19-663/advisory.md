# ZDI-19-663: Oracle WebLogic DeploymentService Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-663
- **ZDI-CAN:** ZDI-CAN-8666
- **Date:** 2019-07-22
- **CVE:** CVE-2019-2827
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** Kamlapati Choubey of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-663/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle WebLogic. Authentication is required to exploit this vulnerability. The specific flaw exists within the DeploymentService, which listens on TCP port 7001 by default. When parsing the wl_request_type header, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2019-5072835.html

## Disclosure Timeline

- 2019-04-26 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
- 2019-07-22 - Advisory Updated
