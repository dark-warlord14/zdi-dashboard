# ZDI-21-341: (0Day) (Pwn2Own) Sony X800H Smart TV Vewd Type-Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-341
- **ZDI-CAN:** ZDI-CAN-12060
- **Date:** 2021-03-18
- **CVE:** N/A
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Sony
- **Affected Products:** X800H
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-341/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sony X800H Smart TV. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays by the Vewd TV Internet Browser. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/07/20 – ZDI reported the vulnerability to the vendor 11/10/20 – The vendor acknowledged the report 11/13/20 – ZDI reminded the vendor of the 90 day allowance for Pwn2Own competition fixes 11/19/20 – The vendor confirmed the vulnerability 12/01/20 – The vendor requested an extension until July 12/04/20 – ZDI communicated an extension could only be granted until March 03/08/21 – The vendor requested an extension until June 03/11/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 03/18/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-11-07 - Vulnerability reported to vendor
- 2021-03-18 - Coordinated public release of advisory
