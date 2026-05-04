# ZDI-18-577: Microsoft Edge CSS Background Property Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-577
- **ZDI-CAN:** ZDI-CAN-5605
- **Date:** 2018-06-13
- **CVE:** CVE-2018-0763
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** akayn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-577/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSS background-related properties. By manipulating a document's elements, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0763

## Disclosure Timeline

- 2018-01-30 - Vulnerability reported to vendor
- 2018-06-13 - Coordinated public release of advisory
- 2018-06-13 - Advisory Updated
