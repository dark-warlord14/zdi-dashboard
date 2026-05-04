# ZDI-07-048: Microsoft Internet Explorer substringData Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-048
- **ZDI-CAN:** ZDI-CAN-096
- **Date:** 2007-08-14
- **CVE:** CVE-2007-2223
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of various Microsoft software User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the substringData() method available on the TextNode JavaScript object. When specific parameters are passed to the method, an integer overflow occurs causing incorrect memory allocation. If this event occurs after a different ActiveX object has been instantiated, an exploitable condition is created when the ActiveX object is deallocated which can result in the execution of arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-042.mspx

## Disclosure Timeline

- 2006-10-03 - Vulnerability reported to vendor
- 2007-08-14 - Coordinated public release of advisory
