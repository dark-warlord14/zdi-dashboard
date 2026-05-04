# ZDI-16-533: Microsoft Internet Explorer Table Layout Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-533
- **ZDI-CAN:** ZDI-CAN-3857
- **Date:** 2016-10-11
- **CVE:** CVE-2016-3383
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0011
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-533/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of table layout. By manipulating a document's elements an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-118

## Disclosure Timeline

- 2016-07-12 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
