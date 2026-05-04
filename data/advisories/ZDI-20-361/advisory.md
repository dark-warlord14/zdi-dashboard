# ZDI-20-361: (0Day) Corel PaintShop Pro PNG File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-361
- **ZDI-CAN:** ZDI-CAN-9694
- **Date:** 2020-04-02
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Corel
- **Affected Products:** PaintShop Pro
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-361/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Corel PaintShop Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of PNG files. When parsing PNG files, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/18/19 – ZDI reported the vulnerabilities to the vendor 11/18/19 – The vendor acknowledged receipt and provided ticket #s 12/04/19 – The vendor confirmed the issues were being looked at 02/20/20 – ZDI requested a status update 03/04/20 – ZDI requested a status update and notified of the intent of publishing the cases as 0-day 03/17/20 – ZDI requested a status update and notified of the intent of publishing the cases as 0-day 03/25/20 – ZDI notified of the intent of publishing the cases as 0-day on April 2nd -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-11-18 - Vulnerability reported to vendor
- 2020-04-02 - Coordinated public release of advisory
