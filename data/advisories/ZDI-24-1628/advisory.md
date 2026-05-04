# ZDI-24-1628: (0Day) Fuji Electric Tellus Lite V-Simulator 5 V8 File Parsing Stack-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1628
- **ZDI-CAN:** ZDI-CAN-24770
- **Date:** 2024-11-27
- **CVE:** CVE-2024-11802
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Tellus Lite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1628/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Tellus Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of V8 files in the V-Simulator 5 component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/18/24 - ZDI reported the vulnerability to the vendor 07/18/24 - the vendor acknowledged the receipt of the report 08/21/24 - the vendor confirmed the reported issue and requested an extension until April 2025 10/07/24 - ZDI notified the vendor of the intention to publish the case as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-18 - Vulnerability reported to vendor
- 2024-11-27 - Coordinated public release of advisory
- 2024-11-27 - Advisory Updated
