# ZDI-24-1310: Lenovo Service Bridge Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1310
- **ZDI-CAN:** ZDI-CAN-23010
- **Date:** 2024-09-27
- **CVE:** CVE-2024-4696
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lenovo
- **Affected Products:** Service Bridge
- **Credit:** Darrel Huang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1310/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Lenovo Service Bridge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the LscShim module. When parsing a crafted URL, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Lenovo has issued an update to correct this vulnerability. More details can be found at: https://support.lenovo.com/ca/en/product_security/ps500631-lenovo-service-bridge-vulnerability

## Disclosure Timeline

- 2024-05-06 - Vulnerability reported to vendor
- 2024-09-27 - Coordinated public release of advisory
- 2024-09-27 - Advisory Updated
