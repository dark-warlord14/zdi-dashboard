# ZDI-21-407: (0Day) (Pwn2Own) Samsung Q60T TV Internet Browser Intermediate Representation Opcode Type-Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-407
- **ZDI-CAN:** ZDI-CAN-12057
- **Date:** 2021-04-13
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Q60T
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-407/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Q60 Smart QLED TV. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays in JavaScript. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/05/20 – ZDI reported the vulnerability to the vendor 03/24/21 – ZDI requested an update and notified the vendor of the intention to publish the case as a 0-day advisory on 03/31/21 03/24/21 – The vendor communicated the issue was fixed 03/25/21 – ZDI provided evidence of the issue still being present 03/26/21 – The vendor indicated the updated version was under testing and not released yet 03/26/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 03/31/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-11-05 - Vulnerability reported to vendor
- 2021-04-13 - Coordinated public release of advisory
