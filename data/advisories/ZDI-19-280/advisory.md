# ZDI-19-280: Microsoft Chakra lastIndexOf Integer Underflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-280
- **ZDI-CAN:** ZDI-CAN-7919
- **Date:** 2019-03-12
- **CVE:** CVE-2019-0746
- **CVSS:** 3.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-280/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the lastIndexOf method in JavaScript. By performing actions in JavaScript, an attacker can trigger an integer underflow before reading memory. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0746

## Disclosure Timeline

- 2019-01-22 - Vulnerability reported to vendor
- 2019-03-12 - Coordinated public release of advisory
