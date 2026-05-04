# ZDI-16-532: Microsoft Edge JavaScript eval Function Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-532
- **ZDI-CAN:** ZDI-CAN-3866
- **Date:** 2016-10-11
- **CVE:** CVE-2016-3382
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-532/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge and Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the JavaScript eval function. By performing actions in script an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-118

## Disclosure Timeline

- 2016-07-12 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
