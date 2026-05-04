# ZDI-15-378: Microsoft Internet Explorer Filesystem Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-378
- **ZDI-CAN:** ZDI-CAN-2727
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2430
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-378/
## Vulnerability Details

This vulnerability allows attackers to escalate privileges on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of junction points in the Favorites folder linked to other folders. An attacker running code in the context of a low-rights Internet Explorer process can set up a junction point in the Favorites folder and then the IE broker process will change access control rights in the targeted folders (which are normally unmodifiable by the low-rights process). An attacker can leverage this vulnerability to execute code under the context of a medium integrity process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-090

## Disclosure Timeline

- 2015-02-09 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
