# ZDI-24-524: A10 Thunder ADC CsrRequestView Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-524
- **ZDI-CAN:** ZDI-CAN-22517
- **Date:** 2024-05-29
- **CVE:** CVE-2024-30368
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** A10
- **Affected Products:** Thunder ADC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-524/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of A10 Thunder ADC. Authentication is required to exploit this vulnerability. The specific flaw exists within the CsrRequestView class. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of a10user.

## Additional Details

A10 has issued an update to correct this vulnerability. More details can be found at: https://support.a10networks.com/support/security_advisory/cve-2024-30368-cve-2024-30369

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
