# ZDI-14-221: (Pwn2Own) Microsoft Windows DirectShow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-221
- **ZDI-CAN:** ZDI-CAN-2231
- **Date:** 2014-07-09
- **CVE:** CVE-2014-2780
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** DirectShow
- **Credit:** VUPEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-221/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Stretch object. The issue lies in the failure to properly sanitize user-supplied data. An attacker can leverage this vulnerability to elevate privileges and execute code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-041.aspx

## Disclosure Timeline

- 2014-03-11 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
