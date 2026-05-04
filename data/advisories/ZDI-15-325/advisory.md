# ZDI-15-325: Microsoft Internet Explorer DLL Planting Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-325
- **ZDI-CAN:** ZDI-CAN-2726
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2368
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-325/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DLL loading by the Internet Explorer broker process, which can be induced to load a library in its context from a directory controlled by the low-integrity process. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-069

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
