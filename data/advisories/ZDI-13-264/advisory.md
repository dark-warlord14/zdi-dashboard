# ZDI-13-264: Microsoft Internet Explorer CSelectTracker Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-264
- **ZDI-CAN:** ZDI-CAN-1933
- **Date:** 2013-11-24
- **CVE:** CVE-2013-3910
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter 'corelanc0d3r' Van Eeckhoutte - Corelan - www.corelangcv.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-264/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSelectTracker objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-088

## Disclosure Timeline

- 2013-07-23 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
