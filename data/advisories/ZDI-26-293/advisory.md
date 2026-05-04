# ZDI-26-293: (0Day) Microsoft Office URI Handler NTLM Response Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-293
- **ZDI-CAN:** ZDI-CAN-28651
- **Date:** 2026-04-21
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** Len Sadowski (lytnc) and Oğuz Bektaş (_ozb_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-293/
## Vulnerability Details

This vulnerability allows remote attackers to disclose NTLM responses on affected installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Microsoft Office URI schemes. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to disclose NTLM responses in the context of the current user.

## Additional Details

02/05/26 – ZDI reported the vulnerability to the vendor 02/05/26 – the vendor acknowledged the receipt of the report 03/04/26 – the vendor communicated that the vulnerability did not meet the bar for security servicing 04/13/26 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2026-02-05 - Vulnerability reported to vendor
- 2026-04-21 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
