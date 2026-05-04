# ZDI-18-264: Microsoft Edge Select Element Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-264
- **ZDI-CAN:** ZDI-CAN-5497
- **Date:** 2018-03-26
- **CVE:** CVE-2018-0839
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-264/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTML select elements. By manipulating a document's elements an attacker can trigger a read past the end of an allocated array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2018-0839

## Disclosure Timeline

- 2017-12-08 - Vulnerability reported to vendor
- 2018-03-26 - Coordinated public release of advisory
- 2018-03-26 - Advisory Updated
