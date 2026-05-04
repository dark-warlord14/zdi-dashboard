# ZDI-10-014: Microsoft Internet Explorer item Object Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-014
- **ZDI-CAN:** ZDI-CAN-544
- **Date:** 2010-01-21
- **CVE:** CVE-2010-0248
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter Vreugdenhil ( http://www.vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of cloned DOM objects in JavaScript. A specially crafted sequence of object cloning can result in the use of a pointer after it has been freed. Successful exploitation can lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-002.mspx

## Disclosure Timeline

- 2009-08-14 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory
