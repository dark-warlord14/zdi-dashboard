# ZDI-25-1149: (0Day) Hugging Face Transformers Transformer-XL Model Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1149
- **ZDI-CAN:** ZDI-CAN-25424
- **Date:** 2025-12-18
- **CVE:** CVE-2025-14921
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hugging Face
- **Affected Products:** Transformers
- **Credit:** The_Kernel_Panic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1149/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Transformers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of model files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

11/04/24 – ZDI submitted the report to a third-party bug bounty program 12/17/24 – the vendor rejected the vulnerability 12/12/25 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 12/18/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2024-11-04 - Vulnerability reported to vendor
- 2025-12-18 - Coordinated public release of advisory
- 2025-12-18 - Advisory Updated
