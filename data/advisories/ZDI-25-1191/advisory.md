# ZDI-25-1191: (0Day) FontForge PFB File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1191
- **ZDI-CAN:** ZDI-CAN-28546
- **Date:** 2025-12-29
- **CVE:** CVE-2025-15273
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** FontForge
- **Affected Products:** FontForge
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of FontForge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PFB files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

12/12/25 - ZDI submitted the reports to the vendor via third-party platform 12/13/25 - ZDI reached out to the vendor’s GitHub account 12/13/25 – the vendor rejected the vulnerability, stating that only pull requests that include the required fixes will be considered 12/15/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/29/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-12-12 - Vulnerability reported to vendor
- 2025-12-29 - Coordinated public release of advisory
- 2026-01-08 - Advisory Updated
