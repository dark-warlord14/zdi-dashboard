# ZDI-15-342: Microsoft Internet Explorer EditWith Broker API Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-342
- **ZDI-CAN:** ZDI-CAN-2870
- **Date:** 2015-07-20
- **CVE:** CVE-2015-2402
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-342/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer running in either Protected Mode or Enhanced Protected Mode. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the EditWith function of the document broker. The document broker can be induced to use a file path from a registry key that is controlled by the low integrity process. This can be changed while the broker is attempting to use it, resulting in a race condition and the execution of arbitrary executables at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-065.aspx

## Disclosure Timeline

- 2015-04-09 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
