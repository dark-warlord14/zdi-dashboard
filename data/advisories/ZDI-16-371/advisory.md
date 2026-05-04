# ZDI-16-371: Microsoft Edge CBaseScriptable PrivateQueryInterface Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-371
- **ZDI-CAN:** ZDI-CAN-3665
- **Date:** 2016-06-22
- **CVE:** CVE-2016-3222
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Shi Ji (@Puzzor) of VARAS@IIE
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-371/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of CBaseScriptable::PrivateQueryInterface. By performing certain operations in script, an attacker can cause Microsoft Edge to read uninitialized data from a memory location on the stack. An attacker can leverage this to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-068

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2016-06-22 - Coordinated public release of advisory
