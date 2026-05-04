# ZDI-18-580: Microsoft Chakra Typed Array Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-580
- **ZDI-CAN:** ZDI-CAN-6050
- **Date:** 2018-06-13
- **CVE:** CVE-2018-8236
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Chakra
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-580/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of typed arrays in JavaScript. By performing actions in JavaScript, an attacker can cause a typed array object to be accessed after it is no longer in a usable state. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8236

## Disclosure Timeline

- 2018-04-13 - Vulnerability reported to vendor
- 2018-06-13 - Coordinated public release of advisory
- 2018-06-13 - Advisory Updated
