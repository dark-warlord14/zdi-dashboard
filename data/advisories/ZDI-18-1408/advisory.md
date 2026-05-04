# ZDI-18-1408: Microsoft Windows JScript Array concat Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1408
- **ZDI-CAN:** ZDI-CAN-7156
- **Date:** 2018-12-13
- **CVE:** CVE-2018-8643
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Yu Haiwan and Wu HongJun from Nanyang Technological University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1408/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows JScript. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the Array.concat method in JScript. By creating an out-of-memory condition, an attacker can trigger access to a pointer prior to initialization. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8643

## Disclosure Timeline

- 2018-08-21 - Vulnerability reported to vendor
- 2018-12-13 - Coordinated public release of advisory
