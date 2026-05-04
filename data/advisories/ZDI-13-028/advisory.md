# ZDI-13-028: Microsoft Internet Explorer SetCapture Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-028
- **ZDI-CAN:** ZDI-CAN-1640
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0018
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair (www.krash.in)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the setCapture method. By calling setCapture on a carefully structured document an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS13-009

## Disclosure Timeline

- 2012-11-08 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
