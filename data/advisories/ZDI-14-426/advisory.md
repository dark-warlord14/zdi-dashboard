# ZDI-14-426: AlienVault Unified Security Management cloneid SQL Injection and Scanner Binary Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-426
- **ZDI-CAN:** ZDI-CAN-2049
- **Date:** 2015-02-23
- **CVE:** N/A
- **CVSS:** 7.9
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:N
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-426/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Unified Security Management. Authentication is required to exploit this vulnerability. The specific flaws exist within the cloneid request parameter and Scanner Binary fields. An attacker can leverage these vulnerabilities to read files and achieve remote code execution under the context of the root user.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/2306/security-advisory-all-alienvault-versions-prior-to-4-4-1

## Disclosure Timeline

- 2014-03-14 - Vulnerability reported to vendor
- 2015-02-23 - Coordinated public release of advisory
