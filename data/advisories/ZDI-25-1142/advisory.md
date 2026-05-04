# ZDI-25-1142: (0Day) Hugging Face Diffusers CogView4 Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1142
- **ZDI-CAN:** ZDI-CAN-27424
- **Date:** 2025-12-18
- **CVE:** CVE-2025-14922
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hugging Face
- **Affected Products:** Diffusers
- **Credit:** Xingyu Wang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Diffusers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of checkpoints. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

11/25/25 - ZDI submitted the report to the vendor’s security team via email 11/25/25 – the vendor acknowledged the receipt of the report 11/28/25 – the vendor confirmed that no changes will be made and closed the report as informative 12/12/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/18/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-11-25 - Vulnerability reported to vendor
- 2025-12-18 - Coordinated public release of advisory
- 2025-12-30 - Advisory Updated
