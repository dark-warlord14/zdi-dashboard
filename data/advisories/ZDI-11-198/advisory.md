# ZDI-11-198: (Pwn2Own) Microsoft Internet Explorer Uninitialized Variable Information Leak Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-198
- **ZDI-CAN:** ZDI-CAN-1158
- **Date:** 2011-06-14
- **CVE:** CVE-2011-1346
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-198/
## Vulnerability Details

This vulnerability allows remote attackers to leak information on vulnerable installations of Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Internet Explorer that allows malicious users to leak information about the memory layout of an Internet Explorer process. When creating a new 'Option' HTML Element, the 'index' field of the object is not set to zero and can be used to leak the location of the global variable table. This can be used to defeat ASLR or to remove the need for heap spraying while exploiting a remote code execution flaw.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-050.mspx

## Disclosure Timeline

- 2011-03-09 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
