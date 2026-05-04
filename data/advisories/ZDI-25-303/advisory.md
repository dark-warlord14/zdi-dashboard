# ZDI-25-303: Apple Safari SandboxBroker ZIP File Processing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-303
- **ZDI-CAN:** ZDI-CAN-26148
- **Date:** 2025-05-21
- **CVE:** CVE-2025-24222
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-303/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ZIP files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the SandboxBroker process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/122716

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
