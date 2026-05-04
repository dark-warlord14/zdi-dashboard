# ZDI-15-019: Microsoft Internet Explorer CShadow Direction Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-019
- **ZDI-CAN:** ZDI-CAN-2570
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0036
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Pawel Wylecial
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CShadow::put_Direction function. The issue lies in the failure to properly sanitize a user-supplied value. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-10-09 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
