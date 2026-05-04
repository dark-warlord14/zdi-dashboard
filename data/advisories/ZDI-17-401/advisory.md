# ZDI-17-401: Microsoft Internet Explorer InsertRow Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-401
- **ZDI-CAN:** ZDI-CAN-4573
- **Date:** 2017-06-13
- **CVE:** CVE-2017-8547
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Yu Haiwan Wu HongJun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-401/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of script methods that insert rows into HTML tables. By performing actions in script, an attacker can trigger a read past the end of an allocated array. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8547

## Disclosure Timeline

- 2017-03-24 - Vulnerability reported to vendor
- 2017-06-13 - Coordinated public release of advisory
