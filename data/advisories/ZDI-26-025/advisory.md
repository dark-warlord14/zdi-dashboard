# ZDI-26-025: (0Day) Katana Network Development Starter Kit executeCommand Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-025
- **ZDI-CAN:** ZDI-CAN-27786
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0759
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Katana Network
- **Affected Products:** Development Starter Kit
- **Credit:** Peter Girnus (@gothburz) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Katana Network Development Starter Kit. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the executeCommand method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

08/11/25 – ZDI requested the vendor’s PSIRT contacts in a GitHub issue 08/11/25 – the vendor provided their contacts 08/14/25 – ZDI submitted the report to the vendor 08/21/25 – the vendor confirmed that their project was not affected by the reported issue 12/14/25 – ZDI communicated disagreement with vendor's assessment 12/17/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
