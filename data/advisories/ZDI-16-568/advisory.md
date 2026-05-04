# ZDI-16-568: Adobe Flash SWF Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-568
- **ZDI-CAN:** ZDI-CAN-3957
- **Date:** 2016-10-12
- **CVE:** CVE-2016-6986
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** b0nd@Garage4Hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-568/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of SWF data. A crafted SWF can trigger a read past the end of an allocated buffer. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-32.html

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2016-10-12 - Coordinated public release of advisory
