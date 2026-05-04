# ZDI-16-504: AlienVault Unified Security Management Multiple PHP Scripts Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-16-504
- **ZDI-CAN:** ZDI-CAN-3704
- **Date:** 2016-09-08
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-504/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Unified Security Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within multiple PHP scripts in AlienVault Unified Security Management. These scripts contain flaws that allow an attacker to bypass authentication, upload arbitrary files, and include malicious code from a remote resource. An attacker can chain these vulnerabilities to execute arbitrary code in the context of the process.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/7110/

## Disclosure Timeline

- 2016-05-02 - Vulnerability reported to vendor
- 2016-09-08 - Coordinated public release of advisory
