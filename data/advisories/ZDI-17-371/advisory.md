# ZDI-17-371: Microsoft Windows JavaScript Array Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-371
- **ZDI-CAN:** ZDI-CAN-4772
- **Date:** 2017-05-30
- **CVE:** CVE-2017-0266
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-371/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays in JavaScript. By performing actions in JavaScript an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0266

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-05-30 - Coordinated public release of advisory
