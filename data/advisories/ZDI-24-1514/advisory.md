# ZDI-24-1514: (0Day) Hugging Face Transformers MaskFormer Model Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1514
- **ZDI-CAN:** ZDI-CAN-25191
- **Date:** 2024-11-19
- **CVE:** CVE-2024-11393
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hugging Face
- **Affected Products:** Transformers
- **Credit:** The_Kernel_Panic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1514/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Transformers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of model files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

09/11/24 – ZDI submitted the report to the vendor via a bug bounty platform 10/14/24 – the vendor rejected the vulnerability 11/06/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-09-11 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
