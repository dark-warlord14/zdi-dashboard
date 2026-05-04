# ZDI-25-1148: (0Day) Hugging Face Transformers SEW-D convert_config Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1148
- **ZDI-CAN:** ZDI-CAN-28252
- **Date:** 2025-12-18
- **CVE:** CVE-2025-14927
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hugging Face
- **Affected Products:** Transformers
- **Credit:** Peter Girnus (@gothburz), Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Transformers. User interaction is required to exploit this vulnerability in that the target must convert a malicious checkpoint. The specific flaw exists within the convert_config function. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

10/14/25 - ZDI submitted the report to a third-party bug bounty program 11/11/25 – ZDI asked for updates 11/12/25 – the vendor rejected the report and closed the case 12/12/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/18/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-10-14 - Vulnerability reported to vendor
- 2025-12-18 - Coordinated public release of advisory
- 2025-12-18 - Advisory Updated
