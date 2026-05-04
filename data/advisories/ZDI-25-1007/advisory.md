# ZDI-25-1007: Apple Safari JavaScriptCore operationMapIteratorNext Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1007
- **ZDI-CAN:** ZDI-CAN-27825
- **Date:** 2025-11-13
- **CVE:** CVE-2025-43438
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** shandikri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1007/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of operationMapIteratorNext DFG operation. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125640

## Disclosure Timeline

- 2025-08-19 - Vulnerability reported to vendor
- 2025-11-13 - Coordinated public release of advisory
- 2025-11-13 - Advisory Updated
