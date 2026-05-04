# ZDI-18-1134: Microsoft Internet Explorer WebCrypto importKey Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1134
- **ZDI-CAN:** ZDI-CAN-6405
- **Date:** 2018-10-10
- **CVE:** CVE-2018-8491
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1134/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of imported keys in WebCrypto. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8491

## Disclosure Timeline

- 2018-06-28 - Vulnerability reported to vendor
- 2018-10-10 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
