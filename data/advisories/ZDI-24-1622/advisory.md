# ZDI-24-1622: (0Day) Fuji Electric Monitouch V-SFT V9C File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1622
- **ZDI-CAN:** ZDI-CAN-24506
- **Date:** 2024-11-27
- **CVE:** CVE-2024-11796
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Monitouch V-SFT
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1622/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Monitouch V-SFT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of V9C files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/16/24 - ZDI reported the vulnerability to the vendor 07/18/24 - the vendor acknowledged the receipt of the report 03/21/24 - the vendor confirmed the reported issue and requested an extension until April 2025 10/07/24 - ZDI notified the vendor of the intention to publish the case as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-11-27 - Coordinated public release of advisory
- 2024-11-27 - Advisory Updated
