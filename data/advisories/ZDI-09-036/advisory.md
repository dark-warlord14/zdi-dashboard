# ZDI-09-036: Microsoft Internet Explorer setCapture Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-036
- **ZDI-CAN:** ZDI-CAN-425
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1529
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific vulnerability exists when calling the setCapture method on a range of objects. When setCapture is called on a collection of specially crafted objects memory becomes corrupted. When the capture is released, arbitrary memory is accessed potentially leading to remote code execution. Exploitation of this vulnerability will lead to system compromise under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-019.mspx

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
