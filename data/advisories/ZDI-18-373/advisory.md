# ZDI-18-373: Microsoft Edge CSS var Function Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-373
- **ZDI-CAN:** ZDI-CAN-5313
- **Date:** 2018-04-25
- **CVE:** CVE-2018-0763
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** @j00sean (Thanks to Domato: https://github.com/google/domato)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-373/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the var function in CSS. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0763

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2018-04-25 - Coordinated public release of advisory
- 2018-04-25 - Advisory Updated
