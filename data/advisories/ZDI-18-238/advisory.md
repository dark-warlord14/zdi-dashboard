# ZDI-18-238: Microsoft Edge CQuotes Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-238
- **ZDI-CAN:** ZDI-CAN-5485
- **Date:** 2018-03-19
- **CVE:** CVE-2018-0763
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Dmitri Kaslov of Telspace Systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-238/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CQuotes objects. By manipulating a document's elements an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to disclose information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0763

## Disclosure Timeline

- 2017-12-07 - Vulnerability reported to vendor
- 2018-03-19 - Coordinated public release of advisory
- 2018-03-19 - Advisory Updated
