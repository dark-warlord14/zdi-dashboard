# ZDI-18-162: Microsoft Edge CSS var Function Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-162
- **ZDI-CAN:** ZDI-CAN-5323
- **Date:** 2018-02-21
- **CVE:** CVE-2018-0763
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** @j00sean (Thanks to Domato: https://github.com/google/domato)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-162/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of custom properties in CSS. By manipulating a document's elements, an attacker can trigger a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0763

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2018-02-21 - Coordinated public release of advisory
- 2018-02-21 - Advisory Updated
