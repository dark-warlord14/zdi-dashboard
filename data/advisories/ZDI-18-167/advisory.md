# ZDI-18-167: Microsoft Edge Select Element Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-167
- **ZDI-CAN:** ZDI-CAN-5486
- **Date:** 2018-02-21
- **CVE:** CVE-2018-0839
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Dmitri Kaslov of Telspace Systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-167/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTML select elements. By manipulating a document's elements an attacker can trigger a read past the end of an allocated array. An attacker can leverage this vulnerability to disclose information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0839

## Disclosure Timeline

- 2017-12-07 - Vulnerability reported to vendor
- 2018-02-21 - Coordinated public release of advisory
- 2018-02-21 - Advisory Updated
