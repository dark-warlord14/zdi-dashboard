# ZDI-13-275: Adobe Flash Player Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-275
- **ZDI-CAN:** ZDI-CAN-1997
- **Date:** 2013-12-15
- **CVE:** CVE-2013-5330
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-275/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of certain AVM2 instructions, allowing direct memory access outside of the domain memory. By leveraging this flaw, an attacker can execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb13-26.html

## Disclosure Timeline

- 2013-09-27 - Vulnerability reported to vendor
- 2013-12-15 - Coordinated public release of advisory
