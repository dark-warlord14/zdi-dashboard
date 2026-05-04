# ZDI-16-157: Microsoft Internet Explorer CSVGAnimatedAngle Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-157
- **ZDI-CAN:** ZDI-CAN-3297
- **Date:** 2016-02-09
- **CVE:** CVE-2016-0072
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-157/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of CSVGAnimatedAngle objects. By manipulating a document's elements, an attacker can cause a CSVGAnimatedAngle object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS16-009

## Disclosure Timeline

- 2015-09-17 - Vulnerability reported to vendor
- 2016-02-09 - Coordinated public release of advisory
